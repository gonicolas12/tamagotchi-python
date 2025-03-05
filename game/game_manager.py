"""
Game management module, containing the main class that orchestrates all functionalities.
"""

import time
import random
from models.creature import Creature

class Game:
    """Class managing the game and its interactions."""
    
    def __init__(self):
        """
        Initializes the game with its basic parameters.
        """
        self.creature = None
        self.available_types = ["chaton", "chiot", "dragon", "robot", "lapin"]
        self.last_action = time.time()

        # Add an attribute to store the current weather and the last update
        self.current_weather = None
        self.last_weather_update = -1  # Initialized to -1 to force update at startup
    
    def create_creature(self, name, creature_type, color="standard", character_trait="normal"):
        """
        Creates a new creature with the specified name and type.
        
        Args:
            name (str): Name of the creature
            creature_type (str): Type of creature to create
            color (str): Color of the creature
            character_trait (str): Dominant character trait
            
        Returns:
            str: Confirmation or error message
        """
        if creature_type.lower() not in map(str.lower, self.available_types):
            return f"Type de créature invalide. Types disponibles : {', '.join(self.available_types)}."
        
        self.creature = Creature(name, creature_type, color, character_trait)
        self.last_action = time.time()
        
        # Initialize weather when a creature is created
        weather = self.update_weather(force=True)
        
        return f"{name} le {creature_type} {color} de nature {character_trait} a été créé !\n{weather['message']}"
    
    def load_creature(self, filename="sauvegarde.json"):
        """
        Loads a creature from a save file.
        
        Args:
            filename (str): Path to the save file
            
        Returns:
            str: Confirmation or error message
        """
        creature = Creature.load(filename)
        if creature:
            self.creature = creature
            self.last_action = time.time()
            
            # Initialize weather when a creature is loaded
            weather = self.update_weather(force=True)
            
            return f"{creature.name} a été chargé !\n{weather['message']}"
        return "Impossible de charger la créature."
    
    def update_weather(self, force=False):
        """
        Updates the weather if a day has passed or if forced.
        
        Args:
            force (bool): If True, updates the weather regardless of time passed
            
        Returns:
            dict or None: The new weather if updated, None otherwise
        """
        if not self.creature:
            return None
            
        current_day = int(self.creature.age)
        
        # Update weather if a day has passed or if forced
        if force or current_day > self.last_weather_update:
            from game.events import generate_random_weather
            self.current_weather = generate_random_weather()
            self.last_weather_update = current_day
            
            # Apply weather effects to creature
            if self.creature:
                self.creature.happiness = max(0, min(100, 
                                            self.creature.happiness + self.current_weather["happiness_effect"]))
            
            return self.current_weather
        
        return None
    
    def get_current_weather(self):
        """
        Returns the current weather information.
        
        Returns:
            dict or None: Current weather information or None if no weather
        """
        return self.current_weather
    
    def do_action(self, action, **params):
        """
        Performs an action on the current creature.
        
        Args:
            action (str): Name of the action to perform
            **params: Additional parameters specific to the action
            
        Returns:
            str: Result of the action
        """
        if not self.creature:
            return "Aucune créature n'a été créée ou chargée."
        
        # Calculate time elapsed since last action
        current_time = time.time()
        hours_elapsed = (current_time - self.last_action) / 3600  # Convert to hours
        
        # Save the age before the action to detect a day change
        previous_age_day = int(self.creature.age)
        
        result = ""
        weather_updated = False
        
        # Update creature state based on elapsed time
        if hours_elapsed > 0.01:  # To avoid too frequent updates (less than 36 seconds)
            result = self.creature.pass_time(hours_elapsed)
            if result == "death":
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée. Retour au menu principal."
            
            # Check if a day has passed
            current_age_day = int(self.creature.age)
            
            # If a day or more has passed, update the weather
            if current_age_day > previous_age_day:
                # Calculate how many days have passed
                days_passed = current_age_day - previous_age_day
                
                # Update the weather for the current day
                weather = self.update_weather(force=True)
                if weather:
                    result += f"\n{weather['message']}"
                    weather_updated = True
        
        # Perform the requested action
        action_result = ""
        if action == "feed":
            food = params.get("food", "standard")
            action_result = self.creature.feed(food)
        elif action == "play":
            duration = params.get("duration", 1)
            
            # Explicitly make time pass for playing
            # (in addition to the specific effects of the play action)
            time_message = self._format_time_message(duration)
            
            play_result = self.creature.play(duration)
            if play_result == "death":
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée pendant le jeu. Retour au menu principal."
                
            # Combine time message with play result
            action_result = f"{time_message}\n{play_result}"
            
            # Check if a day has passed during play
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "sleep":
            duration = params.get("duration", 8)
            
            # Explicitly make time pass for sleeping
            # (in addition to the specific effects of the sleep action)
            time_message = self._format_time_message(duration)
            
            sleep_result = self.creature.sleep(duration)
            if sleep_result == "death":
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée pendant son sommeil. Retour au menu principal."
                
            # Combine time message with sleep result
            action_result = f"{time_message}\n{sleep_result}"
            
            # Check if a day has passed during sleep
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "heal":
            action_result = self.creature.heal()
        elif action == "save":
            filename = params.get("filename", "sauvegarde.json")
            action_result = self.creature.save(filename)
        elif action == "explore":
            # Exploration takes 30 minutes (0.5 hours)
            exploration_time = 0.5
            
            # First, explicitly make time pass for exploration
            time_result = self.creature.pass_time(exploration_time)
            if time_result == "death":
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée pendant l'exploration. Retour au menu principal."
                
            # Then, generate a random event
            from game.events import generate_random_event
            event_result = generate_random_event(self.creature)
            
            # Combine results
            action_result = f"Votre créature a exploré pendant 30 minutes.\n{event_result}"
            
            # Check if a day has passed during exploration
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "meet":
            # Meeting another creature takes 30 minutes (0.5 hours)
            meet_time = 0.5
            time_message = self._format_time_message(meet_time)
            
            # Generate a meeting with another creature
            possible_types = self.available_types.copy()
            if self.creature.creature_type.lower() in map(str.lower, possible_types):
                possible_types.remove(self.creature.creature_type.lower())
            
            other_type = params.get("type", random.choice(possible_types))
            other_name = params.get("name", f"{other_type.capitalize()}-{random.randint(1, 100)}")
            
            # Meet the creature
            encounter_result = self.creature.encounter_creature(other_name, other_type)
            
            # Check if the creature died as a result of the encounter
            if self._check_creature_death():
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée pendant la rencontre. Retour au menu principal."
            
            # Combine results
            action_result = f"{time_message}\n{encounter_result}"
            
            # Check if a day has passed during the meeting
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "play_mini_game":
            from game.mini_games import mini_game_list
            
            game = params.get("game")
            if not game:
                # If no game is specified, display the list of available games
                available_games = mini_game_list()
                game_names = [game["nom"] for game in available_games]
                return f"Mini-jeux disponibles: {', '.join(game_names)}"
            
            # Mini-games take 1 hour
            mini_game_time = 1.0
            time_message = self._format_time_message(mini_game_time)
            
            game_result = self.creature.play_mini_game(game)
            if game_result["success"]:
                action_result = f"{time_message}\n{game_result['message']} +{game_result['happiness_bonus']} bonheur, +{game_result['points']} points"
                if game_result.get("item"):
                    action_result += f"\nVous avez gagné un objet: {game_result['item']}!"
            else:
                action_result = f"{time_message}\n{game_result['message']}"
            
            # Check if a day has passed during the mini-game
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "use_object":
            item = params.get("item")
            if not item:
                # If no item is specified, display the inventory
                if not self.creature.inventory:
                    return "L'inventaire est vide."
                return f"Objets disponibles: {', '.join(self.creature.inventory)}"
            
            # Using an object takes 15 minutes
            object_time = 0.25
            time_message = self._format_time_message(object_time)
            
            # Use the object
            object_result = self.creature.use_object(item)
            
            # Check if the creature died as a result of using the object
            if self._check_creature_death():
                from ui.display import display_death
                display_death(self.creature.name, self.creature.age)
                self.creature = None
                return "Votre créature est décédée. Retour au menu principal."
            
            # Combine messages
            action_result = f"{time_message}\n{object_result}"
            
            # Check if a day has passed while using the object
            if int(self.creature.age) > previous_age_day and not weather_updated:
                weather = self.update_weather(force=True)
                if weather:
                    action_result += f"\n{weather['message']}"
        elif action == "shop":
            points = self.creature.game_points
            if params.get("buy"):
                item = params.get("buy")
                price = self._get_object_price(item)
                
                if not price:
                    return f"L'objet {item} n'est pas disponible dans la boutique."
                
                if points < price:
                    return f"Vous n'avez pas assez de points pour acheter {item}. Prix: {price} points, points disponibles: {points}."
                
                self.creature.game_points -= price
                self.creature.inventory.append(item)
                return f"Vous avez acheté {item} pour {price} points."
            else:
                # This function now only returns the points, as the catalog is displayed via shop_menu
                return points
        else:
            action_result = f"Action inconnue: {action}"
        
        # Check if the creature died during the action
        if action_result == "death":
            from ui.display import display_death
            display_death(self.creature.name, self.creature.age)
            self.creature = None
            return "Votre créature est décédée. Retour au menu principal."
        
        self.last_action = current_time
        
        # Combine the results of the action with the result of the passage of time
        if result and action_result:
            return f"{result}\n{action_result}"
        elif result:
            return result
        else:
            return action_result
    
    def _check_creature_death(self):
        """
        Checks if the creature is dead.
        
        Returns:
            bool: True if the creature is dead, False otherwise
        """
        return self.creature is not None and self.creature.health <= 0
    
    def _format_time_message(self, hours):
        """
        Formats a message about elapsed time.
        
        Args:
            hours (float): Number of hours elapsed
            
        Returns:
            str: Formatted message
        """
        if hours < 1:
            minutes = int(hours * 60)
            return f"{minutes} minute(s) se sont écoulées."
        elif hours == 1:
            return "1 heure s'est écoulée."
        elif hours < 24:
            return f"{hours} heures se sont écoulées."
        else:
            days = int(hours // 24)
            remaining_hours = hours % 24
            if remaining_hours == 0:
                if days == 1:
                    return "1 jour s'est écoulé."
                else:
                    return f"{days} jours se sont écoulés."
            else:
                if days == 1:
                    return f"1 jour et {remaining_hours} heure(s) se sont écoulés."
                else:
                    return f"{days} jours et {remaining_hours} heure(s) se sont écoulés."
    
    def get_creature_state(self):
        """
        Returns the current state of the creature.
        
        Returns:
            dict or None: State of the creature or None if no creature
        """
        if not self.creature:
            return None
        return self.creature.get_state()
    
    def _get_shop_catalog(self):
        """
        Returns the catalog of items available in the shop.
        
        Returns:
            list: List of available items with their prices
        """
        return [
            {
                "nom": "Friandise",
                "prix": 10,
                "description": "Augmente la faim et un peu le bonheur"
            },
            {
                "nom": "Jouet",
                "prix": 15,
                "description": "Augmente le bonheur mais consomme de l'énergie"
            },
            {
                "nom": "Potion d'énergie",
                "prix": 20,
                "description": "Restaure beaucoup d'énergie"
            },
            {
                "nom": "Potion de santé",
                "prix": 25,
                "description": "Soigne la créature et améliore sa santé"
            },
            {
                "nom": "Amulette de protection",
                "prix": 50,
                "description": "Objet permanent qui améliore la santé"
            },
            {
                "nom": "Livre magique",
                "prix": 40,
                "description": "Objet permanent qui augmente le bonheur et donne des points de jeu"
            }
        ]
    
    def _get_object_price(self, object_name):
        """
        Returns the price of an item from the shop.
        
        Args:
            object_name (str): Name of the item
            
        Returns:
            int or None: Price of the item or None if the item doesn't exist
        """
        catalog = self._get_shop_catalog()
        for item in catalog:
            if item["nom"] == object_name:
                return item["prix"]
        return None
    
    def get_available_character_traits(self):
        """
        Returns the list of available character traits.
        
        Returns:
            dict: Character traits with their descriptions
        """
        return {
            "normal": "Aucun bonus ou malus particulier",
            "joueur": "Bonus de bonheur, légère perte d'énergie",
            "gourmand": "Faim plus rapide, légère perte de santé",
            "sportif": "Bonus d'énergie, faim plus rapide",
            "paresseux": "Perte d'énergie, léger bonus de bonheur",
            "curieux": "Bonus de bonheur et d'énergie",
            "timide": "Malus de bonheur et social",
            "sociable": "Bonus de bonheur et social",
            "intelligent": "Bonus aux mini-jeux"
        }
    
    def get_available_colors(self):
        """
        Returns the list of available colors according to creature type.
        
        Returns:
            dict: Available colors by creature type
        """
        colors = {
            "chaton": ["gris", "roux", "blanc", "noir", "tigré"],
            "chiot": ["marron", "blanc", "noir", "tacheté"],
            "dragon": ["rouge", "vert", "bleu", "noir", "doré"],
            "robot": ["argent", "or", "bleu", "noir", "rouge"],
            "lapin": ["blanc", "gris", "marron", "noir", "roux"]
        }
        
        # Add "standard" color for all types
        for creature_type in colors:
            if "standard" not in colors[creature_type]:
                colors[creature_type].append("standard")
        
        return colors
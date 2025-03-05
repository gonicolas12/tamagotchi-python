"""
Creature class defining the attributes and behaviors of a virtual creature.
"""

import random
from utils.file_manager import save_data, load_data

class Creature:
    """Class representing a virtual creature with its attributes and behaviors."""
    
    def __init__(self, name, creature_type, color="standard", character_trait="normal"):
        """
        Initializes a new creature with its basic attributes.
        
        Args:
            name (str): The name of the creature
            creature_type (str): The type of creature (e.g., chaton, chiot, dragon...)
            color (str): The color of the creature
            character_trait (str): The dominant character trait
        """
        self.name = name
        self.creature_type = creature_type
        self.hunger = 50  # 0-100, 0 = starving, 100 = satiated
        self.energy = 100  # 0-100, 0 = exhausted, 100 = full of energy
        self.happiness = 50  # 0-100, 0 = unhappy, 100 = very happy
        self.health = 100  # 0-100, 0 = very sick, 100 = perfect health
        self.age = 0  # in days
        self.is_sick = False  # health state (sick or not)
        self.evolution_stage = "bébé"  # evolution stage (bébé, jeune, adulte)
        
        # Customization
        self.color = color
        self.character_trait = character_trait
        
        # Social attributes
        self.friends = []  # List of friends (names)
        self.social_level = 0  # 0-100, 0 = solitary, 100 = very sociable
        
        # Inventory and items
        self.inventory = []  # List of owned items
        self.game_points = 0  # Points earned in mini-games
        
        # Specific modifiers according to creature type
        self.modifiers = self._define_modifiers()
        
        # Apply bonuses according to character trait
        self._apply_bonus_trait()
    
    def _define_modifiers(self):
        """
        Defines specific modifiers according to creature type.
        
        Returns:
            dict: Dictionary containing modifiers for each attribute
        """
        modifiers = {
            "chaton": {"hunger": 1.2, "energy": 0.9, "happiness": 1.1},
            "chiot": {"hunger": 1.3, "energy": 1.2, "happiness": 1.3},
            "dragon": {"hunger": 1.5, "energy": 0.8, "happiness": 0.9},
            "robot": {"hunger": 0.7, "energy": 1.4, "happiness": 0.8},
            "lapin": {"hunger": 1.1, "energy": 1.1, "happiness": 1.2}
        }
        
        return modifiers.get(self.creature_type.lower(), {"hunger": 1.0, "energy": 1.0, "happiness": 1.0})
    
    def _apply_bonus_trait(self):
        """
        Applies bonuses or penalties according to the creature's character trait.
        """
        trait_effects = {
            "joueur": {"happiness": 10, "energy": -5},
            "gourmand": {"hunger": -10, "health": -5},
            "sportif": {"energy": 10, "hunger": -5},
            "paresseux": {"energy": -10, "happiness": 5},
            "curieux": {"happiness": 5, "energy": 5},
            "timide": {"happiness": -5, "social_level": -20},
            "sociable": {"happiness": 5, "social_level": 20},
            "intelligent": {"game_points": 10}
        }
        
        if self.character_trait in trait_effects:
            for attribute, value in trait_effects[self.character_trait].items():
                if hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    new_value = max(0, min(100, current_value + value))
                    setattr(self, attribute, new_value)
    
    def feed(self, food="standard"):
        """
        Feeds the creature, increases its hunger gauge.
        
        Args:
            food (str): Type of food ("standard", "premium" or "malsaine")
            
        Returns:
            str: Message indicating the result of the action
        """
        if food == "standard":
            hunger_gain = 20 * self.modifiers["hunger"]
        elif food == "premium":
            hunger_gain = 30 * self.modifiers["hunger"]
            self.happiness += 5
        elif food == "malsaine":
            hunger_gain = 15 * self.modifiers["hunger"]
            self.health -= 5
        
        self.hunger = min(100, self.hunger + hunger_gain)
        result = self._update_state()
        if result == "death":
            return "death"
        return f"{self.name} a été nourri avec de la nourriture {food}."
    
    def play(self, duration=1):
        """
        Plays with the creature, increases its happiness but reduces its energy.
        
        Args:
            duration (float): Play duration in hours
            
        Returns:
            str: Message indicating the result of the action
        """
        if self.energy < 20:
            return f"{self.name} est trop fatigué pour jouer !"
        
        # Aging - playing also makes time pass
        self.age += duration / 24  # convert hours to days
        
        happiness_gain = 15 * duration
        energy_loss = 10 * duration
        
        self.happiness = min(100, self.happiness + happiness_gain * self.modifiers["happiness"])
        self.energy = max(0, self.energy - energy_loss)
        self.hunger = max(0, self.hunger - 5 * duration)
        
        # Check for evolution based on new age
        evolution = self._check_evolution()
        if evolution:
            return evolution
            
        result = self._update_state()
        if result == "death":
            return "death"
        return f"{self.name} a joué pendant {duration} heure(s) et est maintenant plus heureux !"
    
    def sleep(self, duration=8):
        """
        Makes the creature sleep, restores its energy but reduces its hunger.
        
        Args:
            duration (float): Sleep duration in hours
            
        Returns:
            str: Message indicating the result of the action
        """
        # Aging - sleeping makes time pass
        self.age += duration / 24  # convert hours to days
        
        energy_gain = 10 * duration * self.modifiers["energy"]
        hunger_loss = 5 * duration
        
        self.energy = min(100, self.energy + energy_gain)
        self.hunger = max(0, self.hunger - hunger_loss)
        
        # Check for evolution based on new age
        evolution = self._check_evolution()
        if evolution:
            return evolution
            
        result = self._update_state()
        if result == "death":
            return "death"
        return f"{self.name} a dormi pendant {duration} heures et a récupéré de l'énergie."
    
    def heal(self):
        """
        Heals the creature if it is sick.
        
        Returns:
            str: Message indicating the result of the action
        """
        if not self.is_sick:
            return f"{self.name} n'est pas malade."
        
        self.is_sick = False
        self.health = min(100, self.health + 30)
        
        self._update_state()
        return f"{self.name} a été soigné et se sent mieux !"
    
    def pass_time(self, hours=1):
        """
        Simulates the passage of time and updates the creature's state.
        
        Args:
            hours (float): Number of hours elapsed
            
        Returns:
            str: Message describing what happened during this time
        """
        self.hunger = max(0, self.hunger - 3 * hours)
        self.energy = max(0, self.energy - 2 * hours)
        self.happiness = max(0, self.happiness - 2 * hours)
        
        # Aging - time is explicitly passing
        self.age += hours / 24  # convert hours to days
        
        # Possibility of getting sick
        if random.random() < 0.05 * hours and not self.is_sick:
            self.is_sick = True
            self.health = max(0, self.health - 10)
            result = self._update_state()
            if result == "death":
                return "death"
            return f"{self.name} est tombé malade !"
        
        # Check for evolution based on new age
        evolution = self._check_evolution()
        if evolution:
            return evolution
        
        # Random event
        if random.random() < 0.1 * hours:
            from game.events import generate_random_event
            event = generate_random_event(self)
            result = self._update_state()
            if result == "death":
                return "death"
            return event
        
        result = self._update_state()
        if result == "death":
            return "death"
        return f"{hours} heure(s) se sont écoulées."
    
    def _update_state(self):
        """
        Updates the general state of the creature based on its attributes.
        """
        # If hunger is low, health decreases
        if self.hunger < 20:
            self.health = max(0, self.health - 5)
        
        # If energy is low, happiness decreases
        if self.energy < 20:
            self.happiness = max(0, self.happiness - 5)
        
        # If the creature is sick, its attributes degrade faster
        if self.is_sick:
            self.energy = max(0, self.energy - 2)
            self.happiness = max(0, self.happiness - 2)
            
        # Check if the creature has died
        if self.health <= 0:
            self.health = 0
            return "death"
        
        return None
    
    def _check_evolution(self):
        """
        Checks if the creature can evolve based on its age.
        
        Returns:
            str or None: Evolution message or None if no evolution
        """
        if self.age >= 30 and self.evolution_stage == "bébé":
            self.evolution_stage = "jeune"
            evolution_message = f"{self.name} a évolué en {self.evolution_stage} !"
            from ui.display import display_evolution
            display_evolution(evolution_message)
            return evolution_message
        elif self.age >= 60 and self.evolution_stage == "jeune":
            self.evolution_stage = "adulte"
            evolution_message = f"{self.name} a évolué en {self.evolution_stage} !"
            from ui.display import display_evolution
            display_evolution(evolution_message)
            return evolution_message
        return None
        
    def encounter_creature(self, other_name, other_type):
        """
        Simulates an encounter with another creature.
        
        Args:
            other_name (str): Name of the other creature
            other_type (str): Type of the other creature
            
        Returns:
            str: Description of the encounter
        """
        from game.events import generate_encounter
        
        # Check if it's a friend
        is_friend = other_name in self.friends
        
        # Generate the encounter
        scenario = generate_encounter(self)
        
        # Possibility of becoming friends
        if "amis" in scenario["message"] and other_name not in self.friends:
            self.friends.append(other_name)
            self.social_level = min(100, self.social_level + 10)
            
        # Apply the effects of the encounter
        if "happiness_effect" in scenario:
            self.happiness = max(0, min(100, self.happiness + scenario["happiness_effect"]))
        
        if "energy_effect" in scenario:
            self.energy = max(0, min(100, self.energy + scenario["energy_effect"]))
            
        if "hunger_effect" in scenario:
            self.hunger = max(0, min(100, self.hunger + scenario["hunger_effect"]))
            
        # Meeting other creatures takes time (30 minutes)
        self.age += 0.5 / 24
            
        return scenario["message"]
        
    def play_mini_game(self, game):
        """
        Plays a mini-game and earns rewards.
        
        Args:
            game (str): The chosen mini-game
            
        Returns:
            dict: Result of the mini-game
        """
        from game.mini_games import play_mini_game
        
        # Check if the creature is in a state to play
        if self.energy < 15:
            return {"success": False, "message": f"{self.name} est trop fatigué pour jouer !"}
        
        # Play the mini-game
        result = play_mini_game(game, self.character_trait)
        
        # Apply rewards
        if result["success"]:
            self.happiness = min(100, self.happiness + result["happiness_bonus"])
            self.game_points += result["points"]
            
            # Add the item to the inventory if there is one
            if "item" in result and result["item"]:
                self.inventory.append(result["item"])
        
        # Spend energy
        self.energy = max(0, self.energy - 10)
        
        # Mini-games take time (1 hour)
        self.age += 1.0 / 24
        
        return result
        
    def use_object(self, item):
        """
        Uses an item from the inventory.
        
        Args:
            item (str): Name of the item to use
            
        Returns:
            str: Result of the use
        """
        if item not in self.inventory:
            return f"{self.name} ne possède pas cet objet."
        
        # Effects of different items
        effects = {
            "Friandise": {"hunger": 15, "happiness": 5},
            "Jouet": {"happiness": 15, "energy": -5},
            "Potion d'énergie": {"energy": 30},
            "Potion de santé": {"health": 30, "is_sick": False},
            "Amulette de protection": {"health": 10},
            "Livre magique": {"happiness": 10, "game_points": 5}
        }
        
        # Apply effects
        if item in effects:
            for attribute, value in effects[item].items():
                if attribute == "is_sick":
                    self.is_sick = value
                elif hasattr(self, attribute):
                    current_value = getattr(self, attribute)
                    if isinstance(current_value, (int, float)):
                        new_value = max(0, min(100, current_value + value))
                        setattr(self, attribute, new_value)
            
            # Remove the item from the inventory (except permanent items)
            if item not in ["Amulette de protection", "Livre magique"]:
                self.inventory.remove(item)
            
            # Using items takes a little time (15 minutes)
            self.age += 0.25 / 24
            
            return f"{self.name} a utilisé {item} et en ressent les effets !"
        
        return f"{item} n'a pas d'effet connu."
    
    def get_state(self):
        """
        Returns the current state of the creature as a dictionary.
        
        Returns:
            dict: Current states of the creature
        """
        critical_state = self._check_critical_state()
        
        # Round numeric values to nearest 0.5 for better presentation
        def round_half(value):
            return round(value * 2) / 2
        
        return {
            "nom": self.name,
            "type": self.creature_type,
            "couleur": self.color,
            "trait": self.character_trait,
            "age": round(self.age, 1),
            "stade": self.evolution_stage,
            "faim": round_half(self.hunger),
            "energie": round_half(self.energy),
            "bonheur": round_half(min(100, self.happiness)),  # Cap at 100
            "sante": round_half(min(100, self.health)),  # Cap at 100
            "est_malade": self.is_sick,
            "niveau_social": round_half(self.social_level),
            "amis": self.friends,
            "points_jeu": round(self.game_points),  # Round to integer
            "inventaire": self.inventory,
            "etat_critique": critical_state
        }
    
    def _check_critical_state(self):
        """
        Checks if one of the creature's attributes is in a critical state.
        
        Returns:
            str or None: Alert message or None if everything is fine
        """
        if self.hunger < 20:
            return f"{self.name} a très faim !"
        if self.energy < 20:
            return f"{self.name} est très fatigué !"
        if self.happiness < 20:
            return f"{self.name} est très malheureux !"
        if self.health < 20:
            return f"{self.name} est en mauvaise santé !"
        if self.is_sick:
            return f"{self.name} est malade et a besoin de soins !"
        return None
    
    def save(self, filename="sauvegarde.json"):
        """
        Saves the creature's state to a JSON file.
        
        Args:
            filename (str): Name of the save file
            
        Returns:
            str: Confirmation message
        """
        data = {
            "nom": self.name,
            "type_creature": self.creature_type,
            "couleur": self.color,
            "trait_caractere": self.character_trait,
            "faim": self.hunger,
            "energie": self.energy,
            "bonheur": self.happiness,
            "sante": self.health,
            "age": self.age,
            "est_malade": self.is_sick,
            "stade_evolution": self.evolution_stage,
            "niveau_social": self.social_level,
            "amis": self.friends,
            "points_jeu": self.game_points,
            "inventaire": self.inventory
        }
        
        save_data(data, filename)
        
        return f"Créature sauvegardée dans {filename}"
    
    @classmethod
    def load(cls, filename="sauvegarde.json"):
        """
        Loads a creature from a JSON file.
        
        Args:
            filename (str): Name of the save file
            
        Returns:
            Creature or None: Instance of the creature or None if failure
        """
        data = load_data(filename)
        
        if data:
            # Get customization attributes if they exist
            color = data.get("couleur", "standard")
            character_trait = data.get("trait_caractere", "normal")
            
            creature = cls(data["nom"], data["type_creature"], color, character_trait)
            creature.hunger = data["faim"]
            creature.energy = data["energie"]
            creature.happiness = data["bonheur"]
            creature.health = data["sante"]
            creature.age = data["age"]
            creature.is_sick = data["est_malade"]
            creature.evolution_stage = data["stade_evolution"]
            
            # Load advanced attributes if they exist
            if "niveau_social" in data:
                creature.social_level = data["niveau_social"]
            if "amis" in data:
                creature.friends = data["amis"]
            if "points_jeu" in data:
                creature.game_points = data["points_jeu"]
            if "inventaire" in data:
                creature.inventory = data["inventaire"]
            
            return creature
        
        return None
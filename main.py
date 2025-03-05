"""
Virtual Creature Simulator
Main entry point of the program
"""

import random
from game.game_manager import Game
from ui.menu import main_menu, actions_menu, mini_games_menu, objects_menu, shop_menu, customization_menu, food_menu
from ui.display import display_state, display_home, display_help

def play():
    """
    Main function that runs the game.
    Presents menus and manages the game flow.
    """
    game = Game()
    quit_game = False
    
    # Display welcome
    display_home()
    
    while not quit_game:
        choice = main_menu()
        
        if choice == "1":
            # Create a new creature
            print("\n=== CRÉATION DE CRÉATURE ===")
            print(f"Types disponibles: {', '.join(game.available_types)}")
            name = input("Nom de votre créature: ")
            creature_type = input("Type de créature: ")
            
            # Check if the creature type is valid
            if creature_type.lower() not in map(str.lower, game.available_types):
                print(f"Type de créature invalide. Types disponibles : {', '.join(game.available_types)}.")
                continue
            
            # Display customization menu
            traits = game.get_available_character_traits()
            colors = game.get_available_colors()
            customization = customization_menu(traits, colors, creature_type)
            
            result = game.create_creature(name, creature_type, customization["color"], customization["trait"])
            print(result)
            
            if "a été créé" in result:
                # If creation succeeded, display actions menu
                manage_actions(game)
        
        elif choice == "2":
            # Load an existing creature
            filename = input("Nom du fichier de sauvegarde (défaut: sauvegarde.json): ")
            if not filename:
                filename = "sauvegarde.json"
            
            result = game.load_creature(filename)
            print(result)
            
            if "a été chargé" in result:
                # If loading succeeded, display actions menu
                manage_actions(game)
        
        elif choice == "3":
            # Quit the game
            print("Merci d'avoir joué. À bientôt !")
            quit_game = True
        
        else:
            print("Choix invalide. Veuillez réessayer.")


def manage_actions(game):
    """
    Manages available actions to interact with the creature.
    
    Args:
        game: The game manager instance
    """
    continue_actions = True
    while continue_actions:
        action_choice = actions_menu()
        
        if action_choice == "1":  # Feed
            food = food_menu()
            result = game.do_action("feed", food=food)
            print(result)
            # Check if creature died
            if "décédée" in result:
                continue_actions = False
        
        elif action_choice == "2":  # Play
            print("\n=== JOUER ===")
            try:
                duration = float(input("Durée (en heures): "))
                result = game.do_action("play", duration=duration)
                print(result)
                # Check if creature died
                if "décédée" in result:
                    continue_actions = False
            except ValueError:
                print("Durée invalide. Veuillez entrer un nombre.")
        
        elif action_choice == "3":  # Sleep
            print("\n=== DORMIR ===")
            try:
                duration = float(input("Durée (en heures): "))
                result = game.do_action("sleep", duration=duration)
                print(result)
                # Check if creature died
                if "décédée" in result:
                    continue_actions = False
            except ValueError:
                print("Durée invalide. Veuillez entrer un nombre.")
        
        elif action_choice == "4":  # Heal
            result = game.do_action("heal")
            print(result)
            # Check if creature died
            if "décédée" in result:
                continue_actions = False
        
        elif action_choice == "5":  # Display state
            state = game.get_creature_state()
            weather = game.get_current_weather()
            display_state(state, weather)
        
        elif action_choice == "6":  # Save
            filename = input("Nom du fichier de sauvegarde (défaut: sauvegarde.json): ")
            if not filename:
                filename = "sauvegarde.json"
            result = game.do_action("save", filename=filename)
            print(result)
        
        elif action_choice == "7":  # Explore
            print("\n=== EXPLORER ===")
            result = game.do_action("explore")
            print(result)
            # Check if creature died
            if "décédée" in result:
                continue_actions = False
        
        elif action_choice == "8":  # Meet another creature
            print("\n=== RENCONTRER UNE CRÉATURE ===")
            possible_types = game.available_types.copy()
            state = game.get_creature_state()
            if state["type"].lower() in map(str.lower, possible_types):
                possible_types.remove(state["type"].lower())
            
            print(f"Types disponibles: {', '.join(possible_types)}")
            other_type = input("Type de créature à rencontrer (laissez vide pour aléatoire): ")
            if not other_type:
                other_type = random.choice(possible_types)
            
            other_name = input(f"Nom de la créature à rencontrer (laissez vide pour aléatoire): ")
            if not other_name:
                other_name = f"{other_type.capitalize()}-{random.randint(1, 100)}"
            
            result = game.do_action("meet", type=other_type, name=other_name)
            print(result)
            # Check if creature died
            if "décédée" in result:
                continue_actions = False
        
        elif action_choice == "9":  # Mini-games
            chosen_game = mini_games_menu()
            if chosen_game:
                result = game.do_action("play_mini_game", game=chosen_game)
                print(result)
                # Check if creature died
                if "décédée" in result:
                    continue_actions = False
        
        elif action_choice == "10":  # Inventory and items
            state = game.get_creature_state()
            chosen_item = objects_menu(state["inventaire"])
            if chosen_item:
                result = game.do_action("use_object", item=chosen_item)
                print(result)
                # Check if creature died
                if "décédée" in result:
                    continue_actions = False
        
        elif action_choice == "11":  # Shop
            # Get game points first
            state = game.get_creature_state()
            points = state["points_jeu"]
            
            # Display shop menu with points directly
            catalog = game._get_shop_catalog()
            
            # Pass points to the shop_menu function
            item_to_buy = shop_menu(catalog, points)
            if item_to_buy:
                result = game.do_action("shop", buy=item_to_buy)
                print(result)
        
        elif action_choice == "12":  # Return to main menu
            continue_actions = False

        elif action_choice == "13":  # Help
            display_help()
        
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    play()
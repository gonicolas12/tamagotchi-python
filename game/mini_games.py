"""
Module managing mini-games for the virtual creature simulator.
"""

import random
import time

def play_mini_game(game, character_trait=None):
    """
    Plays a specific mini-game and returns the result.
    
    Args:
        game (str): Name of the mini-game
        character_trait (str): Character trait of the creature playing
        
    Returns:
        dict: Result of the mini-game
    """
    if game == "Devinette":
        return riddle_game(character_trait)
    elif game == "Reflexe":
        return reflex_game(character_trait)
    elif game == "Memoire":
        return memory_game(character_trait)
    else:
        return {"success": False, "message": f"Le mini-jeu '{game}' n'existe pas."}


def riddle_game(character_trait=None):
    """
    Mini-game where the player must guess a number between 1 and 10.
    
    Args:
        character_trait (str): Character trait of the creature
        
    Returns:
        dict: Game result
    """
    # Bonus for intelligent creatures
    hints = 0
    if character_trait == "intelligent":
        hints = 1
    
    secret_number = random.randint(1, 10)
    
    print("\n=== JEU DE DEVINETTE ===")
    print("Devinez un nombre entre 1 et 10.")
    
    if hints > 0:
        if secret_number <= 5:
            print("Indice: Le nombre est entre 1 et 5.")
        else:
            print("Indice: Le nombre est entre 6 et 10.")
    
    tries = 0
    max_tries = 3
    
    while tries < max_tries:
        try:
            attempt = int(input(f"Essai {tries+1}/{max_tries}: "))
            tries += 1
            
            if attempt == secret_number:
                happiness_bonus = 15
                points = 10 * (max_tries - tries + 1)
                item = None
                
                # Chance to get a bonus item
                if random.random() < 0.3:
                    possible_items = ["Friandise", "Jouet"]
                    item = random.choice(possible_items)
                
                return {
                    "success": True,
                    "message": f"Bravo ! Le nombre était bien {secret_number}.",
                    "happiness_bonus": happiness_bonus,
                    "points": points,
                    "item": item
                }
            elif attempt < secret_number:
                print("C'est plus !")
            else:
                print("C'est moins !")
                
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            tries += 1
    
    return {
        "success": False,
        "message": f"Dommage, le nombre était {secret_number}.",
        "happiness_bonus": 5,  # Little bonus for trying
        "points": 0
    }


def reflex_game(character_trait=None):
    """
    Mini-game where the player must press Enter as quickly as possible.
    
    Args:
        character_trait (str): Character trait of the creature
        
    Returns:
        dict: Game result
    """
    import time
    import random
    import threading
    import sys
    import select
    
    # Bonus for sporty creatures
    time_bonus = 0
    if character_trait == "sportif":
        time_bonus = 0.2
    
    print("\n=== JEU DE RÉFLEXE ===")
    print("Appuyez sur Entrée quand vous verrez 'MAINTENANT!'")
    print("Préparez-vous...")
    
    # Variables for false start detection
    false_start = False
    start_signal_shown = False
    
    # Function to check for input before the start signal
    def check_false_start():
        nonlocal false_start
        while not start_signal_shown and not false_start:
            # Check if the user has pressed a key (cross-platform)
            if sys.platform == 'win32':
                import msvcrt
                if msvcrt.kbhit():
                    msvcrt.getch()  # Consume the input
                    false_start = True
                    for _ in range(10):  # Wait a bit before checking again
                        time.sleep(0.1)
                        while msvcrt.kbhit(): # Clear the buffer
                            msvcrt.getch()
                    return
            else:
                # For Linux/Mac
                if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                    sys.stdin.readline()  # Consume the input
                    false_start = True
                    # It's not easy to clear the buffer on Linux/Mac in the same way
                    return
            time.sleep(0.1)
    
    # Start the false start detection thread
    thread = threading.Thread(target=check_false_start)
    thread.daemon = True
    thread.start()
    
    # Random wait time
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)
    
    # If a false start was detected during the wait
    if false_start:
        print("\nFAUX DÉPART ! Vous avez appuyé trop tôt.")
        
        # Clear the input buffer to prevent extra key presses from being counted after the game ends
        if sys.platform == 'win32':
            import msvcrt
            # Clear all pending inputs
            while msvcrt.kbhit():
                msvcrt.getch()
        else:
            # For Linux/Mac, another approach is needed
            # Force a user input which will be ignored, effectively clearing the buffer
            print("Appuyez sur Entrée pour continuer...")
            input()
            
        return {
            "success": False,
            "message": "Attendez le signal la prochaine fois.",
            "happiness_bonus": 0,
            "points": 0,
            "item": None
        }
    
    # Start signal
    start_signal_shown = True
    print("MAINTENANT!")
    start = time.time()
    
    input()  # Waits for the Enter key press
    
    reaction_time = time.time() - start - time_bonus
    reaction_time = max(0, reaction_time)  # Prevents negative times
    
    print(f"Votre temps de réaction: {reaction_time:.3f} secondes")
    
    # Determine success and rewards
    if reaction_time < 0.5:
        happiness_bonus = 20
        points = 30
        item = "Potion d'énergie" if random.random() < 0.4 else None
        message = "Réflexes exceptionnels ! Votre créature est impressionnée !"
        success = True
    elif reaction_time < 1.0:
        happiness_bonus = 15
        points = 20
        item = "Friandise" if random.random() < 0.3 else None
        message = "Très bons réflexes ! Votre créature est contente."
        success = True
    elif reaction_time < 2.0:
        happiness_bonus = 10
        points = 10
        item = None
        message = "Réflexes corrects. Votre créature apprécie l'effort."
        success = True
    else:
        happiness_bonus = 5
        points = 0
        item = None
        message = "Un peu lent... Mais l'important c'est de participer !"
        success = False
    
    return {
        "success": success,
        "message": message,
        "happiness_bonus": happiness_bonus,
        "points": points,
        "item": item
    }


def memory_game(character_trait=None):
    """
    Mini-game where the player must memorize and reproduce a sequence.
    
    Args:
        character_trait (str): Character trait of the creature
        
    Returns:
        dict: Game result
    """
    import os
    import platform
    
    # Function to clear the screen
    def clear_screen():
        # For Windows
        if platform.system() == "Windows":
            os.system('cls')
        # For others (Linux, macOS)
        else:
            os.system('clear')
    
    # Bonus for intelligent creatures
    sequence_length = 6
    if character_trait == "intelligent":
        sequence_length = 8
    
    print("\n=== JEU DE MÉMOIRE ===")
    print(f"Mémorisez la séquence de {sequence_length} symboles.")
    print("Vous aurez 3 secondes pour la mémoriser avant que l'écran ne s'efface.")
    input("Appuyez sur Entrée quand vous êtes prêt...")
    
    # Generate a random sequence
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    sequence = [random.choice(symbols) for _ in range(sequence_length)]
    
    print("\nVoici la séquence:")
    print(' '.join(sequence))
    
    # Wait for 3 seconds before clearing the screen
    time.sleep(3)
    clear_screen()
    
    # Ask the user to reproduce the sequence
    print("=== JEU DE MÉMOIRE ===")
    print("Entrez la séquence (lettres séparées par des espaces):")
    response = input().upper().split()
    
    # Check the length of the response
    if len(response) != sequence_length:
        return {
            "success": False,
            "message": f"La longueur de la séquence est incorrecte. Il fallait {sequence_length} symboles.",
            "happiness_bonus": 5,
            "points": 0
        }
    
    # Count the number of correct symbols
    correct = sum(1 for a, b in zip(sequence, response) if a == b)
    
    # Determine success and rewards
    if correct == sequence_length:
        happiness_bonus = 25
        points = sequence_length * 5
        item = "Livre magique" if random.random() < 0.2 else None
        message = "Mémoire parfaite ! Votre créature est impressionnée !"
        success = True
    elif correct >= sequence_length - 1:
        happiness_bonus = 20
        points = correct * 3
        item = "Jouet" if random.random() < 0.3 else None
        message = "Presque parfait ! Votre créature est contente."
        success = True
    elif correct >= sequence_length / 2:
        happiness_bonus = 15
        points = correct * 2
        item = None
        message = "Pas mal ! Votre créature apprécie l'effort."
        success = True
    else:
        happiness_bonus = 5
        points = 0
        item = None
        message = f"Dommage... La séquence était {' '.join(sequence)}."
        success = False
    
    return {
        "success": success,
        "message": message,
        "happiness_bonus": happiness_bonus,
        "points": points,
        "item": item
    }


def mini_game_list():
    """
    Returns the list of available mini-games with their description.
    
    Returns:
        list: List of available mini-games
    """
    return [
        {
            "nom": "Devinette",
            "description": "Devinez un nombre entre 1 et 10",
            "difficulte": "Facile"
        },
        {
            "nom": "Reflexe",
            "description": "Testez vos réflexes en appuyant sur Entrée au bon moment",
            "difficulte": "Moyen"
        },
        {
            "nom": "Memoire",
            "description": "Mémorisez et reproduisez une séquence de symboles",
            "difficulte": "Difficile"
        }
    ]
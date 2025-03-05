"""
Module managing the different menus of the user interface.
"""

def main_menu():
    """
    Displays the main menu of the game.
    
    Returns:
        str: User's choice
    """
    # ANSI color codes
    BLUE = "\033[38;5;39m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Calculate the length of the title to adjust the separators
    title = "SIMULATEUR DE CRÉATURE VIRTUELLE"
    title_length = len(title) + 7  # +7 for the emojis and space
    
    blue_separator = BLUE + "=" * title_length + RESET
    
    print("\n" + blue_separator)
    print(f"{BOLD}{BLUE}🐾 {title} 🐾{RESET}")
    print(blue_separator)
    print("1. 🆕 Créer une nouvelle créature")
    print("2. 💾 Charger une créature existante")
    print("3. 🚪 Quitter")
    choice = input("✨ Votre choix: ")
    return choice


def actions_menu():
    """
    Displays the menu of possible actions on the creature.
    
    Returns:
        str: User's choice
    """
    # ANSI color codes
    BLUE = "\033[38;5;39m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Total width of the separator (set to a value large enough to be wider than the title)
    separator_width = 40
    
    # Title to display
    title = "ACTIONS"
    
    # Calculate the spaces needed to center the title (considering the emojis)
    total_title_width = len(title) + 6  # Title + 2 emojis + 2 spaces
    padding = (separator_width - total_title_width) // 2
    
    # Create the separator
    blue_separator = BLUE + "=" * separator_width + RESET
    
    print("\n" + blue_separator)

    # Add spaces before the title to center it
    print(f"{BLUE}{' ' * padding}🎮 {BOLD}{title}{RESET}{BLUE} 🎮{RESET}")
    print(blue_separator)
    print("")
    print("1. 🍕 Nourrir")
    print("2. 🎯 Jouer")
    print("3. 💤 Dormir")
    print("4. 🏥 Soigner")
    print("5. 📊 Afficher l'état")
    print("6. 💾 Sauvegarder")
    print("7. 🌍 Explorer (événement aléatoire)")
    print("8. 👋 Rencontrer une autre créature")
    print("9. 🎲 Mini-jeux")
    print("10. 🎒 Inventaire et objets")
    print("11. 🛒 Boutique")
    print("12. 🔙 Retour au menu principal")
    print("13. ❓ Aide")
    choice = input("✨ Votre choix: ")
    return choice


def food_menu():
    """
    Displays the menu of available food types.
    
    Returns:
        str: Chosen food type
    """
    print("\n" + "🍽️" * 13)
    print("🍔 TYPES DE NOURRITURE 🍔")
    print("🍽️" * 13)
    print()

    print("1. 🥗 Standard (équilibré)")
    print("2. 🍱 Premium (délicieux et sain)")
    print("3. 🍫 Malsaine (savoureux mais pas bon pour la santé)")
    choice = input("✨ Votre choix: ")
    
    if choice == "1":
        return "standard"
    elif choice == "2":
        return "premium"
    elif choice == "3":
        return "malsaine"
    else:
        print("⚠️ Choix invalide, nourriture standard sélectionnée par défaut.")
        return "standard"


def mini_games_menu():
    """
    Displays the menu of available mini-games.
    
    Returns:
        str: Name of the chosen mini-game or None if return
    """
    from game.mini_games import mini_game_list
    
    games = mini_game_list()
    
    print("\n" + "🎮" * 9)
    print("🎲  MINI-JEUX  🎲")
    print("🎮" * 9)
    print()
    
    for i, game in enumerate(games, 1):
        difficulty_emoji = "🟢" if game['difficulte'] == "Facile" else "🟡" if game['difficulte'] == "Moyen" else "🔴"
        print(f"{i}. {game['nom']} - {game['description']} ({difficulty_emoji} {game['difficulte']})")
    print(f"{len(games) + 1}. 🔙 Retour")
    
    choice = input("✨ Votre choix: ")
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(games):
            return games[index]["nom"]
        elif index == len(games):
            return None
        else:
            print("⚠️ Choix invalide.")
            return None
    except ValueError:
        print("⚠️ Choix invalide.")
        return None


def objects_menu(inventory):
    """
    Displays the menu of items in the inventory.
    
    Args:
        inventory (list): List of items in the inventory
        
    Returns:
        str: Name of the chosen item or None if return
    """
    if not inventory:
        print("🎒 L'inventaire est vide.")
        input("Appuyez sur Entrée pour continuer...")
        return None
    
    print("\n" + "🎒" * 9)
    print("📦  INVENTAIRE  📦")
    print("🎒" * 9)
    print()

    # Emoji mapping for items
    item_emojis = {
        "Friandise": "🍬",
        "Jouet": "🧸",
        "Potion d'énergie": "⚡",
        "Potion de santé": "💊",
        "Amulette de protection": "🔮",
        "Livre magique": "📚"
    }
    
    for i, item in enumerate(inventory, 1):
        emoji = item_emojis.get(item, "📦")
        print(f"{i}. {emoji} {item}")
    print(f"{len(inventory) + 1}. 🔙 Retour")
    
    choice = input("✨ Choisissez un objet à utiliser: ")
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(inventory):
            return inventory[index]
        elif index == len(inventory):
            return None
        else:
            print("⚠️ Choix invalide.")
            return None
    except ValueError:
        print("⚠️ Choix invalide.")
        return None


def shop_menu(catalog, points=None):
    """
    Displays the shop menu.
    
    Args:
        catalog (list): List of items available in the shop
        points (int, optional): Available points to display
        
    Returns:
        str: Name of the item to buy or None if return
    """

    print("\n" + "🛒" * 8)
    print("🏬  BOUTIQUE  🏬")
    print("🛒" * 8)
    print()

    # Display available points after the shop title
    if points is not None:
        print(f"(Points disponibles: {points})")

    print()

    # Emoji mapping for items
    item_emojis = {
        "Friandise": "🍬",
        "Jouet": "🧸",
        "Potion d'énergie": "⚡",
        "Potion de santé": "💊",
        "Amulette de protection": "🔮",
        "Livre magique": "📚"
    }
    
    for i, item in enumerate(catalog, 1):
        emoji = item_emojis.get(item['nom'], "📦")
        print(f"{i}. {emoji} {item['nom']} - 💰 {item['prix']} points - {item['description']}")
    print(f"{len(catalog) + 1}. 🔙 Retour")
    
    choice = input("✨ Choisissez un objet à acheter: ")
    
    try:
        index = int(choice) - 1
        if 0 <= index < len(catalog):
            return catalog[index]["nom"]
        elif index == len(catalog):
            return None
        else:
            print("⚠️ Choix invalide.")
            return None
    except ValueError:
        print("⚠️ Choix invalide.")
        return None


def customization_menu(traits, colors, creature_type):
    """
    Displays the creature customization menu.
    
    Args:
        traits (dict): Dictionary of available character traits
        colors (dict): Dictionary of available colors by type
        creature_type (str): Selected creature type
        
    Returns:
        dict: Customization choices (trait and color)
    """
    customization = {}
    
    # Choice of character trait
    print("\n" + "🧬" * 13)
    print("🧬  TRAITS DE CARACTÈRE 🧬")
    print("🧬" * 13)
    print()

    # Emoji mapping for traits
    trait_emojis = {
        "normal": "😊",
        "joueur": "🎯",
        "gourmand": "🍽️",
        "sportif": "🏃",
        "paresseux": "😴",
        "curieux": "🔍",
        "timide": "🙈",
        "sociable": "👋",
        "intelligent": "🧠"
    }
    
    traits_list = list(traits.items())
    for i, (trait, description) in enumerate(traits_list, 1):
        emoji = trait_emojis.get(trait, "✨")
        print(f"{i}. {emoji} {trait} - {description}")
    
    # Validate trait choice
    valid_trait = False
    while not valid_trait:
        trait_choice = input("✨ Choisissez un trait de caractère (défaut: normal): ")
        
        # If the user just presses Enter, use the default value
        if trait_choice.strip() == "":
            customization["trait"] = "normal"
            valid_trait = True
        else:
            try:
                trait_index = int(trait_choice) - 1
                if 0 <= trait_index < len(traits_list):
                    customization["trait"] = traits_list[trait_index][0]
                    valid_trait = True
                else:
                    print(f"⚠️ Erreur: Veuillez entrer un nombre entre 1 et {len(traits_list)}.")
            except ValueError:
                print("⚠️ Erreur: Veuillez entrer un nombre valide.")
    
    # Choice of color
    available_colors = colors.get(creature_type.lower(), ["standard"])
    
    print(f"\n" + "🎨" * 13)
    print(f"🎨  COULEURS POUR {creature_type.upper()} 🎨")
    print("🎨" * 13)
    print()
    
    # Color emojis
    color_emojis = {
        "standard": "⚪",
        "gris": "⚪",
        "roux": "🟠",
        "blanc": "⚪",
        "noir": "⚫",
        "tigré": "🐯",
        "marron": "🟤",
        "tacheté": "🐾",
        "rouge": "🔴",
        "vert": "🟢",
        "bleu": "🔵",
        "doré": "🟡",
        "argent": "⚪",
        "or": "🟡"
    }
    
    for i, color in enumerate(available_colors, 1):
        emoji = color_emojis.get(color, "🎨")
        print(f"{i}. {emoji} {color}")
    
    # Validate color choice
    valid_color = False
    while not valid_color:
        color_choice = input("✨ Choisissez une couleur (défaut: standard): ")
        
        # If the user just presses Enter, use the default value
        if color_choice.strip() == "":
            customization["color"] = "standard"
            valid_color = True
        else:
            try:
                color_index = int(color_choice) - 1
                if 0 <= color_index < len(available_colors):
                    customization["color"] = available_colors[color_index]
                    valid_color = True
                else:
                    print(f"⚠️ Erreur: Veuillez entrer un nombre entre 1 et {len(available_colors)}.")
            except ValueError:
                print("⚠️ Erreur: Veuillez entrer un nombre valide.")
    
    return customization
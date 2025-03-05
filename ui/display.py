"""
Module managing the display of creature information.
"""

def display_weather(weather):
    """
    Displays the current weather.
    
    Args:
        weather (dict): Weather information
    """
    if not weather:
        return
        
    # Weather type emojis
    weather_emojis = {
        "soleil": "☀️",
        "pluie": "🌧️",
        "neige": "❄️",
        "orage": "⚡",
        "brouillard": "🌫️",
        "vent": "💨",
        "canicule": "🔥"
    }
    
    emoji = weather_emojis.get(weather["type"], "")
    print(f"\n🌍 Météo actuelle: {emoji} {weather['message']}")
    
    # Display happiness effect
    effect = weather["happiness_effect"]
    if effect > 0:
        print(f"😊 Effet sur le bonheur: +{effect}%")
    else:
        print(f"😔 Effet sur le bonheur: {effect}%")

def display_state(state, weather=None):
    """
    Displays the state of the creature in a formatted way.
    
    Args:
        state (dict): Dictionary containing the creature's states
        weather (dict): Current weather information
    """
    if not state:
        print("❌ Aucune créature à afficher.")
        return
    
    # ANSI color codes
    ORANGE = "\033[38;5;208m"
    YELLOW = "\033[38;5;220m"
    BLUE = "\033[38;5;39m"
    GREEN = "\033[38;5;46m"
    PINK = "\033[38;5;213m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Type emojis
    type_emojis = {
        "chaton": "🐱",
        "chiot": "🐶",
        "dragon": "🐉",
        "robot": "🤖",
        "lapin": "🐰"
    }
    
    # Stage emojis
    stage_emojis = {
        "bébé": "👶",
        "jeune": "👦",
        "adulte": "🧑"
    }
    
    # Character trait emojis
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
    
    type_emoji = type_emojis.get(state['type'].lower(), "🐾")
    stage_emoji = stage_emojis.get(state['stade'], "👤")
    trait_emoji = trait_emojis.get(state['trait'], "✨")
    
    # Create a dynamic title that adapts to the length of the name
    title = f"{BOLD}🌟  ÉTAT DE {state['nom'].upper()}  🌟{RESET}"
    title_length = len(f"🌟  ÉTAT DE {state['nom'].upper()}  🌟")
    
    # The number of stars must be at least equal to the length of the title
    stars_line = "🌟" * ((title_length + 1) // 2)  # Division by 2 because emojis take 2 characters
    
    print("\n" + "🌟" + stars_line)
    print(title)
    print("🌟" + stars_line)
    print()
    print(f"{type_emoji} Nom: {state['nom']} le {state['type']} {state['couleur']}")
    print(f"{trait_emoji} Trait de caractère: {state['trait']}")
    print(f"{stage_emoji} Âge: {state['age']} jours ({state['stade']})")
    
    # Use colored progress bars for attributes
    print(f"\n📊 {BOLD}ATTRIBUTS{RESET}")
    print(f"🍔 Faim:    {ORANGE}{'█' * int(state['faim']/10)}{RESET}{' ' * (10-int(state['faim']/10))} {state['faim']}%")
    print(f"⚡ Énergie: {YELLOW}{'█' * int(state['energie']/10)}{RESET}{' ' * (10-int(state['energie']/10))} {state['energie']}%")
    print(f"😊 Bonheur: {BLUE}{'█' * int(state['bonheur']/10)}{RESET}{' ' * (10-int(state['bonheur']/10))} {state['bonheur']}%")
    print(f"❤️ Santé:   {GREEN}{'█' * int(state['sante']/10)}{RESET}{' ' * (10-int(state['sante']/10))} {state['sante']}%")
    print(f"👋 Social:  {PINK}{'█' * int(state['niveau_social']/10)}{RESET}{' ' * (10-int(state['niveau_social']/10))} {state['niveau_social']}%")
    
    if state["est_malade"]:
        print(f"\n{RED}🤒 ÉTAT: MALADE{RESET}")
    
    if state["etat_critique"]:
        print(f"\n{RED}⚠️ ALERTE: {state['etat_critique']}{RESET}")
    
    # Display friends
    if state["amis"]:
        print(f"\n{BOLD}👥 AMIS{RESET}")
        for friend in state["amis"]:
            print(f"  👤 {friend}")
    
    # Display items
    if state["inventaire"]:
        # Item emojis
        item_emojis = {
            "Friandise": "🍬",
            "Jouet": "🧸",
            "Potion d'énergie": "⚡",
            "Potion de santé": "💊",
            "Amulette de protection": "🔮",
            "Livre magique": "📚"
        }
        
        print(f"\n{BOLD}🎒 INVENTAIRE{RESET}")
        for item in state["inventaire"]:
            emoji = item_emojis.get(item, "📦")
            print(f"  {emoji} {item}")
    
    # Display mini-game points
    print(f"\n💰 Points de jeu: {state['points_jeu']}")
    
    # Display weather if available
    if weather:
        display_weather(weather)


def display_home():
    """
    Displays a welcome message and an introduction to the game.
    """
    # ANSI color codes
    BLUE = "\033[38;5;39m"
    GREEN = "\033[38;5;46m"
    YELLOW = "\033[38;5;220m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    # Calculate the length of the title to adjust the separators
    title = "BIENVENUE DANS LE SIMULATEUR DE CRÉATURE VIRTUELLE"
    title_length = len(title) + 7  # +7 for the emojis and the space
    
    blue_separator = BLUE + "=" * title_length + RESET
    
    print("\n" + blue_separator)
    print(f"{BOLD}{BLUE}🎮 {title} 🎮{RESET}")
    print(blue_separator)
    print(f"\n{GREEN}Dans ce jeu, vous allez prendre soin d'une créature virtuelle.{RESET}")
    print(f"{GREEN}Vous devrez veiller à ses besoins (faim, énergie, bonheur, santé){RESET}")
    print(f"{GREEN}et l'aider à grandir et à évoluer.{RESET}")
    print(f"\n{YELLOW}Chaque créature a des caractéristiques spécifiques qui influencent{RESET}")
    print(f"{YELLOW}ses besoins et son comportement.{RESET}")
    print(f"\n{BOLD}Bon jeu !{RESET}")
    print(blue_separator)
    input(f"\n{BLUE}Appuyez sur Entrée pour continuer...{RESET}")


def display_evolution(message):
    """
    Displays a special message for the evolution of the creature.
    
    Args:
        message (str): Evolution message to display
    """
    # ANSI color codes
    PURPLE = "\033[38;5;165m"
    YELLOW = "\033[38;5;220m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    print("\n" + "✨" * 20)
    print(f"{BOLD}{PURPLE}🌟 ÉVOLUTION DE VOTRE CRÉATURE 🌟{RESET}")
    print("✨" * 20)
    print(f"\n{YELLOW}{message}{RESET}")
    print(f"\n{BOLD}Votre créature a atteint un nouveau stade de développement !{RESET}")
    print("✨" * 20)
    input(f"\n{PURPLE}Appuyez sur Entrée pour continuer...{RESET}")


def display_death(name, age):
    """
    Displays a death message when the creature dies.
    
    Args:
        name (str): The name of the deceased creature
        age (float): The age of the creature in days
    """
    # Calculate days and hours
    days = int(age)
    hours = int((age - days) * 24)
    
    # ANSI color codes
    RED = "\033[31m"
    GRAY = "\033[38;5;240m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    print("\n" + "💔" * 20)
    print(f"{BOLD}{RED}    😢 VOTRE CRÉATURE EST DÉCÉDÉE 😢{RESET}")
    print("💔" * 20)
    print(f"\n{RED}Votre créature {name} est décédée... 😭{RESET}")
    print(f"{GRAY}Elle a vécu {days} jours et {hours} heures.{RESET}")
    print(f"\n{BOLD}Reposez en paix, petit être virtuel. 🕊️{RESET}")
    print("💔" * 20)
    input(f"\n{RED}Appuyez sur Entrée pour continuer...{RESET}")


def display_help():
    """
    Displays a help message with explanations of the different attributes.
    """
    # ANSI color codes
    BLUE = "\033[38;5;39m"
    GREEN = "\033[38;5;46m"
    YELLOW = "\033[38;5;220m"
    ORANGE = "\033[38;5;208m"
    PINK = "\033[38;5;213m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    
    width = 9  # Number of "❓" on the top and bottom lines
    
    # Create the top and bottom lines
    top_bottom = "❓" * width
    
    title = "AIDE"
    
    # Calculate the total space to account for each "❓" occupying 2 characters
    total_spaces = width * 2 - 4
    padding_left = (total_spaces - len(title)) // 2
    padding_right = total_spaces - len(title) - padding_left
    
    middle_line = "❓" + " " * padding_left + f"{BOLD}{BLUE}AIDE{RESET}" + " " * padding_right + "❓"
    
    print("\n" + top_bottom)
    print(middle_line)
    print(top_bottom)
    
    print(f"\n{BOLD}{YELLOW}Attributs de votre créature:{RESET}")
    print(f"{ORANGE}🍔 Faim:{RESET} représente l'état de satisfaction alimentaire.")
    print(f"         Si elle tombe trop bas, votre créature perdra de la santé.")
    print()
    print(f"{YELLOW}⚡ Énergie:{RESET} représente le niveau d'énergie de votre créature.")
    print(f"         Si elle tombe trop bas, votre créature ne pourra plus jouer.")
    print()
    print(f"{BLUE}😊 Bonheur:{RESET} représente le niveau de contentement de votre créature.")
    print(f"         Jouer et interagir avec elle augmente son bonheur.")
    print()
    print(f"{GREEN}❤️ Santé:{RESET} représente l'état de santé général de votre créature.")
    print(f"         Si elle tombe malade, vous devrez la soigner.")
    print(f"         ⚠️ ATTENTION: Si la santé atteint 0, votre créature mourra.")
    print()
    print(f"{PINK}👋 Social:{RESET} représente le niveau de sociabilité de votre créature.")
    print(f"         Rencontrer d'autres créatures augmente son niveau social.")

    
    print(f"\n{BOLD}{YELLOW}Actions disponibles:{RESET}")
    print(f"🍕 Nourrir: augmente la faim de votre créature.")
    print(f"🎯 Jouer: augmente le bonheur mais diminue l'énergie.")
    print(f"💤 Dormir: restaure l'énergie mais diminue la faim.")
    print(f"🏥 Soigner: guérit votre créature si elle est malade.")
    print(f"📊 Afficher l'état: affiche les attributs de votre créature.")
    print(f"💾 Sauvegarder: sauvegarde l'état de votre créature.")
    print(f"🌍 Explorer: déclenche un événement aléatoire.")
    print(f"👋 Rencontrer: interagir avec une autre créature.")
    print(f"🎲 Mini-jeux: jouer à des mini-jeux pour gagner des points.")
    print(f"🎒 Inventaire: utiliser des objets de votre inventaire.")
    print(f"🛒 Boutique: acheter des objets avec vos points de jeu.")
    
    print(f"\n{BOLD}{BLUE}Conseils:{RESET}")
    print(f"• Surveillez régulièrement les jauges de votre créature")
    print(f"• Jouez avec votre créature pour augmenter son bonheur")
    print(f"• Nourrissez-la quand sa jauge de faim est basse")
    print(f"• Faites-la dormir quand son énergie est faible")
    print(f"• Soignez-la dès qu'elle tombe malade")
    print(f"• Participez aux mini-jeux pour gagner des points et des objets")
    
    print("\n" + top_bottom)
    input(f"\n{BLUE}Appuyez sur Entrée pour continuer...{RESET}")
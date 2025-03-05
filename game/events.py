"""
Module managing random events that occur in the game.
"""

import random

def generate_random_event(creature):
    """
    Generates a random event that affects the creature's state.
    
    Args:
        creature: The creature affected by the event
        
    Returns:
        str: Description of the event that occurred
    """
    events = [
        {
            "message": f"🧸 {creature.name} a trouvé un jouet !",
            "effects": {"happiness": 10}
        },
        {
            "message": f"😠 {creature.name} s'est disputé avec une autre créature.",
            "effects": {"happiness": -5}
        },
        {
            "message": f"🍽️ {creature.name} a mangé un bon repas.",
            "effects": {"hunger": 10, "happiness": 5}
        },
        {
            "message": f"🎨 {creature.name} a fait un dessin.",
            "effects": {"happiness": 8}
        },
        {
            "message": f"🌧️ Il pleut dehors, votre créature reste à l'intérieur.",
            "effects": {"energy": 5, "happiness": -3}
        },
        {
            "message": f"☀️ Le soleil brille, votre créature profite du beau temps.",
            "effects": {"happiness": 7, "energy": -3}
        },
        {
            "message": f"💤 {creature.name} a fait une sieste imprévue.",
            "effects": {"energy": 15, "hunger": -5}
        },
        {
            "message": f"😱 {creature.name} a eu peur d'un bruit fort.",
            "effects": {"happiness": -8, "energy": -5}
        },
        {
            "message": f"🍬 Un visiteur a donné une friandise à {creature.name}.",
            "effects": {"hunger": 8, "happiness": 5}
        },
        {
            "message": f"😣 {creature.name} a trébuché et s'est fait mal.",
            "effects": {"happiness": -5, "energy": -10}
        },
        {
            "message": f"🦠 {creature.name} a attrapé le covid-19.",
            "effects": {"happiness": -10, "energy": -15, "health": -20}
        },
        {
            "message": f"💦 {creature.name} a voulu apprendre à nager mais s'est noyé.",
            "effects": {"happiness": -15, "energy": -20, "health": -30}
        },
        {
            "message": f"🤢 {creature.name} a mal digéré un aliment.",
            "effects": {"happiness": -5, "energy": -8, "health": -10}
        },
        {
            "message": f"🎁 {creature.name} a reçu un cadeau inattendu.",
            "effects": {"happiness": 15}
        },
    ]

    # Specific event for each type of creature
    if creature.creature_type.lower() == "chaton":
        events.append({
            "message": f"🐭 {creature.name} a chassé une souris imaginaire.",
            "effects": {"happiness": 10, "energy": -8}
        })
    elif creature.creature_type.lower() == "chiot":
        events.append({
            "message": f"🦴 {creature.name} a enterré un trésor dans le jardin.",
            "effects": {"happiness": 12, "energy": -10}
        })
    elif creature.creature_type.lower() == "dragon":
        events.append({
            "message": f"🔥 {creature.name} a craché une petite flamme.",
            "effects": {"happiness": 15, "energy": -12}
        })
    elif creature.creature_type.lower() == "robot":
        events.append({
            "message": f"🔄 {creature.name} a reçu une mise à jour.",
            "effects": {"energy": 20, "happiness": 8}
        })
    elif creature.creature_type.lower() == "lapin":
        events.append({
            "message": f"🥕 {creature.name} a grignoté une carotte.",
            "effects": {"hunger": 15, "happiness": 8}
        })
    
    # Select a random event
    event = random.choice(events)
    
    # Apply the event effects to the creature
    for attribute, value in event["effects"].items():
        if hasattr(creature, attribute):
            current_value = getattr(creature, attribute)
            
            # Ensure the value stays between 0 and 100
            new_value = max(0, min(100, current_value + value))
            setattr(creature, attribute, new_value)
    
    return event["message"]


def generate_random_weather():
    """
    Generates a weather event that can influence the creature's mood.
    
    Returns:
        dict: Information about the weather event
    """
    weather_events = [
        {"type": "soleil", "message": "Il fait beau aujourd'hui !", "happiness_effect": 5},
        {"type": "pluie", "message": "Il pleut aujourd'hui.", "happiness_effect": -3},
        {"type": "neige", "message": "Il neige aujourd'hui !", "happiness_effect": 2},
        {"type": "orage", "message": "Il y a un orage aujourd'hui.", "happiness_effect": -8},
        {"type": "brouillard", "message": "Il y a du brouillard aujourd'hui.", "happiness_effect": -2},
        {"type": "vent", "message": "Il y a du vent aujourd'hui.", "happiness_effect": -1},
        {"type": "canicule", "message": "Il fait très chaud aujourd'hui !", "happiness_effect": -10}
    ]
    
    return random.choice(weather_events)


def generate_encounter(creature):
    """
    Generates an encounter with another creature.
    
    Args:
        creature: The creature having the encounter
        
    Returns:
        dict: Information about the encounter
    """
    creature_types = ["chaton", "chiot", "dragon", "robot", "lapin", "hamster", "oiseau", "poisson"]
    creature_types.remove(creature.creature_type.lower()) if creature.creature_type.lower() in creature_types else None
    
    other_type = random.choice(creature_types)
    other_name = f"{other_type.capitalize()}-{random.randint(1, 100)}"
    
    # Emoji mapping for creature types
    type_emojis = {
        "chaton": "🐱",
        "chiot": "🐶",
        "dragon": "🐉",
        "robot": "🤖",
        "lapin": "🐰",
        "hamster": "🐹",
        "oiseau": "🐦",
        "poisson": "🐠"
    }
    
    creature_emoji = type_emojis.get(creature.creature_type.lower(), "🐾")
    other_emoji = type_emojis.get(other_type.lower(), "🐾")
    
    scenarios = [
        {
            "message": f"👫 {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} et ils sont devenus amis.",
            "happiness_effect": 15
        },
        {
            "message": f"😠 {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} mais ils ne se sont pas entendus.",
            "happiness_effect": -5
        },
        {
            "message": f"🍽️ {creature_emoji} {creature.name} a partagé sa nourriture avec {other_emoji} {other_name}.",
            "happiness_effect": 8,
            "hunger_effect": -10
        },
        {
            "message": f"🎮 {other_emoji} {other_name} a appris un nouveau jeu à {creature_emoji} {creature.name}.",
            "happiness_effect": 12
        },
        {
            "message": f"👻 {other_emoji} {other_name} a effrayé {creature_emoji} {creature.name} avec une farce.",
            "happiness_effect": -8
        },
        {
            "message": f"🧭 {creature_emoji} {creature.name} a aidé {other_emoji} {other_name} à retrouver son chemin.",
            "happiness_effect": 10
        },
        {
            "message": f"😠 {other_emoji} {other_name} a volé un jouet à {creature_emoji} {creature.name}.",
            "happiness_effect": -5
        },
        {
            "message": f"🎯 {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} et ils ont joué ensemble.",
            "happiness_effect": 10
        },
        {
            "message": f"🍽️ {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} et ils ont partagé un repas.",
            "happiness_effect": 12,
            "hunger_effect": 10
        },
        {
            "message": f"💤 {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} et ils ont fait une sieste ensemble.",
            "happiness_effect": 8,
            "energy_effect": 10
        },
        {
            "message": f"🎨 {creature_emoji} {creature.name} a rencontré {other_emoji} {other_name} et ils ont dessiné ensemble.",
            "happiness_effect": 10
        }
    ]
    
    scenario = random.choice(scenarios)
    return scenario
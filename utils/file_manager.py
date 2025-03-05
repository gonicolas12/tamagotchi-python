"""
Module for managing data files (save and load).
"""

import json
import os

def save_data(data, filename):
    """
    Saves data to a JSON file.
    
    Args:
        data (dict): Data to save
        filename (str): Name of the save file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde: {e}")
        return False


def load_data(filename):
    """
    Loads data from a JSON file.
    
    Args:
        filename (str): Name of the file to load
        
    Returns:
        dict or None: Loaded data or None if error
    """
    if not os.path.exists(filename):
        print(f"Le fichier {filename} n'existe pas.")
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Erreur lors du chargement: {e}")
        return None
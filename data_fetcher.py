import warnings
# Suppress all urllib3 warnings including NotOpenSSLWarning
warnings.filterwarnings('ignore', module='urllib3')
warnings.filterwarnings('ignore', message='.*urllib3.*')

import requests
from typing import Dict, List

ANIMALS_URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = '1NRWsZJaHGhsICY1cICvxA==t2tvwgU62kbF4mwI'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    try:
        # Make a request to the API to get animal data
        response = requests.get(
            ANIMALS_URL,
            params={'name': animal_name},
            headers={'X-Api-Key': API_KEY}
        )
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Convert the response to Python data
        api_data = response.json()
        
        # Create a list to store our animals
        animals = []
        
        # Go through each animal from the API
        for animal_info in api_data:
            # Create an animal dictionary with the information we need
            animal = {
                'name': animal_info.get('name', 'Unknown'),
                'taxonomy': {
                    'kingdom': animal_info.get('taxonomy', {}).get('kingdom', 'Unknown'),
                    'phylum': animal_info.get('taxonomy', {}).get('phylum', 'Unknown'),
                    'class': animal_info.get('taxonomy', {}).get('class', 'Unknown'),
                    'order': animal_info.get('taxonomy', {}).get('order', 'Unknown'),
                    'family': animal_info.get('taxonomy', {}).get('family', 'Unknown'),
                    'genus': animal_info.get('taxonomy', {}).get('genus', 'Unknown'),
                    'scientific_name': animal_info.get('taxonomy', {}).get('scientific_name', 'Unknown')
                },
                'locations': animal_info.get('locations', []),
                'characteristics': {
                    'diet': animal_info.get('characteristics', {}).get('diet', 'Unknown'),
                    'skin_type': animal_info.get('characteristics', {}).get('skin_type', 'Unknown'),
                    'type': animal_info.get('characteristics', {}).get('type', 'Unknown'),
                    'distinctive_feature': animal_info.get('characteristics', {}).get('distinctive_feature', ''),
                    'temperament': animal_info.get('characteristics', {}).get('temperament', ''),
                    'training': animal_info.get('characteristics', {}).get('training', ''),
                    'average_litter_size': animal_info.get('characteristics', {}).get('average_litter_size', ''),
                    'common_name': animal_info.get('characteristics', {}).get('common_name', animal_info.get('name', '')),
                    'slogan': animal_info.get('characteristics', {}).get('slogan', ''),
                    'group': animal_info.get('characteristics', {}).get('group', ''),
                    'color': animal_info.get('characteristics', {}).get('color', ''),
                    'lifespan': animal_info.get('characteristics', {}).get('lifespan', '')
                }
            }
            # Add this animal to our list
            animals.append(animal)
        
        return animals
        
    except requests.RequestException as e:
        print(f"Error getting animal data for {animal_name}: {e}")
        return []
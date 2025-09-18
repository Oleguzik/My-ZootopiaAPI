"""
Animal data HTML generator.

This script reads animal data from a JSON file and generates an HTML page
with styled cards for each animal.
"""

import json
from typing import Dict, List, Optional


def serialize_animal(animal: Dict) -> str:
    """
    Generate HTML card markup for a single animal.

    Args:
        animal: Dictionary containing animal data with 'name', 'characteristics',
               and 'locations' fields.

    Returns:
        str: HTML markup for the animal card or empty string if required fields missing.
    """
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations', [])
    name = animal.get('name')
    
    if not name:
        return ''
    
    # Building the card
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    
    if diet := characteristics.get('diet'):
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
    
    if animal_type := characteristics.get('type'):
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    
    output += '  </p>\n'
    output += '</li>\n'
    
    return output


def read_json_file(filepath: str) -> List[Dict]:
    """
    Read and parse a JSON file.
    Args:
        filepath: Path to the JSON file.
    """
    with open(filepath, 'r') as file:
        return json.load(file)


def read_template_file(filepath: str) -> str:
    """
    Read an HTML template file.

    Args:
        filepath: Path to the template file.
    """
    with open(filepath, 'r') as file:
        return file.read()


def generate_html(animals: List[Dict], template: str) -> str:
    """
    Generate complete HTML by combining animal data with template.

    Args:
        animals: List of animal dictionaries to serialize.
        template: HTML template string containing __REPLACE_ANIMALS_INFO__ placeholder.
    """
    # Generate HTML for all animals
    animals_html = ''
    for animal in animals:
        animals_html += serialize_animal(animal)
    
    # Insert the generated HTML into the template
    return template.replace('__REPLACE_ANIMALS_INFO__', animals_html)


def write_html_file(filepath: str, content: str) -> None:
    """
    Write content to an HTML file.

    Args:
        filepath: Path where the file should be written.
        content: String content to write to the file.
    """
    with open(filepath, 'w') as file:
        file.write(content)


def main() -> None:
    try:
        # Read input files
        animals_data = read_json_file('animals_data.json')
        template = read_template_file('animals_template.html')
        
        # Generate and write HTML
        html_content = generate_html(animals_data, template)
        write_html_file('animals.html', html_content)
        
        print("Successfully generated animals.html!")

    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e.filename}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

import requests
import json
import subprocess
from typing import Dict, List, Optional


ANIMALS_URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = '1NRWsZJaHGhsICY1cICvxA==t2tvwgU62kbF4mwI'

def fetch_animal_data(animal_name: str) -> List[Dict]:
    """
    Get animal information from the internet API.
    
    Args:
        animal_name: Name of the animal to search for
    Returns:
        A list of animals with their information
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

def serialize_animal(animal: Dict) -> str:
    """ Generate HTML card markup for a single animal card """
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations', [])
    name = animal.get('name')
    
    if not name:
        return ''
    
    # Building the card
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <div class="card__text">\n'
    output += '    <ul class="card__details">\n'
    
    if diet := characteristics.get('diet'):
        output += f'      <li><strong>Diet:</strong> {diet}</li>\n'
    
    if locations:
        output += f'      <li><strong>Location:</strong> {locations[0]}</li>\n'
    
    if animal_type := characteristics.get('type'):
        output += f'      <li><strong>Type:</strong> {animal_type}</li>\n'
    
    output += '    </ul>\n'
    output += '  </div>\n'
    output += '</li>\n'
    
    return output


def read_template_file(filepath: str) -> str:
    """ Read an HTML template file """
    with open(filepath, 'r') as file:
        return file.read()


def generate_html(animals: List[Dict], template: str) -> str:
    """ Generate complete HTML by combining animal data with template """
    animals_html = ''
    for animal in animals:
        animals_html += serialize_animal(animal)
    
    # Insert the generated HTML into the template
    return template.replace('__REPLACE_ANIMALS_INFO__', animals_html)


def generate_common_error_html(template: str, error_type: str, title: str, message: str, suggestion: str, emojis: str) -> str:
    """ Generate HTML with a nice error message using CSS classes """
    error_class = f"error-container {error_type}"
    error_html = f'''
        <div class="{error_class}">
            <h2 class="error-title">
                {title}
            </h2>
            <p class="error-message">
                {message}
            </p>
            <p class="error-suggestion">
                {suggestion}
            </p>
            <div class="error-emojis">
                {emojis}
            </div>
        </div>
    '''
    
    # Insert the error message into the template
    return template.replace('__REPLACE_ANIMALS_INFO__', error_html)


def generate_animal_not_found_error(animal_name: str, template: str) -> str:
    """ Generate HTML error for when an animal doesn't exist """
    title = "🦄 Oops! Animal Not Found!"
    message = f'The animal "<strong>{animal_name}</strong>" doesn\'t exist in our database.'
    suggestion = "🤔 Try searching for: fox, cat, dog, lion, elephant, bird, fish or snake! 🐾"
    emojis = "🦊 🐱 🐶 🦁 🐘 🐦 🐟 🐍"
    
    return generate_common_error_html(template, "error-not-found", title, message, suggestion, emojis)


def write_html_file(filepath: str, content: str) -> None:
    """ Write content to an HTML file"""
    with open(filepath, 'w') as file:
        file.write(content)


def get_available_skin_types(animals: List[Dict]) -> List[str]:
    """
    Extract all unique skin_type values from the animals data.

    Args:
        animals: List of animal dictionaries.

    Returns:
        Sorted list of unique skin_type values, including 'Unknown' for missing values.
    """
    skin_types = set()
    has_missing = False
    
    for animal in animals:
        characteristics = animal.get('characteristics', {})
        skin_type = characteristics.get('skin_type')
        
        if skin_type:
            skin_types.add(skin_type)
        else:
            has_missing = True
    
    result = sorted(list(skin_types))
    if has_missing:
        result.append('Unknown (missing skin_type)')
    
    result.insert(0, 'All skin types')
    
    return result


def get_user_skin_type_choice(available_types: List[str]) -> str:
    """
    Display available skin types and get user selection.

    Args:
        available_types: List of available skin type options.

    Returns:
        Selected skin type string.
    """
    print("\nAvailable skin types:")
    for i, skin_type in enumerate(available_types, 1):
        print(f"{i}. {skin_type}")
    
    while True:
        try:
            choice = input("\nEnter the number of your choice: ").strip()
            index = int(choice) - 1
            
            if 0 <= index < len(available_types):
                selected = available_types[index]
                print(f"You selected: {selected}")
                return selected
            else:
                print(f"Please enter a number between 1 and {len(available_types)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(1)


def filter_animals_by_skin_type(animals: List[Dict], selected_skin_type: str) -> List[Dict]:
    """
    Filter animals by the selected skin type.

    Args:
        animals: List of all animal dictionaries.
        selected_skin_type: The skin type to filter by.

    Returns:
        List of animals matching the selected skin type.
    """
    if selected_skin_type == 'All skin types':
        return animals
    
    filtered_animals = []
    
    for animal in animals:
        characteristics = animal.get('characteristics', {})
        skin_type = characteristics.get('skin_type')
        
        # Handle the "Unknown" case
        if selected_skin_type == 'Unknown (missing skin_type)':
            if not skin_type:  # Missing skin_type
                filtered_animals.append(animal)
        else:
            if skin_type == selected_skin_type:
                filtered_animals.append(animal)
    
    return filtered_animals


def get_animal_name_from_user() -> str:
    """ Get animal name from user for searching """
    while True:
        animal_name = input("\nEnter a name of an animal: ").strip()
        if animal_name:
            return animal_name.lower()
        else:
            print("Please enter a valid animal name")


def compile_less_to_css(less_file: str, css_file: str) -> None:
    """ Compile LESS file to CSS using lessc command """
    try:
        subprocess.run(['lessc', less_file, css_file], check=True, capture_output=True)
        print(f"Successfully compiled {less_file} to {css_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LESS: {e.stderr.decode()}")
        raise
    except FileNotFoundError:
        print("Error: lessc not found. Install with: npm install -g less")
        raise


def main() -> None:
    try:
        # Compile LESS to CSS
        compile_less_to_css('styles.less', 'styles.css')
        
        # Get animal name from user
        animal_name = get_animal_name_from_user()
        print(f"Fetching '{animal_name}' data from API...")
        animals_data = fetch_animal_data(animal_name)
        
        if not animals_data:
            print(f"No {animal_name} data found from API. Generating error page...")
            
            # Generate HTML with error message
            template = read_template_file('animals_template.html')
            html_content = generate_animal_not_found_error(animal_name, template)
            write_html_file('animals.html', html_content)
            
            print(f"\nError page generated successfully: animals.html")
            return
            
        print(f"\nFound {len(animals_data)} '{animal_name}'-related animals from API")
        
        # Get available skin types and user selection
        available_skin_types = get_available_skin_types(animals_data)
        
        if not available_skin_types:
            print("No skin types found in the API data.")
            return
        
        selected_skin_type = get_user_skin_type_choice(available_skin_types)
        
        # Filter animals by selected skin type
        filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)
        
        print(f"\nFound {len(filtered_animals)} animals with skin type '{selected_skin_type}'")
        
        # Read template file
        template = read_template_file('animals_template.html')
        
        # Generate and write HTML
        html_content = generate_html(filtered_animals, template)
        write_html_file('animals.html', html_content)
        
        print("HTML was successfully generated to the file animals.html.")

    except FileNotFoundError as e:
        print(f"Error: Required file not found - {e.filename}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

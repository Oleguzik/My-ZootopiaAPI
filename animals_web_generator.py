import json

def main():
    """
    Read animals data from JSON file, generate HTML with animal information.
    """
    try:
        with open('animals_data.json', 'r') as file:
            animals_data = json.load(file)
        
        with open('animals_template.html', 'r') as file:
            html_template = file.read()
        
        # Generate animals output string
        output = ""
        for animal in animals_data:
            characteristics = animal.get('characteristics', {})
            locations = animal.get('locations', [])

            name = animal.get('name')
            diet = characteristics.get('diet')
            animal_type = characteristics.get('type')
            
            if name:
                output += '<li class="cards__item">\n'
                output += f'  <div class="card__title">{name}</div>\n'
                output += '  <p class="card__text">\n'
                
                # Add the details to card text
                if diet:
                    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
                
                if locations:
                    output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
                
                if animal_type:
                    output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
                
                output += '  </p>\n'
                output += '</li>\n'
        
        # Replace the placeholder with the animals data
        new_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)
        
        # Write the new HTML content to a new file
        with open('animals.html', 'w') as file:
            file.write(new_html)

        print("Successfully generated animals.html!")

    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

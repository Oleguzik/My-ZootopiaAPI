import json

def main():
    """
    Read animals data from JSON file and template HTML, build HTML list items
    per animal with <br/> separators, inject into template, and write animals.html.
    """
    try:
        # Read the JSON file
        with open('animals_data.json', 'r') as file:
            animals_data = json.load(file)
        
        # Read the HTML template
        with open('animals_template.html', 'r') as file:
            html_template = file.read()
        
        # Generate animals output string as HTML list items
        output = ""
        for animal in animals_data:
            characteristics = animal.get('characteristics', {})
            locations = animal.get('locations', [])

            item_parts = []
            name = animal.get('name')
            if name:
                item_parts.append(f"Name: {name}<br/>\n")

            diet = characteristics.get('diet')
            if diet:
                item_parts.append(f"Diet: {diet}<br/>\n")

            if locations:
                item_parts.append(f"Location: {locations[0]}<br/>\n")

            animal_type = characteristics.get('type')
            if animal_type:
                item_parts.append(f"Type: {animal_type}<br/>\n")

            # Only add a list item if we have at least one field
            if item_parts:
                output += '<li class="cards__item">\n'
                output += ''.join(item_parts)
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

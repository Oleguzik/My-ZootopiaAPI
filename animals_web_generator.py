import json

def main():
    """
    Read animals data from JSON file, generate HTML with animal information.
    """
    try:
        # Read the JSON file
        with open('animals_data.json', 'r') as file:
            animals_data = json.load(file)
        
        # Read the HTML template
        with open('animals_template.html', 'r') as file:
            html_template = file.read()
        
        # Generate animals output string
        output = ""
        for animal in animals_data:
            name = animal.get('name')
            if name:
                output += f"Name: {name}\n"
            
            characteristics = animal.get('characteristics', {})
            diet = characteristics.get('diet')
            if diet:
                output += f"Diet: {diet}\n"
            
            locations = animal.get('locations', [])
            if locations:
                first_location = locations[0]
                output += f"Location: {first_location}\n"
            
            animal_type = characteristics.get('type')
            if animal_type:
                output += f"Type: {animal_type}\n"
            
            # Add empty line between animals
            output += "\n"
        
        # Replace the placeholder with the animals data
        new_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)
        
        # Write the new HTML content to a new file
        with open('animals.html', 'w') as file:
            file.write(new_html)
        
        print("Successfully generated animals.html!")
        print("Preview of the generated content:")
        print(new_html)
    
    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

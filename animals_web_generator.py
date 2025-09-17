import json

def main():
    """
    Read animals data from JSON file and print formatted information for each animal.
    """
    try:
        # Read the JSON file
        with open('animals_data.json', 'r') as file:
            animals_data = json.load(file)
        
        # Iterate through each animal
        for animal in animals_data:
            # Extract name (always present based on structure)
            name = animal.get('name')
            if name:
                print(f"Name: {name}")
            
            # Extract diet from characteristics
            characteristics = animal.get('characteristics', {})
            diet = characteristics.get('diet')
            if diet:
                print(f"Diet: {diet}")
            
            # Extract first location from locations list
            locations = animal.get('locations', [])
            if locations:
                first_location = locations[0]
                print(f"Location: {first_location}")
            
            # Extract type from characteristics
            animal_type = characteristics.get('type')
            if animal_type:
                print(f"Type: {animal_type}")
            
            # Add empty line between animals
            print()
    
    except FileNotFoundError:
        print("Error: animals_data.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in animals_data.json.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

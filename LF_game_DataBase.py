import csv
from SD_game_Objects import CharacterList, Hero, Monster

FILENAME = "characters.csv"

# Function to save characters into the CSV file
def write_characters(CharacterList):
    with open(FILENAME, mode='w', newline="") as file:
        writer = csv.writer(file)
        for character in CharacterList:
            # Assuming 'character' is either a Hero or Monster instance
            writer.writerow([character.name, character.hp, character.atk, character.defense, character.role])

# Function to upload characters from the CSV file
def get_characters():
    character_list = CharacterList()
    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                name, hp, atk, defense, role = row
                # Instantiate the correct class based on the role
                if role == "boss":
                    character = Monster(name, int(hp), int(atk), int(defense), role)
                elif role in ["healer", "warrior"]:
                    character = Hero(name, int(hp), int(atk), int(defense), role)
                character_list.addCharacter(character)
    except FileNotFoundError:
        pass
    
    return character_list

""" This code is for the UI of a simple game program. It uses the database and object files to allow the user 
to run the game properly. It includes a display menu, the functionality of adding, removing, listing, and playing characters. """

from SD_game_Objects import CharacterList, Hero, Monster
from LF_game_DataBase import write_characters, get_characters



def display_menu():  # commands 
    print("\nCOMMAND MENU")
    print("List     - List all characters")
    print("Add      - Add a character")
    print("Delete   - Delete a character")
    print("Play     - Select a character and Play")
    print("Exit     - Exit program")


def list_characters(character_list): # observing the list function
    if character_list.getCount() == 0:  
        print("No characters available.")
    else:
        print("Available characters:\n")
        
        character_list.display_list()  # accessing the list from teammates work here 


def add_character(character_list):  # add the character function
    name = input("Name: ")
    while True:
        try:
            hp = int(input("Health Points (1-200): "))
            if 1 <= hp <= 200:
                break
            else:
                print("Health Points need to be between 1 and 200. Please try again.")
        except ValueError:
            print("Please enter an integer...")  # getting the health value

    while True:
        try:
            atk = int(input("Attack (1-200): "))
            if 1 <= atk <= 200:
                break
            else:
                print("Attack needs to be between 1 and 200. Please try again.")
        except ValueError:
            print("Please enter an integer...")  # getting the attack value 

    while True:
        try:
            defense = int(input("Defense (1-200): "))
            if 1 <= defense <= 200:
                break
            else:
                print("Defense needs to be between 1 and 200. Please try again.")
        except ValueError:
            print("Please enter an integer...")  # getting the defense value 

    while True:
        char_type = input("Select character type (Hero/Monster): ").strip().lower()  
        if char_type in ["hero", "monster"]:
            break
        else:
            print("Please select a valid character type.")  # while loop checks for the character to be hero or monster

    if char_type == "hero":
        while True:
            role = input("Role (Warrior/Healer): ").strip().lower()
            if role in ["warrior", "healer"]:
                break
            else:
                print("Please select a valid role.")  # if the character is a hero we are getting a role for it 
        new_character = Hero(name, hp, atk, defense, role.capitalize())

    else:
        role = "Boss"  # monsters are assigned Boss role
        new_character = Monster(name, hp, atk, defense, role)  

    
    character_list.addCharacter(new_character)  # adding this new character to the list 
    print("Character successfully added")  # confirming for the user 


def delete_character(character_list):  # function that deletes characters
    while True: 
        name = input("Enter name of the character to remove: ")   
        if character_list.getCharacter(name):  
            character_list.removeCharacter(name)  # access the list and be like if it is in the list then remove it 
            print(f"Character removed successfully")
            print()
            character_list.display_list()   # displays the character chart after
            break
        else:
            print(f"No character named {name}. Please try again.")



def play_game(character_list):  # game moves functionality
    while True: 
        name = input("Enter name of the character to select: ")
        selected_character = character_list.getCharacter(name)
        if selected_character: 
            print(f"{selected_character.name} selected")  # if all is good now we can play the game
            break
        else: 
            print(f"No character named {name}. Please try again.")

    print("ACTIONS:")
    print("Attack   - Attack another character")
    print("Special  - Use special move on another character")
    print("Cancel   - Cancel turn")


    while True:
        action = input("\nSelect action: ").strip().lower()
        if action == "cancel":
            print("Turn was canceled")
            print()
            character_list.display_list()  # displays the character chart after
            break
        elif action in ["attack", "special"]:
            while True:
                target_name = input("Enter the name of the target: ")
                target = character_list.getCharacter(target_name)
                if not target:
                    print(f"No character named {target_name}. Please try again.")
                    continue
                else:

                    if action == "attack":
                        selected_character.attack(target)
                    elif action == "special":
                        selected_character.special_move(target)

                    if target.hp <= 0:
                        character_list.removeCharacter(target.name)  # removes the defeated character name
                    print()
                    character_list.display_list()   # displays the character chart after
                    return  
                    
                    break
        else:
            print("Please enter a valid action..\n")


def main():
    print("Welcome to My Game!")
    character_list = get_characters()   # load characters from the database file 
    display_menu()

    if character_list.getCount() < 2:
            print("\nPlease add at least two characters to continue...", end = "")  # need to first get the starting characters
        
    while character_list.getCount() < 2:
        character_number = character_list.getCount() + 1  
        print(f"\nCharacter {character_number}:")  
        add_character(character_list) # adds the starting characters to the list

    while True:   # while loop to run through the actions from the menu and call the function needed

        command = input("\nCommand: ").strip().lower()
        if command == "list":
            list_characters(character_list)
        elif command == "add":
            add_character(character_list)
            print()
            character_list.display_list()
        elif command == "delete":
            delete_character(character_list)
        elif command == "play":
            play_game(character_list)
        elif command == "exit":
            print("Saving characters...")
            write_characters(character_list)  # Save these characters to the database file
            print("Thank you for playing! Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
            continue
            
        



if __name__ == "__main__":
    main()

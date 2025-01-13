import random

# Base class for all characters
class Character:
    def __init__(self, name, health_points, attack_power, defense_points):
        # Initialize a character with common attributes
        self.name = name  # Character's name
        self.hp = health_points  # Hit points (HP) representing the character's life
        self.atk = attack_power  # Attack power of the character
        self.defense = defense_points  # Defense points reducing incoming damage

    def attack(self, target):
        # Perform a basic attack on a target character
        damage_dealt = max(0, self.atk - target.defense)  # Calculate damage, ensuring it is non-negative
        target.hp -= damage_dealt  # Subtract damage from the target's HP
        print(f"{self.name} attacks {target.name} for {damage_dealt} damage!\n")
        if target.hp <= 0:  # Check if the target's HP drops to zero or below
            print(f"{target.name} has been defeated!\n")

    def show_status(self):
        # Abstract method to show character status; meant to be overridden
        pass

    def special_move(self, target):
        # Abstract method for special moves; meant to be overridden
        pass


# Child class for Hero characters
class Hero(Character):
    def __init__(self, name, health_points, attack_power, defense_points, role):
        # Initialize a hero with additional role attribute
        super().__init__(name, health_points, attack_power, defense_points)
        self.role = role.lower()  # Role of the hero (e.g., healer, warrior)

    def show_status(self):
        # Display the hero's current status in a formatted way
        print(f"{self.name:10} | {self.hp:3} | {self.atk:3} | {self.defense:3} | ({self.role})")

    def special_move(self, target):
        # Perform a special move based on the hero's role
        if self.role == "healer":
            heal_amount = random.randint(50, 60)  # Generate a random heal amount
            target.hp += heal_amount  # Increase the target's HP
            print(f"{self.name} uses Healing, restoring {heal_amount} HP to {target.name}!\n")

        if self.role == "warrior":
            print(f"{self.name} uses Valor and deals triple damage!\n")
            damage_dealt = max(0, self.atk * 3 - target.defense)  # Calculate triple damage
            target.hp -= damage_dealt  # Subtract damage from the target's HP
            print(f"{self.name} attacks {target.name} for {damage_dealt} damage!\n")
            if target.hp <= 0:  # Check if the target is defeated
                print(f"{target.name} has been defeated!\n")


# Child class for Monster characters
class Monster(Character):
    def __init__(self, name, health_points, attack_power, defense_points, role):
        # Initialize a monster with additional role attribute
        super().__init__(name, health_points, attack_power, defense_points)
        self.role = role.lower()  # Role of the monster (e.g., boss)

    def show_status(self):
        # Display the monster's current status in a formatted way
        print(f"{self.name:10} | {self.hp:3} | {self.atk:3} | {self.defense:3} | ({self.role})")

    def special_move(self, target):
        # Perform a special move based on the monster's role
        if self.role == "boss":
            atk_reduction = target.atk // 2  # Calculate attack reduction
            target.atk -= atk_reduction  # Reduce the target's attack power
            print(f"{self.name} lets out a mighty roar, intimidating {target.name} and reducing their attack by {atk_reduction}!\n")


# Class to manage a list of characters
class CharacterList:
    def __init__(self):
        # Initialize an empty list to store characters
        self.__characters = []

    def addCharacter(self, character):
        # Add a character to the list
        self.__characters.append(character)

    def getCharacter(self, name):
        # Retrieve a character by name
        for character in self.__characters:
            if character.name == name:
                return character
        return None  # Return None if character is not found

    def getCharacterNames(self):
        # Return a list of all character names
        return [character.name for character in self.__characters]

    def removeCharacter(self, name):
        # Remove a character by name
        self.__characters = [character for character in self.__characters if character.name != name]

    def getCount(self):
        # Return the number of characters in the list
        return len(self.__characters)

    def __iter__(self):
        # Make the character list iterable
        for character in self.__characters:
            yield character

    def display_list(self):
        # Display all characters in the list with their attributes
        print(f"   {'Name':10} | {' HP':3} | {'ATK':3} | {'DEF':3} |  Role")
        for i, character in enumerate(self.__characters, start=1):
            print(f"{i}. ", end="")
            character.show_status()



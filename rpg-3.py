"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

This version adds new characters, a store with items to purchase and use, and a main menu.
"""
import random

class Character:
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("%s's health: %d" % (self, self.health))
        print("%s's power: %d" % (self, self.power))

    def attack(self, enemy):
        if isinstance(enemy, Zombie):
            print("The attack doesn't seem to have any effect.")
        elif isinstance(enemy, Wizard):
            if random.random() < 0.1:
                enemy.health -= self.power
            else:
                print("The attack did not have any effect!")
        elif enemy.items["Armor"] > 0:
            enemy.health - self.power + int(enemy.items["Armor"])
        else:
            enemy.health -= self.power
            print("%s does %d damage to %s" % (self, self.power, enemy))
            if enemy.health <= 0:
                print("%s is dead." % (enemy.name))

class Hero(Character):
    evade = 0
    coins = 10
    items = {
        "Supertonic": 1,
        "Armor": 0,
        "Evade": 0,
        "Powerboost" : 0}
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        if isinstance(enemy, Zombie):
            print("The attack doesn't seem to have any effect.")
        elif random.random() < 0.2:
            enemy.health - self.power*2
            print("DOUBLE DAMAGE! %s does %d damage to %s" % (self, self.power*2, enemy))
            if enemy.health <= 0:
                print("%s is dead." % (enemy.name))
        else:        
            enemy.health -= self.power
            print("%s does %d damage to %s" % (self, self.power, enemy))
            if enemy.health <= 0:
                print("%s is dead." % (enemy.name))
                if isinstance(enemy, Goblin):
                    self.coins += 5
                    print("You earned 5 coins for defeating %s" % (enemy.name))
                elif isinstance(enemy, Wizard):
                    self.coins += 6
                    print("You earned 6 coins for defeating %s" % (enemy.name))


class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        if self.name == "Doom":
            return True
        elif self.health > 0:
            return True

class Medic(Character):
   def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Wizard(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

main_menu = """-----------------------
What do you want to do?
1. fight enemy
2. do nothing
3. flee
4. use item
5. buy items
-----------------------
> """

#Character Instances
spiderman = Hero("Spiderman", 10, 5)
superman = Hero("Superman", 15, 10)
batman = Hero("Batman", 8, 5)
green_goblin = Goblin("Green Goblin", 6, 2)
venom = Zombie("Venom", 10, 2)
medic = Medic("Dr. House", 10, 1)
shadow = Wizard("Shadowman", 1, 2)
doom = Zombie("Doom", 10, 10) #Doom is an unkillable zombie

welcome_menu = """
><><><><><><><><><><><><><><><
      Dungeon Fighting
a text-based Role-Playing Game
><><><><><><><><><><><><><><><
"""

# #Unused user selection menu
# # user_selection_menu = """
# # Choose your fighter:
# # 1. Spiderman
# # 2. Superman
# # 3. Batman
# """

def transition():
    pause = input("Press any key to continue")
    print("\033c")

running = True
error_message = "Sorry. You don't have enough coins for that right now."

def store_logic():

    store_menu = """*********************
    Welcome to the store! 
    You have *** %d *** coins
    Please choose an item:
    1. SuperTonic - retores 10 health pts (5 coins)
    2. Armor - reduces damage by 2 pts (4 coins)
    3. Evade - reduces chances of taking damage (4 coins)
    4. Powerboost - permanently increases your power (10 coins)
    5. Quit store
    """ % (spiderman.coins)
    
    
    while running == True:
        print("\033c")
        print(store_menu)
        store_selection = input("Which item would you like to purchase? ")
        if store_selection == "1":
            if spiderman.coins >= 5:
                spiderman.items["Supertonic"] += 1
                spiderman.coins -= 5
                print("You bought Supertonic!")
            else:
                print(error_message)
            break
        elif store_selection == "2":
            if spiderman.coins >= 4:
                spiderman.items["Armor"] += 2
                spiderman.coins -= 4
                print("You are now equipped with armor!")
                print(spiderman.items["Armor"])
            else:
                print(error_message)
            break
        elif store_selection == "3":
            if spiderman.coins >= 4:
                spiderman.items["Evade"] += 1
                spiderman.coins -= 4                
                print("You now have Evade equipped!")
            else:
                print(error_message)
            break
        elif store_selection == "4":
            if spiderman.coins >= 10:
                spiderman.items["Powerboost"] += 1
                spiderman.coins -= 10
                print("You now have a powerboost!")
            else:
                print(error_message)
            break
        elif store_selection == "5":
            print("Thanks for shopping in the store.")
            pause = input("Press any key to return to the main menu")
            break
        else:
            print("Please choose a selection from the menu.")

        transition()


def main():
    # print("\033c")
    while venom.alive() and spiderman.alive():
        spiderman.print_status()
        venom.print_status()
        print(main_menu)
        user_input = input()

        if user_input == "1":
            spiderman.attack(venom)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("You got away!")
            break
        elif user_input == "4":
            if spiderman.items != {}:
                print("Your current items: ")
                print(spiderman.items)
                use_item = input("""
                Which item would you like to use?
                1. Supertonic
                2. Powerboost
                >""")
                if use_item == "1" and spiderman.items["Supertonic"] > 0:
                    spiderman.health += 10
                    spiderman.items["Supertonic"] -= 1
                    print("The supertonic added 10 pts to your health!")
                elif use_item == "2":
                    spiderman.power += 5
                    spiderman.items["Powerboost"] -= 1
                    print("The powerboost took effect! Your power is now %d" % (spiderman.power))
            else:
                print("You don't have any items right now.")
        elif user_input == "5":
            if spiderman.coins > 0:
                print("\033c")
                store_logic()  
            else:
                print("Sorry. You don't have enough coins yet.")  
        else:
            print("Invalid input: %r" % user_input)

        if venom.health > 0:
            venom.attack(spiderman)
     
#Clear terminal and print welcome menu
print("\033c")            
print(welcome_menu)
pause = input("Press any key to begin")

main()


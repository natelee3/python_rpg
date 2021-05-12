"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

This version adds a parent class Character and another sub-class Zombie
which can't take any damage.
"""
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
        if self.potion > 0:
            print("Potions remaining: %d" % self.potion)

    def attack(self, enemy):
        if isinstance(enemy, Zombie):
            print("The attack doesn't seem to have any effect.")
        else:
            enemy.health -= self.power
            print("%s does %d damage to %s" % (self, self.power, enemy))
            if enemy.health <= 0:
                print("%s is dead." % (enemy.name))

class Hero(Character):
    potion = 2
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Goblin(Character):
    potion = 0
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
class Zombie(Character):
    potion = 0
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

main_menu = """-----------------------
What do you want to do?
1. fight enemy
2. do nothing
3. flee
4. use potion
-----------------------
> """

spiderman = Hero("Spiderman", 10, 5)
green_goblin = Goblin("Green Goblin", 6, 2)
venom = Zombie("Venom", 10, 2)


def main():

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
            print("You got away! Goodbye.")
            break
        elif user_input == "4":
            if spiderman.potion > 0:
                spiderman.health += 3
                spiderman.potion -= 1
                print("The potion added 3 pts to your health!")
            else:
                print("You don't have any potions left")
        else:
            print("Invalid input: %r" % user_input)

        if venom.health > 0:
            venom.attack(spiderman)
            

main()


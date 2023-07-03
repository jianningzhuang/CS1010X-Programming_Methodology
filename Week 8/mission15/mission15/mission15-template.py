#
# CS1010X --- Programming Methodology
#
# Mission 15 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from engine import *
import simulation
import random

# Rename XX_AI to YourName_AI
class Jianning_AI(Tribute):
    def next_action(self):
        # Next action should return a tuple of what your next action should
        # be. For the full list of tuple that your AI can return, refer to
        # the pdf file

        # As an example: the following code will make your AI just walk around
        # randomly every turn. You do NOT have to use this code if you don't
        # want to!

        #loot everything before the chicken/enemy can, you wouldn't want to face an angry chicken with a loaded bow
        for nearby_object in self.objects_around(): 
            if isinstance(nearby_object, Thing): #only Thing objects can be taken
                return ("TAKE", nearby_object)
            
        #load ranged weapon(if any) with ammo(if any matching)
        for weapon in self.get_weapons():
            if isinstance(weapon, RangedWeapon):
                for item in self.get_inventory():
                    if isinstance(item, Ammo) and item.weapon_type() == weapon.get_name():
                        return ("LOAD", weapon, item)

        #heal up if health is low, provided you have medicine
        if self.get_health() <= 50 and self.get_medicine():
            return ("EAT", self.get_medicine()[0])

        #eat up if hunger is high, provided you have food
        if self.get_hunger() >= 50 and self.get_food():
            return ("EAT", self.get_food()[0])  #just eat first thing you take out, how to be picky in this situation

        #if no weapons, run
        if not self.get_weapons():
            exits = self.get_exits()
            if exits:
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                return ("GO", direction)
            
            
                    
        #attck mercilessly now we are all geared up
        for enemy in self.objects_around(): #there should only be LivingThings left but we can check to make sure
            if isinstance(enemy, LivingThing):
                best_weapon, highest_damage = None, 0
                for weapon in self.get_weapons(): #already checked to make sure at least 1 weapon
                    if isinstance(weapon, RangedWeapon) and weapon.shots_left() == 0: #check to see if rangedweapon is loaded
                        continue
                        
                    if best_weapon == None or weapon.max_damage() > highest_damage:
                        best_weapon = weapon  #pick weapon with highest damage
                        highest_damage = weapon.max_damage()
                if highest_damage == 0:
                    exits = self.get_exits()  #run if cannot deal damage
                    if exits:
                        index = random.randint(0, len(exits)-1)
                        direction = exits[index]
                        return ("GO", direction)
                    
                if enemy.get_health() > 0:
                    return ("ATTACK", enemy, best_weapon)

        #loot any drops from enemy
        for nearby_object in self.objects_around(): 
            if isinstance(nearby_object, Thing): #only Thing objects can be taken
                return ("TAKE", nearby_object)
            

        #move on to next area to loot/kill
        exits = self.get_exits()
        if exits:
            index = random.randint(0, len(exits)-1)
            direction = exits[index]
            return ("GO", direction)
        


        return None #if nothing to interact with or nowhere to go
        

        


        
##        exits = self.get_exits()
##        if exits:
##            index = random.randint(0, len(exits)-1)
##            direction = exits[index]
##            return ("GO", direction)
##
##        # Otherwise, do nothing
##        return None


# NOTE: DO NOT remove the 2 lines of code below.
#
# In particular, you will need to modify the `your_AI = XX_AI` line so that
# `XX_AI` is the name of your AI class.
# For instance, if your AI class is called `MyPrecious_AI`, then you have to
# modify that line to:
#
#     your_AI = MyPrecious_AI
#
# Failure to do so will result in the following exception on Coursemology when
# you run the test cases:
#
#     Traceback (most recent call last):
#       in <module>
#     NameError: name 'your_AI' is not defined
#
# You have been warned!
time_limit = 50 # Modify if your AI needs more than 50 moves for task 2
your_AI = Jianning_AI # Modify if you changed the name of the AI class



##################
# Simulation Code
##################
##########
# Task 1 #
##########
# Goal:
# 1. Your AI should be able to pick up a Weapon / RangedWeapon
# 2. Your AI should be able to kill chicken
# 3. Your AI should be able to pick up chicken_meat after killing chicken

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
simulation.task1(Jianning_AI("Jianning AI", 100), gui=True)


##########
# Task 2 #
##########
## 1. Your AI should be able to pick up a Weapon / RangedWeapon
## 2. Your AI should be able to move around and explore
## 3. Your AI should be able to find harmless Tribute and kill him

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI

time_limit = 20    # You may change the time limit if your AI is taking too long
#simulation.task2(Jianning_AI("Jianning AI", 100), time_limit, gui=True)



#################
# Optional Task
#################
## You can create your own map and see how your AI behaves!

# Define the parameters of the map
def config():
    ## The game should have a 3x3 map
    game_map = GameMap(3)

    ## You can change the numbers to create different kinds of maps for
    ## the optional task.
    game_config = GameConfig()
    game_config.set_item_count(Weapon, 3)
    game_config.set_item_count(Animal, 10)
    game_config.set_item_count(RangedWeapon, 5)
    game_config.set_item_count(Food, 5)
    game_config.set_item_count(Medicine, 5)

    game = GameEngine(game_map, game_config)

    # Add some dummy tributes
    ryan = Tribute("Ryan", 100)
    waihon = Tribute("Wai Hon", 100)
    soedar = Tribute("Soedar", 100)

    game.add_tribute(ryan)
    game.add_tribute(waihon)
    game.add_tribute(soedar)

    # Yes, your AI can fight with himself
    #ai_clone = XX_AI("AI Clone", 100)
    #game.add_tribute(ai_clone)

    return game

# Replace XX_AI with the class name of your AI
# Replace gui=True with gui=False if you do not wish to see the GUI
#simulation.optional_task(Jianning_AI("Jianning AI", 100), config, gui= False)

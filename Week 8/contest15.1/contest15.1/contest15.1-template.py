#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
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


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])
        game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

        return (GameMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              #qualifer_map(4, False),
              #qualifer_map(4, False),
              qualifer_map(4, True),
              #qualifer_map(4, True),
              #qualifer_map(4, True),
             ]



    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
    #match.gui_simulate_round(0)

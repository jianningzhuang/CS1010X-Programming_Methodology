from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
    def next_action(self):

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

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
    # Yong Jing's AI
    
    def act_take(self, obj):
        assert (isinstance(obj, Thing)), f'invalid thing to pick up: {obj}'
        return ('TAKE', obj)

    def act_attack(self, lv_thing, wpn):
        assert (isinstance(lv_thing, LivingThing) and isinstance(wpn, Weapon)), f'invalid weapon or target: {wpn} {lv_thing}'
        return ('ATTACK', lv_thing, wpn)

    def act_load(self, wpn, ammo):
        assert (isinstance(ammo, Ammo) and isinstance(wpn, RangedWeapon)), f'invalid ranged weapon or ammo: {wpn} {ammo}'
        return ('LOAD', wpn, ammo)

    def act_go(self, direction):
        assert (direction == 'UP' or direction == 'DOWN' or direction == 'NORTH' or direction == 'SOUTH'or direction == 'EAST' or direction == 'WEST'), f'invalid direction: {direction}'
        return ('GO', direction)

    def act_eat(self, food):
        assert (isinstance(food, Food)), f'invalid food to eat: {food}'
        return ('EAT', food)
                
    def AI_get_important_objects_around(self):
        #sort objects around based on priority to respond to first
        
        def priority(obj):
            return (isinstance(obj, Tribute),
                    isinstance(obj, Weapon) or isinstance(obj, Ammo) or isinstance(obj, Food),
                    isinstance(obj, Animal)
                    )
        
        return(sorted(self.objects_around(), key = priority, reverse = True))

    def AI_load_weapon(self):
        #loads ammo into weapon. returns None if no suitable ammo to load
        for obj in self.get_inventory():
            if isinstance(obj, Ammo):
                ammo = obj
                for wpn in self.get_weapons():
                    if ammo.weapon_type() == wpn.get_name():
                        return self.act_load(wpn, ammo)
                    
    def AI_attack(self, target):
        #attacks target. returns None if no suitable weapon
                
        def AI_choose_weapon():
            #get usuable weapon with the highest min damage. returns None if no usable weapon
            
            def usable_weapon(wpn):
                #return ( isinstance(wpn, RangedWeapon) and wpn.shots_left() > 0)
                return (not isinstance(wpn, RangedWeapon)) or wpn.shots_left() > 0
                
            weapons = list(filter(usable_weapon, self.get_weapons()))
            if len(weapons) > 0:
                chosen_weapon = weapons[0]
                for wpn in weapons[1:]:
                    if wpn.min_damage() > chosen_weapon.min_damage():
                        chosen_weapon = wpn
                return chosen_weapon
                
        wpn = AI_choose_weapon()
        if wpn != None:
            return self.act_attack(target, wpn)
        
    def AI_load_and_attack(self, target):
        #attacks target or loads weapon if no suitable weapon. returns None if no suitable weapon and no suitable ammo to load
        try_attack = self.AI_attack(target)
        if try_attack != None:
            return try_attack
        else:
            return self.AI_load_weapon()
        
    def AI_fight_or_flight(self, target):
        #attacks target if self has more hp else run away
        if self.get_health() >= target.get_health():
            try_load_and_attack = self.AI_load_and_attack(target)
            if try_load_and_attack != None:
                return try_load_and_attack
            else:
                return self.AI_move()
        else:
            try_run = self.AI_move()
            if try_run == None:
                return self.AI_load_and_attack(target)
            return try_run
        
        
    def AI_heal(self):
        #eats and heals. returns None if no requirement or no food to eat

        def wastage_and_restoration(food, max_health):
            food_val = food.get_food_value()
            hunger_restore = min(self.get_hunger(), food_val)
            food_wastage = max(0, food_val - hunger_restore)

            med_value = food.get_medicine_value() if isinstance(food, Medicine) else 0
            health_restore = min(max_health - self.get_health(), med_value)
            med_wastage = max(0, med_value - health_restore)

            return med_wastage, food_wastage, health_restore, hunger_restore
            
        def choose_food(max_health):                
            def food_priority(food): 
                # Returns medicine in priority of least wastage, restoring most health followed by restoring most hunger followed. returns None if no requirement or no food
                med_wastage, food_wastage, health_restore, hunger_restore = wastage_and_restoration(food, max_health)
                return -med_wastage, -food_wastage, health_restore, hunger_restore

            foods = list(filter(lambda food: food.get_food_value() >= 0, self.get_food()))
            if len(foods) > 0:
                return max(foods, key = food_priority)
            
        AI_MAX_HEALTH = 100
        chosen_food = choose_food(AI_MAX_HEALTH)
        if chosen_food != None:
            med_wastage, food_wastage, _, _ = wastage_and_restoration(chosen_food, AI_MAX_HEALTH)
            if self.get_health() < AI_MAX_HEALTH or self.get_hunger() >= 95 or (med_wastage == 0 and food_wastage == 0):
                return self.act_eat(chosen_food)
        
    def AI_move(self):
        #move to a random place. returns None if no place to go
        if len(self.get_exits()) > 0:
            return self.act_go(random.choice(self.get_exits()))
                
    def next_action(self):        
        for obj in self.AI_get_important_objects_around():
            #Respond to highest priority object
            if isinstance(obj, Tribute):
                #Fight or flight!
                try_attack_or_run_away = self.AI_fight_or_flight(obj)
                if try_attack_or_run_away != None:
                    return try_attack_or_run_away
                else:
                    #Perhaps there are other items in the room that we can use
                    continue
                
            elif isinstance(obj, Weapon) or isinstance(obj, Ammo) or isinstance(obj, Food):
                #Pick up all food, weapon and ammo
                return self.act_take(obj)
            
            elif isinstance(obj, Animal):
                #Attack animal for food
                try_attack_animal = self.AI_load_and_attack(obj)
                if try_attack_animal != None:
                    return try_attack_animal
                else:
                    #Perhaps there are other items in the room that we can use
                    continue

        #If nothing around, eat and heal if neccesary
        try_eat_and_heal = self.AI_heal()
        if try_eat_and_heal != None:
            return try_eat_and_heal
        
        #If nothing around, load weapon if neccesary
        try_load_wpn = self.AI_load_weapon()
        if try_load_wpn != None:
            return try_load_wpn
        
        #If no weapon to load, move to another place
        return self.AI_move()
        
        return None


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

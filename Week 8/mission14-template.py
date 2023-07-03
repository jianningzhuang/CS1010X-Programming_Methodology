#
# CS1010X --- Programming Methodology
#
# Mission 14 Template
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#                                                                               #
# PASTE YOUR MISSION 13 CODE HERE                                               #
#                                                                               #
#################################################################################

class Weapon(Thing):
    
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def min_damage(self):
        return self.min_dmg

    def max_damage(self):
        return self.max_dmg

    def damage(self):
        return random.randint(self.min_dmg, self.max_dmg)

class Ammo(Thing):

    def __init__(self, name, weapon, quantity):
        super().__init__(name)
        self.weapon = weapon
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def weapon_type(self):
        return self.weapon.name

    def remove_all(self):
        self.quantity = 0

class RangedWeapon(Weapon):

    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0

    def shots_left(self):
        return self.shots

    def load(self, ammo):
        if self.name == ammo.weapon_type():
            self.shots += ammo.get_quantity()
            ammo.remove_all()
        
    def damage(self):
        if self.shots == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()

class Food(Thing):
    
    def __init__(self, name, food_value):
        super().__init__(name)
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value
    

class Medicine(Food):

    def __init__(self, name, food_value, medicine_value):
        super().__init__(name, food_value)
        self.medicine_value = medicine_value

    def get_medicine_value(self):
        return self.medicine_value

class Animal(LivingThing):

    def __init__(self, name, health, food_value, threshold = None):
        super().__init__(name, health, threshold)
        self.food_value = food_value
        if threshold == None:
            self.threshold = random.randint(0, 4)
        else:
            self.threshold = threshold

    def get_food_value(self):
        return self.food_value

    def get_threshold(self):
        return self.threshold

    def go_to_heaven(self):
        self.get_place().add_object(Food(self.name + " meat", self.food_value))
        super().go_to_heaven()
    

#################################################################################
#                                                                               #
# MISSION 14                                                                    #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


#############
##  Task 1 ##
#############

class Tribute(Person):


    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        # add hunger property
        self.hunger = 0




    ############
    #  Task 1b #
    ############
    # definition of get_hunger here
    def get_hunger(self):
        return self.hunger




    ############
    #  Task 1c #
    ############
    # definition of add_hunger here
    def add_hunger(self, hunger):
        self.hunger += hunger
        if self.hunger >= 100:
            self.go_to_heaven()




    ############
    #  Task 1d #
    ############
    # definition of reduce_hunger here
    def reduce_hunger(self, hunger):
        self.hunger = max(0, self.hunger - hunger)




    #############
    ##  Task 2 ##
    #############
    # definition of eat here
    def eat(self, food):
        if food in self.get_inventory():
            self.reduce_hunger(food.get_food_value())
            if isinstance(food, Medicine):
                self.add_health(food.get_medicine_value())
            self.remove_item(food)
                
            
        




    ############
    #  Task 3a #
    ############
    # definition of get_weapons here
    def get_weapons(self):
        armskote = ()
        for item in self.get_inventory():
            if isinstance(item, Weapon):
                armskote += (item, )
        return armskote




    ############
    #  Task 3b #
    ############
    # definition of get_food here
    def get_food(self):
        rations = ()
        for item in self.get_inventory():
            if isinstance(item, Food):
                rations += (item, )
        return rations




    ############
    #  Task 3c #
    ############
    # definition of get_medicine here
    def get_medicine(self):
        first_aid_kit = ()
        for item in self.get_inventory():
            if isinstance(item, Medicine):
                first_aid_kit += (item, )
        return first_aid_kit




    #############
    ##  Task 4 ##
    #############
    # definition of attack here
    def attack(self, living_thing, weapon):
        if weapon in self.get_inventory() and living_thing in self.objects_around():
            living_thing.reduce_health(weapon.damage())
            




#############
##  Task 5 ##
#############
# You can either draw it here or attach a image file when you submit.




################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

# Uncomment to test task 4
test_task4()

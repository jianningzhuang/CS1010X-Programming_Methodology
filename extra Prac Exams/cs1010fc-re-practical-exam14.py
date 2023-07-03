#******************************************************
#*
#*  CS1010FC Make Up Practical Exam
#*  AY2013/2014, Semester 2
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

###
### Question 1
###


### Your answer here.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def factorial_digit_sum(n):
    result = 0
    for digit in str(fact(n)):
        result += int(digit)
    return result

# Tests

def test_q1a():
    print("Testing Q1A")
    print("You should come up with some tests here")
    print(fact(5) == 120)
    print("===========================================")

def test_q1b():
    print("Testing Q1B")
    print(factorial_digit_sum(1) == 1)
    print(factorial_digit_sum(6) == 9)
    print(factorial_digit_sum(10) == 27)
    print(factorial_digit_sum(11) == 36)
    print(factorial_digit_sum(12) == 27)
    print("===========================================")

# Uncomment to test question 1
#test_q1a()
#test_q1b()


###
### Question 2
###

import csv
def read_csv(filename):
    with open(filename, 'r') as f:
        lines = tuple(f)[1:] # remove header
        cleaned = tuple(map(lambda x: x[:-1].split(','), lines))
    return cleaned

def mins(time_str):
    hr, m = tuple(map(lambda x: int(x), time_str.split(':')))
    return hr * 60 + m


### Your answers here.

def city(stopover):
    result = ""
    for i in range(len(stopover)):
        if stopover[i] == " " and stopover[i + 1: i + 4] == "via":
            break
        elif stopover[i] == " " and stopover[i + 1] == "(":
            break
        result += stopover[i]
    return result

def list_of_carriers(filename, origin):
    data = read_csv(filename)
    result = []
    for flight in data:
        if city(flight[4]) == origin and flight[2] not in result:
            result.append(flight[2])
    return result


def gap_mode(filename, start, end):
    data = read_csv(filename)
    arrived = []
    for scheduled, arrival, airline, flight, frm, terminal, belt, status in data:
        if status == "Landed" and start <= arrival <= end:
            arrived.append(arrival)
    arrived.sort()
    freq = {}
    for i in range(len(arrived) - 1):
        difference = mins(arrived[i+1]) - mins(arrived[i])
        if difference not in freq:
            freq[difference] = 0
        freq[difference] += 1

    mode = None
    highest = None
    for key, value in freq.items():
        if highest == None or value > highest:
            highest = value
            mode = key
    result = ()
    for key, value in freq.items():
        if value == highest:
            result += (key, )
    return result
#print(sorted(gap_mode('arrivals.csv', '00:00', '12:00')))

#print(sorted(list_of_carriers('arrivals.csv', 'Bangkok')))

# Tests

def test_q2a():
    test1_ans = ['GARUDA INDONESIA', 'TIGERAIR MANDALA', 'LION MENTARI AIRLINES', 'SINGAPORE AIRLINES LTD', 'TIGERAIR SINGAPORE', 'VALUAIR', 'INDONESIA AIRASIA', 'THY TURKISH AIRLINES']
    test2_ans = ['SINGAPORE AIRLINES LTD', 'JETSTAR', 'SILKAIR (SINGAPORE) PTE LTD', 'MALAYSIA AIRLINES', 'AIRASIA', 'TIGERAIR SINGAPORE']
    test3_ans = ['SINGAPORE AIRLINES LTD']
    
    print("Testing Q2A")
    print(sorted(list_of_carriers('arrivals.csv', 'Jakarta')) == sorted(test1_ans))
    print(sorted(list_of_carriers('arrivals.csv', 'Kuala Lumpur')) == sorted(test2_ans))
    print(list_of_carriers('arrivals.csv', 'San Francisco') == test3_ans)
    print("===========================================")
    
def test_q2b():
    print("Testing Q2B")
    print(gap_mode('arrivals.csv', '00:00', '23:59') == (2,))
    print(gap_mode('arrivals.csv', '04:00', '12:00') == (3,))
    print("===========================================")
    

# Uncomment to test question 2
#test_q2a()
#test_q2b()


###
### Question 3
###


### Your answer here.

class Item(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Recipe(object):

    def __init__(self, name, items):
        self.original = name
        self.name = name + " Recipe"
        self.items = items

    def get_name(self):
        return self.name

    def get_items(self):
        return list(self.items)

class Inventory(object):

    def __init__(self):
        self.inventory = []

    def add(self, o):
        if o not in self.inventory:
            self.inventory.append(o)
        merged = True
        while merged:
            merged = False
            for item in self.inventory:
                if isinstance(item, Recipe):
                    if self.enough(item, self.inventory.copy()):
                        self.enough(item, self.inventory)
                        item.name = item.original
                        merged = True
                        break;
            
        
        

    def get_items(self):
        result = ()
        for item in self.inventory:
            result += (item.name, )
        print(result)
        return result

    def enough(self, r, inventory_copy):
        for item in r.get_items():
            found = False
            for o in inventory_copy:
                if o.name == item:
                    inventory_copy.remove(o)
                    found = True
                    break
            if found == False:
                return False
        return True



# Tests
def test_q3():
 
    print("Testing Q3")

    SnY = Recipe("Sange and Yasha", ["Sange", "Yasha"])
    sange = Recipe("Sange", ["Orge Axe", "Belt of Giant Strength"])
    yasha = Recipe("Yasha", ["Blade of Alacrity", "Boots of Elvenskin"])
    axe = Item("Orge Axe")
    belt = Item("Belt of Giant Strength")
    blade = Item("Blade of Alacrity")
    boots = Item("Boots of Elvenskin")
    maginas_items = Inventory()

    maginas_items.add(SnY)
    print(maginas_items.get_items() == ('Sange and Yasha Recipe',))
    maginas_items.add(sange)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha Recipe', 'Sange Recipe')))

    maginas_items.add(blade)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha Recipe', 'Sange Recipe', 'Blade of Alacrity')))

    maginas_items.add(boots)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha Recipe', 'Sange Recipe', 'Blade of Alacrity', 'Boots of Elvenskin')))

    maginas_items.add(yasha)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha Recipe', 'Sange Recipe', 'Yasha')))

    maginas_items.add(belt)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha Recipe', 'Sange Recipe', 'Yasha', 'Belt of Giant Strength')))

    maginas_items.add(axe)
    print(maginas_items.get_items() == ('Sange and Yasha',))

    MKB = Recipe("Monkey King Bar", ["Javelin", "Javelin", "Demon Edge"])
    javelin1 = Item("Javelin")
    javelin2 = Item("Javelin")
    edge = Item("Demon Edge")

    maginas_items.add(javelin2)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha', 'Javelin')))

    maginas_items.add(javelin1)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha', 'Javelin', 'Javelin')))

    maginas_items.add(edge)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha', 'Javelin', 'Javelin', 'Demon Edge')))

    maginas_items.add(MKB)
    print(sorted(maginas_items.get_items()) == sorted(('Sange and Yasha', 'Monkey King Bar')))

# Uncomment to test question 3
test_q3()


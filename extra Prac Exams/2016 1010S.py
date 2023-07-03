##############
# Question 1 #
##############

def next_pos(seq, i):
    for j in range(1, len(seq) + 1):
        if seq[(i + j)%len(seq)] == True:
            return (i + j)%len(seq)


def next_k(seq, i, k):
    if k == 0:
        return i
    else:
        return next_k(seq, next_pos(seq, i), k-1)


def josephus(n, k):
    state = [True]*n
    current = n-1
    for i in range(n - 1):
        next = next_k(state, current, k)
        print(next)
        state[next] = False
        current = next
    return next_k(state, current, k)
    
        
        

# Test cases
def test_q1a():
    print(next_pos((True, True, False, True, False), 1))
    print(next_pos((True, True, False, True, False), 3))
    print(next_pos((False, False, True, False, False, False), 3))

def test_q1b():
    print(next_k((True, True, False, True, False), 0, 2))
    print(next_k((True, True, False, True, False), 2, 3))

def test_q1c():
    print(josephus(10, 2))
    print(josephus(10, 3))
    print(josephus(41, 2))

# Uncomment to test
#test_q1a()
#test_q1b()
#test_q1c()

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows


def highest_year(fname, course):
    data = read_csv(fname)[1:]
    result = {}
    for year, sex, course_, num in data:
        if course_ == course and num.isdigit():
            if year not in result:
                result[year] = 0
            result[year] += int(num)
    highest = None
    ans = None
    for y in result:
        if highest == None or result[y] > highest:
            highest = result[y]
            ans = y
    return (ans, highest)
                
            
    


def gender_ratio(fname, course):
    data = read_csv(fname)[1:]
    result = {}
    for year, sex, course_, num in data:
        if course_ == course and num.isdigit():
            if year not in result:
                result[year] = {}
            result[year][sex] = int(num)
    for y in result:
        if result[y]["Females"] == 0:
            result[y] = float("inf")
        else:
            result[y] = round(result[y]["Males"]/result[y]["Females"],2)
    return result


# Test cases
def test_q2a():
    print(highest_year("graduates.csv", "Law"))
    print(highest_year("graduates.csv", "Medicine"))
    print(highest_year("graduates.csv", "Dentistry"))

def test_q2b():
    print(gender_ratio("graduates.csv", "Law") == 
            {'1993': 0.99, '1994': 0.88, '1995': 0.94, '1996': 0.71,
             '1997': 0.93, '1998': 0.68, '1999': 1.19, '2000': 0.94, 
             '2001': 0.6,  '2002': 0.95, '2003': 0.73, '2004': 0.62,
             '2005': 0.5,  '2006': 0.52, '2007': 0.68, '2008': 0.82,
             '2009': 0.78, '2010': 1.54, '2011': 0.58, '2012': 0.68,
             '2013': 1.06, '2014': 1.02})
    print(gender_ratio("graduates.csv", "Accountancy") == 
            {'1993': 0.74, '1994': 0.72, '1995': 0.73, '1996': 0.61, 
             '1997': 0.5,  '1998': 0.54, '1999': 0.62, '2000': 0.51, 
             '2001': 0.53, '2002': 0.42, '2003': 0.42, '2004': 0.6, 
             '2005': 0.43, '2006': 0.38, '2007': 0.45, '2008': 0.55, 
             '2009': 0.58, '2010': 0.69, '2011': 0.65, '2012': 0.76, 
             '2013': 0.58, '2014': 0.73})
    print(gender_ratio("graduates.csv", "Services") == 
            {'2007': float("inf"),  '2008': 0.33, '2009': 0.36, '2010': 0.83, 
             '2011': 0.48, '2012': 0.82, '2013': 0.34, '2014': 0.62})

# Uncomment to test
#test_q2a()
#test_q2b()

##############
# Question 3 #
##############

class Trainer:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.pokemon = []

    def curr_level(self):
        return self.name + " is currently at level " + str(self.level)

    def list_pokemons(self):
        result = ()
        for pokemon in self.pokemon:
            result += (pokemon.name,)
        return result

    def catch(self, pokemon):
        if pokemon.trainer != None:
            return pokemon.name + " is already owned by " + pokemon.trainer.name
        elif pokemon.level > self.level:
            return pokemon.name + " got away!"
        else:
            self.pokemon.append(pokemon)
            pokemon.trainer = self
            return self.name + " has caught " + pokemon.name

    def give(self, pokemon, new_trainer):
        if pokemon not in self.pokemon:
            return self.name + " does not own " + pokemon.name
        elif self == new_trainer:
            return "Cannot give to self"
        elif pokemon.level > new_trainer.level:
            return new_trainer.name + "'s level is not high enough"
        else:
            self.pokemon.remove(pokemon)
            new_trainer.pokemon.append(pokemon)
            pokemon.trainer = new_trainer
            return pokemon.name + " transfers from " + self.name + " to " + new_trainer.name

class Pokemon:

    def __init__(self, name, level, *evolutions):
        self.name = name
        self.level = level
        self.evolution = evolutions
        self.trainer = None

    def curr_level(self):
        return self.name + " is currently at level " + str(self.level)

    def owned_by(self):
        if self.trainer != None:
            return self.name + "'s owner is " + self.trainer.name
        else:
            return self.name + " has no trainer"

    def power_up(self):
        if self.trainer == None:
            return self.name + " needs a trainer to power up"
        elif self.level < self.trainer.level:
            self.level += 1
            return self.name + " powers up to level " + str(self.level)
        elif self.level == self.trainer.level:
            for pokemon in self.trainer.pokemon:
                if pokemon.level < self.trainer.level:
                    return self.name + " cannot exceed trainer's level"
            self.trainer.level += 1
            return self.trainer.name + " levels up to level " + str(self.trainer.level)

    def evolve(self):
        if self.evolution != ():
            print(self.evolution)
            new = Pokemon(self.evolution[0], self.level, *self.evolution[1:])
            if self.trainer != None:
                self.trainer.pokemon.remove(self)
                self.trainer.pokemon.append(new)
                new.trainer = self.trainer
                self.trainer = None
            return new
                
        else:
            raise EvolveError(self.name + " cannot evolve further", self)

class EvolveError(Exception):

    def __init__(self, message, pokemon):
        self.message = message
        self.pokemon = pokemon

    def __str__(self):
        return self.message

        

# Test cases
def test_q3():
    ash = Trainer("Ash")
    misty = Trainer("Misty")
    pikachu = Pokemon("Pikachu", 1)
    staryu = Pokemon("Staryu", 1)
    p1 = Pokemon("Pidgey", 1)
    p2 = Pokemon("Pidgey", 1)

    print('ash.curr_level():', ash.curr_level() == "Ash is currently at level 1")
    print('ash.list_pokemons():', ash.list_pokemons() == ())
    print('pikachu.curr_level():', pikachu.curr_level() == "Pikachu is currently at level 1")
    print('pikachu.owned_by():', pikachu.owned_by() == "Pikachu has no trainer")
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu needs a trainer to power up")
    print('ash.catch(pikachu):', ash.catch(pikachu) == "Ash has caught Pikachu")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pikachu',])
    print('pikachu.owned_by():', pikachu.owned_by() == "Pikachu's owner is Ash")
    print('pikachu.power_up():', pikachu.power_up() == "Ash levels up to level 2")
    print('ash.curr_level():', ash.curr_level() == "Ash is currently at level 2")
    print('misty.catch(staryu):', misty.catch(staryu) == "Misty has caught Staryu")
    print('ash.catch(staryu):', ash.catch(staryu) == "Staryu is already owned by Misty")
    print('ash.catch(p1):', ash.catch(p1) == "Ash has caught Pidgey")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pikachu'])
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu powers up to level 2")
    print('pikachu.power_up():', pikachu.power_up() == "Pikachu cannot exceed trainer's level")
    print('p1.power_up():', p1.power_up() == "Pidgey powers up to level 2")
    print('ash.catch(p2):', ash.catch(p2) == "Ash has caught Pidgey")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pidgey', 'Pikachu'])
    print('ash.give(p1, ash):', ash.give(p1, ash) == "Cannot give to self")
    print('ash.give(staryu, misty):', ash.give(staryu, misty) == "Ash does not own Staryu")
    print('ash.give(p1, misty):', ash.give(p1, misty) == "Misty's level is not high enough")
    print('ash.give(p2, misty):', ash.give(p2, misty) == "Pidgey transfers from Ash to Misty")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Pidgey', 'Pikachu'])
    print('misty.list_pokemons():', sorted(misty.list_pokemons()) == ['Pidgey', 'Staryu'])
    print('p2.owned_by():', p2.owned_by() == "Pidgey's owner is Misty")
    charmander = Pokemon("Charmander", 3, "Charmelon", "Charizard")
    print('ash.catch(charmander):', ash.catch(charmander) == "Charmander got away!")
    print('p1.power_up():', p1.power_up() == "Ash levels up to level 3")    
    charmelon = charmander.evolve()
    print('charmelon == charmander:', not (charmelon == charmander))
    print('ash.catch(charmelon):', ash.catch(charmelon) == "Ash has caught Charmelon")
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Charmelon', 'Pidgey', 'Pikachu'])
    charizard = charmelon.evolve()
    print('ash.list_pokemons():', sorted(ash.list_pokemons()) == ['Charizard', 'Pidgey', 'Pikachu'])
    print('charizard.owned_by():', charizard.owned_by() == "Charizard's owner is Ash")
    print('charmelon.owned_by():', charmelon.owned_by() == "Charmelon has no trainer")

    try:
        charizard.evolve()
    except EvolveError as e:
        p = e.pokemon
        print(p.curr_level() == "Charizard is currently at level 3")
        print(str(e) == "Charizard cannot evolve further")


# Uncomment to test
test_q3()

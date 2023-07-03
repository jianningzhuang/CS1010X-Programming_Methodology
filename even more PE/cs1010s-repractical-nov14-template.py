#******************************************************
#*
#*  CS1010S Make Up Practical Exam
#*  AY2014/2015, Semester 1
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

def interleave(s1, s2):
    result = ""
    for i in range(len(s1)):
        result += s1[i]
        result += s2[i]
    return result

def full_interleave(s1, s2, n):
    result = ""
    index = 0
    while index < len(s1) and index < len(s2):
        result += s1[index: index + n]
        result += s2[index: index + n]
        index += n
    if index >= len(s1):
        result += s2[index:]
    else:
        result += s1[index:]
    return result

# Tests

def test_q1a():
    print("Testing Q1A")
    print(interleave('abcde', '12345') == 'a1b2c3d4e5')
    print(interleave('Happy', 'Daddy') == 'HDaapdpdyy')
    print(interleave('AAAAA', 'aaaaa') == 'AaAaAaAaAa')
    print("===========================================")

def test_q1b():
    print("Testing Q1B")
    print(full_interleave('abcdefgh', '12345', 2) == 'ab12cd34ef5gh')
    print(full_interleave('abcd', '1234567', 3) == 'abc123d4567')
    print(full_interleave('Does', 'Nothing', 10) == 'DoesNothing')
    print(full_interleave('This c', 's iool!', 3) == 'This is cool!')
    print("===========================================")

# Uncomment to test question 1
#test_q1a()
#test_q1b()



###
### Question 2
###

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

### Your answer here.

def yearly_avg(filename, cat):
    data = read_csv(filename)[1:]
    result = {}
    for year, month, category, session, quota, bids, success, price in data:
        if category == cat:
            if year not in result:
                result[year] = []
            result[year].append(int(price))
    for y in result:
        result[y] = int(round(sum(result[y])/len(result[y]), 0))
        
    return result

def count_exceptions(filename, cat):
    data = read_csv(filename)[1:]
    result = {}
    for year, month, category, session, quota, bids, success, price in data:
        if category == cat or category == "E":
            if (year, month, session) not in result:
                result[(year, month, session)] = {}
            result[(year, month, session)][category] = int(price)
    count = 0
    for s in result:
        if result[s]["E"] < result[s][cat]:
            count += 1
    return count


# Tests
def test_q2a():
    # The below is for comparing decimal numbers in the tests
    global yearly_avg
    _avg = yearly_avg
    
    def rnd(d):
        # Rounding if getting proper dict type
        if type(d) != dict:
            return d
        for k in d:
            d[k] = float("%0.0f" % d[k])
        return d

    yearly_avg = lambda x,y: rnd(_avg(x, y))
    
    print("Testing Q2A")   
    print(yearly_avg('coe-2005-2014.csv', 'A') == {'2005': 16551, '2006': 11187, '2007': 14101, '2008': 12330, '2009': 11600, '2010': 30405, '2011': 48206, '2012': 63898, '2013': 74690, '2014': 67922 })
    print(yearly_avg('coe-2005-2014.csv', 'B') == {'2005': 15709, '2006': 12430, '2007': 15936, '2008': 13412, '2009': 12412, '2010': 39834, '2011': 64938, '2012': 84431, '2013': 78712, '2014': 73329})
    print("===========================================")

def test_q2b():
    print("Testing Q2B")
    print(count_exceptions('coe-2005-2014.csv', 'A') == 10)
    print(count_exceptions('coe-2005-2014.csv', 'B') == 64)
    print(count_exceptions('coe-2005-2014.csv', 'C') == 5)
    print(count_exceptions('coe-2005-2014.csv', 'D') == 0)
    print("===========================================")


# Uncomment to test question 2
#test_q2a()
#test_q2b()



###
### Question 3
###

### Your answer here.

class Spaceship:

    def __init__(self, name, location):
        self.name = name
        self.location_ = location
        self.guardians = []

    def location(self):
        return self.location_

    def go_to(self, planet):
        if self.guardians == []:
            return self.name + " does not have any guardians on board"
        else:
            for guardian in self.guardians:
                if planet in guardian.planets:
                    self.location_ = planet
                    for g in self.guardians:
                        g.location_ = planet
                    return self.name + " travels to " + planet
            return planet + " is not a known location"

    def contains(self):
        result = []
        for guardian in self.guardians:
            result.append(guardian.name)
        return result

class Guardian:

    def __init__(self, name, location, *planets):
        self.name = name
        self.location_ = location
        self.planets = planets
        if location not in self.planets:
            self.planets += (location, )
        self.ship = None

    def known_planets(self):
        result = []
        for planet in self.planets:
            result.append(planet)
        return result

    def board(self, ship):
        if self.location_ != ship.location_:
            return self.name + " cannot board the " + ship.name
        else:
            self.ship = ship
            ship.guardians.append(self)
            common = []
            for g in ship.guardians:
                print(g.name)
                for planet in g.planets:
                    if planet not in common:
                        common.append(planet)
            print(common)
            for g in ship.guardians:
                g.planets = common
            return self.name + " boards the " + ship.name

    def location(self):
        if self.ship != None:
            return self.name + " is on the ship " + self.ship.name + " at the planet " + self.location_
        else:
            return self.name + " is on the planet " + self.location_
        


# Tests

def test_q3():
    print("Testing Q3")

    milano = Spaceship("Milano", "Morag")
    print(milano.location() == 'Morag')

    quill = Guardian("Quill", "Morag","Earth")
    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag']))

    groot = Guardian("Groot", "Earth", "Xandar")
    drax = Guardian("Drax", "Earth", "Nowhere")
    gamora = Guardian("Gamora", "Xandar")
    rocket = Guardian("Rocket", "Nowhere")

    print(milano.contains() == [])
    
    print(milano.go_to("Earth") == 'Milano does not have any guardians on board')
    
    print(rocket.board(milano) == 'Rocket cannot board the Milano')
    print(quill.board(milano) == 'Quill boards the Milano')
    print(milano.go_to("Earth") == 'Milano travels to Earth')
    print(milano.go_to("Xandar") == 'Xandar is not a known location')
    print(milano.location() == 'Earth')
    
    print(sorted(milano.contains()) == sorted(['Quill']))
    print(quill.known_planets())

    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag']))
    print(sorted(groot.known_planets()) == sorted(['Earth', 'Xandar']))
    print(groot.board(milano) == 'Groot boards the Milano')
    print(quill.known_planets())
    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag', 'Xandar']))
    print(sorted(groot.known_planets()) == sorted(['Earth', 'Morag', 'Xandar']))

    print(drax.board(milano) == 'Drax boards the Milano')
    print(sorted(quill.known_planets()) == sorted(['Earth', 'Morag', 'Nowhere', 'Xandar']))
    print(sorted(groot.known_planets()) == sorted(['Earth', 'Morag', 'Nowhere', 'Xandar']))
    print(sorted(drax.known_planets()) == sorted(['Earth', 'Morag', 'Nowhere', 'Xandar']))

    print(milano.go_to("Xandar") == 'Milano travels to Xandar')
    print(gamora.board(milano) == 'Gamora boards the Milano')

    print(rocket.location() == 'Rocket is on the planet Nowhere')
    print(milano.go_to("Nowhere") == 'Milano travels to Nowhere')
    print(rocket.board(milano) == 'Rocket boards the Milano')
    print(rocket.location() == 'Rocket is on the ship Milano at the planet Nowhere')

    print(sorted(milano.contains()) == sorted(['Drax', 'Gamora', 'Groot', 'Quill', 'Rocket']))
    print(milano.go_to("Earth") == 'Milano travels to Earth') # Let's go and save the Earth
    print("===========================================")

# Uncomment to test question 3
test_q3()


# END OF THE TEMPLATE

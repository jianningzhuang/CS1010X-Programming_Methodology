##############
# Question 1 #
##############

### Your answer here.
# Q1A
def valid_move(game, start, end):
    for i in range(len(game)):
        if start in range(game[i][0], game[i][1] + 1):
            if end < game[i+1][0]:
                return True
    return False
            


### Your answer here.
# Q1B
def make_move(game, start, end):
    new_state = []
    for pile in game:
        if start in range(pile[0], pile[1] + 1):
            if start == pile[0] and end >= pile[1]:
                continue
            elif start == pile[0]:
                split1 = [end + 1, pile[1]]
                new_state.append(split1)
                continue
            elif end >= pile[1]:
                split1 = [pile[0], start - 1]
                new_state.append(split1)
                continue
            split1 = [pile[0], start - 1]
            split2 = [end + 1, pile[1]]
            new_state.append(split1)
            new_state.append(split2)
                      
        else:
            new_state.append(pile)
    game.clear()
    game.extend(new_state)
    return game


# Tests
def test_q1a():
    game = [[1, 3], [8, 9], [14,20]]
    print(valid_move(game, 2, 8))
    print(valid_move(game, 4, 7))
    print(valid_move(game, 2, 6))

def test_q1b():
    game = [[1, 20]]
    print(make_move(game, 10, 13))
    print(make_move(game, 4, 7))
    print(make_move(game, 15, 17))


# Uncomment to test question 1
#test_q1a()
#test_q1b()



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
    with open(csvfilename, encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

import math
def get_distance(lat1, long1, lat2, long2):
    """
    Takes in two pairs of lat-long float coordinates,
    returns the distance between the two coordinates
    """
    return round(math.sqrt( (lat1-lat2)**2 + (long1-long2)**2 ), 5)



### Your answer here.
# Q2A

def k_nearest_listings(fname, latitude, longitude, k):
    data = read_csv(fname)[1:]
    result = []
    for ID, name, region, neigh, lat, long, price, review in data:
        result.append([int(ID), get_distance(latitude, longitude, float(lat), float(long))])
    result.sort(key = lambda x: x[1])
    final = list(map(lambda x: x[0], result[:k]))
    i = 0
    while result[k+i][1] == result[k-1][1]:
        final.append(result[k+i][0])
        i += 1
    return final
        


### Your answer here.
# Q2B      
def neighbourhood_price_per_region(fname, region):
    data = read_csv(fname)[1:]
    result = {}
    for ID, name, region_, neigh, lat, long, price, review in data:
        if region_ == region and int(review) >= 1:
            if neigh not in result:
                result[neigh] = [float(price)]
            else:
                result[neigh].append(float(price))
    for elem in result:
        result[elem] = round(sum(result[elem])/len(result[elem]), 2)
    return result
            
        


# Tests
def test_q2a():
    print(k_nearest_listings("listings.csv", 1.38837, 103.67087, 1) == \
        [13756029])
    print(k_nearest_listings("listings.csv", 1.42724, 103.84648, 3) == \
        [9980935, 9105592, 15189554])
    print(k_nearest_listings("listings.csv", 1.29114, 103.87363, 5) == \
        [35199403, 1178486, 17540932, 35219943, 8623041])

def test_q2b():
    print(neighbourhood_price_per_region("listings.csv", "East Region") == \
        {'Tampines': 97.02, 'Bedok': 124.14, 'Pasir Ris': 86.35})
    print(neighbourhood_price_per_region("listings.csv", "North-East Region") == \
        {'Serangoon': 88.4, 'Hougang': 89.16, 'Punggol': 75.0, 'Ang Mo Kio': 80.96, 'Sengkang': 57.02})
    print(neighbourhood_price_per_region("listings.csv", "North Region") == \
        {'Woodlands': 90.02, 'Sembawang': 89.58, 'Central Water Catchment': 110.36, 'Yishun': 96.68, 'Mandai': 56.67, 'Sungei Kadut': 49.0})


# Uncomment to test question 2
#test_q2a()
#test_q2b()    

##############
# Question 3 #
##############

class Doll:
    
    group = {}

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = None
        self.root = self
        Doll.group[self] = [self]

    def encase(self, other):
        if self.child != None:
            return self.name + " already contains " + self.child.name
        elif self.parent != None:
            return self.name + " is currently encased in " + self.parent.name
        elif other.parent != None:
            return other.name + " is currently encased in " + other.parent.name
        else:
            self.child = other
            other.parent = self
            Doll.group[self.root].remove(self)
            self.root = other.root
            Doll.group[other.root].append(self)
            return self.name + " encases " + other.name

    def release(self):
        if self.parent != None:
            return self.name + " is currently encased in " + self.parent.name
        elif self.child == None:
            return self.name + " does not contain any dolls"
        else:
            temp = self.child
            self.child.parent = None
            self.child = None
            return self.name + " releases " + temp.name

    def get_name(self):
        return self.name
    def get_mother(self):
        return self.parent
    def get_daughter(self):
        return self.child

    def series(self):
        result = ()
        for doll in Doll.group[self.root]:
            result += (doll.name,)
        return result

    def deeply_contains(self, other):
        while self != None:
            if self == other:
                return True
            self = self.child
        return False

    def num_encased(self):
    
        path = []
        count = 0
        start = self.root
        while start.parent != None:
            count += 1
            path.append(start.name)
            start = start.parent
        if count == 0:
            return 1
        return count
            
        


# Test cases

def test_q3():
    alice = Doll("Alice")
    betty = Doll("Betty")
    clara = Doll("Clara")
    doris = Doll("Doris")
    
    _=alice.get_name(); print(_ == "Alice", "\talice.get_name():\t", _)
    _=alice.get_mother(); print(_ == None, "\talice.get_mother():\t", _)
    _=alice.get_daughter(); print(_ == None, "\talice.get_daughter():\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice',), "\talice.series():\t", _)
    _=betty.encase(alice); print(_ == "Betty encases Alice", "\tbetty.encase(alice):\t", _)
    _=betty.get_daughter() is alice; print(_ == True, "\tbetty.get_daughter() is alice:\t", _)
    _=alice.get_mother() is betty; print(_ == True, "\talice.get_mother() is betty:\t", _)
    _=betty.encase(clara); print(_ == "Betty already contains Alice", "\tbetty.encase(clara):\t", _)
    _=alice.encase(clara); print(_ == "Alice is currently encased in Betty", "\talice.encase(clara):\t", _)
    _=clara.encase(alice); print(_ == "Alice is currently encased in Betty", "\tclara.encase(alice):\t", _)
    _=clara.encase(betty); print(_ == "Clara encases Betty", "\tclara.encase(betty):\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\talice.series():\t", _)
    _=betty.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\tbetty.series():\t", _)
    _=clara.series(); print(tuple(sorted(_)) == ('Alice', 'Betty', 'Clara'), "\tclara.series():\t", _)
    _=alice.num_encased(); print(_ == 2, "\talice.num_encased():\t", _)
    _=betty.num_encased(); print(_ == 2, "\tbetty.num_encased():\t", _)
    _=clara.num_encased(); print(_ == 2, "\tclara.num_encased():\t", _)
    _=clara.deeply_contains(alice); print(_ == True, "\tclara.deeply_contains(alice):\t", _)
    _=alice.deeply_contains(clara); print(_ == False, "\talice.deeply_contains(clara):\t", _)
    _=alice.release(); print(_ == "Alice is currently encased in Betty", "\talice.release():\t", _)
    _=betty.release(); print(_ == "Betty is currently encased in Clara", "\tbetty.release():\t", _)
    _=clara.release(); print(_ == "Clara releases Betty", "\tclara.release():\t", _)
    _=betty.release(); print(_ == "Betty releases Alice", "\tbetty.release():\t", _)
    _=alice.release(); print(_ == "Alice does not contain any dolls", "\talice.release():\t", _)
    _=alice.series() == betty.series() == clara.series(); print(_ == True, "\talice.series() == betty.series() == clara.series():\t", _)
    _=alice.encase(clara); print(_ == "Alice encases Clara", "\talice.encase(clara):\t", _)
    _=alice.num_encased(); print(_ == 1, "\talice.num_encased():\t", _)
    _=betty.num_encased(); print(_ == 1, "\tbetty.num_encased():\t", _)
    _=clara.num_encased(); print(_ == 1, "\tclara.num_encased():\t", _)
    _=betty.encase(doris); print(_ == "Betty encases Doris", "\tbetty.encase(doris):\t", _)
    _=alice.series(); print(tuple(sorted(_)) == ('Alice', 'Clara'), "\talice.series():\t", _)
    _=betty.series(); print(tuple(sorted(_)) == ('Betty', 'Doris'), "\tbetty.series():\t", _)
    _=clara.series(); print(tuple(sorted(_)) == ('Alice', 'Clara'), "\tclara.series():\t", _)
    _=doris.series(); print(tuple(sorted(_)) == ('Betty', 'Doris'), "\tdoris.series():\t", _)
    
# Uncomment to test question 3
test_q3()    

###
### Question 1
###

# Q1A
def num_triangles(n):
    if n == 0:
        return 1
    else:
        return 3*num_triangles(n-1) + 2


# Q1B
def area(n):
    if n == 0:
        return 1
    else:
        return 0.75*area(n-1)


# Q1C
def row(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        last_row = row(n-1)
        new_row = []
        for i in range(len(last_row) - 1):
            new_row.append((last_row[i] + last_row[i+1])%2)
        new_row = [1] + new_row + [1]
        return new_row
            
        



# Tests
def test_q1a():
    print(num_triangles(0))
    print(num_triangles(1))
    print(num_triangles(2))
    print(num_triangles(3))
    

def test_q1b():
    print(area(0))
    print(area(1))
    print(area(2))
    print(area(3))


def test_q1c():
    print(row(0))
    print(row(1))
    print(row(2))
    print(row(3))
    for i in range(16):        
        print(" "*(15-i), *row(i))

# Uncomment to test question 1
#test_q1a()
#test_q1b()
#test_q1c()   


    

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
# Q2A
def monthly_max(fname, location, year):
    data = read_csv(fname)[1:]
    result = {}
    for station, year_, month, day , mean, max in data:
        if station == location and int(year_) == year:
            if month not in result:
                result[month] = [float(max)]
            else:
                result[month].append(float(max))
    for i in result:
        result[i] = round(sum(result[i])/len(result[i]), 2)
    return result
            


# Q2B
def windest_location(fname, year):
    data = read_csv(fname)[1:]
    result = {}
    for station, year_, month, day , mean, max in data:
        if int(year_) == year:
            if month not in result:
                result[month] = {}
            if station not in result[month]:
                result[month][station] = [float(mean)]
            else:
                result[month][station].append(float(mean))
    for i in result:
        highest = None
        loc = None
        for j in result[i]:
            if highest == None or round(sum(result[i][j])/len(result[i][j]), 2) > highest:
                highest = round(sum(result[i][j])/len(result[i][j]), 2)
                loc = j
        result[i] = (loc, highest)
    return result



# Tests
def test_q2a():
    print(monthly_max("wind.csv", "Changi", 2013) == \
        {'Jan': 32.51, 'Feb': 29.63, 'Mar': 31.86, 'Apr': 33.29,
         'May': 30.48, 'Jun': 30.54, 'Jul': 30.91, 'Aug': 33.98, 
         'Sep': 33.22, 'Oct': 32.56, 'Nov': 28.88, 'Dec': 30.79})
    print(monthly_max("wind.csv", "Paya Lebar", 2015) == \
        {'Jan': 38.35, 'Feb': 39.59, 'Mar': 36.0, 'Apr': 33.06,
         'May': 32.39, 'Jun': 31.9, 'Jul': 37.14, 'Aug': 33.64, 
         'Sep': 30.51, 'Oct': 27.75, 'Nov': 29.11, 'Dec': 36.84})
    print(monthly_max("wind.csv", "Marina Barrage", 2018) == \
        {'Jan': 31.09, 'Feb': 33.93, 'Mar': 31.85})


def test_q2b():
    print(windest_location("wind.csv", 2015) == \
        {'Jan': ('Paya Lebar', 18.0), 'Feb': ('Paya Lebar', 18.84), 
         'Mar': ('Paya Lebar', 13.91), 'Apr': ('Paya Lebar', 10.44), 
         'May': ('East Coast Parkway', 10.87), 
         'Jun': ('East Coast Parkway', 13.03), 
         'Jul': ('East Coast Parkway', 15.75), 
         'Aug': ('East Coast Parkway', 14.66), 
         'Sep': ('East Coast Parkway', 13.01), 
         'Oct': ('East Coast Parkway', 10.06), 
         'Nov': ('Paya Lebar', 8.36), 'Dec': ('Paya Lebar', 11.73)})
    print(windest_location("wind.csv", 2017) == \
        {'Jan': ('Marina Barrage', 16.34), 'Feb': ('Marina Barrage', 18.16), 
         'Mar': ('Marina Barrage', 13.65), 'Apr': ('Marina Barrage', 12.46), 
         'May': ('East Coast Parkway', 11.67), 
         'Jun': ('East Coast Parkway', 11.67), 
         'Jul': ('East Coast Parkway', 14.9), 
         'Aug': ('East Coast Parkway', 13.97), 
         'Sep': ('East Coast Parkway', 11.93), 
         'Oct': ('East Coast Parkway', 10.75), 
         'Nov': ('East Coast Parkway', 10.78), 
         'Dec': ('East Coast Parkway', 11.02)})
    print(windest_location("wind.csv", 2018) == \
        {'Jan': ('Paya Lebar', 12.88), 'Feb': ('Paya Lebar', 20.0), 'Mar': ('Paya Lebar', 13.64)})

# Uncomment to test question 2
#test_q2a()
#test_q2b()   




###
### Question 3
###

class Pilot:

    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold
        self.partners = {}
        self.jaegar = None

    def train(self, partner):
        if self == partner:
            return self.name + " cannot train with self"
        else:
            if partner in self.partners:
                self.partners[partner] += 1
            else:
                self.partners[partner] = 1
            if self in partner.partners:
                partner.partners[self] += 1
            else:
                partner.partners[self] = 1
            return self.name + " trains with " + partner.name

    def show_partners(self):
        result = ()
        for partner, value in self.partners.items():
            result += ((partner.name, value), )
        return result

    def board(self, jaegar):
        if self.jaegar != None:
            return self.name + " is already on " + self.jaegar.name
        else:
            self.jaegar = jaegar
            jaegar.pilots.append(self)
            return self.name + " boards " + jaegar.name

    def alight(self):
        if self.jaegar == None:
            return self.name + " is not on a Jaeger"
        else:
            temp = self.jaegar
            self.jaegar = None
            temp.pilots.remove(self)
            return self.name + " alights from " + temp.name
        


class Jaeger:

    def __init__(self, name):
        self.name = name
        self.pilots = []

    def drift(self):
        if len(self.pilots) < 2:
            return self.name + " has insufficient pilots"
        for i in self.pilots:
            for j in self.pilots:
                if i != j:
                    if i not in j.partners:
                        return i.name + " and " + j.name + " are not compatible"
                    elif i.partners[j] < i.threshold or j.partners[i] < j.threshold:
                        return i.name + " and " + j.name + " are not compatible"

        return "Drift successful. "+ self.name + " is operational"
        
        




def test_q3():
    raleigh = Pilot("Raleigh", 3)
    yancy = Pilot("Yancy", 2)
    mako = Pilot("Mako", 5)

    gipsy = Jaeger("Gipsy Danger")
    crimson = Jaeger("Crimson Typhoon")      
           
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (), "\traleigh.show_partners():\t", _)
    _=raleigh.train(yancy); print(_ == "Raleigh trains with Yancy", "\traleigh.train(yancy):\t", _)
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (('Yancy', 1),), "\traleigh.show_partners():\t", _)
    _=yancy.show_partners(); print(tuple(sorted(_)) == (('Raleigh', 1),), "\tyancy.show_partners():\t", _)
    _=yancy.train(raleigh); print(_ == "Yancy trains with Raleigh", "\tyancy.train(raleigh):\t", _)
    _=raleigh.board(gipsy); print(_ == "Raleigh boards Gipsy Danger", "\traleigh.board(gipsy):\t", _)
    _=yancy.board(gipsy); print(_ == "Yancy boards Gipsy Danger", "\tyancy.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Raleigh and Yancy are not compatible", "\tgipsy.drift():\t", _)
    _=raleigh.train(yancy); print(_ == "Raleigh trains with Yancy", "\traleigh.train(yancy):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)
    _=yancy.board(crimson); print(_ == "Yancy is already on Gipsy Danger", "\tyancy.board(crimson):\t", _)
    _=yancy.alight(); print(_ == "Yancy alights from Gipsy Danger", "\tyancy.alight():\t", _)
    _=gipsy.drift(); print(_ == "Gipsy Danger has insufficient pilots", "\tgipsy.drift():\t", _)
    _=mako.alight(); print(_ == "Mako is not on a Jaeger", "\tmako.alight():\t", _)
    _=mako.board(gipsy); print(_ == "Mako boards Gipsy Danger", "\tmako.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Raleigh and Mako are not compatible", "\tgipsy.drift():\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.show_partners(); print(tuple(sorted(_)) == (('Raleigh', 1),), "\tmako.show_partners():\t", _)
    _=raleigh.show_partners(); print(tuple(sorted(_)) == (('Mako', 1), ('Yancy', 3)), "\traleigh.show_partners():\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=mako.train(raleigh); print(_ == "Mako trains with Raleigh", "\tmako.train(raleigh):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)
    _=yancy.board(gipsy); print(_ == "Yancy boards Gipsy Danger", "\tyancy.board(gipsy):\t", _)
    _=gipsy.drift(); print(_ == "Mako and Yancy are not compatible", "\tgipsy.drift():\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=yancy.train(mako); print(_ == "Yancy trains with Mako", "\tyancy.train(mako):\t", _)
    _=gipsy.drift(); print(_ == "Drift successful. Gipsy Danger is operational", "\tgipsy.drift():\t", _)

# Uncomment to test question 3
test_q3()           

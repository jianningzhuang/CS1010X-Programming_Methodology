###
### Question 1
###

# Q1A
def brake_at(dest, speed):
    result = dest
    while speed > 0:
        speed = speed//2
        result -= speed
    return result


# Q1B
def braking_points(curr, dest, speed):
    result = []
    if curr > brake_at(dest, speed):
        return result
    while curr < dest:
        if (curr + speed) <= brake_at(dest, speed):
            curr += speed
        else:
            result.append(curr)
            speed = speed//2
            curr += speed
    result.append(dest)
    return result



# Tests
def test_q1a():
    print(brake_at(89, 4))
    print(brake_at(89, 10))
    print(brake_at(89, 20))


def test_q1b():
    print(braking_points(44, 89, 10))
    print(braking_points(71, 89, 20))
    print(braking_points(71, 89, 22))


# Uncomment to test
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
# Q2A

    
def monthly_avg(fname, currency, year, component):
    data = read_csv(fname)[1:]
    avg = {}
    index = {"Open":4, "High":5, "Low":6, "Close":7, "Volume":8, "Market Cap":9}
    for elem in data:
        if int(elem[0]) == year and elem[3] == currency:
            if elem[1] not in avg:
                avg[elem[1]] = []
            avg[elem[1]].append(float(elem[index[component]]))
    for m in avg:
        avg[m] = round(sum(avg[m])/len(avg[m]), 4)
    return avg
            


# Q2B
def highest_gain(fname, year, component):
    data = read_csv(fname)[1:]
    result = {}
    index = {"Open":4, "High":5, "Low":6, "Close":7, "Volume":8, "Market Cap":9}
    for elem in data:
        if int(elem[0]) == year:
            if elem[1] not in result:
                result[elem[1]] = {}
            if elem[3] not in result[elem[1]]:
                result[elem[1]][elem[3]] = []
            result[elem[1]][elem[3]].append(float(elem[index[component]]))
    for m in result:
        max_val = None
        max_c = None
        for c in result[m]:
            highest = None
            lowest = None
            for value in result[m][c]:
                if highest == None or value > highest:
                    highest = value
                if lowest == None or value < lowest:
                    lowest = value
            gain = round((((highest/lowest) - 1)*100), 2)
            if max_val == None or gain > max_val:
                max_val = gain
                max_c = c
        result[m] = (max_c, max_val)
    return result



## BONUS Q2C ##
def max_single_sell(fname, currency, component):
    pass



# Tests
def test_q2a():
    print(monthly_avg('crypto.csv', 'ETH', 2017, 'Close') == \
        {'Nov': 296.4443, 'Oct': 306.2474, 'Sep': 293.0473, 
         'Aug': 301.6094, 'Jul': 224.1239, 'Jun': 313.7343, 
         'May': 125.7494, 'Apr': 50.3367, 'Mar': 34.7916, 
         'Feb': 12.3711, 'Jan': 10.2013})

    print(monthly_avg('crypto.csv', 'BTC', 2013, 'High') == \
        {'Dec': 856.4419, 'Nov': 569.307, 'Oct': 161.9442, 
         'Sep': 134.164, 'Aug': 116.0023, 'Jul': 93.869, 
         'Jun': 111.3007, 'May': 123.949, 'Apr': 143.4667})


def test_q2b():
    print(highest_gain('crypto.csv', 2017, "Volume") == \
        {'Nov': ('XPR', 695.17), 'Oct': ('XPR', 3485.19), 
         'Sep': ('LTC', 1792.14), 'Aug': ('XPR', 5524.07), 
         'Jul': ('LTC', 1354.52), 'Jun': ('XPR', 1071.13), 
         'May': ('ETH', 2302.35), 'Apr': ('XPR', 4537.85), 
         'Mar': ('XPR', 7003.02), 'Feb': ('ETH', 1049.67), 
         'Jan': ('XPR', 1975.93)})
 
    print(highest_gain('crypto.csv', 2013, "Market Cap") == \
        {'Dec': ('XPR', 272.37), 'Nov': ('LTC', 1862.94), 
         'Oct': ('BTC', 88.94), 'Sep': ('XPR', 171.23), 
         'Aug': ('XPR', 109.9), 'Jul': ('BTC', 59.08), 
         'Jun': ('LTC', 52.22), 'May': ('LTC', 48.27), 
         'Apr': ('BTC', 7.15)})


def test_q2c():
    print(max_single_sell('crypto.csv', 'ETH', 'Close'))
    print(max_single_sell('crypto.csv', 'BTC', 'Close'))
    print(max_single_sell('crypto.csv', 'DASH', 'Close'))


#test_q2a()
test_q2b()
##test_q2c()




###
### Question 3
###

### Your answer here.
class Entity:
    pass

class Overmind:
    pass



# Tests
def test_q3():
    demodog    = Entity('Demodog', 10)
    demogorgon = Entity('Demogorgon', 50)
    dartagnan  = Entity("D'artagnan", 20)
    mindflayer = Overmind('Mindflayer', 25)
    mindreader = Overmind('Mindreader', 5)
    eleven = Overmind('Eleven', 5)

    _=demodog.attack(demodog); print(_ == "Demodog cannot attack itself", '\tdemodog.attack(demodog):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog deals 10 damage to Demogorgon", '\tdemodog.attack(demogorgon):\t', _)
    _=demodog.get_master(); print(_ == None, '\tdemodog.get_master():\t', _)
    _=mindreader.mind_control(mindreader); print(_ == "Mindreader cannot mind-control itself", '\tmindreader.mind_control(mindreader):\t', _)
    _=mindreader.mind_control(demodog); print(_ == "Mindreader mind-controls Demodog", '\tmindreader.mind_control(demodog):\t', _)
    _=mindreader.mind_control(demogorgon); print(_ == "Mindreader mind-controls Demogorgon", '\tmindreader.mind_control(demogorgon):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon'), '\tmindreader.get_slaves():\t', _)
    _=demodog.get_master(); print(_ == "Mindreader", '\tdemodog.get_master():\t', _)
    _=mindreader.attack(demodog); print(_ == "Mindreader cannot attack its slave", '\tmindreader.attack(demodog):\t', _)
    _=demodog.attack(mindreader); print(_ == "Demodog cannot attack its master", '\tdemodog.attack(mindreader):\t', _)
    _=demodog.attack(demogorgon); print(_ == "Demodog cannot attack its master's slave", '\tdemodog.attack(demogorgon):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 25 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer mind-controls Mindreader", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 90 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindflayer.mind_control(demodog); print(_ == "Demodog is already a slave of Mindflayer", '\tmindflayer.mind_control(demodog):\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader cannot mind-control its master", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer mind-controls D'artagnan", '\tmindflayer.mind_control(dartagnan):\t', _)
    _=mindreader.mind_control(dartagnan); print(_ == "Mindreader and D'artagnan have the same master", '\tmindreader.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindreader'), '\tmindflayer.get_slaves():\t', _)
    _=eleven.mind_control(mindreader); print(_ == "Eleven over-mind-controls Mindreader from Mindflayer", '\televen.mind_control(mindreader):\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=eleven.attack(mindflayer); print(_ == "Eleven deals 70 damage to Mindflayer", '\televen.attack(mindflayer):\t', _)
    _=mindflayer.attack(eleven); print(_ == "Mindflayer deals 45 damage to Eleven", '\tmindflayer.attack(eleven):\t', _)
    _=mindreader.attack(mindflayer); print(_ == "Mindreader deals 65 damage to Mindflayer", '\tmindreader.attack(mindflayer):\t', _)
    _=eleven.mind_control(dartagnan); print(_ == "Eleven over-mind-controls D'artagnan from Mindflayer", '\televen.mind_control(dartagnan):\t', _)
    _=mindflayer.get_slaves(); print(tuple(sorted(_)) == (), '\tmindflayer.get_slaves():\t', _)
    _=mindreader.mind_control(mindflayer); print(_ == "Mindreader mind-controls Mindflayer", '\tmindreader.mind_control(mindflayer):\t', _)
    _=mindreader.get_slaves(); print(tuple(sorted(_)) == ('Demodog', 'Demogorgon', 'Mindflayer'), '\tmindreader.get_slaves():\t', _)
    _=eleven.get_slaves(); print(tuple(sorted(_)) == ("D'artagnan", 'Demodog', 'Demogorgon', 'Mindflayer', 'Mindreader'), '\televen.get_slaves():\t', _)
    _=mindflayer.mind_control(mindreader); print(_ == "Mindflayer cannot mind-control its master", '\tmindflayer.mind_control(mindreader):\t', _)
    _=mindflayer.mind_control(dartagnan); print(_ == "Mindflayer and D'artagnan have the same master", '\tmindflayer.mind_control(dartagnan):\t', _)

# Uncomment to test question 3
##test_q3()



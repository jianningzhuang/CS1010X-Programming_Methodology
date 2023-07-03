# CS1010S AY2013/2014 Semester 1
# Solutions for Make Up Practical Exam
#

# Problem 1
# ------------
#
def odd_position_digits(num):
    result = ""
    str_num = str(num)
    for i in range(0, len(str_num), 2):
        result += str_num[i]
    return int(result)

def reverse_even(num):
    odd = ""
    even = ""
    result = ""
    str_num = str(num)
    for i in range(len(str_num)):
        if i%2 == 0:
            odd += str_num[i]
        else:
            even += str_num[i]
    for j in range(len(even)):
        result += odd[j]
        result += even[-j - 1]
    result += odd[j + 1:]
    return int(result)
    

#print(reverse_even(123456789))

# Problem 2
# ------------
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

# This is the warm up exercise.
def available_venues(file):
    data = read_csv(file)[1:]
    result = []
    for info in data:
        if info[7] not in result:
            result.append(info[7])
    return len(result)


print("available_venues(\"timetable1.csv\") =>",available_venues("timetable1.csv"))
print("available_venues(\"timetable2.csv\") =>",available_venues("timetable2.csv"))

def convert(start, end):
    if start[0] == "0":
        start = start[1:]
    if end[0] == "0":
        end = end[1:]
    hours = int(end) - int(start)
    mins = (hours//100)*60 + hours%100
    return mins


def venue_occupancy(filename):
    data = read_csv(filename)[1:]
    result = {}
    for mc, cn, lesson, dayc, dayt, start, end, venue, ay, sem, lm, lmj, isdelete in data:
        if venue not in result:
            result[venue] = {}
        if dayc not in result[venue]:
            result[venue][dayc] = 0
        if start < "0800":
            start = "0800"
        if end > "1700":
            end = "1700"
        if 1 <= int(dayc) <= 5:
            result[venue][dayc] += convert(start, end)
    total = 0
    for v in result:
        weekly = 0
        for d in result[v]:
            result[v][d] = result[v][d]/convert("0800", "1700")
            weekly += result[v][d]
        total += weekly/5
    return total/len(result)
        
        
    

print("venue_occupancy(\"timetable1.csv\") =>",venue_occupancy("timetable1.csv"))
print("venue_occupancy(\"timetable2.csv\") =>",venue_occupancy("timetable2.csv"))



# Problem 3
# ------------
# This is very similar to the polling station question Except that
# there's a need to create a new Person object to keep track of
# who has done what.
class IPPT:

    def __init__(self):
        self.station = []
        self.people = 0

    def add_station(self, name, 

class Station:
    pass

class Person:
    pass

ippt2013 = IPPT()

chin_up = ippt2013.add_station("chin up",10)
sit_up = ippt2013.add_station("sit up",10)
sbj = ippt2013.add_station("broad jump",10)

print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("chin_up.complete(5)")
chin_up.complete(5)

print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sit_up.complete(10)")
sit_up.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sbj.complete(10)")
sbj.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("chin_up.complete(10)")
chin_up.complete(10)

print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sit_up.complete(10)")
sit_up.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sbj.complete(10)")
sbj.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("chin_up.complete(10)")
chin_up.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sit_up.complete(10)")
sit_up.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("sbj.complete(10)")
sbj.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

print("chin_up.complete(10)")
chin_up.complete(10)
print("ippt2013.left() =>",ippt2013.left())
print("chin_up.count() =>",chin_up.count())
print("sit_up.count() =>",sit_up.count())
print("sbj.count() =>",sbj.count())

#******************************************************
#*
#*  CS1010S Practical Exam
#*  AY2013/2014, Semester 1
#*  Matric No: <fill in your matric no here>
#*
#******************************************************

###
### Question 1
###

### Your answer here.

def letter_count(*words):
    result = {}
    for word in words:
        for letter in word:
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result

def most_frequent(*words):
    freq = letter_count(*words)
    max = None
    for letter in freq:
        if max == None or freq[letter] > max:
            max = freq[letter]
    result = []
    for l in freq:
        if freq[l] == max:
            result.append(l)
    result.sort()
    return result

# Tests


def test_q1a():
    print("Testing Q1A")
    print(letter_count("this") == {'s': 1, 'h': 1, 'i': 1, 't': 1})
    print(letter_count("this","is") == {'s': 2, 'h': 1, 'i': 2, 't': 1})
    print(letter_count("this","Is") == {'s': 2, 'h': 1, 'i': 1, 'I': 1, 't': 1})
    print(letter_count("this","is","a") == {'s': 2, 'h': 1, 'i': 2, 'a': 1, 't': 1})
    print(letter_count("this","is","a","good") == {'h': 1, 'i': 2, 'o': 2, 'd': 1, 's': 2, 'a': 1, 'g': 1, 't': 1})
    print(letter_count("this","is","a","good","day") == {'h': 1, 'i': 2, 'o': 2, 'd': 2, 's': 2, 'a': 2, 'y': 1, 'g': 1, 't': 1})
    print(letter_count("baa", "baa","banana") =={'b': 3, 'a': 7, 'n': 2})
    print("===========================================")

def test_q1b():
    # Keep in mind that your answer might be slightly different
    # because of the ordering, but might still be correct.
    print("Testing Q1B")
    print(most_frequent("this") == ['i', 'h', 's', 't'])
    print(most_frequent("this","is") == ['i', 's'])
    print(most_frequent("this","Is") == ['s'])
    print(most_frequent("this","is","a") ==['i', 's'])
    print(most_frequent("this","is","a","good") == ['i', 'o', 's'])
    print(most_frequent("this","is","a","good","day") == ['a', 'd', 'i', 'o', 's'])
    print(most_frequent("baa", "baa","banana") == ['a'])
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

def highest_quota_no_exams(exams_file, modules_file, k):
    exams = read_csv(exams_file)[1:]
    modules = read_csv(modules_file)[1:]
    have_exams = []
    for exam in exams:
        if exam[2] not in have_exams:
            have_exams.append(exam[2])
    result = {}
    for info in modules:
        if info[0] not in have_exams:
            if info[0] not in result:
                result[info[0]] = {}
            if info[1] not in result[info[0]]:
                result[info[0]][info[1]] = 0
            result[info[0]][info[1]] += int(info[2])
    for m in result:
        max = None
        for g in result[m]:
            if max == None or result[m][g] > max:
                max = result[m][g]
        result[m] = max
    sorting = []
    for m ,v in result.items():
        sorting.append([m, v])
    sorting.sort(key = lambda x: x[1], reverse = True)
    final = tuple(map(lambda x: x[0], sorting[:k]))
    index = 0
    while sorting[k + index][1] == sorting[k - 1][1]:
        final += (sorting[k + index][0], )
        index += 1
    return final
            




# Tests
#print(highest_quota_no_exams("exams1.csv","modules1.csv",3) == ('CS1280', 'CS1281', 'CS2250'))
#print(highest_quota_no_exams("exams2.csv","modules2.csv",5) == ('CS1281', 'CS2250', 'CS2261', 'CS3243', 'CS1105'))

###
### Question 3
###

### Your answer here.

class Person:

    def __init__(self, name):
        self.name = name
        self.dreaming = False
        self.dreams = []

    def get_name(self):
        return self.name

    def dream_level(self):
        return len(self.dreams)

    def dream(self, *people):
        for person in people:
            if self.dream_level() != person.dream_level() or self.dreams != person.dreams:
                return None
        dreamers = people + (self, )
        new = Dream(*dreamers)
        new.main = self
        for p in dreamers:
            p.dreams.append(new)
            p.dreaming = True
        return new
            
    def kick(self):
        if self.dreaming == True:
            d = self.dreams.pop()
            print(self.dreams)
            if self.dreams == []:
                self.dreaming = False
            if d.main == self:
                level = self.dream_level()
                for p in d.people:
                    for died in p.dreams[level + 1:]:
                        died.a = False
                        died.people = []
                        died.main = None
                    p.dreams = p.dreams[:level]
                    if p.dreams == []:
                        p.dreaming = False
                d.a = False
                d.people = []
            else:
                d.people.remove(self)

class Dream:

    def __init__(self, *people):
        self.main = None
        self.people = list(people)
        self.a = True

    def dreamers(self):
        return list(self.people)

    def active(self):
        return self.a
        
        


# Tests
def test_q3():
 
    print("Testing Q3")
    yusuf = Person("Yusuf")
    eames = Person("Eames")
    arthur = Person("Arthur")
    robert = Person("Robert")
    dominick = Person("Dominick")
    jewels = Person("Jewels")

    yusuf.dream(eames,arthur,robert,dominick)
    print("yusuf.dream(eames,arthur,robert,dominick)")
    print(yusuf.get_name() == "Yusuf")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 1)
    print(robert.dream_level() == 1)
    print(eames.dream_level() == 1)
    print(dominick.dream_level() == 1)

    dream = arthur.dream(jewels,eames,robert,dominick) # Jewels not in dream!
    print("dream = arthur.dream(jewels,eames,robert,dominick)")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 1)
    print(robert.dream_level() == 1)
    print(eames.dream_level() == 1)
    print(dominick.dream_level()  == 1)
    print(dream == None)
    
    dream = arthur.dream(eames,robert,dominick)
    print("dream = arthur.dream(eames,robert,dominick)")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 2)
    print(robert.dream_level() == 2)
    print(eames.dream_level() == 2)
    print(dominick.dream_level() == 2)
    print(dream.active())

    dream = jewels.dream(robert,dominick) # Jewels not in dream!
    print("dream = jewels.dream(robert,dominick)")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 2)
    print(robert.dream_level() == 2)
    print(eames.dream_level() == 2)
    print(dominick.dream_level() == 2)
    print(dream == None)

    dream = eames.dream(robert,dominick)
    print("dream = eames.dream(robert,dominick)")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 2)
    print(robert.dream_level() == 3)
    print(eames.dream_level() == 3)
    print(dominick.dream_level() == 3)
    print(dream.active())
    
    arthur.kick() # Major collapse
    print("arthur.kick()")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 1)
    print(robert.dreams)
    print(robert.dream_level() == 1)
    print(eames.dream_level() == 1)
    print(dominick.dream_level() == 1)
    print(not dream.active())

    arthur.kick() # Major collapse
    print("arthur.kick()")
    print(yusuf.dream_level() == 1)
    print(arthur.dream_level() == 0)
    print(robert.dreams)
    print(robert.dream_level() == 1)
    print(eames.dream_level() == 1)
    print(dominick.dream_level() == 1)

    yusuf.kick() # Major collapse
    print("yusuf.kick()")
    print(yusuf.dream_level() == 0)
    print(arthur.dream_level() == 0)
    print(robert.dream_level() == 0)
    print(eames.dream_level() == 0)
    print(dominick.dream_level() == 0)
    print("===========================================")

# Uncomment to test question 3
test_q3()

###
### Question 4
###

### Your answer here.


# Tests
def test_q4():

    print("Testing Q4")
    and1 = AndGate()
    print("and1 = AndGate()")
    print(not and1.compute([False,False]))
    print(not  and1.compute([False,True]))
    print(not and1.compute([True,False]))
    print(and1.compute([True,True]))

    notg = NotGate()
    print("notg = NotGate()")
    print(notg.compute([False]))
    print(not notg.compute([True]))

    or_and = AndGate().connect(0,OrGate())
    print("or_and = AndGate().connect(0,OrGate()")
    print(not or_and.compute([False,False,False]))
    print(not or_and.compute([False,False,True]))
    print(not or_and.compute([False,True,False]))
    print(or_and.compute([False,True,True]))
    print(not or_and.compute([True,False,False]))
    print(or_and.compute([True,False,True]))
    print(not or_and.compute([True,True,False]))
    print(or_and.compute([True,True,True]))

    or_and2 = AndGate().connect(1,OrGate())
    print("or_and2 = AndGate().connect(1,OrGate())")
    print(not or_and2.compute([False,False,False]))
    print(not or_and2.compute([False,False,True]))
    print(not or_and2.compute([False,True,False]))
    print(not or_and2.compute([False,True,True]))
    print(not or_and2.compute([True,False,False]))
    print(or_and2.compute([True,False,True]))
    print(or_and2.compute([True,True,False]))
    print(or_and2.compute([True,True,True]))
    print("===========================================")

# Uncomment to test question 4
#test_q4()


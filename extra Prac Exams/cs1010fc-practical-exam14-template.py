#******************************************************
#*
#*  CS1010FC Practical Exam
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

def swap(string):
    result = ""
    for i in range(0, len(string), 2):
        pair = string[i:i+2]
        if len(pair) == 1:
            result += pair
        else:
            result += pair[1]
            result += pair[0]

    return result

def shift(chunk, k):
    while k > 0:
        chunk = chunk[1:] + chunk[0]
        k -= 1
    return chunk


def rotate(string, n, k):
    result = ""
    for i in range(0, len(string), n):
        chunk = string[i: i + n]
        if len(chunk) < n:
            result += chunk
        else:
            result += shift(chunk, k)
    return result
    
        

# Tests


def test_q1a():
    print("Testing Q1A")
    print("swap(\"a\"):" + str(swap("a") == "a"))
    print("swap(\"ab\"):" + str(swap("ab") == "ba"))
    print("swap(\"abc\"):" + str(swap("abc") == "bac"))
    print("swap(\"abcc\"):" + str(swap("abcc") == "bacc"))
    print("swap(\"baabaablack\"):" + str(swap("baabaablack") == "abbaaalbcak"))
    print("===========================================")

def test_q1b():
    print("Testing Q1B")
    print("rotate(\"baabaablack\",2,1):" + str(rotate("baabaablack",2,1) == "abbaaalbcak"))
    print("rotate(\"baabaablack\",3,0):" + str(rotate("baabaablack",3,0) == "baabaablack"))
    print("rotate(\"baabaablack\",3,1):" + str(rotate("baabaablack",3,1) == "aabaablabck"))
    print("rotate(\"baabaablack\",3,2):" + str(rotate("baabaablack",3,2) == "abaabaablck"))
    print("rotate(\"baabaablack\",3,3):" + str(rotate("baabaablack",3,3) == "baabaablack"))
    print("rotate(\"baabaablack\",3,4):" + str(rotate("baabaablack",3,4) == "aabaablabck"))
    print("===========================================")

# Uncomment to test question 1
#test_q1a()
#test_q1b()


###
### Question 2
###
import csv
def read_csv(filename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    with open(filename, 'r') as f:
        lines = tuple(f)[1:] # remove header
    entries = map(lambda x: x[:-1].split(','), lines) # split line
    cleaned = map(lambda x: x[0].split() + x[1:], entries) # split date
    return list(cleaned)

### Your answer here.

def convert_date(date):
    cut = 0
    result = []
    for i in range(len(date)):
        if date[i] == "/":
            result.append(date[cut:i])
            cut = i + 1
    result.append(date[cut:])
    return [result[0], result[1], result[2]]

def valid(start, end, date):
    start = convert_date(start)
    end = convert_date(end)
    date = convert_date(date)
    if start[2] > date[2]:
        return False
    elif start[2] == date[2]:
        if start[1] > date[1]:
            return False
        elif start[1] == date[1]:
            if start[0] > date[0]:
                return False
    if end[2] < date[2]:
        return False
    elif end[2] == date[2]:
        if end[1] < date[1]:
            return False
        elif end[1] == date[1]:
            if end[0] < date[0]:
                return False
    return True
    

def average_rate(start_date, end_date, filename):
    data = read_csv(filename)
    result = []
    for date, day, rate, frm, to in data:
        if valid(start_date, end_date, date):
            result.append(float(rate))
    print(sum(result)/len(result))
    return sum(result)/len(result)

def convert(f1, f2):
    data1 = read_csv(f1)
    data2 = read_csv(f2)
    result = {}
    for date1, day1, rate1, frm1, to1 in data1:
        for date2, day2, rate2, frm2, to2 in data2:
            if date1 == date2:
                result[date1] = float(rate2)/float(rate1)

    return result

def trade(f, amt):
    data = read_csv(f)
    result = []
    best = None
    for i in range(len(data) - 1):
        lowest = None
        for j in range(i, len(data)):
            if lowest == None or float(data[j][2]) < lowest:
                lowest = float(data[j][2])
        difference = float(data[i][2])/lowest
        if best == None or difference > best:
            best = difference
    return amt*best
    
                
    
    




# Tests
# Q2a
#print("Testing Q2")
print(average_rate('11/26/2013', '1/31/2014', 'sgd-rmb.csv') == 4.798673749999999)
print(average_rate('11/26/2013', '5/23/2014', 'sgd-myr.csv') == 2.59280477124183)
print(average_rate('11/26/2013', '1/31/2014', 'sgd-myr.csv') == 2.5881937931034478)
print(average_rate('11/26/2013', '1/31/2014', 'sgd-myr2.csv') == 2.5880032142857137)

# Q2b
#myr_rmb = convert('sgd-myr.csv', 'sgd-rmb.csv')
#print(myr_rmb['4/29/2014']==1.9136195527357778)
#print(('5/9/2014' in myr_rmb) == False)

#myr_rmb1 = convert('sgd-myr2.csv', 'sgd-rmb.csv')
#print(myr_rmb1['4/30/2014'] == 1.9237253527095648)
#print('5/9/2014' in myr_rmb1)


# Q2c
#print(trade('sgd-myr.csv',100) == 102.88575760417642)
#print(trade('sgd-myr2.csv',100) == 102.88575760417642)
#print(trade('sgd-rmb.csv',50) == 51.53180938046961)




###
### Question 3
###

### Your answer here.

class Mutant(object):

    def __init__(self, name):
        self.name = name
        self.master = self
        self.mastermind = self

    def get_name(self):
        return self.name

    def get_master(self):
        return self.master

    def get_mastermind(self):
        return self.mastermind

class Telepath(Mutant):

    def __init__(self, name, strength):
        super().__init__(name)
        self.strength = strength
        self.slave = None

    def get_slave(self):
        return self.slave

    def get_chain(self):
        result = [self]
        while self.slave != None:
            if not isinstance(self.slave, Telepath):
                result.append(self.slave)
                break
            else:
                result.append(self.slave)
                self = self.slave
        return result

    def mind_control(self, m):
        if self.master != self:
            return None
        controller = self.get_chain()[-1]
        if isinstance(controller, Telepath):
            if isinstance(m, Telepath) and m.strength >= controller.strength:
                return None
            elif m in self.get_chain():
                return None
            elif m.master != m:
                if m.master.strength >= controller.strength:
                    return None
                else:
                    m.master.slave = None
                    m.master = controller
                    if isinstance(m, Telepath):
                        for x in m.get_chain():
                            x.mastermind = self
                    else:
                        m.mastermind = self
                    controller.slave = m
                    return None
                    
            else:
                m.master = controller
                if isinstance(m, Telepath):
                    for x in m.get_chain():
                        x.mastermind = self
                else:
                    m.mastermind = self
                controller.slave = m
        return None
        


    def release(self, *m):
        if self.master != self:
            return None
        if m == ():
            print('hi')
            for s in self.get_chain():
                if isinstance(s, Telepath):
                    s.slave = None
                s.master = s
                s.mastermind = s
        for x in m:
            if x in self.get_chain():
                x.master.slave = None
                x.master = x
                x.mastermind = x
                if isinstance(x, Telepath):
                    x.release()
            
        
logan = Mutant("Wolverine")
charles = Telepath("Prof. X", 10)
jean = Telepath("Phoenix", 9)
psylocke = Telepath("Psylocke", 8)
emma = Telepath("Frost", 7)


# Tests
def test_q3():
 
    print("Testing Q3")

    logan = Mutant("Wolverine")
    charles = Telepath("Prof. X", 10)
    jean = Telepath("Phoenix", 9)
    psylocke = Telepath("Psylocke", 8)
    emma = Telepath("Frost", 7)

    psylocke.mind_control(logan) # [P -> L]
    print(logan.get_master().get_name() == "Psylocke")
    print(psylocke.get_slave().get_name() == "Wolverine")

    # === jean steals logan from psylocke ===
    jean.mind_control(logan) # [J -> L]
    print(logan.get_master().get_name() == "Phoenix")
    print(jean.get_slave().get_name() == "Wolverine")
    print(psylocke.get_slave() == None)
    print(jean.get_chain())

    charles.mind_control(jean) # [C -> J -> L]
    print(charles.slave.name)
    print(logan.get_master().get_name() == "Phoenix")
    print(jean.get_master().get_name() == "Prof. X")
    print(charles.get_slave().get_name() == "Phoenix")

    # === psylocke fails to steal jean ===
    psylocke.mind_control(jean) # [C -> J -> L]
    print(jean.get_master().get_name() == "Prof. X")

    # === psylocke fails to control charles ===
    psylocke.mind_control(charles) # [C -> J -> L]
    print(charles.get_master().get_name() == "Prof. X")


    charles.release(logan) # [C -> J]
    print(charles.get_slave().get_name() == "Phoenix")
    print(jean.get_slave() == None)
    print(logan.get_master().get_name() == "Wolverine")

    psylocke.mind_control(emma) # [P -> E, C -> J]
    print(emma.get_master().get_name() == "Psylocke")

    charles.mind_control(psylocke) # [C -> J -> P -> E]
    print(emma.get_mastermind().get_name() == "Prof. X")
    print(psylocke.get_mastermind().get_name() == "Prof. X")
    print(jean.get_mastermind().get_name() == "Prof. X")
    print(charles.get_mastermind().get_name() == "Prof. X")

    # === jean cannot release anybody ===
    jean.release(psylocke) # [C -> J -> P -> E]
    print(psylocke.get_master().get_name() == "Phoenix")

    # === emma cannot act ===
    emma.mind_control(logan) # [C -> J -> P -> E]
    print(logan.get_master().get_name() == "Wolverine")

    # === failed cyclic control attempt ===
    charles.mind_control(jean) # [C -> J -> P -> E]
    print(emma.get_slave() == None)

    # === release all ===
    charles.release(jean)
    print(charles.get_master().get_name() == "Prof. X")
    print(jean.master.name)
    print(jean.get_master().get_name() == "Phoenix")
    print(emma.master.name)
    print(emma.get_master().get_name() == "Frost")
    print(psylocke.get_master().get_name() == "Psylocke")
    print(logan.get_master().get_name() == "Wolverine")

# Uncomment to test question 3
#test_q3()


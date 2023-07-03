#******************************************************
#*
#*  CS1010FC Practical Exam
#*  AY2014/2015, Semester 2
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

def depth(tree):
    if tree == [] or tree == ():
        return 1
    elif type(tree) != list and type(tree) != tuple:
        return 0
    else:
        highest = None
        for elem in tree:
            current = depth(elem) + 1
            if highest == None or current > highest:
                highest = current
        return highest

def max_branching(tree):
    if tree == [] or tree == ():
        return 0
    elif type(tree) != list and type(tree) != tuple:
        return 1
    else:
        highest = len(tree)
        for elem in tree:
            if max_branching(elem) > highest:
                highest = max_branching(elem) 
        return highest
    
    

# Tests


def test_q1a():
    print("Testing Q1A")
    print("depth(()):", depth(())==1)
    print("depth((1,)):", depth((1,))==1)
    print("depth((1,2)):", depth((1,2))==1)
    print("depth((1,2,3)):", depth((1,2,3))==1)
    print("depth((1,(2,3))):", depth((1,(2,3)))==2)
    print("depth((1,((2,3),4),(5,6))):", depth((1,((2,3),4),(5,6)))==3)
    print("depth((1,(2,(3,)))):", depth((1,(2,(3,))))==3)
    print("depth([1,2,3]):", depth([1,2,3])==1)
    print("depth([1,[2,3]]):", depth([1,[2,3]])==2)
    print("===========================================")

def test_q1b():
    print("Testing Q1B")
    print("max_branching(()):", max_branching(())==0)
    print("max_branching((1,)):", max_branching((1,))==1)
    print("max_branching((1,2)):", max_branching((1,2))==2)
    print("max_branching((1,2,3)):", max_branching((1,2,3))==3)
    print("max_branching((1,(2,3))):", max_branching((1,(2,3)))==2)
    print("max_branching((1,((2,3),4),(5,6))):", max_branching((1,((2,3),4),(5,6)))==3)
    print("max_branching((1,[(2,3),4],(5,6))):", max_branching((1,[(2,3),4],(5,6)))==3)
    print("max_branching((1,(2,(3,)))):", max_branching((1,(2,(3,))))==2)
    print("max_branching([1,2,3]):", max_branching([1,2,3])==3)
    print("max_branching([1,[2,3]]):", max_branching([1,[2,3]])==2)
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
    return list(entries)

### Your answer here.

def gantry_revenue(cars, gantry, time, filename):
    data = read_csv(filename)
    for gn, loc, start, end, price in data:
        if int(gn) == gantry and int(start) <= time < int(end):
            return cars * float(price)
    return 0

def total_price(gantries, filename):
    result = 0
    for gantry in gantries:
        result += gantry_revenue(1, gantry[0], gantry[1], filename)
    return result

def most_active_gantries(filename):
    data = read_csv(filename)
    freq = {}
    for gn, loc, start, end, price in data:
        if int(gn) not in freq:
            freq[int(gn)] = 0
        freq[int(gn)] += (int(end) - int(start))
    sort = []
    for key, value in freq.items():
        sort.append([key, value])
    sort.sort(key = lambda x: x[1], reverse = True)
    result = [sort[0][0]]
    for i in range(1, len(sort)):
        if sort[i][1] == sort[0][1]:
            result.append(sort[i][0])
    return result
    
    




# Tests
# Q2a
def test_q2a():
    print("Testing Q2A")
    print("gantry_revenue(5000, 31, 709, 'erp_rates.csv'):", gantry_revenue(5000, 31, 709, 'erp_rates.csv')==10000)
    print("gantry_revenue(1000, 38, 1500, 'erp_rates.csv'):",gantry_revenue(1000, 38, 1500, 'erp_rates.csv')==0)
    print("gantry_revenue(2000, 71, 910, 'erp_rates.csv'):", gantry_revenue(2000, 71, 910, 'erp_rates.csv')==1000)
    print("gantry_revenue(1500, 67, 1905, 'erp_rates.csv'):", gantry_revenue(1500, 67, 1905, 'erp_rates.csv')==2250)
    print("gantry_revenue(2500, 56, 857, 'erp_rates.csv'):", gantry_revenue(2500, 56, 857, 'erp_rates.csv')==1250)
    print("gantry_revenue(480, 90, 732, 'erp_rates.csv'):", gantry_revenue(480, 90, 732, 'erp_rates.csv')==720)
    print("gantry_revenue(3200, 30, 820, 'erp_rates.csv'):", gantry_revenue(3200, 30, 820, 'erp_rates.csv')==3200)
    print("gantry_revenue(4650, 42, 923, 'erp_rates.csv'):", gantry_revenue(4650, 42, 923, 'erp_rates.csv')==9300)
    print("gantry_revenue(3800, 20, 1900, 'erp_rates.csv'):", gantry_revenue(3800, 20, 1900, 'erp_rates.csv')==0)
    print("gantry_revenue(0, 67, 1959, 'erp_rates.csv'):", gantry_revenue(0, 67, 1959, 'erp_rates.csv')==0)

# Q2b
def test_q2b():
    print("Testing Q2B")
    print("total_price([(39, 732), (58, 803), (70, 926)], 'erp_rates.csv'):",total_price([(39, 732), (58, 803), (70, 926)], 'erp_rates.csv')==1.5)
    print("total_price([(31, 925), (52, 1100)], 'erp_rates.csv'):",total_price([(31, 925), (52, 1100)], 'erp_rates.csv')==1.0)
    print("total_price([(31, 840), (51, 1735), (74,1830)], 'erp_rates.csv'):",total_price([(31, 840), (51, 1735), (74,1830)], 'erp_rates.csv')==9.0)
    print("total_price([(40, 705), (41, 925), (93, 1033), (53, 1802)], 'erp_rates.csv'):",total_price([(40, 705), (41, 925), (93, 1033), (53, 1802)], 'erp_rates.csv')==1.0)
    print("total_price([], 'erp_rates.csv'):",total_price([], 'erp_rates.csv')==0)
    print("total_price([(90, 831)], 'erp_rates.csv'):",total_price([(90, 831)], 'erp_rates.csv')==2.0)
    print("total_price([(67, 1650), (92, 1732), (46, 1930)], 'erp_rates.csv'):",total_price([(67, 1650), (92, 1732), (46, 1930)], 'erp_rates.csv')==0.5)
    print("total_price([(35, 701), (68, 915)], 'erp_rates.csv'):",total_price([(35, 701), (68, 915)], 'erp_rates.csv')==2.5)
    print("total_price([(42, 718), (57, 855), (46, 1904), (67, 1956)], 'erp_rates.csv'):",total_price([(42, 718), (57, 855), (46, 1904), (67, 1956)], 'erp_rates.csv')==4.5)
    print("total_price([(54, 1200), (43, 1410), (71, 1720)], 'erp_rates.csv'):",total_price([(54, 1200), (43, 1410), (71, 1720)], 'erp_rates.csv')==0)

# Q2c
def test_q2c():
    print("Testing Q2C")
    print("most_active_gantries('erp_rates.csv'):", sorted(most_active_gantries('erp_rates.csv'))==[52, 53, 74])


# Uncomment to test question 2
#test_q2a()
#test_q2b()
#test_q2c()

###
### Question 3
###

### Your answer here.
class Polynomial(): # Immutable polynomial 

    def __init__(self, terms):
            
        self.coeffs = list(terms)

    def degree(self):
        return len(self.coeffs) - 1

    def coeff(self,d):
        return self.coeffs[d]

    def coefficients(self): # Helper method - returns [a_0, a_1, ..., a_n]
        # Implemented for you - shouldn't need to change code. 
        result = []
        for i in range(self.degree()+1):
            result.append(self.coeff(i))
        return result

            
    def add(self, p):
        result = []
        if self.degree() <= p.degree():
            for i in range(len(self.coefficients())):
                result.append(self.coefficients()[i] + p.coefficients()[i])
            result.extend(p.coefficients()[i+1:])
        else:
            for i in range(len(p.coefficients())):
                result.append(self.coefficients()[i] + p.coefficients()[i])
            result.extend(self.coefficients()[i+1:])
        return Polynomial(result)
            
                
    def minus(self, p):
        result = []
        if self.degree() <= p.degree():
            for i in range(len(self.coefficients())):
                result.append(self.coefficients()[i] - p.coefficients()[i])
            for j in p.coefficients()[i+1:]:
                result.append(-j)
        else:
            for i in range(len(p.coefficients())):
                result.append(self.coefficients()[i] - p.coefficients()[i])
            result.extend(self.coefficients()[i+1:])
        flag = False
        for i in range(len(result) - 1, -1, -1):
            if result[i] != 0:
                result = result[:i+1]
                flag = True
                break
        if flag == False:
            result = [0]

        return Polynomial(result)
    
    def times(self,p):
        result = [0]*(self.degree() + p.degree() + 1)
        for i in range(len(self.coefficients())):
            for j in range(len(p.coefficients())):
                result[i+j] += self.coefficients()[i]*p.coefficients()[j]
        return Polynomial(result)

    def flip(self, coeffs):
        result = []
        for elem in coeffs:
            result = [elem] + result
        return result

    def quotient(self,p):
        poly = self.flip(self.coefficients())
        divisor = p.flip(p.coefficients())
        q = [0]*(self.degree() - p.degree() + 1)
        for i in range(self.degree() - p.degree() + 1):
            if poly[i] != 0:
                factor = poly[i]/divisor[0]
                q[i] = factor
                for j in range(p.degree() + 1):
                    poly[i + j] -= factor*divisor[j]
        return Polynomial(self.flip(q))
            

    def remainder(self,p):
        return self.minus(self.quotient(p).times(p))

# Tests
def test_q3():
 
    print("Testing Q3")
    p1 = Polynomial((1,0,1))  # x^2+1
    print("p1.coefficients():", p1.coefficients() == [1, 0, 1])

    p2 = Polynomial((1,1))  # x+1
    print("p2.coefficients():", p2.coefficients() == [1, 1])

    p3 = p1.add(p2)
    print("p3.coefficients():", p3.coefficients() == [2, 1, 1])

    p4 = p1.minus(p2)
    print("p4.coefficients():", p4.coefficients() == [0, -1, 1])

    p5 = p1.times(p2)
    print("p5.coefficients():", p5.coefficients() == [1, 1, 1, 1])

    p6 = Polynomial((-1,1))  # x-1
    p7 = p5.times(p6)
    print("p7.coefficients():", p7.coefficients() == [-1, 0, 0, 0, 1])

    p8 = Polynomial((-1,0,0,0,1))  # x^4-1
    p9 = p7.quotient(p6)
    print("p9.coefficients():", p9.coefficients() == [1.0, 1.0, 1.0, 1.0])

    p10 = p7.remainder(p6)
    print(p10.coefficients())
    print("p10.coefficients():", p10.coefficients() == [0])

    p11 = Polynomial((1,0,1,0,1))  # x^4+x^2+1
    p12 = p11.quotient(p2)
    print("p12.coefficients():", p12.coefficients() == [-2.0, 2.0, -1.0, 1.0])

    p13 = p11.remainder(p2)
    print(p13.coefficients())
    print("p13.coefficients():", p13.coefficients()==[3.0])

# Uncomment to test question 3
test_q3()


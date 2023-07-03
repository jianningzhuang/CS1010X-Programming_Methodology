##########################################
# Question 1a: Alien numbers [ 5 Marks ] #
##########################################

def ET_number(num, mapping):
    base = len(mapping)
    result = ""
    while num > 0:
        result = mapping[num%base] + result
        num = num//base
    return result

def test1a():
    print("=====Test 1a=====")
    # checking if simple decimal numbers can be produced
    print(ET_number(5, ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for switching some digits
    print(ET_number(20, ('9','8','7','6','5','4','3','2','1','0')) == '79')
    # checking for different bases
    print(ET_number(10, ('0','1','2','3','4','5')) == '14')
    print(ET_number(6, ('0','4')) == '440')
    print(ET_number(5, ('1', '0')) == '010')
    print(ET_number(10, ('a', 'b', 'c')) == 'bab')
    print(ET_number(20, ('0','1','2','3','4','5','6','7','8','9', "A", "B", "C")))
    


test1a()

#################################################
# Question 1b: Largest alien number [ 5 Marks ] #
#################################################

def coeff(digit, mapping):
    for i in range(len(mapping)):
        if digit == mapping[i]:
            return i

def ET_to_decimal(ET_num, mapping):
    base = len(mapping)
    power = len(ET_num) - 1
    result = 0
    for digit in ET_num:
        result += coeff(digit, mapping) * (base**power)
        power -= 1
    return result
        
        

def max_ET_number(ET_numbers, mapping):
    max_val = None
    max_ET = None
    for ET_num in ET_numbers:
        decimal = ET_to_decimal(ET_num, mapping)
        if max_val == None or decimal > max_val:
            max_val = decimal
            max_ET = ET_num
    return max_ET

def test1b():
    print("=====Test 1b=====")
    # checking for normal decimal
    print(max_ET_number(('1','2','3','4','5'), ('0','1','2','3','4','5','6','7','8','9')) == '5')
    # checking for swapped digits
    print(max_ET_number(('12','34','42','58'), ('0','1','8','3','5','4','6','7','2','9')) == '42')
    print(max_ET_number(('19','20','21','22','23'), ('0','2','1','3','4','5','6','7','8','9')) == '19')
    # different bases
    print(max_ET_number(('14','15'),('0','1','2','3','5','4'))=='14')
    print(max_ET_number(('707','700','770'),('0','7'))=='770')
    print(max_ET_number(('0', '4', '40', '44', '400', '404', '440', '444', '4000', '4004', '4040'),('0','4'))=='4040')
    print(max_ET_number(('317','311','713','413'),('7','1','3','4'))=='413')
    print(max_ET_number(('aba', 'abc', 'ca', 'cb'), ('a', 'b', 'c')) == 'cb')

#test1b()

############################
# Question 2: Tesla stocks #
############################

import csv
import datetime

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, 'r') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

######################################################
# Question 2a: Retrieving tweets by date [ 3 Marks ] #
######################################################
def get_tweet_by_date(date):
    tweet_data = read_csv("tweets.csv")[1:]
    result = ()
    for handle, name, content, replies, retweets, favorite, date_t in tweet_data:
        if date_t == date:
            result += (content, )
    return result
        

def test2a():
    print("=====Test 2a=====")
    print(get_tweet_by_date('12/21/2019') == ('Great show  https://t.co/12rguHHpgz', 'Holiday gift ideas https://t.co/uBBofvkYAI'))
    print(get_tweet_by_date('5/1/2020') == ('Now give people back their FREEDOM', 'I am selling almost all physical possessions. Will own no house.', 'Tesla stock price is too high imo', "And the rocket's red glare, the bombs bursting in air", 'Rage, rage against the dying of the light of consciousness'))
    print(get_tweet_by_date('12/12/2001') == ())
    print(get_tweet_by_date('5/21/2021') == ()) 

#test2a()

#############################################################
# Question 2b: Effect of tweets on stock prices [ 3 Marks ] #
#############################################################
def tweet_effect(date):
    tweets = get_tweet_by_date(date)
    if tweets == ():
        return None
    start = datetime.datetime.strptime(date, "%m/%d/%Y")
    end = start + datetime.timedelta(days = 5)
    tesla_data = read_csv("TSLA.csv")[1:]
    result = []
    for d, price in tesla_data:
        current_date = datetime.datetime.strptime(d, "%m/%d/%Y")
        if start <= current_date <= end:
            result.append(float(price))
    tweets += (result, )
    return tweets
        


def test2b():
    print("=====Test 2b=====")
    print(tweet_effect('5/8/2013') == ("Just want to say thanks to customers & investors that took a chance on Tesla through the long, dark night. We wouldn't be here without you.", [55.790001, 69.400002, 76.760002, 87.800003]))
    print(tweet_effect('3/23/2017') == None)
    print(tweet_effect('7/14/2019') == ('To Infinity and Beyond! https://t.co/dgysTBqWfV', [253.5, 252.380005, 254.860001, 253.539993, 258.179993]))

#test2b()

##########################################
# Question 2c: Money tweets [ 4 Marks ]  #
##########################################

def fluctuation(lst):
    if lst == []:
        return None
    highest = None
    lowest = None
    for elem in lst:
        if highest == None or elem > highest:
            highest = elem
        if lowest == None or elem < lowest:
            lowest = elem
    return highest - lowest

def money_tweets(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    tweet_data = read_csv("tweets.csv")[1:]
    max_fluc = None
    worst_day = None
    seen = []
    for handle, name, content, replies, retweets, favorite, date_t in tweet_data:
        if date_t in seen:
            continue
        seen.append(date_t)
        current_date = datetime.datetime.strptime(date_t, "%m/%d/%Y")
        if start <= current_date <= end:
            effect = tweet_effect(date_t)
            fluc = fluctuation(effect[-1])
            if fluc != None:
                if max_fluc == None or fluc > max_fluc:
                    max_fluc = fluc
                    worst_day = date_t
    if worst_day == None:
        return None
    tweets = get_tweet_by_date(worst_day)
    result = (tweets, max_fluc)
    return result

def test2c():
    print("=====Test 2c=====")
    print(money_tweets('5/12/2020', '5/21/2020') == (('Ice cream sundae in a martini glass https://t.co/zAVFlOsYkM', 'Super exciting day coming up! https://t.co/7ZdFsJE9zR', 'https://t.co/lQWpSwtRj7'), 22.669983000000002))
    print(money_tweets('4/29/2020', '5/1/2020') == (('FREE AMERICA NOW', 'Give people their freedom back! https://t.co/iG8OYGaVZ0', 'Bravo Texas! https://t.co/cVkDewRqGv'), 99.19000299999993))

#test2c()

############################################
# Question 3: TOY TRAIN                    #
############################################

class carriage:
    
    def __init__(self, x, y): #do we need to check for invalid positions?
##        if x < 0 or y < 0:
##            return "Invalid position"
        self.x = x
        self.y = y
        self.temp_x = x
        self.temp_y = y
        self.before = None
        self.after = None
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_pos(self):
        return (self.x, self.y)

    def adjacent(self, other):
        if self.x == other.x and abs(self.y - other.y) == 1:
            return True
        if self.y == other.y and abs(self.x - other.x) == 1:
            return True
        return False
    
    def attach(self, car):
##        if isinstance(car, engine):
##            return "Can't attach."
        if self.after != None or car.before != None:
            return "Can't attach."
        if self.adjacent(car):
            self.after = car
            car.before = self
            return "Attached."
        else:
            return "Can't attach."
    
        
    

class engine(carriage):
    
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_carriages(self):
        result = []
        while self.after != None:
            result.append(self.after)
            self = self.after
        return result

    def one_move(self, direction): #do we need to check for invalid moves?
        self.temp_x = self.x
        self.temp_y = self.y
        if direction == "u":
            self.y += 1
        elif direction == "d":
##            if self.y - 1 < 0:
##                return "Invalid move"
            self.y -= 1
        elif direction == "r":
            self.x += 1
        elif direction == "l":
##            if self.x - 1 < 0:
##                return "Invalid move"
            self.x -= 1
##        else:
##            return "Invalid move"
        for c in self.get_carriages():
            c.temp_x = c.x
            c.temp_y = c.y
            c.x = c.before.temp_x
            c.y = c.before.temp_y

    def status(self):
        return list(map(lambda x: x.get_pos(), self.get_carriages()))
        
    def move(self, track):
        for char in track:
            self.one_move(char)
            for c in self.get_carriages():
##                print(self.get_pos())
##                print(self.status())
                if self.get_pos() == c.get_pos():
                    self.x = self.temp_x
                    self.y = self.temp_y
                    for ca in self.get_carriages():
                        ca.x = ca.temp_x
                        ca.y = ca.temp_y
                    return "Collision!"
        return None
            

def test3():
    print("=====Test 3=====")
    c0 = carriage(1,0)
    c1 = carriage(1,1)
    c2 = carriage(1,2)
    c3 = carriage(2,2)
    c4 = carriage(3,4)
    e  = engine(2,3)

    # Checking for get_x and get_y functions
    print(c1.get_x() == 1)
    print(c3.get_y() == 2)
    # Checking for get_pos function
    print(c0.get_pos() == (1,0))

    # Attaching carraiges together to build the train
    print(e.attach(c3) == "Attached.")
    print(c3.attach(c2) == "Attached.")
    print(c2.attach(c1) == "Attached.")

    # c1 and c4 are not adjacent
    print(c1.attach(c4) == "Can't attach.")
    
    print(c1.attach(c0) == "Attached.")

    # Checking for movement
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos())== ((2, 3), (2, 2), (1, 2), (1, 1), (1, 0)))
    print(e.move('uuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((2, 6), (2, 5), (2, 4), (2, 3), (2, 2)))
    print(e.move('r') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 6), (2, 6), (2, 5), (2, 4), (2, 3)))
    print(e.move('uuuuuu') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((3, 12), (3, 11), (3, 10), (3, 9), (3, 8)))
    print(e.move('rdll') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('ldrr') == "Collision!")
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 11), (4, 12), (3, 12), (3, 11), (3, 10)))
    print(e.move('d') == None)
    print((e.get_pos(), c3.get_pos(), c2.get_pos(), c1.get_pos(), c0.get_pos()) == ((4, 10), (4, 11), (4, 12), (3, 12), (3, 11)))

test3()

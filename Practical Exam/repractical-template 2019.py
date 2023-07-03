#################
# Q1a - Shuffle #
#################

def shuffle(a, times):
    while times > 0:
        result = []
        if len(a)%2 == 1:
            mid = len(a)//2 + 1
        else:
            mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        for i in range(len(right)):
            result.append(left[i])
            result.append(right[i])
        if len(a)%2 == 1:
            result.append(left[-1])
        a = result
        times -= 1
    return a
            

def test1a():
    print('=== Q1a ===')
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 1)==[1, 5, 2, 6, 3, 7, 4, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 2)==[1, 3, 5, 7, 2, 4, 6, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 3)==[1, 2, 3, 4, 5, 6, 7, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 1)==[1, 5, 2, 6, 3, 7, 4])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 2)==[1, 3, 5, 7, 2, 4, 6])
 
test1a()


##########################
# Q1b - Back to Original #
##########################

def back_to_original(a):
    original = a.copy()
    a = shuffle(a, 1)
    count = 1
    while original != a:
        a = shuffle(a, 1)
        count += 1
    return count
        

def test1b():
    print('=== Q1b ===')    
    print(back_to_original([1, 2, 3, 4, 5, 6, 7, 8])==3)
    print(back_to_original([1, 2, 3, 4, 5])==4)
    print(back_to_original([1, 1, 1, 1])==1)
 
test1b()

##############
# Question 2 #
##############

import csv
from datetime import datetime

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

###############
# Question 2a #
###############

def get_dates_for_hashtag(filename, hashtag):
    data = read_csv(filename)
    result = []
    for tweet in data[1:]:
        if hashtag in tweet[3] and tweet[0] not in result:
            result.append(tweet[0])
    return result
        

def test2a():
    print("===2a===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ObamacareFail")	
    tweets.sort()
    print(tweets == ['16-10-25', '16-10-29', '16-10-31'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ElectionDay")
    tweets.sort()
    print(tweets == ['16-08-09', '16-11-08'])
    print(get_dates_for_hashtag("donald-tweets.csv", "China")==[]) 

test2a()

###############
# Question 2b #
###############

def active_hour(filename,start_date,end_date):
    data = read_csv(filename)
    freq = {}
    for tweet in data[1:]:
        if datetime.strptime(start_date, "%y-%m-%d") <= datetime.strptime(tweet[0], "%y-%m-%d") <= datetime.strptime(end_date, "%y-%m-%d"):
            if datetime.strptime(tweet[1], "%X").hour not in freq:
                freq[datetime.strptime(tweet[1], "%X").hour] = 1
            else:
                freq[datetime.strptime(tweet[1], "%X").hour]  += 1
    highest = None
    result = []
    for hour in freq:
        if highest == None or freq[hour] > highest:
            highest = freq[hour]
            result = [hour]
        elif freq[hour] == highest:
            result.append(hour)
        result.sort()
    return result
def test2b():
    print("===2b===")
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-08")==[21])
    print(active_hour("donald-tweets.csv", "16-08-23", "16-11-06")==[1])
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-06")==[0, 23])

#test2b()

###############
# Question 2c #
###############

def top_k(filename,k,start_date,end_date):
    data = read_csv(filename)
    result = []
    for tweet in data[1:]:
        if datetime.strptime(start_date, "%y-%m-%d") <= datetime.strptime(tweet[0], "%y-%m-%d") <= datetime.strptime(end_date, "%y-%m-%d"):
            result.append([tweet[2], int(tweet[4])])
    result.sort(key = lambda x: x[1], reverse = True)
    final = list(map(lambda x: x[0], result))[:k]
    return final
        
    
def test2c():
    print("===2c===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])

#test2c()


##############
# Question 3 #
##############


 
class Student:

    cohort = []

    def __init__(self, name):
        self.name = name
        self.courses = []
        Student.cohort.append(self)

    def add_courses(self, *courses):
        for course in courses:
            if course not in self.courses:
                self.courses.append(course)

    def drop_courses(self, *courses):
        for course in courses:
            if course in self.courses:
                self.courses.remove(course)

    def get_courses(self):
        return self.courses

    def is_coursemate(self, student):
        for course in self.courses:
            if course in student.courses:
                return True
        return False

    def common_courses(self, student):
        result = []
        for course in self.courses:
            if course in student.courses:
                result.append(course)
        return result

    def friend_list(self):
        result = []
        for s in Student.cohort:
            if s != self and self.is_coursemate(s):
                result.append(s)
        return result

    def common_friends(self, student):
        result = []
        f1 = self.friend_list()
        f2 = student.friend_list()
        for f in f1:
            if f != student and f in f2:
                result.append(f.name)
        return result

    def six_degrees(self, student):
        initial = [self]
        pathq = [initial]
        while len(pathq) != 0:
            tmp = pathq.pop(0)
            last_node = tmp[-1]
            if last_node == student:
                return len(tmp) - 1
            for next in last_node.friend_list():
                if next not in tmp:
                    new_path = tmp + [next]
                    pathq.append(new_path)
        return None
        
        

    
    

        
        

    

            
    
# sample execution
def test3():
    print("===3===")
    benj = Student("Ben Junior")
    benj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS2016", "GEM2455")
    tanj = Student("Tan Junior")
    tanj.add_courses("CS1010", "CS1014", "CS2010", "CS2060", "CS3243")
    amanda = Student("Amanda See")
    amanda.add_courses("GEM1010", "CS1014",  "CS1231", "CS2017", "GEM2455")
    ad = Student("Ad Lee")
    ad.add_courses("CS1010", "CS1000", "CS2010", "CS2040", "CS1207")
    ayush = Student("Ayush")
    ayush.add_courses("MA1016", "MA1014", "MA2050", "MA2016")

    print(benj.is_coursemate(tanj))
    print(benj.is_coursemate(amanda))
    print(benj.is_coursemate(ad))
    print(benj.is_coursemate(ayush)==False)
    print(benj.common_courses(tanj)==['CS1010', 'CS1014', 'CS2010', 'CS2060'])
    print(benj.common_courses(amanda)==['CS1014', 'GEM2455']) # Found interesting girl in class!
    print(benj.common_courses(ad)==['CS1010', 'CS2010'])
    print(benj.common_courses(ayush)==[])

    amanda.drop_courses("CS1014", "GEM2455") # She disappears from our class :'(
    amanda.add_courses("CS3243")
    print(benj.is_coursemate(amanda)==False)
    
    print(benj.common_courses(amanda)==[]) # Girl disappears
    print(amanda.get_courses()==['GEM1010', 'CS1231', 'CS2017', 'CS3243']) # What is she taking now? 

    print(benj.six_degrees(amanda)==2) # How can we get to know her?


    print(benj.common_friends(amanda)==['Tan Junior'])
    print(amanda.common_courses(tanj)==['CS3243'])

    tanj.drop_courses("CS3243")
    print(benj.six_degrees(amanda)==None) 
    print(benj.common_friends(amanda)==[])

    amanda.add_courses("MA2050")
    amanda.is_coursemate(ayush)
    ayush.add_courses("CS1000")
    print(benj.six_degrees(amanda)==3)

    
test3()

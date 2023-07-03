

#################
# Q1a - Shuffle #
#################

def shuffle(a, times):
    def do_once(a):
        length = int((len(a)+1)/2)
        a1 = a[:length]
        a2 = a[length:]
        
        result = []
        for i in range(len(a1)):
            result.append(a1[i])
            if i<len(a2):
                result.append(a2[i])
        return result

    for i in range(times):
        a = do_once(a)
    return a

def test1a():
    print('=== Q1a ===')
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 1)==[1, 5, 2, 6, 3, 7, 4, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 2)==[1, 3, 5, 7, 2, 4, 6, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8], 3)==[1, 2, 3, 4, 5, 6, 7, 8])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 1)==[1, 5, 2, 6, 3, 7, 4])
    print(shuffle([1, 2, 3, 4, 5, 6, 7], 2)==[1, 3, 5, 7, 2, 4, 6])


def test1a_e():
    print('=== Q1_e ===')
    '''
    Single shuffles - No recursion happens
    '''
    #Empty lists
    print(shuffle([], 1) == [])
    #Single element lists
    print(shuffle([3], 1) == [3])
    # Simple shuffle check. For even and odd number of elements
    print(shuffle([10, 11, 12, 13 , 14, 15, 16, 17], 1) == [10, 14, 11, 15, 12, 16, 13, 17])
    print(shuffle([10, 11, 12, 13, 15, 16, 17], 1) == [10, 15, 11, 16, 12, 17, 13])
    # Check against the assumption that the list in sorted
    print(shuffle([9, 8, 7, 6, 5, 4, 3], 1) == [9, 5, 8, 4, 7, 3, 6])
    #print(shuffle([7, 2, 6, 1, 3, 49, 22, 21], 1) == [7, 3, 2, 49, 6, 22, 1, 21])    
    # Check for being type agnostic
    #print(shuffle([ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 1) == ['A', 8, 2, 9, 3, 10, 4, 'J', 5, 'Q', 6, 'K', 7])
    '''
    Multiple shuffles - Check for recursion
    '''
    #Empty lists
    print(shuffle([], 7) == [])
    #Single element lists
    print(shuffle([9], 2) == [9])
    # Simple shuffle check. For even and odd number of elements
    print(shuffle([1, 2, 3], 2) == [1, 2, 3])
    #print(shuffle([10, 11, 12, 13 , 14, 15, 16, 17], 17) == [10, 12, 14, 16, 11, 13, 15, 17])
    #print(shuffle([10, 11, 12, 13, 15, 16, 17], 3) == [10, 11, 12, 13, 15, 16, 17])
    # Check against the assumption that the list in sorted
    #print(shuffle([9, 8, 7, 6, 5, 4, 3], 11) == [9, 7, 5, 3, 8, 6, 4])
    print(shuffle([7, 2, 6, 1, 3, 49, 22, 21], 7) == [7, 3, 2, 49, 6, 22, 1, 21])    
    # Check for being type agnostic
    print(shuffle([ 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 2) == ['A', 'J', 8, 5, 2, 'Q', 9, 6, 3, 'K', 10, 7, 4])
    '''
    shuffling list of lists!
    '''
    print(shuffle([[1, 2, "buckle my show"],[3, 4, "lock the door"],[5, 6, "pick up the sticks"],[7, 8, "lay them straight"],23,"asgard",22.3], 1) == [[1, 2, 'buckle my show'], 23, [3, 4, 'lock the door'], 'asgard', [5, 6, 'pick up the sticks'], 22.3, [7, 8, 'lay them straight']])

#test1a()
#test1a_e()

##########################
# Q1b - Back to Original #
##########################

def back_to_original(a):
    def do_once(a):
        length = int((len(a)+1)/2)
        a1 = a[:length]
        a2 = a[length:]
        
        result = []
        for i in range(len(a1)):
            result.append(a1[i])
            if i<len(a2):
                result.append(a2[i])
        return result

    count = 1
    b = do_once(a)
    while a != b:
        b = do_once(b)
        count += 1
    return count 

def test1b():
    print('=== Q1b ===')    
    print(back_to_original([1, 2, 3, 4, 5, 6, 7, 8])==3)
    print(back_to_original([1, 2, 3, 4, 5])==4)
    print(back_to_original([1, 1, 1, 1])==1)

def test1b_e():
    print('=== Q1b_e ===')
    #empty lists
    print(back_to_original([])==1)

    #single element lists
    print(back_to_original([3])==1)

    #Single shuffle returns
    print(back_to_original([0, 0, 0, 0])==1)
    print(back_to_original([1, 2, 2, 1])==1)

    # arbitrary shuffles
    print(back_to_original([1, 1, 1, 2, 2, 2])==4)
    print(back_to_original([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2])==10)
    #print(back_to_original([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])==10)

    print(back_to_original([0, 0, 0, 1, 0])==4)
    print(back_to_original([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])==4)
    print(back_to_original([1, 2, 1, 1])==2)

    #type agnostic shuffles
    print(back_to_original([[1, 2, "buckle my show"],[3, 4, "lock the door"],[5, 6, "pick up the sticks"],[7, 8, "lay them straight"],23,"asgard",22.3])==3)


#test1b()
#test1b_e()

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
    data = read_csv(filename)[1:]

    results = []
    for date,time,tweet,htags,likes,rt in data:
        if hashtag in htags and date not in results:
            results.append(date)
    return results
    

def test2a():
    print("===2a===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ObamacareFail")	
    print(tweets == ['16-10-31', '16-10-29', '16-10-25'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "ElectionDay")
    print(tweets == ['16-11-08', '16-08-09'])
    print(get_dates_for_hashtag("donald-tweets.csv", "China")==[]) 

def test2a_e():
    print("===2a_e===")
    tweets = get_dates_for_hashtag("donald-tweets.csv", "vaticanwalls")	
    print(tweets == ['16-02-19'])
    tweets = get_dates_for_hashtag("donald-tweets.csv", "IranDeal")
    print(set(tweets) == set(['15-09-09', '15-08-28', '15-08-11', '15-07-28']))
    #print(set(get_dates_for_hashtag("donald-tweets.csv", "India"))==set(['16-04-27']))
    #print(set(get_dates_for_hashtag("donald-tweets.csv", "BigLeagueTruth"))==set(['16-10-20', '16-10-10', '16-10-05', '16-10-03']))
    print(set(get_dates_for_hashtag("donald-tweets.csv", "RIGGED"))==set(['16-10-18']))
    print(set(get_dates_for_hashtag("donald-tweets.csv", "RiggedSystem"))==set(['16-10-17', '16-07-05'])) 

    print(get_dates_for_hashtag('modi-tweets-cleaned.csv', 'gqworld')==['11-09-21'])

#test2a()
#test2a_e()

###############
# Question 2b #
###############

def active_hour(filename,start_date,end_date):
    start = datetime.strptime(start_date+" 00:00:00", "%y-%m-%d %X")
    end = datetime.strptime(end_date+" 23:59:59", "%y-%m-%d %X")

    counts =  {}
    for i in range(24):
        counts[i] = 0
    
    data = read_csv(filename)[1:]
    for date,time,tweet,htags,likes,rt in data:
        date = datetime.strptime(date+" "+time, "%y-%m-%d %X")
        if start<=date<=end: 
            counts[date.hour] += 1
    max_count = max(counts.values())
    if max_count == 0:
        return None
    results = list(filter(lambda x:x[1] == max_count,counts.items()))
    return list(map(lambda x:x[0], results))
    
def test2b():
    print("===2b===")
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-08")==[21])
    print(active_hour("donald-tweets.csv", "16-08-23", "16-11-06")==[1])
    print(active_hour("donald-tweets.csv", "16-11-06", "16-11-06")==[0, 23])

def test2b_e():
    print("===2b_e===")
    print(set(active_hour("donald-tweets.csv", "16-10-06", "16-11-09"))==set([1]))
    print(set(active_hour("donald-tweets.csv", "16-08-23", "16-12-31"))==set([1]))
    print(active_hour("donald-tweets.csv", "17-11-06", "17-12-06")==None)
    print(active_hour("donald-tweets.csv", "16-10-06", "16-11-09")==[1])

    print(active_hour('modi-tweets-cleaned.csv','09-04-03','19-02-01')==[19])
    print(active_hour("modi-tweets-cleaned.csv", "09-10-06", "12-11-09")==[9])
    print(active_hour("modi-tweets-cleaned.csv", "12-10-06", "14-11-09")==[20])
    print(active_hour("modi-tweets-cleaned.csv", "15-10-06", "17-11-09")==[19])

#test2b()
#test2b_e()

###############
# Question 2c #
###############

def top_k(filename,k,start_date,end_date):
    start = datetime.strptime(start_date+" 00:00:00", "%y-%m-%d %X")
    end = datetime.strptime(end_date+" 23:59:59", "%y-%m-%d %X")

    tweets =  {}
    data = read_csv(filename)[1:]
    for date,time,tweet,htags,likes,rt in data:
        date = datetime.strptime(date+" "+time, "%y-%m-%d %X")
        if start<=date<=end: 
            tweets[tweet] = int(likes)
    results = list(tweets.items())
    results.sort(key=lambda x:x[1],reverse=True)
    results = results[:k]
    return list(map(lambda x:x[0],results))
    
def test2c():
    print("===2c===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])

def test2c_e():
    print("===2c_e===")
    tweets = ['TODAY WE MAKE AMERICA GREAT AGAIN!']
    print(top_k("donald-tweets.csv", 1, "16-11-08", "16-11-08")==tweets)
    tweets = ['The media is spending more time doing a forensic analysis of Melanias speech than the FBI spent on Hillarys emails.', 'Such a great honor to be the Republican Nominee for President of the United States. I will work hard and never let you down! AMERICA FIRST!', 'Here is my statement. https://t.co/WAZiGoQqMQ']
    print(top_k("donald-tweets.csv", 3, "15-10-13", "16-10-11")==tweets)
    print(top_k("donald-tweets.csv", 1, "16-11-18", "16-11-20")==[])
    tweets = top_k("donald-tweets.csv", 2, "15-07-18", "15-07-18")
    ans = ['Its a national embarrassment that an illegal immigrant can walk across the border and receive free health care and one of our Veterans.....', '....that has served our country is put on a waiting list and gets no care.']
    print(tweets == ans)

    tweets = top_k('modi-tweets-cleaned.csv', 5, '09-04-03', '10-04-03')
    ans = ['i wish to ask the prime minister are you not weak if indeed you are a strong government the country needs proof of that', 'who will save us from the antics of pakistan despite mumbai attacks congress still asleep', 'my stand is clear from the beginning that i am in gujarat will remain in gujarat and will do service to the people of the state', 'hang me if i am guilty   httpwwwnarendramodiin', 'vote for bringing back indian black money deposited in swiss bank participate in the nationwide poll campaign at wwwnarendramodiinpolls']
    print(tweets==ans)
    
    tweets = top_k('modi-tweets-cleaned.csv', 5, '14-04-03', '16-04-03')
    ans = ['india has won        ', 'congratulations team india for the amazing victory indvspak', 'what a match proud of our team great innings imvkohli  exemplary leadership msdhoni', 'that was a thrilling game congratulations team india very happy well played bangladesh indvsban', 'as the year 2016 begins my greetings  good wishes to everyone may 2016 bring joy peace prosperity  good health in everyones lives']
    print(tweets == ans)

    tweets = top_k('modi-tweets-cleaned.csv', 1, '19-02-03', '19-04-03')
    ans = ['        1145  1200             i would be addressing the nation at around 1145 am  1200 noon with an important message   do watch the address on television radio or social media']
    print(tweets==ans)

    tweets = top_k('modi-tweets-cleaned.csv', 7, '18-01-03', '18-01-04')
    ans = ['i bow to the great savitribai phule on her jayanti hers was a life devoted to the empowerment of the poor and marginalised she gave utmost importance to education and social reform we are deeply guided by her ideals and are working tirelessly towards fulfilling her vision', 'sharing a newsletter containing highlights of last weeks mannkibaat  httpjansamparknicincampaigns201803janindexhtml ']
    print(tweets == ans)

#test2c()
#test2c_e()


##############
# Question 3 #
##############

##class Course:
##    all_courses = {}
##
##    def __init__(self, name):
##        self.name = name
##        self.students = []
##        Course.all_courses[name] = self
##
##    def add_student(self,student):
##        if student not in self.students:
##            self.students.append(student)
##
##    def remove_student(self,student):
##        if student in self.students:
##            self.students.remove(student)
##
##class Student:
##    
##    def __init__(self, name):
##        self.name = name
##        self.courses = {}
##        self.private = False
##
##    def add_courses(self, *courses):
##        for course in courses:
##            if course not in Course.all_courses:
##                c = Course(course)
##            else:
##                c = Course.all_courses[course]
##            c.add_student(self)
##            self.courses[course] = c
##
##    def drop_courses(self, *courses):
##        for course in courses:
##            if course not in Course.all_courses:
##                c = Course(course)
##            else:
##                c = Course.all_courses[course]
##            c.remove_student(self)
##            if course in self.courses:
##                del self.courses[course]
##
##    def get_courses(self):
##        return list(self.courses.keys())
##            
##    def common_courses(self,other):
##        result = []
##        for course in self.courses:
##            if course in other.courses:
##                result.append(course)
##        return result
##
##    def is_coursemate(self,other):
##        return self.common_courses(other) != []
##
##    def common_friends(self,other):
##        results = []
##        my_friends = self.friends()
##        for friend in other.friends():
##            if friend in my_friends and friend not in results:
##                results.append(friend)
##        return list(map(lambda x: x.name, results))
##
##    def friends(self):  # Helper function
##        result = []
##        for course in self.courses:
##            for student in self.courses[course].students:
##                if student not in result and student != self:
##                    result.append(student)
##        return result
##
##    def six_degrees(self,other):
##        friends = self.friends()
##        if other in friends:
##            return 1
##
##        count = 1
##        loop_detect = []
##        while True:
##            new_friends = []
##            count +=1
##            for friend in friends:
##                for f in friend.friends():
##                    if f not in new_friends and f != self:
##                        new_friends.append(f)
##
##            names = list(map(lambda x:x.name,new_friends))
##            names.sort()
##            if names in loop_detect:
##                return None
##            elif other in new_friends:
##                return count
##
##            friends = new_friends
##            loop_detect.append(names)

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


def test3():
    print("===3a===")

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
    ayush.add_courses("CS1000")
    print(benj.six_degrees(amanda)==3)

'''
Evaluation test cases
-----------------------------------------------------------------
Methods to be tested:
=================================================================
o add_courses (1 mark)
	* add_single_course() - 1/2 mark
                        o Normal add courses
                        o Adding a course that is already being taken
	* add_multiple_courses() - 1/2 mark
                        o Adding multiple courses 
                        o Adding multiple courses, some of which are already being taken 
                        o Adding multiple course, all of which are already being taken 
o drop_courses (1 mark)
	* drop_single_course() - 1/2 mark
                        o Normal drop courses
                        o Dropping a course that is not being taken
	* drop_multiple_courses() - 1/2 mark
                        o Dropping multiple valid courses
                        o Dropping multiple courses, some of which are not being taken 
                        o Dropping multiple courses, all of which are not being taken 
o get_courses (1 mark)
	* get_courses_check() - 1 mark
                        o retrieve courses after adding them to the student
                        o get_courses right after initialization
o is_coursemate (1 mark)
	* coursemates() - 1 mark
                        o normal check for student from same course
                        o check for student who is not in the same course 
                        o check for a student with a mutual friend but no mutual course
o common_friends (2 marks)
        * check_common_friends()- 1 mark
                        o Check with single common friend 
                        o check with multiple common friends 
	* check_for_loners() - 1 mark
                        o check with no friends for one student 
                        o check for no friends for both students 
o common_courses (1 mark)
	* check_common_course() - 1 mark
                        o Normal common courses check 
                        o check when two people have common friends but no common courses 
o six_degrees (3 marks)
	* six_degrees_general_case() - 1 mark
                        o Normal link length for connected Students
	* six_degreed_none_check() - 1 mark
                        o non-existent link check
                        o Cyclical link check - group of friends are are connected in a cycle. Student being tested for is outside the cycle
                                                Check for seeing if students can terminate the 'searching' operation correctly
                        o Check for six_degrees between people with no friends at all
        * six_degrees_direct_friends() - 1 mark              
                        o Students who are exclusively each others friends
                        o Students who are direct friends in general
	
''' 

peter = None
sam = None
rita = None
mark = None
sara = None

tom = None

def init():
    global peter 
    global sam
    global rita
    
    global mark
    global sara

    global tom

    mark = Student('Mark')
    sara = Student('Sara')

    peter = Student('Peter')
    sam = Student('Sam')
    rita = Student('Rita')

    tom = Student('Tom')

def add_single_course():

    init()
    results = []
    
    peter.add_courses('MA320')
    sam.add_courses('ECE317')
    rita.add_courses('CE101')

    # Simple add courses
    results.append(peter.get_courses()==['MA320'])
    results.append(sam.get_courses()==['ECE317'])
    results.append(rita.get_courses()==['CE101'])
    
    #Adding a course that is already being taken by the student
    peter.add_courses('CS101')
    sam.add_courses('ECE317')
    
    results.append(set(peter.get_courses())==set(['MA320','CS101']))
    results.append(sam.get_courses()==['ECE317'])

    return results
    
def add_multiple_courses():
    
    results = []
    
    #simple add multiple courses
    mark.add_courses('MA320', 'MA110', 'MA400')
    results.append(set(mark.get_courses())==set(['MA320', 'MA110', 'MA400']))
    #check against passing duplicate courses in the arguments
    sara.add_courses('CE101', 'CE102', 'CE101', 'CE103')
    results.append(set(sara.get_courses())==set(['CE101', 'CE102', 'CE103']))
    #adding multiple courses, some of which are already being taken by the student
    sara.add_courses('CE103', 'CE104')
    results.append(set(sara.get_courses())==set(['CE101', 'CE102', 'CE103', 'CE104']))
    #adding all redundant courses
    sara.add_courses('CE101', 'CE102', 'CE103', 'CE104')
    results.append(set(sara.get_courses())==set(['CE101', 'CE102', 'CE103', 'CE104']))
    
    return results

def drop_single_course():

    results = []

    #drop of a course that is not being taken
    mark.drop_courses('CE101')
    #simple course drop
    mark.drop_courses('MA400')

    results.append(set(mark.get_courses())==set(['MA320','MA110']))

    return results

def drop_multiple_courses():

    results = []

    #dropping courses, none of which are being taken
    sam.drop_courses('NE001', 'NE002', 'NE003')
    #dropping courses some of which are not being taken
    sara.drop_courses('CE104', 'ME102')

    results.append(set(sara.get_courses())==set(['CE101','CE102','CE103']))

    #dropping all of sara's courses
    sara.drop_courses('CE101','CE102','CE103')
    results.append(sara.get_courses()==None or sara.get_courses()==[])

    return results

def get_courses_check():
    
    results = []

    #add some courses to tom and see if get_courses can retrieve it
    #kind of redundant, but benefits students to get some partial marks
    results.append(tom.get_courses()==[])
    tom.add_courses('PE321', 'PE211')
    results.append(set(tom.get_courses())==set(['PE321', 'PE211']))

    return results 

def coursemates():
 
    results = []

    # peter and mark both take MA320
    results.append(peter.is_coursemate(mark))
    # peter and sam have no courses in common
    results.append(not peter.is_coursemate(sam))
    sam.add_courses('MA110')
    # peter and sam still don't have any courses in common
    results.append(not peter.is_coursemate(sam))

    return results
    
def check_common_friends():

    results = []

    peter.add_courses('AC314','CS215','CS228')
    mark.add_courses('AC314','MA001','MA802')
    sam.add_courses('AC314','CAD101','E345')
    sara.add_courses('CAD101','CE101','CE103','CE104','DS315')
    rita.add_courses('DS315','AC322','AC317')

    #TO BE DEBUGGED: People shouldn't be their own common friends!
    results.append(peter.common_friends(sam)==['Mark'])
    results.append(peter.common_friends(rita)==[])
    results.append(peter.common_friends(sara)==['Sam'])
    results.append(mark.common_friends(rita)==[])
    results.append(mark.common_friends(sara)==['Sam'])

    return results

def check_for_loners():

    #make sure the student's logic doesn't break when testing for common friends between loners (people with no friends)

    results = []

    rita.drop_courses('DS315','CE101')
    #rita is now a loner
    results.append(rita.common_friends(sam)==[] or rita.common_friends(sam)==None)
    results.append(rita.common_friends(tom)==[] or rita.common_friends(tom)==None)

    return results

def check_common_courses():

    results = []
    #simple checks for common courses between people. nothing special here
    
    results.append(set(peter.common_courses(mark))==set(['AC314','MA320']))
    results.append(set(sam.common_courses(rita))==set([]) or sam.common_courses(rita)==None)  

    rita.drop_courses('CE101','AC322','AC317')
    tom.drop_courses('PE321','PE211')

    #check that the students logic doesn't break when the Student in question has no courses
    results.append(rita.common_courses(tom)==[] or rita.common_courses(tom)==None)

    return results

def six_degree_general_case():

    results = []

    peter.add_courses('MA444')
    peter.drop_courses('MA320','AC314')
    mark.drop_courses('MA320','AC314')
    mark.add_courses('PY200')
    sara.add_courses('PY200')
    rita.add_courses('CE103','CS777')
    tom.add_courses('CS777','MA444')

    '''
    At this stage, the network of friends should like like the following:

    (ONLY COMMON COURSES WRITTEN)

    (MARK)--PY200--(SARA)--CE103--(RITA)--CS777--(TOM)
      |              |                              |
    MA110         CAD101                          MA444
      |              |                              |
    (SAM)------------+                           (PETER)

    '''

    results.append(peter.six_degrees(sara)==3)
    results.append(mark.six_degrees(peter)==4)
    results.append(rita.six_degrees(peter)==2)
    results.append(sam.six_degrees(tom)==3)

    return results

def six_degree_none_check():
    
    results = []

    rita.drop_courses('CE103')
    tom.drop_courses('MA444')

    #sara and rita are not friends anymore
    results.append(sara.six_degrees(rita)==None)
    #tom and peter are not friends anymore
    results.append(tom.six_degrees(peter)==None)

    return results

def six_degree_direct_friends():
    
    results = []

    #check for six_degreed==1 for people who are in the same courses
    results.append(mark.six_degrees(sara)==1)
    results.append(rita.six_degrees(tom)==1)

    return results

def test3_e():
    print('===Q3_e===')
    print(add_single_course())
    print(add_multiple_courses())
    print(drop_single_course())
    print(drop_multiple_courses())
    print(get_courses_check())
    print(coursemates())
    print(check_common_friends())
    print(check_for_loners())
    print(check_common_courses())
    print(six_degree_general_case())
    print(six_degree_none_check())
    print(six_degree_direct_friends())

test3()    
test3_e()




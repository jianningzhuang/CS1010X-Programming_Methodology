import csv
from math import sqrt

##############
# Question 1 #
##############


###################
# Q1a - In circle #
###################

def digit_product(n):
    result = 1
    for digit in str(n):
        result *= int(digit)
    return result
    


def test1a():
    print('=== Q1a ===')
    print(digit_product(1111)==1)
    print(digit_product(123)==6)
    print(digit_product(123041)==0)

test1a()



########################
# Q1b - Furthest Apart #
########################

def max_digit_product(n, k):
    string_n = str(n)
    max_val = None
    for i in range(len(string_n) - k + 1):
        subset = string_n[i:i+k]
        if max_val == None or digit_product(int(subset)) > max_val:
            max_val = digit_product(int(subset))
    return max_val
        


def test1b():
    print('=== Q1b ===')
    print(max_digit_product(11123,1)==3)
    print(max_digit_product(11123,2)==6)
    print(max_digit_product(1111111,5)==1)
    print(max_digit_product(189113451,2)==72)

test1b()


###########################
# Q2 - Show me the Money! #
###########################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
def count_NA_employment(data):
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):
    return len(list(filter(lambda x: x[5] == "NA", data)))

#######
# Q2A #
#######

def parse_data(filename):
    data = read_csv(filename)[1:]
    result = {}
    for year, uni, school, degree, variable, value in data:
        if (int(year), uni, school, degree) not in result:
            result[(int(year), uni, school, degree)] = ["NA", "NA"]
        if variable == "employment_rate_overall" and value != "":
            result[(int(year), uni, school, degree)][0] = float(value)
        if variable == "basic_monthly_median" and value != "":
            result[(int(year), uni, school, degree)][1] = float(value)
    ans = []
    for i in result:
        tmp = list(i) + result[i]
        ans.append(tmp)
    return ans
        
        
        
            
        

def count_NA_employment(data):   # Helper for testing
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):       # Helper for testing
    return len(list(filter(lambda x: x[5] == "NA", data)))

def test2a():
    print('=== Q2a ===')
    print(len(parse_data("employment.csv"))==179)
    print(count_NA_employment(parse_data("employment.csv"))==1)
    print(count_NA_salary(parse_data("employment.csv"))==1)

test2a()

#######
# Q2B #
#######

def compute_employment_rate(filename,university,degree,start,end):
    data = parse_data(filename)
    result = []
    for item in data:
        if item[1] == university and item[3] == degree and start <= int(item[0]) <= end:
            if item[4] == "NA":
                continue
            else:
                result.append(float(item[4]))
    if result == []:
        return "NA"
    return sum(result)/len(result)

def test2b():
    print('=== Q2b ===')
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)==100.0)
    print(compute_employment_rate("employment.csv",'Nanyang Technological University', \
        "Bachelor of Medicine and Bachelor of Surgery",2000,2018)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Medicine and Bachelor of Surgery",2014,2014)=="NA")
    print(compute_employment_rate("employment.csv",'National University of Singapore', \
        "Bachelor of Computing (Computer Science)",2014,2018)==93.8)

test2b()

#######
# Q2C #
#######

def top_k_degree(filename,start,end,k):
    data = parse_data(filename)
    median = {}
    for year, uni, school, degree, ero, bmm in data:
        if start <= int(year) <= end:
            if (uni, degree) not in median:
                if bmm != "NA":
                    median[(uni, degree)] = [[int(year), float(bmm)]]
            else:
                if bmm != "NA":
                    median[(uni, degree)].append([int(year), float(bmm)])
    result = []
    for key, value in median.items():
        value.sort(key = lambda x: x[0])
        print(value)
        increasing = True
        for i in range(1, len(value)):
            if value[i][1] <= value[i-1][1]:
                increasing = False
                break
        if increasing == True:
            acc = 0.0
            for j in value:
                acc += j[1]
            acc = acc/len(value)
            result.append([key[1], key[0], acc])

    if result == []:
        return []


    result.sort(key = lambda x: x[2], reverse = True)
    final = result[:k]
    i = 0
    while result[i+k][2] == result[k-1][2]:
        final.append(result[i+k])
        i += 1
    final_final = list(map(lambda x: x[:2], final))
    print(final_final)
    return final_final
        
            
                
        
    

def test2c():
    print('=== Q2c ===')
    print(top_k_degree("employment.csv",2014,2015,3)==\
          [['Business and Computing', 'Nanyang Technological University'],\
           ['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], \
           ['Bachelor of Business Administration (Hons)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2014,2018,3)==[])

#test2c()

################################
# Q3 - Social Network Security #
################################

privacy_settings = ["private", "friends", "FOF", "public"]
# private = no one can read
# friends = friends can read
# FOF = friends of friends can read
# public = anyone can read

class User:

    def __init__(self, name):
        self.name = name
        self.requests = []
        self.friends = []
        self.wall = []

    def request(self, user):
        if self in user.requests:
            return False
        elif user in self.requests:
            self.friends.append(user)
            user.friends.append(self)
            self.requests.remove(user)
            return True
        else:
            user.requests.append(self)
            return True
    def accept(self, user):
        if user in self.requests:
            self.requests.remove(user)
            self.friends.append(user)
            user.friends.append(self)
            return True
        else:
            return False

    def is_friend(self, user):
        return user in self.friends

    def unfriend(self, user):
        if user not in self.friends:
            return False
        else:
            self.friends.remove(user)
            user.friends.remove(self)
            return True

    def post(self, message, *privacy_setting):
        if privacy_setting == ():
            if self.wall == []:
                privacy_setting = ("public",)
            else:
                privacy_setting = (self.wall[-1][1],)
        if privacy_setting[0] not in ["private", "friends", "FOF", "public"]:
            return "Bad privacy setting"
        self.wall.append([message, privacy_setting[0]])


    def friend_of_friend(self, other):
        if other in self.friends:
            return True
        else:
            for friend in self.friends:
                if other in friend.friends:
                    return True
            return False

    def read_posts(self, user):
        result = []
        for post in user.wall:
            if self == user:
                result.append(post[0])
            elif post[1] == "public":
                result.append(post[0])
            elif post[1] == "friends":
                if self in user.friends:
                    result.append(post[0])
            elif post[1] == "FOF":
                if user.friend_of_friend(self):
                    result.append(post[0])
        return result

    def update_privacy(self, message, privacy_setting):
        if privacy_setting not in ["private", "friends", "FOF", "public"]:
            return "Bad privacy setting"
        found = False
        for i in range(len(self.wall)-1, -1, -1):
            if self.wall[i][0] == message:
                if self.wall[i][1] == privacy_setting:
                    continue
                else:
                    self.wall[i][1] = privacy_setting
                    found = True
                    break

        if found == False:
            return "Message not found"
        
        

    
        

def test3():
    print('=== Q3 ===')
    ben = User("Ben")
    oana = User("Oana")
    chenhao = User("Chenhao")
    clement = User("Clement")

    print(ben.is_friend(oana)==False)
    print(ben.is_friend(chenhao)==False)
    print(ben.accept(oana)==False)

    print(oana.request(ben)==True)
    print(oana.request(chenhao)==True)
    print(oana.request(chenhao)==False)
    print(oana.is_friend(ben)==False)
    print(oana.is_friend(chenhao)==False)

    print(ben.accept(oana)==True)
    print(chenhao.request(oana)==True)
    print(oana.is_friend(ben)==True)
    print(oana.is_friend(chenhao)==True)

    ben.post("CS1010X is fun")
    ben.post("No tutorials next week","FOF")
    ben.post("Did you remember to order pizza?","friends")
    ben.post("Exam grading will be done on Tuesday.")
    ben.post("Finals will be very difficult","private")

    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    ben.post("Finals will be very difficult")
    ben.update_privacy("Finals will be very difficult","public")
    print(ben.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben) == ['CS1010X is fun', 'No tutorials next week', 'Finals will be very difficult'])
    print(clement.read_posts(ben) == ['CS1010X is fun', 'Finals will be very difficult'])

    ben.update_privacy("Finals will be very difficult","friends")
    print(ben.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(oana.read_posts(ben)== ['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben) == ['CS1010X is fun'])

    print(ben.wall)

    ben.update_privacy("Finals will be very difficult","friends")
    print("check")
    print(ben.wall)
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

    print(oana.unfriend(chenhao)==True)
    print(oana.unfriend(chenhao)==False)
    print(oana.is_friend(chenhao)==False)

    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

test3()

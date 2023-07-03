import csv
from math import sqrt

##############
# Question 1 #
##############


#######################
# Q1a - Digit Product #
#######################

def digit_product(n):
    result = 1
    for c in str(n):
        result *= int(c)
    return result

def test1a():
    print('=== Q1a ===')
    print(digit_product(1111)==1)
    print(digit_product(123)==6)
    print(digit_product(123041)==0)

def test1a_e():
    print('=== Q1a_e ===')
    print(digit_product(0)==0)
    print(digit_product(8)==8)
    print(digit_product(51324)==120)

#test1a()
#test1a_e()


###########################
# Q1b - Max Digit Product #
###########################

def max_digit_product(n,k):
    digits = []
    digits.extend(str(n))
    digits = list(map(lambda x: int(x),digits))
    max_product = 0
    for i in range(len(digits)-k+1):
        product = 1
        for j in range(k):
            product *= digits[i+j]
        max_product = max(product,max_product)
    return max_product

def test1b():
    print('=== Q1b ===')
    print(max_digit_product(11123,1)==3)
    print(max_digit_product(11123,2)==6)
    print(max_digit_product(1111111,5)==1)
    print(max_digit_product(189113451,2)==72)

def test1b_e():
    print('=== Q1b_e ===')
    print(max_digit_product(0,1)==0)
    print(max_digit_product(123,5)==0)
    print(max_digit_product(33421625,2)==12)
    print(max_digit_product(100000,2)==0)
    print(max_digit_product(98231567,4)==432)
    
#test1b()
#test1b_e()


###########################
# Q2 - Show me the Money! #
###########################
# These functions are provided for you
# Do not make any changes to them

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

#######
# Q2A #
#######

##def parse_data(filename):
##
##    def float_or_NA(value):
##        if value == "NA":
##            return value
##        else:
##            return float(value)
##
##    data = read_csv(filename)
##    table = {}
##    for year,university,school,degree,variable,value in data[1:]:
##        if (year,university,school,degree) not in table:
##            table[(year,university,school,degree)] = ["NA", "NA"]
##        if variable == "employment_rate_overall":
##            table[(year,university,school,degree)][0] = value
##        elif variable == "basic_monthly_median":
##            table[(year,university,school,degree)][1] = value
##        else:
##            print("Unknown variable:", variable)
##    ans = list(table.items())
##    ans = list(map(lambda x: [int(x[0][0]),x[0][1],x[0][2],x[0][3],float_or_NA(x[1][0]),float_or_NA(x[1][1])],ans))
##    return ans
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
def count_NA_employment(data):
    return len(list(filter(lambda x: x[4] == "NA", data)))
def count_NA_salary(data):
    return len(list(filter(lambda x: x[5] == "NA", data)))

def test2a():
    print('=== Q2a ===')
    print(len(parse_data("employment.csv"))==179)
    print(count_NA_employment(parse_data("employment.csv"))==1)
    print(count_NA_salary(parse_data("employment.csv"))==1)

def test2a_e():
    print('=== Q2a_e ===')
    print([2014,'National University of Singapore','Medicine','Bachelor of Medicine and Bachelor of Surgery','NA',4500.0] in parse_data("employment.csv"))
    print([2014,'National University of Singapore','Sciences','Bachelor of Science (Pharmacy) (Hons)',98.9,'NA'] in parse_data("employment.csv"))
    print([2015,'National University of Singapore','Medicine','Bachelor of Science (Nursing)',97.3,3200.0] in parse_data("employment.csv"))
    print(parse_data("empty.csv") == [])
    print(count_NA_employment(parse_data("employment.eval.csv"))==6)
    print(count_NA_salary(parse_data("employment.eval.csv"))==4)
    print(len(parse_data("employment.eval.csv"))==214)
    print([2016, 'Singapore Institute of Technology', 'dummy', 'Bachelor in Science (Physiotherapy)', 'NA', 3300.0] in parse_data("employment.eval.csv"))
    print([2016, 'SUTD', 'dummy', 'Bachelor of Engineering (Engineering Product Development)', 89.9, 3600.0] in parse_data("employment.eval.csv"))
#test2a()
test2a_e()

#######
# Q2B #
#######

def compute_employment_rate(filename,university,degree,start,end):
    data = parse_data(filename)
    count = 0
    total = 0
    for year,u,school,d,employment,monthly in data:
        if employment != "NA" and start<=year<=end and university==u and degree==d:
            total += employment
            count += 1
    if count == 0:
        return "NA"
    else:
        return round(total/count,1)

## Tests ##
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

def test2b_e():
    print('=== Q2b_e ===')
    print(round(compute_employment_rate("employment.csv",'National University of Singapore','Bachelor of Science (Pharmacy) (Hons)',2000,2018),1) == 98.1)
    print(round(compute_employment_rate("employment.csv",'Nanyang Technological University','Computer Science',2015,2018),1) == 92.4)
    print(compute_employment_rate("employment.csv",'Singapore Management University','Computer Science',2015,2018) == 'NA')
    print(compute_employment_rate("empty.csv",'Singapore Management University','Computer Science',2015,2018) == 'NA')
    print(round(compute_employment_rate("employment.eval.csv",'Nanyang Technological University','Biological Sciences',2013,2016),1) == 77.2)
    print(round(compute_employment_rate("employment.eval.csv",'Singapore Institute of Technology','Bachelor of Fine Arts in Digital Arts & Animation',2013,2016),1) == 81.9)
#test2b()
#test2b_e()

#######
# Q2C #
#######

def top_k_degree(filename,start,end,k):
##    data = parse_data(filename)
##    table = {}
##    for year,university,school,degree,employment,monthly in data:
##        if start<=year<=end:
##            if (university,school,degree) not in table:
##                table[(university,school,degree)] = ["NA"]*(end-start+1)
##            table[(university,school,degree)][year-start] = monthly
##
##    # Remove those with missing data
##    to_delete = []
##    for key in table:
##        if "NA" in table[key]:
##            to_delete.append(key)
##    for key in to_delete:
##        del table[key]
##
##    # Remove those for which salaries are not increasing.
##    to_delete.clear()
##    for key in table:
##        salaries = table[key]
##        for i in range(len(salaries)-1):
##            if salaries[i] >= salaries[i+1] and key not in to_delete:
##                to_delete.append(key)
##    for key in to_delete:
##        del table[key]
##
##    # Compute total salaries:
##    for key in table:
##        table[key].append(sum(table[key]))
##
##    ans = list(table.items())
##    ans = list(map(lambda x: [x[0][0],x[0][1],x[0][2],x[1][-1]],ans))
##    ans.sort(key=lambda x: x[3], reverse=True)
##    ans = list(filter(lambda x: x[3]>=ans[k-1][3], ans))
##    return list(map(lambda x: [x[2],x[0]], ans))

    data = parse_data(filename)
    salary = {}
    for year, uni, school, degree, ero, bmm in data:
        if start <= int(year) <= end:
            if (degree, uni) not in salary:
                salary[(degree, uni)] = {}
            salary[(degree, uni)][year] = bmm
    result = []
    for d in salary:
        increasing = []
        for y, s in salary[d].items():
            increasing.append([y, s])
        increasing.sort(key = lambda x: x[0])
        promising = True
        if len(increasing) != (end - start + 1):
            promising = False
        else:
            for i in range(1, len(increasing)):
                if increasing[i][1] == "NA" or increasing[i - 1][1] == "NA" or increasing[i][1] <= increasing[i - 1][1]:
                    promising = False
                    break
        if promising == True:
            average = list(map(lambda x: x[1], increasing))
            result.append([list(d), sum(average)/len(average)])
    result.sort(key = lambda x: x[1], reverse = True)
    final = list(map(lambda x: x[0], result[:k]))
    i = 0
    while (k + i) < len(result) and result[k + i][1] == result[k - 1][1]:
        final.append(result[k + i][0])
        i += 1
    return final
                
        

## Tests ##
def test2c():
    print('=== Q2c ===')
    print(top_k_degree("employment.csv",2014,2015,3)==\
          [['Business and Computing', 'Nanyang Technological University'],\
           ['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], \
           ['Bachelor of Business Administration (Hons)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2014,2018,3)==[])

def test2c_e():
    print('=== Q2c_e ===')
    print(top_k_degree("employment.csv",2014,2015,12)[10:16] == [['Bachelor of Arts (Hons)', 'National University of Singapore'], ['Computer Science', 'Nanyang Technological University'], ['Bachelor of Social Sciences', 'National University of Singapore'], ['Bachelor of Computing (Communications and Media)', 'National University of Singapore'], ['Bachelor of Engineering (Chemical Engineering)', 'National University of Singapore'], ['Bachelor of Engineering (Civil Engineering)', 'National University of Singapore']])
    print(top_k_degree("employment.csv",2013,2015,12) == [['Bachelor of Engineering (Computer Engineering)', 'National University of Singapore'], ['Bachelor of Computing (Computer Science)', 'National University of Singapore'], ['Bachelor of Business Administration (Hons)', 'National University of Singapore'], ['Bachelor of Engineering (Engineering Science)', 'National University of Singapore'], ['Bachelor of Engineering (Industrial and Systems Engineering)', 'National University of Singapore'], ['Accountancy and Business', 'Nanyang Technological University'], ['Bachelor of Computing (Information Systems)', 'National University of Singapore'], ['Computer Engineering', 'Nanyang Technological University'], ['Bachelor of Engineering (Environmental Engineering)', 'National University of Singapore'], ['Bachelor of Arts (Hons)', 'National University of Singapore'], ['Bachelor of Social Sciences', 'National University of Singapore'], ['Computer Science', 'Nanyang Technological University'], ['Bachelor of Engineering (Chemical Engineering)', 'National University of Singapore'], ['Bachelor of Engineering (Civil Engineering)', 'National University of Singapore']])
    print(top_k_degree("empty.csv",2013,2015,1) == [])
    print(top_k_degree("employment.eval.csv",2013,2016,5) == [['Accountancy and Business', 'Nanyang Technological University'], ['Computer Engineering', 'Nanyang Technological University'], ['Computer Science', 'Nanyang Technological University'], ['Maritime Studies', 'Nanyang Technological University'], ['Psychology', 'Nanyang Technological University']])
    print(top_k_degree("employment.eval.csv", 2015, 2016, 15) == [['Computer Science', 'Nanyang Technological University'], ['Accountancy and Business', 'Nanyang Technological University'], ['Computer Engineering', 'Nanyang Technological University'], ['Environmental Engineering', 'Nanyang Technological University'], ['Mechanical Engineering', 'Nanyang Technological University'], ['Maritime Studies', 'Nanyang Technological University'], ['Civil Engineering', 'Nanyang Technological University'], ['Bioengineering', 'Nanyang Technological University'], ['Mathematics & Economics', 'Nanyang Technological University'], ['Psychology', 'Nanyang Technological University'], ['Physics / Applied Physics', 'Nanyang Technological University'], ['Sociology', 'Nanyang Technological University'], ['Linguistics And Multilingual Studies', 'Nanyang Technological University'], ['Chemistry & Biological Chemistry', 'Nanyang Technological University'], ['Communication Studies', 'Nanyang Technological University']])

test2c()
test2c_e()

################################
# Q3 - Social Network Security #
################################

privacy_settings = ["private", "friends", "FOF", "public"]
# private = no one can read
# friends = friends can read
# FOF = friends of friends can read
# public = anyone can read

##class User:
##
##    def __init__(self, name):
##        self.name = name
##        self.current_setting = privacy_settings[3]
##        self.posts = []
##        self.requests = []
##        self.friends = []
##
##    def request(self,user):
##        if user in self.requests:
##            self.confirm_friendship(user)
##            return True
##        elif self not in user.requests:
##            user.requests.append(self)
##            return True
##        else:
##            return False
##
##    def confirm_friendship(self,user): #Helper method
##        self.requests = list(filter(lambda x: x is not user,self.requests))
##        user.requests = list(filter(lambda x: x is not self,user.requests))
##        if user not in self.friends:
##            self.friends.append(user)
##        if self not in user.friends:
##            user.friends.append(self)
##
##    def accept(self,user):
##        if user in self.requests:
##            self.confirm_friendship(user)
##            return True
##        else:
##            return False
##
##    def unfriend(self,user):
##        if user in self.friends:
##            self.friends = list(filter(lambda x: x is not user,self.friends))
##            user.friends = list(filter(lambda x: x is not self,user.friends))
##            return True
##        else:
##            return False
##
##    def post(self, msg, *privacy):
##        if privacy and privacy[0] not in privacy_settings:
##            return "Bad privacy setting"
##        if privacy:
##            self.posts.append([msg, privacy[0]])
##            self.current_setting = privacy[0]
##        else:
##            self.posts.append([msg, self.current_setting])
##
##    def read_posts(self,user):
##        if self == user: #Special case - read own posts.
##            return list(map(lambda x: x[0],self.posts))
##
##        results = []
##        for msg, privacy in user.posts:
##            if privacy=="public" or (privacy=="friends" and self.is_friend(user))\
##               or (privacy=="FOF" and (self.is_friend(user) or self.is_FOF(user))):
##                results.append(msg)
##        return results
##
##    def is_friend(self,user):
##        return user in self.friends
##
##    def is_FOF(self,user): # Helper method
##        for friend in self.friends:
##            if friend.is_friend(user):
##                return True
##        return False
##
##    def update_privacy(self, msg, privacy):
##        if privacy not in privacy_settings:
##            return "Bad privacy setting"
##        for i in range(len(self.posts)-1,-1,-1):
##            m, p = self.posts[i]
##            if msg == m and privacy != p:
##                self.posts[i][1] = privacy
##                return
##        return "Message not found"

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

##################
# Marking scheme #
##################
# 4 marks  - Getting the friend/unfriend mechanism right
#    o 2 marks  - request/accept works correctly
#    o 1 mark  - unfriend works correctly
#    o 1 mark  - is_friend is correct
# 4 marks  - getting permissions correct
#    o 1/2 mark  - Self can read properly
#    o 1/2 mark  - Private cannot read
#    o 1 mark  - Friends can read correctly
#    o 1 mark  - FOF can read correctly
#    o 1 mark  - Update privacy works correctly
# 2 marks  - getting the details right
#    o 1/2 mark  - *args for post() is implemented correctly
#    o 1/2 mark  - "Bad privacy setting" alert correct
#    o 1/2 mark  - "Message not found" alert correct
#    o 1/2 mark  - Remember privacy setting correctly.

def test3():
    print('=== Q3 ===')
    ben = User("Ben")
    oana = User("Oana")
    chenhao = User("Chenhao")
    clement = User("Clement")

    print(ben.is_friend(oana)==False)
    print(ben.is_friend(chenhao)==False)
    print(ben.accept(oana)==False) # No request pending

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

    ben.post("Finals will be very difficult")  # Repeated private message.
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

    ben.update_privacy("Finals will be very difficult","friends")
    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun', 'No tutorials next week'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

    print(oana.unfriend(chenhao)==True)
    print(oana.unfriend(chenhao)==False)
    print(oana.is_friend(chenhao)==False)

    print(oana.read_posts(ben)==['CS1010X is fun', 'No tutorials next week', 'Did you remember to order pizza?', 'Exam grading will be done on Tuesday.', 'Finals will be very difficult', 'Finals will be very difficult'])
    print(chenhao.read_posts(ben)==['CS1010X is fun'])
    print(clement.read_posts(ben)==['CS1010X is fun'])

def test3_e():
    print('=== Q3_e ===')
    def test_request():
        a = User("A")
        b = User("B")
        print(a.request(b) == True)
        print(a.request(b) == False)
        print(b.request(a) == True)
        print( (a.is_friend(b) and b.is_friend(a)) == True )
    def test_accept():
        a = User("A")
        b = User("B")
        a.request(b)
        print(a.accept(b) == False)
        print(b.accept(a) == True)
        print( (a.is_friend(b) and b.is_friend(a)) == True)
    def test_is_friend():
        a = User("A")
        b = User("B")
        c = User("C")
        a.request(b)
        b.accept(a)
        print(a.is_friend(c) == False and c.is_friend(a) == False)
        print(a.is_friend(b) == True and b.is_friend(a) == True)
    def test_unfriend():
        a = User("A")
        b = User("B")
        a.request(b)
        b.accept(a)
        print(a.unfriend(b) == True)
        print(b.unfriend(a) == False)
    def test_post_and_read(opt):
        a = User("A")
        ## friend
        b = User("B"); b.request(a); a.accept(b)
        ## fof
        c = User("C"); b.request(c); c.accept(b)
        ## public
        d = User("D")
        ## default
        a.post("default")
        ## FOF
        a.post("fof", "FOF")
        a.post("fof_next")
        ## friends
        a.post("friends", "friends")
        a.post("friends_next")
        ## private
        a.post("private", "private")
        a.post("private_next")
        ## public
        a.post("public", "public")
        a.post("public_next")
        if opt == "self":
            print(a.read_posts(a) == ["default", "fof", "fof_next", "friends", "friends_next", "private", "private_next", "public", "public_next"])
        elif opt == "friend":
            print(b.read_posts(a) == ["default", "fof", "fof_next", "friends", "friends_next", "public", "public_next"])
        elif opt == "fof":
            print(c.read_posts(a) == ["default", "fof", "fof_next", "public", "public_next"])
        else:
            print(d.read_posts(a) == ["default", "public", "public_next"])
    def test_bad_privacy_warning():
        a = User("A")
        a.post("A")
        print(a.update_privacy("A", "Bad") == "Bad privacy setting")
        print(a.post("Bad", "Bad") == "Bad privacy setting")

    def test_update_privacy():
        a = User("A")
        ## friend
        b = User("B"); b.request(a); a.accept(b)
        ## fof
        c = User("C"); b.request(c); c.accept(b)
        ## public
        d = User("D")
        ## default
        a.post("default")
        ## FOF
        a.post("fof", "FOF")
        a.post("fof")
        ## friends
        a.post("friends", "friends")
        a.post("friends")
        ## private
        a.post("private", "private")
        a.post("private")
        ## public
        a.post("public", "public")
        a.post("public")
        a.update_privacy("public", "FOF")
        a.update_privacy("public", "FOF")
        print(d.read_posts(a) == ["default"])
        print(c.read_posts(a) == ["default", "fof", "fof", "public", "public"])

    def test_message_not_found_warning():
        a = User("A")
        a.post("Hi", "FOF")
        print(a.update_privacy("Hi", "FOF") == "Message not found")
        print(a.update_privacy("Hello", "FOF") == "Message not found")

    test_request()
    test_accept()
    test_is_friend()
    test_unfriend()
    test_post_and_read("self")
    test_post_and_read("friend")
    test_post_and_read("fof")
    test_post_and_read("other")
    test_bad_privacy_warning()
    test_update_privacy()
    test_message_not_found_warning()

#test3()
test3_e()

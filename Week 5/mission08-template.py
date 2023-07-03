#
# CS1010S --- Programming Methodology
#
# Mission 8 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    age_title = ()
    for i in range(len(rows)-1):
        age_title += (int(rows[i+1][0]), )
    rep_title = ()
    for rep in rows[0][1:]:
        rep_title += (int(rep), )
    data = ()
    for row in rows[1:]:
        int_row = ()
        for elem in row[1:]:
            int_row += (int(elem), )
        data += (int_row, )

    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
#print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
#print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
#print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
#print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    if pushup < 1:
        return 0
    elif pushup > 60:
        return 25
    return access_cell(pushup_table, age, pushup)
    

def situp_score(situp_table, age, situp):
    if situp < 1:
        return 0
    elif situp > 60:
        return 25
    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run < 510:
        return 50
    elif run > 1100:
        return 0
    elif run%10 != 0:
        run += (10 - run%10)
    return access_cell(run_table, age, run)
        

# print("## Q2 ##")
##print(pushup_score(pushup_table, 18, 61))   # 25
##print(pushup_score(pushup_table, 18, 70))   # 25
##print(situp_score(situp_table, 24, 0))      # 0
##print(situp_score(situp_table, 24, 25))
##print(run_score(run_table, 30, 720))        # 36
##print(run_score(run_table, 30, 725))        # 35
##print(run_score(run_table, 30, 735))        # 35
##print(run_score(run_table, 30, 500))        # 50
##print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score < 51:
        return "F"
    elif score < 61:
        return "P"
    elif score < 75:
        return "P$"
    elif score < 85:
        return "S"
    else:
        return "G"

##print("## Q3 ##")
##print(ippt_award(50))     # F
##print(ippt_award(51))     # P
##print(ippt_award(61))     # P$
##print(ippt_award(75))     # S
##print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    score = pushup_score(get_pushup_table(ippt_table), age, pushup) \
            + situp_score(get_situp_table(ippt_table), age, situp) \
            + run_score(get_run_table(ippt_table), age, run)
    return (score, ippt_award(score))

# print("## Q4 ##")
##print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
##print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
##print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
##print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
##print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########
def make_training_program(rate_pushup, rate_situp, rate_run):
    def training_program(ippt_table, age, pushup, situp, run, days):
        pushup += days//rate_pushup
        situp += days//rate_situp
        run -= days//rate_run
        return (pushup, situp, run, ippt_results(ippt_table, age, pushup, situp, run))

    return training_program

# print("## Q5 ##")
tp = make_training_program(7, 3, 10)
#print(tp(ippt_table, 25, 30, 25, 820, 30))        # (34, 35, 817, (61, 'P$'))


##########
# Bonus  #
##########

def make_tp_bonus(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):







        
        def possible_tp(pushup, situp, run, days, previous):
    
            if days < 0:
                return ((previous[0], previous[1], previous[2]), )
            else:
                return possible_tp(pushup + 1, situp, run, days - rate_pushup, (pushup, situp, run)) \
                + possible_tp(pushup, situp + 1, run, days - rate_situp, (pushup, situp, run)) \
                + possible_tp(pushup, situp, run - 1, days - rate_run, (pushup, situp, run))
        
        highest_score = 0
        best_tp = ()
        for tp in possible_tp(pushup, situp, run, days, (pushup, situp, run)):
            print(tp)
            score = ippt_results(ippt_table, age, tp[0], tp[1], tp[2])[0]
            if score > highest_score:
                highest_score = score
                best_tp = tp
        
        return (best_tp[0], best_tp[1], best_tp[2], (highest_score, ippt_award(highest_score)))
    return tp_bonus

def make_tp_bonus1(rate_pushup, rate_situp, rate_run):
    def tp_bonus(ippt_table, age, pushup, situp, run, days):
        data = [[pushup, rate_pushup, 1], [situp, rate_situp, 2], [run, rate_run, 3]]
        sorted_data = sorted(data,key = lambda x: x[1])
        print(sorted_data[1][1])
        while days >= sorted_data[1][1]:
            for i in sorted_data:
                if i[2] == 3:
                    i[0] = i[0] - days//i[1]
                else:
                    i[0] = i[0] + days//i[1]
                days = days % i[1]
        for i in sorted_data:
            if i[2] == 1:
                pushup = i[0]
            elif i[2] == 2:
                situp = i[0]
            elif i[2] == 3:
                run = i[0]
        ippt_score = ippt_results(ippt_table,age,pushup,situp,run)
        return (pushup,situp,run,ippt_score)
    return tp_bonus


tp_bonus = make_tp_bonus1(7, 3, 10)

# Note: Depending on your implementation, you might get a different number of
# sit-up, push-up, and 2.4km run timing. However, the IPPT score and grade
# should be the same as the sample output.

print(tp_bonus(ippt_table, 25, 20, 30, 800, 30))      # (20, 40, 800, (58, 'P'))
#print(tp_bonus(ippt_table, 25, 20, 30, 800, 2))       # (20, 30, 800, (52, 'P'))

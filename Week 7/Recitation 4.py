###Question 1

##tup_a = (10, 12, 13, 14) 
##print(tup_a)
##tup_b = ("CS1010S", "CS1231") 
##print(tup_b)
##tup_c = tup_a + tup_b 
##print(tup_c) #(10, 12, 13, 14, "CS1010S", "CS1231")
##print(len(tup_c)) #6
##print(14 in tup_a) #True
##print(11 in tup_c) #False
##tup_d = tup_b[0]*4 #"CS1010SCS1010SCS1010SCS1010S"
##print(tup_d)
##tup_d[0] # "C"
##tup_d[1:] #"S1010SCS1010SCS1010SCS1010S
##count = 0
##for i in tup_a:
##    count +=  i
##print(count) #49
##print(max(tup_a)) #14
##print(min(tup_a)) #10
##print(max(tup_c)) #TypeError
##print(min(tup_c))

###Question 2

def part_a(): #or just concatenate
    result = ()
    for i in range(1, 4):
        result += (i,)
    return result

a = (1, ) + (2, ) + (3, )

#part b is impossible

def part_c():
    result = ()
    for i in range(1, 4):
        if i == 2:
            result += ((i,), )
        else:
            result += (i, )
    return result
c = (1, ) + ((2, ), ) + (3, )

def part_d():
    result = ()
    for i in range(1, 4):
        result += (((2*i)-1, 2*i), )
    return result

d = ((1, 2), ) + ((3, 4), ) + ((5, 6), )

###Question 3

i = (7, 6, 5, 4, 3, 2, 1)
print(i[3])

j = (7 , (6 , 5 , 4 ) , (3 , 2 ) , 1 )
print(j[1][2])

k = (7 , (( 6 , 5 , (4 ,) , 3 ) , 2 ) , 1 )
print(k[1][0][2][0])


###Question 4

def make_module(course_code, units):
    return (course_code, units)

def make_units(lecture, tutorial, lab, homework, prep):
    return (lecture, tutorial, lab, homework, prep)

def get_module_code(course):
    return course[0]

def get_module_units(course):
    return course[1]

def get_module_total_units(units):
    return units[ 0 ] + units[ 1 ] + units[ 2 ] + units[ 3 ] + units[ 4 ]

def make_empty_schedule(): # time: O(1), space: O(1)
    return ()

def add_class(course, schedule): # time: O(len(schedule)), space: O(len(schedule))
    if course in schedule:
        return schedule
    else:
        return schedule + (course, ) #creates a new schedule of length 1 longer

def total_scheduled_units(schedule): # time: O(len(schedule)), space: O(1)
    result = 0
    for course in schedule:
        result += get_module_total_units(get_module_units(course))
    return result

def drop_class(schedule, course): # time: O(n^2), space: O(n^2) worst case look through all n + n-1 + n-2 + ...
##    if schedule == ():
##        return ()
##    elif schedule[0] == course:
##        return schedule[1:]
##    else:
##        return (schedule[0], ) + drop_class(schedule[1:], course)


    
    for i in range(len(schedule)):
        if schedule[i] == course:
            return schedule[:i] + schedule[i+1:]
    return schedule

def credit_limit(schedule, max_credits): # worst case when max_credits = 0 
    if total_schedule_units(schedule) <= max_credits: # O(n) for total_scheduled_units
        return schedule
    else:
        return credit_limit(schedule[1:], max_credits) # O(n^2) both space and time


    
def homework(schedule, max_credits): #remove largest value
    pass














    
                                   
        
    


















        

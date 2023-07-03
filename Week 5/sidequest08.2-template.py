#
# CS1010X --- Programming Methodology
#
# Sidequest 08.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

possible_birthdays = (('May', '15'),
                      ('May', '16'),
                      ('May', '19'),
                      ('June', '17'),
                      ('June', '18'),
                      ('July', '14'),
                      ('July', '16'),
                      ('August', '14'),
                      ('August', '15'),
                      ('August', '17'))

# Albert and Bernard just became friends with Cheryl,
# and they want to know when her birthday is.
# Cheryl gave Albert and Bernard a tuple of 10 possible dates.

#############
# Task 1(a) #
#############

def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    return count == 1

print("\n## Task 1a ##")
print(unique_day("16", possible_birthdays)) # False
print(unique_day("17", possible_birthdays)) # False
print(unique_day("18", possible_birthdays)) # True
print(unique_day("19", possible_birthdays)) # True

#############
# Task 1(b) #
#############

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            count += 1
    return count == 1

print("\n## Task 1b ##")
print(unique_month('May', possible_birthdays)) # False
print(unique_month('June', possible_birthdays)) # False
print(unique_month('March', (('August', '1'), ('March', '2'), ('March', '3')))) # False
print(unique_month('August', (('August', '1'), ('March', '2'), ('March', '3')))) # True

#############
# Task 1(c) #
#############

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0] == month:
            if unique_day(birthday[1], possible_birthdays):
                return True
    return False       

print("\n## Task 1c ##")
print(contains_unique_day("May", possible_birthdays)) # True
print(contains_unique_day("June", possible_birthdays)) # True
print(contains_unique_day("July", possible_birthdays)) # False

#############
# Task 2(a) #
#############

# Albert (given month):
# I don't know Cheryl's birthday, but I know that Bernard does not know too.

def statement1(birthday, possible_birthdays):
    return not unique_month(birthday[0], possible_birthdays) and not contains_unique_day(birthday[0], possible_birthdays)

print("\n## Task 2a ##")
print(statement1(('May', '19'), possible_birthdays)) # False
print(statement1(('August', '14'), possible_birthdays)) # True

#############
# Task 2(b) #
#############

# Bernard (given day):
# At first I don't know when Cheryl's birthday is, but I know now.

def statement2(birthday, possible_birthdays):
    return unique_day(birthday[1], possible_birthdays)

print("\n## Task 2b ##")
print(statement2(('May', '19'), possible_birthdays)) # True
print(statement2(('August', '14'), possible_birthdays)) # False
print(statement2(('August', '17'), possible_birthdays)) # False
print(statement2(('July', '16'), possible_birthdays)) # False

#############
# Task 2(c) #
#############

# Albert (given month):
# Then I also know when Cheryl's birthday is.

def statement3(birthday, possible_birthdays):
    return unique_month(birthday[0], possible_birthdays)

print("\n## Task 2c ##")
print(statement3(('May', '19'), possible_birthdays)) # False
print(statement3(('August', '14'), (('August', '14'),))) # True

##########
# Task 3 #
##########

# Based on statement 1, we can filter out some birthdays.
# From statement 2, we can filter out some more birthdays.
# Finally, using statement 3, we can filter out the remaining wrong birthdays

def get_birthday(possible_birthdays):
##    c = filter(lambda x: statement2(x,
##                                    filter(lambda x: statement1(x, possible_birthdays), possible_birthdays)), possible_birthdays)
##    return tuple(c)

    c = filter(lambda x: statement1(x, possible_birthdays), possible_birthdays)
    return tuple(c)

    
##    c = filter(lambda x: statement3(x,
##                                    filter(lambda x: statement2(x,
##                                                                filter(lambda x: statement1(x, possible_birthdays),possible_birthdays)),
##                                           filter(lambda x: statement1(x, possible_birthdays), possible_birthdays))),
##               filter(lambda x: statement2(x,filter(lambda x: statement1(x, possible_birthdays),possible_birthdays)), filter(lambda x: statement1(x, possible_birthdays), possible_birthdays)))
##    return tuple(c)
##    remaining1 = ()
##    remaining2 = ()
##    last_day = ()
##    for day in possible_birthdays:
##        if statement1(day, possible_birthdays):
##            remaining1 += (day, )
##    for day in remaining1:
##        if statement2(day, remaining1):
##            remaining2 += (day, )
##    for day in remaining2:
##        if statement3(day, remaining2):
##            last_day += (day, )
##    print(remaining1)
##    print(remaining2)
##    return last_day

print("\n## Task 3 ##")
print(get_birthday(possible_birthdays)) # (('July', '16'),)

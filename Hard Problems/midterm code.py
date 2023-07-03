
print("Question 1A")
x = 0
y = 1
def f(y):
    if y > x:
        print("y > x")
    elif x >= y:
        print("x >= y")
    y = y + 1
    return (lambda y: "not ok" if y==False else "ok")
y = f(x)
print(y(None))

print("\n")
print("Question 1B")
def foo(y):
    def goo(z):
        if z <= 1:
            return "ok"
        else:
            z = z // 3
            print(z)
            print(goo(z))
            return goo(z//2)
    return goo(y)
print(foo(9))


print("\n")
print("Question 1C")
def mylove(t):
    length = len(t)
    i = 1
    while i < length:
        s = t
        t = t[0:i]
        for j in range(0, length - i):
            t = t + (s[j] + s[j+i],)
        i *= 2
    return t
print(mylove((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

def prefix(lst):
    for i in range(1, len(lst)):
        lst[i] = lst[i] + lst[i - 1]
    return lst

print(prefix([1,2,3,4,5,6,7,8,9,10]))

print("\n")
print("Question 1D")
def blur(x):
    return lambda x: x**2
def king(x):
    return lambda x: x+2
print( blur(king(king(king)))(4) )
print( king(blur(blur(blur)))(4) )
print( blur(king(blur(king)))(4) )
print( king(blur(king(blur)))(4) )

print("\n")
print("Question 2A")

from math import *

def isPower_of_2(n):
    return (log(n,2) - int(log(n, 2))) == 0

def fun(n):
    if n==0:
        return 0
    elif isPower_of_2(n):
        return n + fun(n//2)
    else:
        return n + fun(n-1)


print(fun(8))

#time: O(n)
#space: O(n)
#The function fun(n) recursively calls fun(n-1) until a power of 2 if hit
#In the worst case, n = 2^x + 2^x - 1 such that fun(n-1) is called (2^x - 1) times until n = 2^x
#After that, fun(n//2) is called until n == 0, which is O(x) times
#If n = 2^x + 2^x - 1, (2^x - 1) is approximately n/2 and x is O(logn)
#At each level of recursion, work done is constant O(1) as we are only adding n (accumualting a value)
#and the isPower_of_2 check is also O(1) in time and space
#worst case time complexity of fun = O(n/2) + O(logn) = O(n)
#space complexity is the maximum depth of the recursion tree = O(n/2) + O(logn) = O(n)

print("\n")
print("Question 2B")

def fun_iter(n):
    result = 0
    while n > 0:
        if isPower_of_2(n):
            result += n
            n = n//2
        else:
            result += n
            n = n - 1
    return result

print(fun_iter(8))

print("\n")
print("Question 2C")

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


def fun2(n):
    result = 0
    for i in range(n):
        for j in range(1, n):
            if (j > i):
                result += fact(j)
    return result


print(fun2(8))

#time and space complexity of fact(n) is O(n)
#for j from 1 to n - 1, fact(j) is called j times
#when j == 1, fact(1) is called once, when i == 0
#when j == 2, fact(2) is called twice, when i == 0 and i == 1
#until j == n - 1, fact(n - 1) is called n-1 times, when i == 0 to i == n - 2
#time complexity is 1^2 + 2^2 + .... (n-1)^2 = (n-1)*(n)*(2n - 1)/6 = O(n^3)


print("\n")
print("Question 3A")

def new_sum( t, term, next ):
    if len(t) < 1:
        return 0
    else:
        return term(t) + new_sum( next(t), term, next )


def even_sum( t ):
    return new_sum( t, lambda x: x[0], lambda x: x[2:] )


print(even_sum( (1,2,3,4,5,6) ))

print("\n")
print("Question 3B")

def folded_sum_square(t):
    return new_sum( t, lambda x: (x[0] + x[-1])**2, lambda x: x[1:-1] )


print(folded_sum_square( (1,2,3,4,5,6) ))

print("\n")
print("Question 3C")

def alternate_sum_12(t):
    return new_sum( t, lambda x: (x[0] + 2*x[1]) if len(x) >= 2 else x[0], lambda x: x[2:] )

print(alternate_sum_12( (1,2,3,4,5,6) ))

print("\n")
print("Question 4")


def make_empty_db():
    return ()

def add_person(db, name, workplace, home, caseType):
    person = (name, workplace, home, caseType)
    db += (person,)
    return db

def remove_person(db, name):
    for i in range(len(db)):
        if db[i][0] == name:
            db = db[:i] + db[i + 1:]
            return db
    return db
    
def same_home_or_office_as(db, name):
    result = ()
    for p in db:
        if p[0] == name:
            home = p[2]
            office = p[1]
    for person in db:
        if person[0] != name:
            if person[1] == home or person[1] == office or person[2] == home or person[2] == office:
                result += (person[0], )
    return result

def add_visited_places(db, name, places):
    for i in range(len(db)):
        if db[i][0] == name:
            db = db[:i] + (db[i] + places,) + db[i + 1:]
            return db
    return db

def same_visited_places_as(db, name):
    result = ()
    for p in db:
        if p[0] == name:
            places = p[4:]
    for person in db:
        if person[0] != name:
            for place in person[4:]:
                if place in places:
                    result += (person[0], )
    return result

def set_case_to_quarantined(db, name):
    for i in range(len(db)):
        if db[i][0] == name:
            if db[i][3] == "c":
                print("Already confirmed before:", name, "-- no quarantined needed")
                return db
            elif db[i][3] == "q":
                print("Already quarantined before:", name)
                return db
            else:
                print("Done quarantine:", name)

                db = db[:i] + (db[i][:3] + ("q",) + db[i][4:],) + db[i + 1:]
                return db
    return db

def set_case_to_confirm(db, name):
    for i in range(len(db)):
        if db[i][0] == name:
            db = db[:i] + (db[i][:3] + ("c",) + db[i][4:],) + db[i + 1:]
            print("Done confirm:", name)

            people_to_quarantine = same_home_or_office_as(db, name) + same_visited_places_as(db, name)
            for p in people_to_quarantine:
                db = set_case_to_quarantined(db, p)
            return db
    return db
            
            
    
                
    
    

db = make_empty_db()
db = add_person( db, "Alice", "H01", "W01", "n")
db = add_person( db, "Ben", "H01", "W02", "n")
db = add_person( db, "Cathy", "H03", "W01", "n")
db = add_person( db, "Dennis", "H04", "H03", "n")
print( same_home_or_office_as( db, "Alice" ) )
print( same_home_or_office_as( db, "Dennis" ) )
db = remove_person( db, "Cathy" )
print( same_home_or_office_as( db, "Alice") )
print( same_home_or_office_as(db, "Dennis") )
db = add_visited_places( db, "Dennis", ("VivoCity", "SAFRA", "Jurong East") )
db = add_visited_places( db, "Ben", ("SAFRA", "NUS") )
print( same_visited_places_as(db, "Dennis") )
db = add_person(db, "John", "H04", "W01", "n" )
print( same_home_or_office_as(db, "John") )

print( same_visited_places_as(db, "John") )
db = set_case_to_quarantined( db, "John" )
print( same_home_or_office_as(db, "Dennis") )
print( same_visited_places_as(db, "Dennis") )

db = set_case_to_confirm( db, "Dennis")




















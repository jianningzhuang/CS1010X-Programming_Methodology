##def square(x):
##    print(x*x)
##
##print(square(3))
##b = square(3)
##print(b)
##print(type(b))
##print(type(square(3)))

from runes import *

#####PRIMITIVES#####
##clear_all() # clears screen
##show(pic) # opens new window with pic
##quarter_turn_right(pic) # rotates pic 90 degrees
##stack(pic1, pic2) # pic1 stacked on top of pic2 with each getting half of screen, picture will look squashed
##stack_frac(frac, pic1, pic2) #odd number division of screen

#####COMBINATIONS#####
def turn_upside_down(pic):
    return quarter_turn_right(quarter_turn_right(pic)) #2 right 90 rotations turns picture upside down

def quarter_turn_left(pic):
    return quarter_turn_right(quarter_turn_right(quarter_turn_right(pic))) # rotate 270 degrees right to get rotate 90 degree left

#####ABSTRACTIONS#####
def beside(pic1, pic2):
    return quarter_turn_right(stack(quarter_turn_left(pic2), quarter_turn_left(pic1))) #pic 1 on left, pic 2 on right

def make_cross(pic):
    return stack(beside(quarter_turn_right(pic), turn_upside_down(pic)), beside(pic, quarter_turn_left(pic))) # making a pattern by reflecting original picture

def repeat_pattern(n, pat, pic): #pat is a function
    if n ==0:
        return pic
    else:
        return pat(repeat_pattern(n-1, pat, pic)) #recursion

def stackn(n, pic):  # stack n pics with equal size on each other
    if n ==1:
        return pic
    else:
        return stack_frac(1/n, pic, stackn(n-1, pic)) #top pic takes up 1/n space, recursion

def nxn(n, pic):
    return stackn(n, quarter_turn_right(stackn(n, quarter_turn_left(pic)))) #quarter turn left inside to counteract quarter turn right outside

#####TESTING#####
##show(rcross_bb)
##show(quarter_turn_right(rcross_bb))
##show(stack(rcross_bb, nova_bb))
##show(stack(sail_bb, stack(rcross_bb, nova_bb)))
##show(turn_upside_down(sail_bb))
##show(quarter_turn_left(sail_bb))
##show(beside(sail_bb, sail_bb))
##show(make_cross(sail_bb))
##show(repeat_pattern(4, make_cross, rcross_bb))
##show(repeat_pattern(3, lambda pic: beside(pic, pic), sail_bb))
##show(stack_frac(1/3, sail_bb, stack(sail_bb, sail_bb)))
##show(stackn(7, sail_bb))
##show(nxn(3, make_cross(rcross_bb)))
##show(nxn(3, sail_bb))


##def foo():
##    return 10
##
##bar = foo() + foo()
##
##print(bar)

### A
##def foo(a, b):
##    return a + a # a function need not use every parameter passed into it
##
### B
##def foo():
##    return   # a function without any parameters or return value is still valid
##
##### C
####def foo:
####    return b #WRONG no parantheses
####
### D
####define foo(a):
####    return a  #WRONG def not define
##
### E
##def foo(a, b, c):
##    a + b + c  # a function does not necessarily need a return
##
### F
##def foo(a) # WRONG indentation
##return a

##def triple(amt):
##    return 3 * amt
##
##print(triple(2))

##def square(x):
##    return x * x
##
##def mean(x, y):
##    return (x + y) / 2
##
##def variance(x, y):
##    return mean(square(x), square(y)) - square(mean(x, y))
##    pass
##print(variance(1,5))
##print(variance(2,4))
##print(variance(3,3))
##print(variance(5,1))


##x = 2
##def square(x):
##    x = 3
##    return x * x
##
##print(square(x), x, square(5))

##def greet(name, language):
##    greeting = ''
##    if language == 'English':
##        greeting += 'Nice to meet you ' + name
##    elif language == 'Klingon':
##        greeting += 'nuqneH ' + name
##    if language == 'Elvish':
##        greeting += 'Gi suilon ' + name
##    return greeting
##print(greet('Okrand', 'Klingon'))

##def is_odd(x):
##    return x%2 == 1
##    pass # remove this line
##    
##def is_negative(x):
##    if x < 0:
##        return True
##    elif x > 0:
##        return False
##    pass # remove this line
##    
##def is_even_and_positive(x):
##    return x%2 == 0 and x > 0
##
##print(is_odd(1))
##print(is_negative(1))
##print(is_even_and_positive(0))

##
##def divisible(value, divider):
##    if value % divider == 0:
##        return True
##    else:
##        return False
##
def test_leap_year(year):
    if year%400 == 0:
        return True
    elif year%4 == 0 and year%100 != 0:
        return True
    else:
        return False
print(test_leap_year(1700))

#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi
##
############
### Task 1 #
############
##

def tree5(n, rune):
    output = rune
    for i in range((n - 1), 0, -1):
        print(i)
        output = overlay_frac(1/(n -1), scale(i/n, rune), output)
    return output

def tree4(n, pic):
    result = pic
    for i in range(2, n+1):
        result = overlay_frac(1/i, scale((n+1-i)/n, pic), result)
    return result

def tree(n, rune):
    if n == 1:
        return rune
    else:
        return overlay_frac((n-1)/n,
            scale((n-1)/n, tree(n-1, rune)),
            rune)

def tree1(n,rune):
    
    fix = n
        
    def myfunc(n,rune):
        if n ==1:
            return scale(1/fix,rune)
        else:
            print(n/fix)
            return overlay_frac(1-1/n,myfunc(n-1,rune),scale(n/fix,rune))
        
    return myfunc(n,rune)

##def scaled_pic(n, denominator, pic):
##    return scale((denominator+1-n)/denominator, pic)
##
##def tree(n, pic):
##    denominator = n
##    if n == 1:
##        return pic
##    else:
##        return overlay_frac(1/n, scaled_pic(n, denominator, pic), tree((n-1), pic))
    

# Test
show(tree(6, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(pic, n):
    L = (1/2 - 1/n)
    result = translate(L*cos(pi/2) ,L*sin(pi/2), scale(2/n, pic))
    for i in range(1, n+1):
        result = overlay_frac(1/i, translate(L*cos(pi/2 + (2*pi*i)/n), L*sin(pi/2 + (2*pi*i)/n), scale(2/n, pic)), result)
    return result

from math import sin, cos, pi
def helix1(rune,n):
    length = (1/2 - 1/n)
    layers = n
    scaled_ruin = scale(2/n,rune)
    angle = (math.pi*2)/n
    pi = math.pi
    def myfunc1(rune,n):
        if n == 1:
            return translate(0,length,scaled_ruin)
        else:
            
            xy_angle =(pi)/2 - ((n-1)*angle)
            x = length*math.cos(xy_angle)
            y = length*math.sin(xy_angle)
   
            return overlay_frac(1-1/n,myfunc1(rune,n-1),translate(x,y,scaled_ruin))                        
    return myfunc1(rune,n)

from math import sin, cos, pi
def helix2(rune,n):
    length = (1/2 - 1/n)
    layers = n
    scaled_ruin = scale(2/n,rune)
    angle = (math.pi*2)/n
    pi = math.pi
    def myfunc1(rune,n):
        if n == 1:
            return translate(0,length,scaled_ruin)
        else:
            print(n)
            xy_angle =(pi)/2 - ((n-1)*angle)
            x = length*math.cos(xy_angle)
            y = length*math.sin(xy_angle)
   
            return overlay_frac(1-1/n,myfunc1(rune, n-1),translate(x,y,scaled_ruin))                        
    return myfunc1(rune,n)  
        

# Test
#show(helix2(make_cross(rcross_bb), 9))

#show(translate(0.25*cos(pi/2 - pi/2), 0.25*sin(pi/2 - pi/2), scale(0.1, circle_bb)))

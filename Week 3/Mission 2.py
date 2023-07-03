#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1: #terminating case
        return pic
    else: #recursive call
        return beside(pic, stack(fractal(pic, n-1), fractal(pic, n-1)))

def fractal1(pic, n):
   if n == 1:
       return pic
   else:
       return beside(pic, fractal(stack(pic, pic), n-1))

# Test
# show(fractal(make_cross(rcross_bb), 3))
#show(fractal1(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    result = pic
    while n > 1: #iterative loop
        result = beside(pic, stack(result, result))
        n -= 1
    return result

def fractal_iter1(pic,n):
    if n>0 and type(n)==int:
        pattern=pic
    while n>0:
        pattern=beside(pic,stack(pattern,pattern))
        pattern_final=beside(pic,stack(pattern,pattern))
        n=n-1
    return pattern_final

# Test
#show(fractal_iter(make_cross(rcross_bb), 1))
#show(fractal_iter1(make_cross(rcross_bb), 3))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    else:
        return beside(pic1, stack(dual_fractal(pic2, pic1, n-1), dual_fractal(pic2, pic1, n-1)))

def dual_fractal1(params_1,params_2,n):
##    if n==2:
##        return beside(params_1,(stack(params_2, params_2)))
    if n>1 :
        return beside(params_1,
                      beside(
                          (stack(params_2, params_2)),dual_fractal(
                              stack(stack(params_1, params_1),(stack(params_1, params_1))),
                              stack(params_2, params_2),
                              n-2)))
    elif n%2 ==1:
        return params_1
    elif n%2 ==2:
        return params_2       
    

# Test
##show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal1(make_cross(rcross_bb), make_cross(nova_bb), 7))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    if n%2 == 0:
        result = pic2
    else:
        result = pic1
    while n > 1:
        if n%2 == 0:
            result = beside(pic1, stack(result, result))
        if n%2 == 1:
            result = beside(pic2, stack(result, result))
        n -= 1
    return result
    
def dual_fractal(rune1, rune2, n):
    a = 2**(n-1)
    def stack_prod(n):
        
        if n%2 == 0:
            return stackn(a, rune2)
        else:
            return stackn(a, rune1)
    result = stack_prod(n)
    if n == 1:
        return rune1
    while n > 1:
        left = stack_prod(n-1)
        result = beside(left, result)
        n -= 1
    return result

def dual_fractal_iter1(pic1, pic2, n):


    if n % 2 == 1:


        pic1, pic2 = pic2, pic1


    result = pic2


    for i in range(1, n):


        result = beside(pic1, stack(result, result))


        pic1, pic2 = pic2, pic1 


    return result

	    

#show(dual_fractal_iter1(make_cross(rcross_bb) , make_cross(nova_bb), 9))
# Test
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 1))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def mosaic(pic1, pic2, pic3, pic4): # from mission 1
    return stack(beside(pic4, pic1), beside(pic3, pic2))

def steps(pic1, pic2, pic3, pic4):
    return overlay_frac(
        1/4, mosaic(blank_bb, blank_bb, blank_bb, pic4),
        overlay_frac(
            1/3, mosaic(blank_bb, blank_bb, pic3, blank_bb),
            overlay(mosaic(blank_bb, pic2, blank_bb, blank_bb),mosaic(pic1, blank_bb, blank_bb, blank_bb))))

def steps1(params_1, params_2, params_3, params_4):
    def mosaic(a, b, c, d):
        return (beside(stack(d,c),stack(a,b)))
    def layer1(params_1):
        return mosaic(params_1, blank_bb, blank_bb, blank_bb)
    def layer2(params_2):
        return mosaic(blank_bb, params_2, blank_bb, blank_bb)
    def layer3(params_3):
        return mosaic(blank_bb, blank_bb, params_3, blank_bb)
    def layer4(params_4):
        return mosaic(blank_bb, blank_bb, blank_bb, params_4)
    return (overlay(overlay(layer4(params_4), layer3(params_3)), overlay(layer2(params_2), layer1(params_1))))
# Test
show(steps1(rcross_bb, sail_bb, corner_bb, nova_bb))

#stereogram(circle_bb)


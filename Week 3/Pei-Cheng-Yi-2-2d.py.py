#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.
"""
Rune-title: Lucky star!

Description:
This is an  attempt to get a higher score for the contest by using
more functions from runes.py. Hopefully it brings you good luck ;)
"""
#TODO
#size of heart_clover --> scale(2/n, pat)
def heart_clover(n, petal_size): #n is an integer that we will use to scale heart_clover
    """
Creates a four leaf heart clover
    """
    heart = scale(petal_size, heart_bb) #Can be adjusted accordingly for aesthetics
    top_left = rotate(math.pi / 4, heart)
    top_right = rotate(7*math.pi / 4, heart)#Somehow flip_horiz() does not work for heart
    bottom_left = flip_vert(top_right)#Switch the left and right to counter the mirror effect
    bottom_right = flip_vert(top_left)
    result = stack(beside(top_left, top_right), beside(bottom_left, bottom_right))
    return scale(2/n, result)

golden_ratio = (1 + 5**0.5) / 2

def star(pat,n, position): #Position ranges from -1 to n
    """
Creates a star at the appropriate position. 
    """
    #Initialised to be 1/4 of heart_clover
    pat = scale(1/(2*n), pat)
    #Angle invovled in each translation = 2pie / 20
    angle = (2 * math.pi) / (20)
    radius = 96 / (16*n)
    #Initial position is to the left of (0, radius)
    x_coord = radius * math.cos(0.5 * math.pi + angle * (position + 1)) * golden_ratio
    y_coord = radius * math.sin(0.5 * math.pi + angle * (position + 1)) * golden_ratio
    new_star = translate(x_coord, y_coord, pat)
    return new_star

def star_circle(pat, n):
    """
We are not allowed to use overlay. But I want to overlay. So here is an improvisation.
    """
    for i in range(-1, n):
        show(star(pat, n, i))

def lucky_star(n):
    """
As the titular function, this will combine multiple star_circle and a heart_clover
    """
    star_circle(pentagram_bb, 20)
    star_circle(heart_bb, 25)
    star_circle(pentagram_bb, 30)
    star_circle(black_bb, 35)
    star_circle(pentagram_bb, 40)
    star_circle(circle_bb, 50)
    return heart_clover(n, 4/3)
    
show(lucky_star(15))




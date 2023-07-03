#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

def border_figure(rune):
    figure = flip_vert(stacker(stacker(rune,3),3))
    return figure    
def stacker(rune,num):
    base = stack_frac(1/3 , scale(0.5,rune) , stack(rune,scale(0.5,rune)))
    return quarter_turn_right(base)

def center():
    return make_cross(make_cross(make_cross(make_cross(ribbon_bb)))) #When zoom out it looks like some sort of noise

def egyptian(pic,reps,middle):
    leftpic = quarter_turn_left(middle)
    
    #Make top and bottom border twice and flip the inside one to the right
    return add_Top_Bottom_Border(pic,reps,reps,quarter_turn_right(add_Top_Bottom_Border(quarter_turn_left(pic),reps - 2,reps,leftpic)))

def add_Top_Bottom_Border(border,picCount,screenCount,middle):
    #picCount : Number of Pictures to print in this border
    #screenCount : Number of Pictures on the screen
    return stack_frac(1 / screenCount ,
    # Top Row
                      besiden(border,picCount),
    # Middle Row,
                  stack_frac((screenCount - 2) / (screenCount - 1),
                   middle
     # Bottom Row
                        ,besiden(border, picCount)))


def besiden(pic,reps):
    #Before turning the pic right, correct orientation
    return quarter_turn_right(stackn(reps,quarter_turn_left(pic)))

##show(border(heart_bb))

def makeBorder(x):
    return egyptian(border_figure(circle_bb),x,egyptian(border_figure(rcross_bb),x,egyptian(border_figure(black_bb),x,center())))


show(makeBorder(6))


#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    def kochizerize(curve):
        scaled_curve = scale(1/3)(curve)
        koch2 = translate(1/3, 0)(rotate(pi/3)(scaled_curve))
        koch3 = translate(1/2, (3**(1/2))/6)(rotate(-pi/3)(scaled_curve))
        koch4 = translate(2/3, 0)(scaled_curve)
        return connect_rigidly(connect_rigidly(scaled_curve, koch2), connect_rigidly(koch3, koch4))
    return repeated(kochizerize, level)(unit_line)

def kochize1(level):
    if level == 0:
        return unit_line
    else:
        first = connect_ends(kochize(level-1),rotate(pi/3)(kochize(level-1)))
        second = connect_ends(rotate(-pi/3)(kochize(level-1)),kochize(level-1))
        return connect_ends(first,second)

        

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize1(level))

##show_connected_koch(1, 4000)
#show_connected_koch(5, 4000)

##########
# Task 2 #
##########


def snowflake():
    snowflake1 = translate(0, 2/3)(kochize(5))
    snowflake2 = translate(1, 2/3)(rotate(-2*pi/3)(kochize(5)))
    snowflake3 = translate(1/2, 2/3 -(3**(1/2))/2)(rotate(2*pi/3)(kochize(5)))
    return connect_rigidly(snowflake1, connect_rigidly(snowflake2, snowflake3))

def snowflake1():
    snowflake_portion = kochize(5)
    return connect_ends(rotate(2*pi/3)(kochize(5)),connect_ends(kochize(5),rotate(-2*pi/3)(kochize(4))))

import math
def new_connect_rigidly(curve1, curve2,curve3):
    def connected_curve(t):
        if (t <= (1 / 3)):
            return curve1(3*t)
        elif t <= (2/3) :
            return curve2(3  * (t - (1 / 3) ))
        else:
            return curve3(3 * (t - (2 / 3) ))
    return connected_curve

def new_connect_ends(curve1, curve2,curve3):
    curve2_start = curve2(0)
    curve1_end = curve1(1)

    x_delta = x_of(curve1_end) - x_of(curve2_start)
    y_delta = y_of(curve1_end) - y_of(curve2_start)

    new_curve2 = translate(x_delta, y_delta)(curve2)
    
    curve3_start = curve3(0)
    curve2_end = new_curve2(1)
    
    x = x_of(curve2_end) - x_of(curve3_start)
    y = y_of(curve2_end) - y_of(curve3_start)

    new_curve3 = translate(x, y)(curve3)
    
    return new_connect_rigidly(curve1, new_curve2 ,new_curve3 )


def hexagon(curve):
    start = curve
    sides = 6
    start = new_connect_ends(curve ,rotate( 2 * math.pi / sides)(curve), rotate( 2 * 2 * math.pi / sides)(curve))
    return connect_ends(start,rotate(3 * 2 * math.pi / sides)(start))
    
def snowflake2():
    return rotate_90(hexagon(kochize(5)))
draw_connected_scaled(100, snowflake2())

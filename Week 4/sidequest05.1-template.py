#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

##draw_points(200, unit_circle)
#draw_points_scaled(200, alternative_unit_circle)

##The points for unit_circle are spaced uniformly apart while the points for alternative_unit_circle are cluttered at the start of the curve but get increasingly spaced apart as t increases.
##
##(2*pi*t) and (2*pi*t*t) represent the angular frequency of a sinusoidal/oscillating function, which measures the angular displacement per unit time.
##
##As t increases uniformly in the unit interval [0,1] (e.g value of 200 in draw_connected calls values of t = 0, .005, 0.010, 0.015.....), angular displacement of (2*pi*t) is constant per unit time, hence the points are spaced out evenly as well.
##
##However for (2*pi*t*t), angular displacement per unit time grows quadratically as t increases, hence points are very close at the start when t is very small but get spaced further and further away as t increases.


##########
# Task 2 #
##########

# (a)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))
    return reflected_curve

def spiral(t):
    return make_point((t)*sin(2*pi*t), (t)*cos(2*pi*t))

def reflected_spiral(t):
    return make_point((-t)*sin(2*pi*-t), (-t)*cos(2*pi*-t))

draw_connected_scaled(1000, reflected_spiral)

# (b)
def heart(t):
    return connect_rigidly(spiral, reflect_through_y_axis(spiral))(t)
##    if t < 0.5:
##        return spiral(2*t)
##    else:
##        return reflected_spiral(2*t -1)
    

#draw_connected_scaled(1000, heart)

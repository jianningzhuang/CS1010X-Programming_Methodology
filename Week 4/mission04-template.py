#
# CS1010X --- Programming Methodology
#
# Mission 4
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

##def unit_line_at_y(y):
##    return lambda t: make_point(t,y)
##
##a_line = unit_line_at_y(0)
##
draw_connected_scaled(200, a_line)



# (a)
# unit_line_at_y : (Number) -> Curve

# (b)
# a_line : (Unit-Interval) -> Point

# (c)
def vertical_line(point, length):
    return lambda t: make_point(x_of(point), y_of(point) + t*length)

#draw_connected(200, squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(vertical_line(make_point(0.1, 0.1), 0.4)))

# (d)
# vertical_line : (Point, Number) -> Curve

# (e)
#draw_connected(200, vertical_line(make_point(0.5, 0.25), 0.5))

##########
# Task 2 #
##########

# (a)
# we can also apply the function reflect_through_y_axis twice and see if it produces the original image

# (b)
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point(-x_of(pt), y_of(pt))

    return reflected_curve
	
#draw_connected_scaled(200, arc)
#draw_connected_scaled(200, (reflect_through_y_axis(arc)))

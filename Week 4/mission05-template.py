#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_rigidly(curve1, curve2):
    def connected_curve(t):
        if (t < 0.5):
            return curve1(2*t)
        else:
            return curve2(2*t - 1)
    return connected_curve

#draw_connected(200, arc)

#draw_connected(200, unit_line)
                      
#draw_connected(200, translate(0.5, 0.5)(unit_line))


def connect_ends(curve1, curve2):
    def continuous_curve(t):
        if (t < 0.5):
            return connect_rigidly(curve1, curve2)(t)
        else:
            return (translate(x_of(curve1(1)) - x_of(curve2(0)), y_of(curve1(1)) - y_of(curve2(0)))(connect_rigidly(curve1, curve2)))(t)
    return continuous_curve

#draw_connected_scaled(200, connect_ends(arc, unit_line))
#draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))
##########
# Task 2 #
##########

#show_connected_gosper(5)

def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(repeated(gosperize, level)(initial_curve))
    draw_points(num_points, squeezed_curve)
    
#show_points_gosper(7, 1000, arc)
#show_points_gosper(5, 500, arc)
##########
# Task 3 #
##########

##def your_gosper_curve_with_angle(level, angle_at_level):
##    if level == 0:
##        return unit_line
##    else:
##        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))
##
##def your_gosperize_with_angle(theta):
##    def inner_gosperize(curve_fn):
##        return put_in_standard_position(connect_ends(joe_rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
##    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))
def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
#draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))

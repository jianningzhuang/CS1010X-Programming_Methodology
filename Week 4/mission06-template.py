#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def gosperize(curve):
    scaled_curve = scale(sqrt(2)/2)(curve)
    left_curve = joe_rotate(pi/4)(scaled_curve)
    right_curve = translate(0.5,0.5)(joe_rotate(-pi/4)(scaled_curve))

    return connect_rigidly(left_curve, right_curve)

def gosper_curve(level):
    return repeated(gosperize, level)(unit_line)

def show_connected_gosper(level):
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(gosper_curve(level))
    draw_connected(200, squeezed_curve)

def gosperize_with_angle(theta):
    def inner_gosperize(curve):
        scale_factor = (1 / cos(theta)) / 2
        scaled_curve = scale(scale_factor)(curve)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5,sin(theta)*scale_factor)(rotate(-theta)(scaled_curve))
        return connect_rigidly(left_curve, right_curve)
    return inner_gosperize

def gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        angle = angle_at_level(level)
        return gosperize_with_angle(angle)(gosper_curve_with_angle(level-1, angle_at_level))

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))
def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize


# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# print(profile_fn(lambda: gosper_curve(1000)(0.1), 500))

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve(25)(0.5), 1000))

# Time measurements
#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

#  1) 117.22710000000004
#  2) 106.52810000000001
#  3) 139.79539999999997
#  4) 114.89259999999996
#  5) 105.56669999999995

#  average = 116.80197999999999

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve_with_angle(25, lambda lvl: pi/4)(0.5), 1000))

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

#  1) 124.5518000000001
#  2) 122.80460000000004
#  3) 124.83440000000002
#  4) 148.97969999999992
#  5) 121.58340000000001

#  average = 128.55078


#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: your_gosper_curve_with_angle(25, lambda lvl: pi/4)(0.5), 100))

#  <...your time measurements here...>
#  <...do for at least 5 times and take the average...>

#  1) 23587.187
#  2) 23359.7974
#  3) 23294.9487
#  4) 23048.0633
#  5) 23278.9262

#  average = 23313.78452


# Conclusion:
# In general, functions that are more customized (such as gosper_curve) have a faster runtime
# than functions that are more customizable (like gosper_curve_with_angle and your_gosper_curve_with_angle)
# for gosper_curve and gosper_curve_with_angle, when the level is doubled, runtime is also doubled, hence runtime is linear wrt to level
# for your_gosper_curve_with_angle, when the level is doubled, runtime quadrupled, hence runtime is quadratic wrt to level
# between gosper_curve and gosper_curve_with_angle, runtime for gosper_curve_with_angle is consistently higher by a constant factor

##########
# Task 2 #
##########


#  1) joe_rotate works and achieves the same purpose as rotate


#  2) in rotate, curve(t) is only evaluated once each time rotate is invoked
#     however for joe_rotate, at each level, the curve function of all pervious levels are evaluated again
#     in the definition of gosper_curve, at each level, rotate is invoked twice by gosperize to form the left and right curves
#     if the original rotate was used, at each level, rotate is only called 2 more times, hence is linear wrt to level
#     if joe_rotate was used, at each level, all the curve functions from previous levels are evaluated twice, and their summation is exponential wrt to level
#     2 + 4 + 8 + .....2^level = (2^(level+1)-1)/(2-1) - 1
#                          = O(2^level)


# from the results in Task 3
# rotate:
# T(n) = 2n + 1
#
# joe_rotate:
# T(n) = 2 + 2T(n-1)           T(1) = 4
# T(n) = 2 + 4 + 4T(n-2)
# .....
# T(n) = 2 + 4 + 8 + .....2^(n-2) + 2^(n-2)T(n-(n-2))
# T(n) = 2 + 4 + 8 + .....2^(n-2) + 2^(n-1) + 2^(n-1)T(1)
# T(n) = (2^n - 1)/(2-1) - 1 + 2^(n-1) * 4
# T(n) = 3*2^n - 2
##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>            <4>
#                      2         <5>            <10>
#                      3         <7>            <22>
#                      4         <9>            <46>
#                      5         <11>           <94>
#
#  Evidence of exponential growth in joe_rotate.
#
# rotate:
# T(n) = 2n + 1
#
# joe_rotate:
# T(n) = 2 + 2T(n-1)           T(1) = 4
# T(n) = 2 + 4 + 4T(n-2)
# .....
# T(n) = 2 + 4 + 8 + .....2^(n-2) + 2^(n-2)T(n-(n-2))
# T(n) = 2 + 4 + 8 + .....2^(n-2) + 2^(n-1) + 2^(n-1)T(1)
# T(n) = (2^n - 1)/(2-1) - 1 + 2^(n-1) * 4
# T(n) = 3*2^n - 2


    



trace(x_of)
gosper_curve(2)(0.5)
print('------')











    




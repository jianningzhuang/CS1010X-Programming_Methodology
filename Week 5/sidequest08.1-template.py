#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    return (velocity*cos(angle*pi/180), velocity*sin(angle*pi/180))

#print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    def distance(x1, x2, y1, y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    a_x, a_y = 0, 0
    for planet in planets:
        a_x += (G*get_mass(planet)*(get_x_coordinate(planet) - current_x))\
               /(distance(current_x, get_x_coordinate(planet), current_y, get_y_coordinate(planet))**3)
        a_y += (G*get_mass(planet)*(get_y_coordinate(planet) - current_y))\
               /(distance(current_x, get_x_coordinate(planet), current_y, get_y_coordinate(planet))**3)
    return (a_x, a_y)

#print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    vx = Y[2]
    vy = Y[3]
    ax = calculate_total_acceleration(planets, Y[0], Y[1])[0]
    ay = calculate_total_acceleration(planets, Y[0], Y[1])[1]
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
#print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(80, 27.1)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)

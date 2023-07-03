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

# Entry 3 of 3
# ============
# Write your function here. It should return a rune.
"""
Rune - Title: Huat ah!

Description:
In the spirit of the Chinese New Year, I have come up with a rune that inscribes the
chinese character for prosperity within a circle of four-leaf clovers.

This is the combination of components from entry 1 and entry 2 with minor tweaks. 
"""
#Helper functions
#left, right
def beside_frac(frac, a, b):
    """
    makes a new Rune from two given Runes by placing
    the first on the left of the second such that the
    first one occupies frac portion of the
    width of the result and the second the rest
    """
    a, b = quarter_turn_left(a), quarter_turn_left(b)
    return quarter_turn_right(stack_frac((1 - frac), b, a))

#TODO
def binary_image(n): #n is an array containing  1 and 0s
    """
    Takes an array of 1s and 0s. Iterate throught the array  and map blank_bb to 1s and
    black_bb to 0s
    Think of it building a black and white image pixel by pixel
    """
    result = blank_bb
    next_row = blank_bb #First column is assumed to be blank
    num_row = len(n)
    
    for i in range(0, num_row): #For each row in the picture
        num_pix = len(n[i])
        for j in range(0, num_pix): #For each pixel in each row
            if i == 0:#First row is assumed to be blank
                result = beside_frac(((j + 1)/ num_pix),result,blank_bb)
                continue
            
            if n[i][j] == 1:
                next_row = beside_frac((j / (j + 1)), next_row, blank_bb)
            else:
                next_row = beside_frac((j / (j + 1)), next_row, black_bb)
        if i == 0:
            continue
        result = stack_frac((i / (i + 1)), result, next_row)
        print( i / num_row , "% done") #Informs the user that the function is running
    return result

huat = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],\
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],\
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],\
        [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],\
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],\
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],\
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],\
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],\
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],\
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],\
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],\
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

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

def huat_ah():
    huat_image = scale(4/5, binary_image(huat))
    star_circle(heart_clover(1.5, 1.1), 21)
    return huat_image
    
show(huat_ah())




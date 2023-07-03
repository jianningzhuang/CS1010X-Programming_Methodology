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

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
"""
Rune-title: Got to cath'em all

Description:
Binary images are image under bitmap mode. To convert a RGB image into a binary image,
we will use thresholding. However this contest does not allow other libraries to be imported
so thresholding will be done outside of this file.

Thresholding:
Obtainn the RGB value of each pixel. If value > 188, then return 1 (white),
else 0 (black). Each row of pixel is stored in a list, all rows are stored
in a list as well.
This list is the value binary_image() will use to generate
the binary image.

I convinced myself that this would be easy :( lets see how it goes

Update: Actually not that hard. But final result is limited by runes.py, the
best runes.py can do is to creat a 15 x 15 pixel image.
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

#Higher resolution RBG image = longer array
#I found out the sad way that rune.py cannot handle pictures bigger than 15 pixel x 15 pixel
#Like think of all the nice pictures I could have generated
#But nope, just a lame pokeball in the end. Like its not even a great ball.
#Sad realistion that I will never be a masterball or even a safari ball

bin_array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],\
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],\
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],\
             [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],\
             [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],\
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],\
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],\
             [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],\
             [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],\
             [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1],\
             [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],\
             [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],\
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],\
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


show(binary_image(bin_array))



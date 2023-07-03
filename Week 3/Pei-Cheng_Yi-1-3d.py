#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

from math import pi

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
"""
Title: Time Tunnel

Remember those time travel tunnel from Doreamon? This rune resembles that.
Also some say 2 years very fast one, but we all know thats nonesense and that an option
to timetravel would have been much appreciated. 

P.s.
I was actually trying to construct a rose. But this looks cool too (and i couldn't
generate a rose after a couple of tries)
"""
def background_pat(pat):
    """
Moves a pattern to the bottom, and stacks an identical pattern that has been moved to the
top. End state we will have 2 identital patterns joined by the x-axis.

pat -- rune
    """
    pat = translate(0, 1/2, pat)
    return stack(pat, flip_vert(flip_horiz(pat)))


def clockhands(hand):
    """
Returns 2 clockhands that intersects and are pi/3.2 radians away from each other

hand -- rune
    """
    def clockhand1(hand):
        """
    Returns a clockhand that has been centred and properly sized
        """
        hand = translate(0, 1/2, hand)
        #x for length and y for thickness
        hand = scale_independent(0.2, 0.06, stack(hand, flip_vert(hand))) 
        hand = translate(-0.1, 0, hand)
        return hand
    return [clockhand1(hand), rotate(math.pi/3.2, clockhand1(hand))]
    
def clock(body, f):
    """
Applies background_pat and f on body to make a rune that resembles the body of a clock

f -- transformation function
body -- rune
    """
    return background_pat(f(body))

def twist(pat):
    """
Rotate the current pattern, make it smaller, put a new (not altered) pattern on
top of it.
Repeat this and we will have a nice pattern by "twisting" existing runes.

pat -- rune
    """
    #Turns the next pattern by a about 60 degrees
    def turned_pat(pat, n):
        result = pat
        for i in range(1, n):
            result = overlay_frac(1/i, pat, scale(49/60, rotate(math.pi / 3, result)))
        return result
    return turned_pat(scale(1.25,make_cross(pat)), 30)
            
def show_hands():
    """
Shows the 2 hands of a clock
    """
    clockhand1, clockhand2 = clockhands(nova_bb)[0], clockhands(nova_bb)[1]
    anaglyph(twist(clockhand1))
    anaglyph(twist(clockhand2))
    
# Display runes here
show_hands()
anaglyph(twist(clock(nova_bb, make_cross))) #shows the body of the clock


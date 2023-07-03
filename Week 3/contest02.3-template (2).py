#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

def spiral_decay(pic, n):
    result = translate(0.35*cos(pi/2) ,0.35*sin(pi/2), scale(0.015, pic))


    for i in range(1, n+1):
        length = (0.35 - i/2500)
        result = overlay_frac(1/i, translate(length*cos(pi/2 + (2*pi*i)/360), length*sin(pi/2 + (2*pi*i)/360), scale(0.015, pic)), result)


    return result

##anaglyph(spiral_decay(circle_bb, 900))

def helix(pic, n):
    result = translate(1/2*cos(pi/2) ,1/2*sin(pi/2), scale(0.05, pic))
    for i in range(1, n+1):
        L = (1/2 - i/2*n)
        result = overlay_frac(1/i, translate(L*cos(pi/2 + (2*pi*i)/n), L*sin(pi/2 + (2*pi*i)/n), scale(0.05, pic)), result)
    return result
        

##pim = image_to_painter("PIM.png")
##hollusion(overlay(pim, heart_bb))

def create_conc_circle_zf ( radius1 , depth1 , radius2 , depth2 ):
    def square ( x ):
        return x * x
    a1_sq = square ( radius1 )
    a2_sq = square ( radius2 )
    def helper (x , y ):
        d_sq = square ( x - 300) + square ( y - 300)
        if d_sq < a1_sq :
            return depth1
        elif d_sq < a2_sq :
            return depth2
        else :
            return 1
    return helper
##show ( function_to_painter ( create_conc_circle_zf (90 , 1/3 , 270 , 2/3)))


# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)

def triangle():
    return scale_independent(1, 3**(1/2)/4, scale(0.29, translate(0.25, 0, beside(edge(), translate(-0.5, 0, sail_bb)))))

def edge():
    return translate(0.5, 0, flip_horiz(sail_bb))

def base():
    return quarter_turn_left(stack_frac(1/3, quarter_turn_right(edge()), stack(black_bb, quarter_turn_left(edge()))))

def height():
    return stack_frac(1/3, translate(1/6, 0, base()), stack(base(), translate(-1/6, 0, base())))

def top():
    return stack_frac(3/4, quarter_turn_left(stack_frac(1/4, blank_bb, quarter_turn_right(height()))), translate(-0.25, 0, scale_independent(6/8, 1, blank_bb)))



def slant():
    return rotate(pi/6, beside(black_bb, blank_bb))

def sixty():
    return scale(0.25, scale_independent(2/(3**(1/2)), 1, height()))

def three_tiles():
    return flip_vert(rotate(pi/3, sixty()))

def six_tiles():
    return translate(-0.135, 0.25, overlay_frac(1/100, three_tiles(), translate(0.285, 0, three_tiles())))

def seven_tiles():
    return overlay_frac(1/100, six_tiles(), translate(0.3, 0.25, three_tiles()))

def dark():
    return overlay_frac(1/100, seven_tiles(), translate(-0.1, 0.065, sixty()))

def triangle_sixty():
    return scale_independent(1, 0.433, triangle())

def one_third():
    return overlay_frac(1/100, dark(), translate(-0.1, -0.122, triangle()))

def penrose():
    return overlay_frac(1/2, one_third(), overlay_frac(4/5, two_third(), three_third()))


def two_third():
    return translate(0.087, -0.01, rotate(-2*pi/3, one_third()))

def three_third():
    return translate(0.05, 0.069, rotate(-4*pi/3, one_third()))

anaglyph(penrose())

bun = translate(-0.05, -0.2, scale(0.35, image_to_painter("bun.png")))

cheese1 = translate(-0.13, -0.3, scale(0.15, image_to_painter("cheese.jpg")))

cheese2 = translate(-0.13, -0.15, scale(0.15, image_to_painter("cheese.jpg")))

cheese3 = translate(-0.13, 0, scale(0.15, image_to_painter("cheese.jpg")))

tomato = scale(0.25, image_to_painter("tomato.jpg"))

patty1 = translate(-0.08, -0.05, scale(0.3, image_to_painter("patty.png")))

patty2 = translate(-0.08, 0.1, scale(0.3, image_to_painter("patty.png")))

patty3 = translate(-0.08, 0.25, scale(0.3, image_to_painter("patty.png")))

def ideal_burger():
    return overlay_frac(1/8, bun,
                        overlay_frac(1/7, cheese1,
                                     overlay_frac(1/6, patty1,
                                                  overlay_frac(1/5, cheese2,
                                                            overlay_frac(1/4, patty2,
                                                                         overlay_frac(1/3, cheese3, patty3))))))

##show(overlay_frac(1/4, bun, patty))

rainbow = image_to_painter("rainbow.webp")
anaglyph(cheese1)


# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)

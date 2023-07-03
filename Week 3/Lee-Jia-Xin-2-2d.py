
from runes import *
from math import sin, cos, pi


# Entry 2 of 3
# ============
def face(eye, mouth):
    return stack(beside(scale(0.5, eye), scale(0.5, eye)),stack(scale(0.3,nova_bb), quarter_turn_left(mouth)))

face1 = face(ribbon_bb, scale(0.5,circle_bb))
face2 = face(heart_bb, scale(0.5, heart_bb)) 
def trail(rune,star):
    return beside(beside(stackn(3, rune),beside(stackn(3, rune), stackn(3, rune))), star)

shooting_star = trail(quarter_turn_right(quarter_turn_right(nova_bb)), pentagram_bb)

star_gazing = stack(shooting_star, beside(face1, face2))

show(star_gazing)

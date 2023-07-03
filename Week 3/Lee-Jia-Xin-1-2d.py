from runes import *

def checker(rune1, rune2):
    return beside(stack(rune1, quarter_turn_left(quarter_turn_left(rune2))), stack(rune2, quarter_turn_right((quarter_turn_right(rune1)))))

def cool_rune1(rune1, rune2, rune3, rune4, rune5):
    return checker(checker(checker(checker(rune1, rune2), rune3), rune4), rune5) 

show(cool_rune1(circle_bb, heart_bb, make_cross(nova_bb), make_cross(rcross_bb),rcross_bb))

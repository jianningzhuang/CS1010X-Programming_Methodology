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

# Entry 2 of 3
# ============
# Write your function here. It should return a rune.


def inception():

    g_pattern = make_cross(rcross_bb)
    g_n = 17

    rows = []

    x_index = 0
    y_index = 0

    x_list = []
    y_list = []

    # blanking out the bottom left section
    for i in range(4):
        for j in range(g_n - 1 - i):
            x_list.append(j)
            y_list.append(i)
            x_list.append(i)
            y_list.append(j)

    # blanking out the right inner triangle
    for j in range(7):
        for i in range(7 - j):
            x_list.append(5 + j + i)
            y_list.append(11 - j)

    def main():
        del rows[:]
        for i in range(g_n):
            nonlocal y_index
            y_index = i
            rows.append(quarter_turn_right(make_row(g_n)))

        return stack_row(g_n)

    def make_row(n):
        nonlocal x_index
        x_index = n - 1

        if n == 0:
            return quarter_turn_left(check_index(x_index, y_index))
        else:

            return stack_frac(
                1 / n,
                quarter_turn_left(check_index(x_index, y_index)),
                make_row(n - 1),
            )

    def stack_row(n):
        if n == 0:
            return rows[0]
        else:
            return stack_frac(1 / n, rows[n - 1], stack_row(n - 1))

    def check_index(x, y):

        for i in range(len(x_list)):

            if x == x_list[i] and y == y_list[i]:
                return blank_bb

        return g_pattern

    g_pattern = main()
    return make_cross(main())


show(inception())

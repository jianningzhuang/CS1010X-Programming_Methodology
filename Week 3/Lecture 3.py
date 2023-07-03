
##ball1, ball2, ball3, ball4, ball5 = 'red', 'green', 'blue', 'red', 'blue'
##ball1, ball2, ball3, ball4, ball5 = ball4, ball2, ball5, ball1, ball3
##ball1, ball2, ball3, ball4, ball5 = ball5, ball1, ball2, ball3, ball4
##print(ball5)


##def bool_eval(x):                  #anything not 0, or empty string is evaluated True as a conditional
##    return True if x else False
##def str_eval(x):
##    return 'True' if x else 'False'
##print(bool_eval('True'))
##print(str_eval(True)) ##'True' != True
##print(str_eval(bool_eval(False)) == 'False')
##print(bool_eval(str_eval(False)) == False)
##print(bool_eval(str_eval(str_eval(False))))

##cube_a = 2 ** 3
##cube_b = 2 ** 3      #Functions variables are equal if they refer to the same memory location
##cube_c = lambda x: x ** 3
##cube_d = lambda x: x ** 3
##cube_e = lambda x: cube_d
##cube_f = lambda cube_d: cube_d
##def cube_g(cube_a):  #The scope of cube_d in cube_f is localized within the function cube_f -- it is a function parameter. 
##    def cube_h(cube_a):
##        return cube_a ** 3
##    return cube_h
##print(cube_g(3)(5) == 3**3)
##print(cube_h(cube_a) == cube_a**3)

##def foo(n):
##    if n == 0:
##        return 0
##    else:
##        return 2 * n + foo(n - 1)
##print(foo(5))

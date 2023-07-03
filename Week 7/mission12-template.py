#
# CS1010X --- Programming Methodology
#
# Mission 12
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's name>, <11a/11b>

from generic_arith_min import *

###########################
# Rational Number Package #
###########################

# Copy and paste the install_rational_package procedure from Mission
# 11a below and complete the tasks below for this mission.

def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )


    def negate_rat(x):   #(RepRat) -> Generic-Rat
        return make_rat(negate(numer(x)), denom(x))

    def is_zero_rat(x):  #(RepRat) -> Py-Bool
        return is_zero(numer(x))

    def is_eq_rat(x, y): #(RepRat, RepRat) -> Py-Bool
        return is_equal(mul(numer(x), denom(y)), mul(numer(y), denom(x)))

    
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    put("negate", ("rational", ), negate_rat)
    put("is_zero", ("rational", ), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)

    # Copy and paste your Mission 11a solution below here:


    ###########
    # Task 1a #
    ###########
    def repord_to_reprat(x):
        return content(create_rational(create_ordinary(x), create_ordinary(1)))

    ###########
    # Task 2a #
    ###########
    def RRmethod_to_ORmethod(method):
        return lambda ord, rat: method(repord_to_reprat(ord), rat)


    def RRmethod_to_ROmethod(method):
        return lambda rat, ord: method(rat, repord_to_reprat(ord))

    ###########
    # Task 3a #
    ###########
    def add_ordrat(x, y): #(RepOrd, RepRat) -> Generic-Rat
        return RRmethod_to_ORmethod(add_rat)(x, y)
    def add_ratord(x, y): #(RepRat, RepOrd) -> Generic-Rat
        return RRmethod_to_ROmethod(add_rat)(x, y)

    def sub_ordrat(x, y):
        return RRmethod_to_ORmethod(sub_rat)(x, y)
    def sub_ratord(x, y):
        return RRmethod_to_ROmethod(sub_rat)(x, y)
    
    def mul_ordrat(x, y):
        return RRmethod_to_ORmethod(mul_rat)(x, y)
    def mul_ratord(x, y):
        return RRmethod_to_ROmethod(mul_rat)(x, y)

    def div_ordrat(x, y):
        return RRmethod_to_ORmethod(div_rat)(x, y)
    def div_ratord(x, y):
        return RRmethod_to_ROmethod(div_rat)(x, y)

    def is_eq_ordrat(x, y):
        return RRmethod_to_ORmethod(is_eq_rat)(x, y)
    def is_eq_ratord(x, y):
        return RRmethod_to_ROmethod(is_eq_rat)(x, y)

    
    put("add", ("ordinary", "rational"), add_ordrat)
    put("sub", ("ordinary", "rational"), sub_ordrat)
    put("mul", ("ordinary", "rational"), mul_ordrat)
    put("div", ("ordinary", "rational"), div_ordrat)
    put("is_equal", ("ordinary", "rational"), is_eq_ordrat)
    put("add", ("rational", "ordinary"), add_ratord)
    put("sub", ("rational", "ordinary"), sub_ratord)
    put("mul", ("rational", "ordinary"), mul_ratord)
    put("div", ("rational", "ordinary"), div_ratord)
    put("is_equal", ("rational", "ordinary"), is_eq_ratord)

        

install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

###########################
# Complex Number Package  #
###########################

# Copy and paste the install_complex_package procedure from Mission
# 11b below and complete the tasks below for this mission.

##def install_complex_package():
##    def make_com(x, y):
##        return tag(repcom(x, y))
##    def repcom(x, y):
##        return (x, y)
##    def real(x):
##        return x[0]
##    def imag(x):
##        return x[1]
##    def tag(x):
##        return attach_tag("complex", x)
##
##    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
##    def add_com(x, y):
##        return make_com( add(real(x), real(y)),
##                         add(imag(x), imag(y)) )
##    def sub_com(x, y):
##        return make_com( sub(real(x), real(y)),
##                         sub(imag(x), imag(y)) )
##    def mul_com(x, y):
##        return make_com( sub(mul(real(x), real(y)),
##                             mul(imag(x), imag(y))),
##                         add(mul(real(x), imag(y)),
##                             mul(real(y), imag(x))))
##    def div_com(x, y):
##        com_conj = complex_conjugate(y)
##        x_times_com_conj = content(mul_com(x, com_conj))
##        y_times_com_conj = content(mul_com(y, com_conj))
##        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
##                         div(imag(x_times_com_conj), real(y_times_com_conj)))
##    def complex_conjugate(x):
##        return (real(x), negate(imag(x)))
##
##    def negate_com(x): #(RepCom) -> Generic-Com
##        return make_com(negate(real(x)), negate(imag(x)))
##
##    def is_zero_com(x): #(RepCom) -> Py-Bool
##        return is_zero(real(x)) and is_zero(imag(x)) 
##
##    def is_eq_com(x, y): #(RepCom, RepCom) -> Py-Bool
##        return is_equal(real(x), real(y)) and is_equal(imag(x), imag(y))
##
##    put("make", "complex", make_com)
##    put("add", ("complex", "complex"), add_com)
##    put("sub", ("complex", "complex"), sub_com)
##    put("mul", ("complex", "complex"), mul_com)
##    put("div", ("complex", "complex"), div_com)
##    put("negate", ("complex", ), negate_com)
##    put("is_zero", ("complex", ), is_zero_com)
##    put("is_equal", ("complex", "complex"), is_eq_com)
##
##    # Copy and paste your Mission 11b solution below here:
##
##
##    ###########
##    # Task 1b #
##    ###########
##    def repord_to_repcom(x):
##        return content(create_complex(create_ordinary(x), create_ordinary(0)))
##
##    ###########
##    # Task 2b #
##    ###########
##    def CCmethod_to_OCmethod(method):
##        return lambda ord, com: method(repord_to_repcom(ord), com)
##
##
##    def CCmethod_to_COmethod(method):
##        return lambda com, ord: method(com, repord_to_repcom(ord))
##
##    ###########
##    # Task 3b #
##    ###########
##    def add_ordcom(x, y): #(RepOrd, RepCom) -> Generic_Com
##        return CCmethod_to_OCmethod(add_com)(x, y)
##    def add_comord(x, y): #(RepCom, RepOrd) -> Generic-Com
##        return CCmethod_to_COmethod(add_com)(x, y)
##
##    def sub_ordcom(x, y):
##        return CCmethod_to_OCmethod(sub_com)(x, y)
##    def sub_comord(x, y):
##        return CCmethod_to_COmethod(sub_com)(x, y)
##
##    def mul_ordcom(x, y):
##        return CCmethod_to_OCmethod(mul_com)(x, y)
##    def mul_comord(x, y):
##        return CCmethod_to_COmethod(mul_com)(x, y)
##
##    def div_ordcom(x, y):
##        return CCmethod_to_OCmethod(div_com)(x, y)
##    def div_comord(x, y):
##        return CCmethod_to_COmethod(div_com)(x, y)
##
##    def is_eq_ordcom(x, y):
##        return CCmethod_to_OCmethod(is_eq_com)(x, y)
##    def is_eq_comord(x, y):
##        return CCmethod_to_COmethod(is_eq_com)(x, y)
##
##    
##    put("add", ("ordinary", "complex"), add_ordcom)
##    put("sub", ("ordinary", "complex"), sub_ordcom)
##    put("mul", ("ordinary", "complex"), mul_ordcom)
##    put("div", ("ordinary", "complex"), div_ordcom)
##    put("is_equal", ("ordinary", "complex"), is_eq_ordcom)
##    put("add", ("complex", "ordinary"), add_comord)
##    put("sub", ("complex", "ordinary"), sub_comord)
##    put("mul", ("complex", "ordinary"), mul_comord)
##    put("div", ("complex", "ordinary"), div_comord)
##    put("is_equal", ("complex", "ordinary"), is_eq_comord)


def install_complex_package():
    # Copy and paste your Mission 11b solution below here:
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)
    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = content(complex_conjugate(y))
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return make_com(real(x), negate(imag(x)))
    
    #RepComt --> Generic-Com (tag is stripped and added back)
    def negate_com(x):
        return make_com(negate(real(x)), negate(imag(x)))
    #RepCom --> Boolean
    def is_zero_com(x):
        return is_zero(real(x)) and is_zero(imag(x))
    #(RepCom, RepCom) --> Boolean
    def is_eq_com(x, y):
        return is_equal(real(x), real(y)) and is_equal(imag(x), imag(y))
        
    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)
    put("negate", ("complex", ), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex","complex"), is_eq_com)
    ###########
    # Task 1b #
    ###########
    def repord_to_repcom(x): #RepCom --> (GenOrd, GenOrd)
        return (create_ordinary(x), create_ordinary(0))
    ###########
    # Task 2b #
    ###########
    def CCmethod_to_OCmethod(method):
        return lambda ord, com: method(repord_to_repcom(ord), com)
    def CCmethod_to_COmethod(method):
        return lambda com, ord: method(com, repord_to_repcom(ord))
    
    ###########
    # Task 3b #
    ###########
    ###CC --> CO
    def add_CO(x,y): 
        return CCmethod_to_COmethod(add_com)(x,y)
    def sub_CO(x,y):
        return CCmethod_to_COmethod(sub_com)(x,y)
    def mul_CO(x,y):
        return CCmethod_to_COmethod(mul_com)(x,y)
    def div_CO(x,y):
        return CCmethod_to_COmethod(div_com)(x,y)
    def is_eq_CO(x,y):
        return CCmethod_to_COmethod(is_eq_com)(x,y)
    
    ###RR --> OR
    def add_OC(x,y): 
        return CCmethod_to_OCmethod(add_com)(x,y)
    def sub_OC(x,y):
        return CCmethod_to_OCmethod(sub_com)(x,y)
    def mul_OC(x,y):
        return CCmethod_to_OCmethod(mul_com)(x,y)
    def div_OC(x,y):
        return CCmethod_to_OCmethod(div_com)(x,y)
    def is_eq_OC(x,y):
        return CCmethod_to_OCmethod(is_eq_com)(x,y)
       
#adding CC --> CO
    put("add", ("complex", "ordinary"), add_CO)
    put("sub", ("complex", "ordinary"), sub_CO)
    put("mul", ("complex", "ordinary"), mul_CO)
    put("div", ("complex", "ordinary"), div_CO)
    put("is_equal", ("complex", "ordinary"), is_eq_CO)    
#adding CC --> OC
    put("add", ("ordinary", "complex"), add_OC)
    put("sub", ("ordinary", "complex"), sub_OC)
    put("mul", ("ordinary", "complex"), mul_OC)
    put("div", ("ordinary", "complex"), div_OC)
    put("is_equal", ("ordinary", "complex"), is_eq_OC)

install_complex_package()

def create_complex(x,y):
    return get("make","complex")(x,y)


#################
# Do not change #
#################

n3 = create_ordinary(3)
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))

def gradeThis_rational_package():
    rationalA = is_equal(n3, r3_1)
    rationalB = is_equal(sub(add(n3, r2_7), r2_7), n3)
    if rationalA and rationalB:
        print("Well done! Your install_rational_package is complete!")
    else:
        print("Please check your solution for install_rational_package.")

n3 = create_ordinary(3)
c3_plus_0i = create_complex(create_ordinary(3), create_ordinary(0))
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))

def gradeThis_complex_package():
    complexA = is_equal(n3, c3_plus_0i)
    complexB = is_equal(sub(add(n3, c2_plus_7i), c2_plus_7i), n3)
    if complexA and complexB:
        print("Well done! Your install_complex_package is complete!")
    else:
        print("Please check your solution for install_complex_package.")

gradeThis_rational_package()
gradeThis_complex_package()

n25 = create_ordinary(25)

c3_plus_4i = create_complex(create_ordinary(3), create_ordinary(4))
c3_minus_4i = create_complex(create_ordinary(3), create_ordinary(-4))

print(is_zero(add(mul(c3_plus_4i, negate(c3_minus_4i)), n25)))

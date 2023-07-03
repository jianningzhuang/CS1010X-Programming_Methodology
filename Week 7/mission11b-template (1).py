#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <Juang Zhianning> <Zhuang Jianning>

###############
# Mission 11b #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)
# (a) What are the types of the input and output of the generic square operation?
# Answer: (Generic-Num, Generic-Num) -> Generic-Num
#          apply_generic strips the tag of both Generic-Nums to find the proc in the operation table indexed by mul and the (tag, tag) tuple
#          multiplication would be carried out in the representations of x but returned with original tagging

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: the programmer would not have to create another row in the operation table just for square
#         and update each package with the corresponding square_tag and put function 

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer: constructors like make_ord only need to attach a string tag to a representation (RepOrd) -> ({ordinary} x RepOrd) = Generic-Ord
#         while operators like add or negate call the function apply_generic which strips the tag/tags of the input and maps it to a tuple
#         because some operations take in 2 inputs and have 2 tags.
#         the operation is then looked up in the dictionary indexed by the type of operation and the tag tuple
#         so even though negate or is_zero only take in 1 input, it's tag is still mapped to a tuple when apply_generic is invoked
#         compared to create_ordinary which only retrieves the operation indexed by "make" and "ordinary" which is make_ord

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

# first_try = create_complex(9, 10)
# second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: create_complex(create_ordinary(9), create_ordinary(10))
#            generic complex number is formed with generic ordinary numbers or generic rational numbers for real and imaginary parts

# What happens: using create_complex(9, 10) and create_complex(3, 10) returns ('complex', (9, 10)) and ('complex', (3, 10))
#               which works well first when add is called => apply_generic strips both 'complex' tags and returns tuple ('complex', 'complex')
#               lookup in the table returns add_com which calls add(real(x), real(y)) = add(9, 3) but 9 and 3 don't have tags
#               which raises the Exception ('Bad tagged datum -- type_tag ', 9) when contents within apply_generic is called
#               this would not have happened if the real and imaginary parts of both complex numbers had 'ordinary' or 'rational' tags
# Why it happens: cannot add(real(x), real(y)) because they don't have tags (see above^)

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))

# csq = square(sub(c2_plus_7i, c3_plus_1i)) = ('complex', (('ordinary', -35), ('ordinary', -12)))

##            +---+---+---+---+
##   csq -->  |       |       |  
##            +---+---+---+---+
##                |       |
##                v       |
#            "complex"    |
#                         |
#                         v
##                +---+---+---+---+    +---+---+---+---+
##                |       |       | -> |       |       |
##                +---+---+---+---+    +---+---+---+---+
##                    |                    |       |
##                    v                    v       v
#                                      "ordinary"  -12
#             +---+---+---+---+
#             |       |       |
#             +---+---+---+---+
#                 |       |
#                 v       v
#             "ordinary"  -35

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?


# Answer: within the add_com function, it makes use of the general operator add to make the new real and imaginary parts, hence there would be a naming conflict
#         naming add_com add instead would make it call itself with no termination case => infinite loop/recursion
#                                                         

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
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
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return (real(x), negate(imag(x)))

    def negate_com(x): #(RepCom) -> Generic-Com
        return make_com(negate(real(x)), negate(imag(x)))

    def is_zero_com(x): #(RepCom) -> Py-Bool
        return is_zero(real(x)) and is_zero(imag(x)) 

    def is_eq_com(x, y): #(RepCom, RepCom) -> Py-Bool
        return is_zero(sub(x,y))

    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)
    put("negate", ("complex", ), negate_com)
    put("is_zero", ("complex", ), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)

# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)),
        add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()

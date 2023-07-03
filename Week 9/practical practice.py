
def make_polynomial(lst):
    def helper(*args):
        if args[0] == "compute":
            result = 0
            for exponent, coefficient in lst:
                result += coefficient * (args[1]**exponent)
            return result
        elif args[0] == "add":
            pass
    return helper

g = make_polynomial([(1,1), (2,-2), (3,1), (0,-2)])
print(g('compute', -1))

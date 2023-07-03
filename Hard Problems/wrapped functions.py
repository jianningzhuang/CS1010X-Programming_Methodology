def make_polynomial(lst):
    seen = []
    for term in lst:
        if term not in seen:
            seen.append(term)
    lst.clear()
    lst.extend(seen)
    def helper(*args):
        if args[0] == "terms":
            return lst
        if args[0] == "compute":
            result = 0
            for exponent, coefficient in lst:
                result += coefficient * (args[1]**exponent)
            return result
        if args[0] == "add":
            new = []
            for term1 in lst:
                for term2 in args[1]("terms"):
                    if term1[0] == term2[0]:
                        tmp = (term1[0], term1[1] + term2[1])
                        if tmp not in new:
                            new.append(tmp)
            return make_polynomial(new)
        if args[0] == "differentiate":
            new = []
            for term in lst:
                if term[0] > 0:
                    new.append((term[0] - 1, term[1]*term[0]))
            lst.clear()
            lst.extend(new)
            
            
    return helper

##g = make_polynomial([(1,1), (2,-2), (3,1), (0,-2)])
##p = g('add', g)
##p('differentiate')
##print(p("terms"))
##print(p('compute', -1))

def f(x,y,v,w):
    return x * v + (y - w)


def genCurr(func, minArgs):
    result = []
    def helper(*args):
        for i in args:
            result.append(i)
        if len(result) < minArgs:
            return None
        else:
            return func(*result)
    return helper

##curry_f = genCurr(f,4)
##print(curry_f(2,3))
##print(curry_f(7,5)) 


def is_symmetric(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[len(lst) - i - 1]:
            return False

    return True

#print(is_symmetric([1,2,2,1]))

        

    












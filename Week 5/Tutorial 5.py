tup1 = (7, (6, 5, 4), 3, (2, 1))
exp1 = tup1[3][1]

#print(exp1)

tup2 = (7, (6,), (5, (4,)), (3, (2, (1,))))
exp2 = tup2[3][1][1][0]

#print(exp2)


tup3 = ((7), (6, 5, 4), (3, 2), 1)
exp3 = tup3[3]

#print(exp3)

tup4 = (7, ((6, 5), (4,), 3, 2), ((1,),))
exp4 = tup4[2][0][0]

#print(exp4)

def even_rank(tup):
    result = ()
    for i in tup[1::2]:
        result += (i,)
    return result

#print(even_rank((3, 1, 4, 3, 2, 3, 19, 7, -90)))

def odd_even_sums(val):
    sum_odd = 0
    sum_even = 0
    for i in val[0::2]:
        sum_odd += i
    for i in val[1::2]:
        sum_even += i
    return (sum_odd, sum_even)

#print(odd_even_sums((1, 3, 2, 4, 5)))


def hanoi(n, src, dsc, aux):
    if n == 1:
        return ((src, dsc), )
    else:
        return (hanoi(n-1, src, aux, dsc) + ((src, dsc), ) + hanoi(n-1, aux, dsc, src))

#print(hanoi(3, 1, 2, 3))














def find_polynomial(f):
    coeff_dic={}
    number=f(10**100)
    def helper(number):
        counter=15
        while -1<number/10**(100*counter)<1:
            if counter==-1:
                return
            counter-=1
        
        coefficient=(number/10**(100*counter))
        coeff_dic[counter]= coefficient
        helper(number-(int(coefficient)*10**(100*counter)))
        
        
    helper(number)
    coeff_list=(sorted(coeff_dic.items()))

    if coeff_list[0][0]==0:
        output=[coeff_list.pop(0)]
    else:
        output=[(0,0)]
    
    for i in coeff_list:
        if i[0]-output[-1][0]>1:
            output.extend(((0,0),)*(i[0]-output[-1][0]-1))
        output.append(i)
    final_output=tuple(map(lambda x: int(x[1]), output))
    return(final_output)

# Do not modify the code below
def f(x):
    return 5 * x**3

def g(x):
    return 6 * x**6 - 2 * x**5 + 3*x + 5 * x**3

def h(x):
    return 5 + 3 * x**2 - 2 * x**11 + x + 3 * x**15

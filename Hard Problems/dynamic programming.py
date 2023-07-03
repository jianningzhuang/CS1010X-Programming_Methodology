
###memoized fib

def memo_fib(n):
    memo = {}
    if n in memo:
        return memo[n]
    elif n < 2:
        return 1
    else:
        result = memo_fib(n-1) + memo_fib(n-2)
        memo[n] = result
    return memo[n]

#print(memo_fib(5))


def create_fib(a,b):
    def f(n):
        if n <= 0:
            return 1
        elif n == a:
            return b
        else:
            return (-1)**(n+1)*(2*f(n-1) - f(n-2))
    return f

f1 = create_fib(18, 173234)
f2 = create_fib(15, -17711)

print(f1(0))
print(f2(7))

def create_fib(a,b):
    def fib(base):
        def helper(n):
            if n == 0:
                return 1
            elif n == 1:
                return base
            else:
                return (-1) ** (n + 1) * (2 * helper(n - 1) - helper(n - 2))
        return helper
    base = (b - fib(0)(a)) / (fib(1)(a) - fib(0)(a))
    return fib(base)

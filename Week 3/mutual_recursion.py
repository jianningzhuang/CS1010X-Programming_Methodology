def ping(n):
    if (n == 0): 
        return n
    else: 
        print("Ping!")
        pong(n - 1)

def pong(n):
    if (n == 0): 
        return n
    else: 
        print("Pong!")
        ping(n - 1)


ping(10)

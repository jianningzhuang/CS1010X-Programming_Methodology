
memo = {}

def cannibal(c, m):
    if (c, m) in memo:
        return memo[(c, m)]
    elif c > m and m != 0:
        return False
    elif c > 3 and c == m:
        return False
    elif (c + m) <= 2:
        memo[(c, m)] = ((c, m),)
    elif c == 0:
        result = ((0, 2), (0, 1)) + cannibal(0, m - 1)
        memo[(c, m)] = result
    elif m == 0:
        result = ((2, 0), (1, 0)) + cannibal(c - 1, 0)
        memo[(c, m)] = result
    elif c == 1 and m == 2:
        memo[(c, m)] = ((1, 1), (1, 0), (1, 1))
##    elif c == 2 and m == 2:
##        memo[(c, m)] = ((2, 0), (1, 0), (0, 2), (1, 0), (2, 0))
##    elif c == 3 and m == 3:
##        memo[(c, m)] = ((2, 0), (1, 0), (2, 0), (1, 0), (0, 2), (1, 1), (0, 2), (1, 0), (2, 0), (1, 0), (2, 0))
    else:
        result = ((2, 0), (1, 0), (0, 2), (0, 1)) + cannibal(c - 1, m - 1)
        memo[(c, m)] = result

    return memo[(c, m)]

    
        
            
    


print(cannibal(3, 3))


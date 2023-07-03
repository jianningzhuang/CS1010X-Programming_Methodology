coins = [1, 5, 10, 20, 50]

memo = {}
def cc(a):
    if a in memo:
        return memo[a]
    else:
        if a == 0:
            return 0
        elif a < 0:
            return float("inf")
        result = None
        for coin in coins:
            num = (cc(a - coin) + 1)
            if result == None or num < result:
                result = num
        memo[a] = result
        return result

#print(cc(101))

seq = ((0, 2), (1, 5), (2, 4), (3, 6), (4, 0))    
    
def adjacent_viruses(seq, row, col):
    count = 0
    zone = [(1,0), (1,1), (0,1), (0,0), (-1,0), (-1,-1), (0,-1),(1,-1),(-1,1)]
    for x, y in zone:
        if (row + x, col + y) in seq:
            count += 1
    return count

print(adjacent_viruses(seq, 4, 4)
)

def adjacent_grid(seq, height, width):
    result = ()
    for i in range(height):
        row = ()
        for j in range(width):
            row += (adjacent_viruses(seq, i, j),)
        result += (row,)
    return result

print(adjacent_grid(seq, 6, 7)
)


def safe_paths(grid):
    def helper(m, n):
        if m == 0 and n == 0:
            return 1
        elif m == 0:
            if grid[m][n - 1] == 0:
                return helper(m, n - 1)
            else:
                return 0
        elif n == 0:
            if grid[m - 1][n] == 0:
                return helper(m - 1, n)
            else:
                return 0
        else:
            ans = 0
            if grid[m][n - 1] == 0:
                ans += helper(m, n - 1)
            if grid[m - 1][n] == 0:
                ans += helper(m - 1, n)
            return ans
    return helper(len(grid) - 1, len(grid[0]) - 1)

print(safe_paths(adjacent_grid(seq, 6, 7)))
        
        
def count_change(amt, denom):
    if amt < 0 or len(denom) == 0:
        return 0
    elif amt == 0:
        return 1
    else:
        return count_change(amt-denom[0], denom) + count_change(amt, denom[1:])


print(count_change(100, [50, 20, 10, 5, 1]))


#space = O(amt/c + len(demon)) if len(denom) not constant and c = smallest denom
#maximum depth of the recursion tree is where denom is sliced to contain smallest denomination and amt decreases by that denom until 0

#time complexity = O(amt^denom)

#the recursive calls within memo_cc still calls count_change which does not do the database lookup if amt and demom have already been stored
#multiple overlapping subproblems are still being computed which does not improve running time


def create_database():
    return {}

def contains(db, amt, denom):
    if (amt, denom) in db:
        return True
    else:
        return False

def put(db, ans, amt, denom):
    db[(amt, denom)] = ans

def get(db, amt, denom):
    return db[(ans, denom)]


#number of subproblems = amt*len(denom) and each subproblem takes constant time to calculate
#time = O(amt*len(denom)) which is polynomial in size of input

#space = O(amt*len(denom)) which is the size of the dictionary
    

#5
#50

def cc_limited(amt, coins):        
    if amt == 0:
        return 1
    elif amt < 0 or len(coins) == 0:
        return 0
    else:
        to_delete = None
        denom = None
        for c in coins:
            if coins[c] == 0:
                to_delete = c
            else:
                denom = c
        if to_delete != None:
            del coins[to_delete]
        temp = dict(coins)
        del temp[denom]
        coins[denom] -= 1
        return cc_limited(amt, temp) + cc_limited(amt - denom, coins)

print(cc_limited(25,{1:30,5:1,10:30}))




            
    

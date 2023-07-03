

memo = {}
coins = {1 : 1, 2 : 5, 3 : 10, 4 : 20, 5 : 50}
count = 0

def cc(amount, kind_of_coins):
    global count
    count += 1
    if (amount, kind_of_coins) in memo:
        return memo[(amount, kind_of_coins)]
    else:
        if kind_of_coins == 0 or amount < 0:
            return 0
        elif amount == 0:
            return 1
        else:
            result = cc(amount, kind_of_coins - 1) + cc(amount - coins[kind_of_coins], kind_of_coins)
            memo[(amount, kind_of_coins)] = result
            return result

print(cc(100, 5))
#print(count)

def dp_cc(amount, kind_of_coins):
    table = {}
    for i in range(kind_of_coins + 1):
        table[(0, i)] = 1
    for j in range(amount + 1):
        table[(j, 0)] = 0

    for j in range(1, amount + 1):
        for i in range(1, kind_of_coins + 1):
            if j - coins[i] >= 0:
                table[(j, i)] = table[(j, i - 1)] + table[(j - coins[i], i)]
            else:
                table[(j, i)] = table[(j, i - 1)] 
#    print(table)
    return table[(amount, kind_of_coins)]

#print(dp_cc(100, 5))


prices = { 1 :1 , 2 :5 , 3 :8 , 4 :9 , 5 : 10 , 6 : 17 , 7 : 17 , 8 : 20 , 9 : 24 , 10 : 30 }

def cut_rod(length, prices):
    p = tuple(prices.items())

    def helper(length, prices):
        if length == 0 or prices == ():
            return 0
        else:
            cut = prices[0][0]
            price = prices[0][1]
            rest = prices[1:]
            if length < cut:
                return helper(length, rest)
            else:
                return max(helper(length, rest), price + helper(length - cut, prices))

    return helper(length, p)

#print(cut_rod(4, prices))

def dp_cut_rod(length, prices):
    p = tuple(prices.items())

    table = {}
    for i in range(length + 1):
        table[(i, 0)] = 0
    for j in range(len(p) + 1):
        table[(0, j)] = 0

    for i in range(1, length + 1):
        for j in range(1, len(p) + 1):
            if i < p[j-1][0]:
                table[(i, j)] = table[(i, j-1)]
            else:
                table[(i, j)] = max(table[(i, j-1)], p[j-1][1] + table[(i - p[j-1][0], j)])
    return table[(length, len(p))]

#print(dp_cut_rod(5, prices))




def cut_rod_brute(length, prices):
    p = list(prices.items())
    def max_val(length, prices):
        if prices == [] or length == 0:
            return 0
        elif prices[0][0] > length:  #explore right branch only
            return max_val(length, prices[1:])
        else:
            cut = prices[0][0]
            return max(max_val(length, prices[1:]), prices[0][1] + max_val(length - cut, prices))
    return max_val(length, p)

print(cut_rod_brute(4, prices))
        
    
    
    
    






















    
        
    

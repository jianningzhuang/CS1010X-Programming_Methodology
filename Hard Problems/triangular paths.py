def ways(m,n):
    if m==0 and n==0:
        return 1
    elif n>m or m<0 or n<0:
        return 0
    else:
        return ways(m-1,n) + ways(m-1,n-1) + ways(m,n-1)

print(ways(4, 4))

def blocked_ways(m,n,blocked):
    if (m,n) in blocked:
        return 0
    elif m==0 and n==0:
        return 1
    elif n>m or m<0 or n<0:
        return 0
    else:
        return blocked_ways(m-1,n,blocked) + \
        blocked_ways(m-1,n-1,blocked) + blocked_ways(m,n-1,blocked)

print(blocked_ways(5, 5, [(2, 0), (3, 2)]))


def memoized_blocked(m,n,blocked):
    d = {}
    for a,b in blocked:
        d[(a,b)]= 0
    def helper(m,n):
        if (m,n) in d:
            return d[(m,n)]
        elif m==0 and n==0:
            return 1
        elif n>m or m<0 or n<0:
            return 0
        else:
            ans = helper(m-1,n) + helper(m-1,n-1) + helper(m,n-1)
            d[(m,n)] = ans
            return ans
    return helper(m,n)

#print(memoized_blocked(10, 10, [(2, 0), (3, 2)]))

def cheapest_path(m,n,blocked):
    if (m,n) in blocked:
        return 4*(m+n+2)
    elif m==0 and n==0:
        return 0
    elif n>m or m<0 or n<0:
        return 4*(m+n+2)
    else:
        return min(1+cheapest_path(m-1,n,blocked),3+ \
        cheapest_path(m-1,n-1,blocked),1+cheapest_path(m,n-1,blocked))

#print(cheapest_path(10, 10, [(2, 0), (3, 2)]))

def ways1(m, n):
    if m == 0 and n == 0:
        return 1
    elif m == n:
        return ways1(m - 1, n - 1) + ways1(m, n - 1)
    elif n == 0:
        return ways(m - 1, n)
    else:
        return ways1(m - 1, n - 1) + ways1(m, n - 1) + ways(m - 1, n)

#print(ways1(4, 4))

def blocked_ways1(m, n, blocked):
    if (m, n) in blocked:
        return 0
    else:
        if m == 0 and n == 0:
            return 1
        elif m == n:
            return blocked_ways1(m - 1, n - 1, blocked) + blocked_ways1(m, n - 1, blocked)
        elif n == 0:
            return blocked_ways(m - 1, n, blocked)
        else:
            return blocked_ways1(m - 1, n - 1, blocked) + blocked_ways1(m, n - 1, blocked) + blocked_ways(m - 1, n, blocked)

#print(blocked_ways1(5, 5, [(2, 0), (3, 2)]))


def memoized_blocked1(m, n, blocked):
    memo = {}
    def helper(m, n, blocked):
        if (m, n) in memo:
            return memo[(m, n)]
        else:
            if (m, n) in blocked:
                result = 0
            else:
                if m == 0 and n == 0:
                    result = 1
                elif m == n:
                    result = helper(m - 1, n - 1, blocked) + helper(m, n - 1, blocked)
                elif n == 0:
                    result = helper(m - 1, n, blocked)
                else:
                    result = helper(m - 1, n - 1, blocked) + helper(m, n - 1, blocked) + helper(m - 1, n, blocked)
            memo[(m, n)] = result
            return result
    helper(m, n, blocked)
    return memo

#print(memoized_blocked1(10, 10, [(2, 0), (3, 2)]))

def dp(m, n, blocked):
    table = {}
    for b in blocked:
        table[(b[0], b[1])] = 0
    for i in range(n + 1):
        for j in range(i, m + 1):
            if (j, i) in table:
                continue
            elif j == 0:
                table[(j, i)] = 1
            elif i == 0:
                table[(j, i)] = table[(j - 1, i)]
            elif j == i:
                table[(j, i)] = table[(j - 1, i - 1)] + table[(j, i - 1)]
            else:
                table[(j, i)] = table[(j - 1, i - 1)] + table[(j, i - 1)] + table[(j - 1, i)]
    return table[(m, n)]

print(dp(10, 10, [(2, 0), (3, 2)]))
                
                
            

def cheapest_way(m, n, blocked):
    if (m, n) in blocked:
        return float("inf")
    else:
        if m == 0 and n == 0:
            return 0
        elif m == n:
            return min(3 + cheapest_way(m - 1, n - 1, blocked), 1 + cheapest_way(m, n - 1, blocked))
        elif n == 0:
            return 1 + cheapest_way(m - 1, n, blocked)
        else:
            return min(3 + cheapest_way(m - 1, n - 1, blocked), 1 + cheapest_way(m, n - 1, blocked), 1 + cheapest_way(m - 1, n, blocked))

#print(cheapest_way(10, 10, [(2, 0), (3, 2)]))



def next(m, n, blocked):
    result = []
    if m == n:
        if (m + 1, n + 1) not in blocked:
            result.append((m + 1, n + 1))
        if (m + 1, n) not in blocked:
            result.append((m + 1, n))
    elif n < m:
        if (m + 1, n + 1) not in blocked:
            result.append((m + 1, n + 1))
        if (m + 1, n) not in blocked:
            result.append((m + 1, n))
        if (m, n + 1) not in blocked:
            result.append((m, n + 1))
    return result

def path(m, n, blocked):
    initial = [(0, 0)]
    pathq = [initial]
    result = []
    while len(pathq) != 0:
        tmp = pathq.pop(0)
        last_node = tmp[-1]
        if last_node == (m, n):
            result.append(tmp)
        for node in next(last_node[0], last_node[1], blocked):
            if node[0] <= m and node[1] <= m and node not in tmp:
                new_path = tmp + [node]
                pathq.append(new_path)
    return len(result)

#print(path(5, 5, [(2, 0), (3, 2)]))

def in_place_reverse(lst):
    for i in range(len(lst)//2):
        lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]
    return lst

#print(in_place_reverse([1,2,3, 4]))


def num_sum(n):
    def helper(n, k):
        if n == 0:
            return 1
        elif n < 0 or k == 0:
            return 0
        else:
            return helper(n, k - 1) + helper(n - k, k)
    return helper(n, n-1)


#print(num_sum(4))

def sum_set(n):
    def helper(n, k, combination):
        if n == 0:
            return [combination]
        elif n < 0 or k == 0:
            return []
        else:
            return helper(n, k - 1, combination) + helper(n - k, k, combination + [k])
    return helper(n, n - 1, [])

#print(sum_set(5))

def sum_set_product(n):
    result = []
    sums = sum_set(n)
    for sum in sums:
        product = 1
        for i in sum:
            product *= i
        if product not in result:
            result.append(product)
    result.sort()
    return result

#print(sum_set_product(6))



def has_prime_sum(n):
    for i in range(2, n//2):
        if is_prime(i) and is_prime(n - i):
            return True
    return False

#print(has_prime_sum(11))

def in_place_quicksort(lst):
    def helper(start, end):
        if start >= end:
            return
        else:
            pivot = lst[end]
            current = start
            for i in range(start, end):
                if lst[i] < pivot:
                    lst[i], lst[current] = lst[current], lst[i]
                    current += 1
            lst[current], lst[end] = lst[end], lst[current]

        helper(start, current - 1)
        helper(current + 1, end)
    helper(0, len(lst) - 1)
    print(lst)

print(in_place_quicksort([3,2,1,5,4]))
                    
                    
        




        
    

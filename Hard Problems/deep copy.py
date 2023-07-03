def deep_copy(lst):
    if lst == []:
        return []
    elif type(lst) != list:
        return lst
    else:
        return [deep_copy(lst[0])] + deep_copy(lst[1:])


def deep_copy_check(lst1, lst2):
    if lst1 != lst2 or lst1 is lst2:
        return False
    for i in range(len(lst1)):
        if type(lst1[i]) == list:
            if not deep_copy_check(lst1[i], lst2[i]):
                return False
        else:
            if lst1[i] is not lst2[i]:
                return False
    return True
    
a = [[[1],2],3,4]
##b = deep_copy(a)
##print(deep_copy_check(a,b))
##b[0][0] = a[0][0]
##print(deep_copy_check(a,b))
##b[0] = a[0]
##print(deep_copy_check(a,b))
##c = deep_copy(b)
##print(deep_copy_check(a,b))
##d = c.copy()
##print(deep_copy_check(a,b))

def deep_replace(lst, a, b):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            deep_replace(lst[i], a, b)
        else:
            if lst[i] == a:
                lst[i] = b

def counting_deep_replace(lst, a, b):
    count = 0
    for i in range(len(lst)):
        if type(lst[i]) == list:
            count += counting_deep_replace(lst[i], a, b)
        else:
            if lst[i] == a:
                lst[i] = b
                count += 1
    return count

 



def dp_broken_paths(m, n, blocks):
    table = {}
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                table[(i, j)] = 1
            elif i == 0:
                if (i, j, i, j - 1) not in blocks:
                    table[(i, j)] = table[(i, j - 1)]
                else:
                    table[(i, j)] = 0
            elif j == 0:
                if (i, j, i - 1, j) not in blocks:
                    table[(i, j)] = table[(i - 1, j)]
                else:
                    table[(i, j)] = 0
            else:
                ans = 0
                if (i, j, i, j - 1) not in blocks:
                    ans += table[(i, j - 1)]
                if (i, j, i - 1, j) not in blocks:
                    ans += table[(i - 1, j)]
                table[(i, j)] = ans
    return table[(m, n)]

def dp_broken_paths1(m,n,blocks):
    t = []
    row = [0]*(m+1)
    for i in range(n+1):
        t.append(row.copy())
    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                t[i][j] = 1
            else:
                ans = 0
                if (i,j,i,j-1) not in blocks and j>0:
                    ans += t[i][j-1]
                if (i,j,i-1,j) not in blocks and i>0:
                    ans += t[i-1][j]
                t[i][j] = ans
    return t[m][n]

def broken_paths(m,n,blocks):
    if m==0 and n==0:
        return 1
    else:
        ans = 0
        if (m,n,m,n-1) not in blocks and n>0:
            ans += broken_paths(m,n-1,blocks)
        if (m,n,m-1,n) not in blocks and m>0:
            ans += broken_paths(m-1,n,blocks)
    return ans

#print(broken_paths(15,14,[(1,1,1,0)]))
print(dp_broken_paths(15,14,[(1,1,1,0)]))

                










    


def contains_square(n):
    for i in range(2, n):
        if n%(i*i) == 0:
            return True
    return False

def square_free(range1, range2):
    count1 = 0
    count2 = 0
    for i in range(range1[0], range1[1] + 1):
        if not contains_square(i):
            print (i)
            count1 += 1
    for j in range(range2[0], range2[1] + 1):
        if not contains_square(j):
            count2 += 1
    print(count1, count2)
    return max(count1, count2)

print(square_free((1, 5), (5, 9)))

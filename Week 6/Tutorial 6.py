###Question 1

def at_least_n(lst,n):
    for i in range(len(lst)):
        if lst[i]<n:
            lst.remove(lst[i])
    return lst
#NOOOOOO! the list is mutated in the for loop,
#hence lst[i] may not be the element we want or lst[i]
#may be out of range as it gets smaller in size whenever the condition is met

###Question 2

def at_least_n1(lst,n):
    for i in lst:
        if i < n:
            lst.remove(i)
    return lst

#NOU!!! lst still mutates through the for loop while i is based on the index of lst hence would skip over some elements it should remove
#never mutate a list through a loop, instead clone it
#check python tutor

lst1 = list(range(10))  
lst2 = list(range(8))
lst3 = list(range(6,10))

def at_least_n2(lst, n):
    for elem in lst[:]:   #CLONE LISTS
        if elem < n:
            lst.remove(elem)
    return lst

#print((at_least_n2(lst1, 5)))

def at_least_n3(lst, n):
    result = []
    for elem in lst[:]:
        if elem >= n:
            result.append(elem)
    return result

#print((at_least_n3(lst1, 5)))

def col_sum(matrix):
    result = []
    for i in range(len(matrix[0])):
        sum_of_each_column = 0
        for row in matrix:
            sum_of_each_column += row[i]
        result.append(sum_of_each_column)
    return result

#print(col_sum([[1,2],[3,4],[5,6]]))

def row_sum(matrix):
    result = []
    for row in matrix:
        sum_of_each_row = 0
        for value in row:
            sum_of_each_row += value
        result.append(sum_of_each_row)
    return result

#print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

matrix1 = [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[ 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix3 = [[1, 2, 3]]

def transpose(matrix): #find a better way
    clone = matrix[:]
    matrix.clear()
    for i in range(len(clone[0])):
        new_row = []
        for row in clone:
            new_row.append(row[i])
        matrix.append(new_row)
    
            
    return matrix

#print(transpose(matrix1))

##"""Insertion sort (see mission)"""
##in place sorting, prefix and suffix
##[5, 7, 4, 9, 8, 5, 6, 3] -> [4, 5, 7, 9, 8, 5, 6, 3] -> [4, 5, 7, 8, 9, 5, 6, 3] -> [4, 5, 5, 7, 8, 9, 6, 3] -> [4, 5, 5, 6, 7, 8, 9, 3] -> [3, 4, 5, 5, 6, 7, 8, 9]
##
##"""Selection sort (see lecture)"""
##[], [5, 7, 4, 9, 8, 5, 6, 3] -> [3], [5, 7, 4, 9, 8, 5, 6] -> [3, 4], [5, 7, 9, 8, 5, 6] ...... [3, 4, 5, 5, 6, 7, 8, 9], []
##
##"""Bubble sort (see recitation)"""
## swapping pairwise, starting over if necessary [5, 7, 4, 9, 8, 5, 6, 3] -> [5, 4, 7, 9, 8, 5, 6, 3] -> [4, 5, 7, 9, 8, 5, 6, 3] .....
##
##"""Merge sort (see lecture)"""
##dividing ==> [5, 7, 4, 9, 8, 5, 6, 3] -> [5, 7, 4, 9] [8, 5, 6, 3] -> [5, 7] [4, 9] [8, 5] [6, 3] -> [5] [7] [4] [9] [8] [5] [6] [3] 
##merging ==> [5] [7] [4] [9] [8] [5] [6] [3] -> [5, 7] [4, 9] [5, 8] [3, 6] -> [4, 5, 7, 9] [3, 5, 6, 8] -> [3, 4, 5, 5, 6, 7, 8, 9]

### DO NOT MODIFY THIS ###
students = [('tiffany', 'A', 15), 
            ('jane', 'B', 10),
            ('ben', 'C', 8), 
            ('simon', 'A', 21), 
            ('eugene', 'A', 21), 
            ('john', 'A', 15), 
            ('jimmy', 'F', 1), 
            ('charles', 'C', 9), 
            ('freddy', 'D', 4), 
            ('dave', 'B', 12)]

def mode_score(students):
    result = []
    scores = []
    for student in students:
        scores.append(student[2])
    frequency = len(scores)
    while frequency >= 1:
        for score in scores:
            if scores.count(score) == frequency and score not in result:
                result.append(score)
        if result != []:
            break
        else:
            frequency -= 1
    return result

#print(mode_score(students))



def top_k(students, k):
    students.sort() #alphabetical
    students.sort(key = lambda student: student[2], reverse = True) # stable grades
    result = students[:k]
    for student in students[k:]:
        if student[2] == students[k-1][2]:
            result.append(student)
    return result

#print(top_k(students, 3))















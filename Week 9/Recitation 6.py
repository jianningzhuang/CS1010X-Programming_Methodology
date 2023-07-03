many_things = [1 , 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')]
#print ( many_things )









def bubble_sort(lst):   #time complexity O(n^2) worst case each iteration through while loop pushes largest element to the back of list
    swaps = True                              # for loop runs n times, space is O(1)
    while swaps:
        swaps = False
        for i in range(len(lst)-1):
            print(lst)
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swaps = True
    
    return lst


def in_place_selection(lst): #time complexity O(n^2) nested for loops space complexity O(1)
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            print(lst)
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
            
students = [
('tiffany ', 'A', 15 ) ,
('jane ', 'B', 10 ) ,
('ben ', 'C', 8 ) ,
('simon ', 'A', 21 ) ,
('john ', 'A', 15 ) ,
('jimmy ', 'F', 1 ) ,
('charles ', 'C', 9 ) ,
('freddy ', 'D', 4 ) ,
('dave ', 'B', 12 )]

#part a
#students.sort(key = lambda x: x[0], reverse = True)


#part b
#students.sort(key = lambda x: x[0])
#students.sort(key = lambda x: x[1])


#part c

##result = ()
##for student in students:
##    if len(student[0])<6:
##        result += (student[0],)

x = tuple(filter(lambda x: len(x[0]) < 6, students))
y = tuple(map(lambda x: x[0] ,x))

#part d

result = ()
visited = ()
for i in range(len(students)):
    if students[i][1] not in visited:
        grade = students[i][1]
        visited += (grade, )
        count = 0
        for student in students:
            if student[1] == grade:
                count += 1
        result += ((grade, count),)
    





print(result)



print(students)











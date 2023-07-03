def count_cycles(tup):
    def func(tup, visited, level, lowertog, lowerlevel):
        ori = visited.copy()
        prev = []
        count = 0
        for i in range(len(tup)):
            if i > 0:
                if type(tup[i - 1]) == list:
                    prev.append(tup[i - 1])
            visited = ori.copy()
            lower = False
            if not lowertog:
                for k in prev:
                    if tup[i] is k:
                        lower = True
                        lowerlevel = level + 1
            else:
                lower = True
            cont = False
            for j in range(len(visited)):
                if tup[i] is visited[j]:
                    if lowertog: #lowertog implies ignore lower loops to prevent double counting
                        if j >= lowerlevel:
                            count -= 1
                    count += 1
                    cont = True
                    break
            if cont:
                continue
            if type(tup[i]) == list or type(tup[i]) == tuple:
                visited.append(tup[i])
                count += func(tup[i], visited, level + 1, lower, lowerlevel)
        return count
    return func(tup, [tup], 0, False, 0)


# Do not modify the code below

t1 = [(1,),(1,)]
t2 = [(1,), [(2,), (0,)]]
t3 = [(1,), [(2,), (0,)]]
t3[1][1] = t3

helper = [(),()]
helper[1] = helper
t4 = [helper, helper]

helper2 = [(),()]
t5 = [helper2, helper2]
helper2[0] = t5
helper2[1] = t5

t6 = [(True,), (True,)]
helper3 = [(True,), (True,)]
t6[0] = helper3
t6[1] = t6
helper3[0] = t6
helper3[1] = helper3

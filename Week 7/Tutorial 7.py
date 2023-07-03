###Question 1

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ([accumulate(op, init, [seq[0] for seq in sequences])]
               + accumulate_n(op, init, [seq[1:] for seq in sequences]))

#print(accumulate_n(lambda x,y: x+y, 0, [[1,2],[3,4],[5,6]]))

###Question 2

def col_sum(m):
    return accumulate_n(lambda x, y: x+y, 0, m)

#print(col_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

###Question 3

def transpose(m):
    result = []
    for i in range(len(m[0])):
        result.append([0]*len(m))
    for row in range(len(m)):
        for column in range(len(m[0])):
            result[column][row] = m[row][column]
    return result

def row_sum(m):
    return accumulate_n(lambda x, y: x+y, 0, transpose(m))

#print(row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))


###Question 4

def count_sentence(sentence):
    return [accumulate(lambda x, y: 1 + y, 0, sentence),
            accumulate(lambda x, y: len(x) + y, 0, sentence) + accumulate(lambda x, y: 1 + y, 0, sentence) - 1]

#print(count_sentence([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']]))



###Question 5

def letter_count(sentence):
    all_letters = []
    for word in sentence:
        for letter in word:
            all_letters.append(letter)
    all_letters.sort()
    result, count, cur_letter = [], 1, all_letters[0]
    for i in range(1, len(all_letters)):
        if all_letters[i] == cur_letter:
            count += 1
        else:
            result.append([cur_letter, count])
            cur_letter = all_letters[i]
            count = 1
    result.append([cur_letter, count])
    return result

#print(sorted(letter_count([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])))


###Question 6

def most_frequent_letters(sentence):
    if sentence == []:
        return []
    frequency = letter_count(sentence)
    most_frequent = None
    for letter in frequency:
        if most_frequent == None or letter[1] > most_frequent:
            most_frequent = letter[1]
    result = []
    for letter in frequency:
        if letter[1] == most_frequent:
            result.append(letter[0])
    return result

#print(set(most_frequent_letters([['C', 'S', '1', '0', '1', '0', 'S'], ['R', 'o', 'c', 'k', 's']])))
#print(most_frequent_letters([['s']]))


###Question 7

def make_queue():
    return []

def enqueue(q, item):
    return q.append(item)

def dequeue(q):
    return q.pop(0)
    
    
def size(q):
    return len(q)
    
### DO NOT MODIFY BEYOND THIS LINE!
q = make_queue()
enqueue(q, 1)
enqueue(q, 5)

###Question 8

def who_wins(m, players):
    game = make_queue()
    for player in players:
        enqueue(game, player)
    print(game)
    while size(game) >= m:
        for i in range(m):
            enqueue(game, dequeue(game))
            print(game)
        dequeue(game)
        print(game)
    return game

#print(set(who_wins(3, ['val', 'hel', 'jam', 'jin', 'tze', 'eli', 'zha', 'lic'])))











































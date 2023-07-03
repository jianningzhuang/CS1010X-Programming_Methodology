###Sequences

def tuplify(number):
    if number == 0:
        return ()
    else:
        return tuplify(number//10) + (number%10, )

#print(tuplify(10))

def untuplify(tpl):
    result = 0
    for digit in tpl:
        result = (result + digit)*10
    return result//10

def untuplify1(tpl):
    if tpl == ():
        return 0
    else:
        return 10*untuplify(tpl[:-1]) + tpl[-1]

#print(untuplify1((1, 0, 2, 4, 8, 6)))

def sum_tuple(t):
    result = 0
    for number in t:
        result += number
    return result

def max_and_min(t):
    max_value, min_value = None, None
    for value in t:
        if max_value == None or value > max_value:
            max_value = value
        if min_value == None or value < min_value:
            min_value = value
    return (max_value, min_value)

def max_and_min1(t):
    if len(t) == 1:
        max_value, min_value = t[0], t[0]
    else:
        result = max_and_min1(t[1:])
        if t[0] < result[0]:
            min_value = t[0]
        if t[0] > result[1]:
            max_value = t[0]
    return (max_value, min_value)
    

#print(max_and_min1((2,10,9,3,4)))


def make_fibonacci(n):
    result = ()
    def fib(x):
        if x < 1:
            return 0
        elif x == 1:
            return 1
        else:
            return fib(x-1) + fib(x-2)
    for i in range(n+1):
        result += (fib(i), )
    return result

#print(make_fibonacci(10))


###Polynomials of Fun

def filtered_accumulate(op, base, term, a, next, b, filter):
    i, total = a, base
    while i <= b:
        if filter(i):
            total = op(term(i), total)
        i = next(i)
    return total

def poly_acc(coefficients, x):
    return filtered_accumulate(lambda a, b: a + b, 0, lambda k: coefficients[k]*(x**k), 0, lambda x: x+1, len(coefficients) - 1, lambda x: True)

def new_poly(coefficients, x):
    return sum(lambda k: coefficients[k]*(x**(len(coefficients) - k - 1)), 0, lambda x: x+1, len(coefficients) - 1)


def calculator_generator(coefficients, ptype):
    if ptype == "old":
        return lambda x: poly(coefficients, x)
    else:
        return lambda x: new_poly(coefficients, x)

###Tuple Interleaving


def interleaved_tuple(tuple_a, tuple_b):
    result = ()
    for i in range(len(tuple_a)):
        result += (tuple_a[i], tuple_b[i])
    return result

#print(interleaved_tuple((1,3,5,7,9),(2,4,6,8,10)))

def interleaved_tuple_adv(tuple_a, tuple_b):
    result = ()
    if len(tuple_a) < len(tuple_b):
        n = len(tuple_a)
        for i in range(n):
            result += (tuple_a[i], tuple_b[i])
        result += tuple_b[n:]
    else:
        n = len(tuple_b)
        for i in range(n):
            result += (tuple_a[i], tuple_b[i])
        result += tuple_a[n:]
    return result

#print(interleaved_tuple_adv((1,3,5),(2,4,6,8,10,12)))

def interleaved_tuple_two(tuple_a, tuple_b):
    result = ()
    for i in range(len(tuple_b)):
        result += (tuple_a[2*i], tuple_a[2*i+1], tuple_b[i])
    return result

#print(interleaved_tuple_two((1,3,5,7,9,11,13,15),(2,4,6,8)))

def is_odd(x):
    return x % 2 == 1

def interleaved_tuple_picky(tuple_a, tuple_b, predicate):
    result = ()
    for i in range(len(tuple_a)):
        if predicate(tuple_a[i]):
            result += (tuple_a[i], )
        else:
            result += (tuple_b[i], )
    return result

#print(interleaved_tuple_picky((1, 2, 3, 4, 5), (9, 11, 13, 15, 17), is_odd))

###Card Magician

cards1 = ('QS', 'AC', 'TD', 'JC', 'KH')

def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output

def compare_cards(card1, card2):
    c1 = 'Z' if card1[0] == 'A' else card1[0]
    c1 = 'Y' if card1[0] == 'K' else c1
    c1 = 'B' if card1[0] == 'T' else c1
    c2 = 'Z' if card2[0] == 'A' else card2[0]
    c2 = 'Y' if card2[0] == 'K' else c2
    c2 = 'B' if card2[0] == 'T' else c2
    return card1[1] > card2[1] if c1 == c2 else c1 > c2


##def sort_deck(deck): #w/o card magician
##    if deck == ():
##        return ()
##    elif len(deck) == 1:
##        return deck
##    else:
##        min_card = None
##        min_index = None
##        for i in range(len(deck)):
##            if min_card == None or compare_cards(min_card, deck[i]):
##                min_card = deck[i]
##                min_index = i
##        new_deck = deck[:min_index] + deck[min_index+1:]
##        return (min_card, ) + sort_deck(new_deck)

def sort_deck(deck):
    a = () # Replace with your answer here.
    b = [deck]*len(deck) # Replace with your answer here.
    c = next_lowest # Replace with your answer here.
    return card_magician(a, b, c)

def next_lowest(result, deck):
    if result == ():
        min_card = None
        for card in deck:
            if min_card == None or compare_cards(min_card, card):
                min_card = card
        result += (min_card, )
    else:
        next_min = result[-1]
        for card in deck:
            if next_min == result[-1] and compare_cards(card, next_min):
                next_min = card
            else:
                if compare_cards(next_min, card) and compare_cards(card, result[-1]):
                    next_min = card
        result += (next_min, )
    return result
            
#print(sort_deck(('AS', '5S', 'TS', '7S')))

cards2 = ('7H', '3S', '6C', 'JH', '2H', '2S', 'TD')

def suit_to_index(card):
    if card[1] == "C":
        return 0
    elif card[1] == "D":
        return 1
    elif card[1] == "H":
        return 2
    elif card[1] == "S":
        return 3

def split_by_suit(result, card):
    updated_suit = result[suit_to_index(card)] + (card, )
    result = result[:suit_to_index(card)] + (updated_suit, ) + result[suit_to_index(card) + 1:]
    return result
    
##    if card[1] == "C":
##        updated_suit = result[0] + (card, )
##        result = (updated_suit, ) + result[1:]
##    elif card[1] == "D":
##        updated_suit = result[1] + (card, )
##        result = result [:1] + (updated_suit, ) + result[2:]   
##    elif card[1] == "H":
##        updated_suit = result[2] + (card, )
##        result = result [:2] + (updated_suit, ) + result[3:] 
##    elif card[1] == "S":
##        updated_suit = result[3] + (card, )
##        result = result [:3] + (updated_suit, )
##    return result

a = ((), (), (), ()) # Replace with your answer here.
b = cards2 # Replace with your answer here.
c = split_by_suit # Replace with your answer here.

# Uncomment the following line.
split_deck = card_magician(a, b, c)

#print(split_deck)

#cards = ()

cards = ('AS', 'AC', 'TD', 'JC', 'AS', 'TD', 'QH')

def appears_once(result, card):
    if card not in result:
        result += (card, )
    else:
        for i in range(len(result)):
            if result[i] == card:
                result = result[:i] + result[i+1:]
                break
    return result
            
        
 
a = () # Replace with your answer here.
b = cards
c = appears_once # Replace with your answer here.

# DO NOT delete this line, otherwise the public test will fail.
# DO NOT call `card_magician` anywhere else than this line below.
# Uncomment the following line.
unique_deck = card_magician(a, b, c)

#print(unique_deck)


##def card_magus(temp, result, cards, trick, output):
##    for card in cards:
##        result = trick(temp, result, card)
##        temp = result[0]
##        result = result[1]
##    return output(result, temp)


def card_magus(a, b, cards, trick, finalize):
    for card in cards:
        a, b = trick(a, b, card)
        print(a, b)
    return finalize(b, a)

##duplicate_cards = card_magus((),
##                             (),
##                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
##                             lambda abra, kadabra, alakazam: (abra + (alakazam,), kadabra) if alakazam in kadabra and not alakazam in abra else (abra, kadabra + (alakazam,)),
##                             lambda please, thank_you: thank_you)
##
##card_to_count = '3D'
##number_of_cards = card_magus(card_to_count,
##                             (),
##                             ('8H', '3D', 'AC', '4S', '3D', '9S', 'TD', 'TD'),
##                             lambda oo, ee, aa: (oo, ee + ((aa,) if aa == oo else ())),
##                             lambda ting, tang: len(ting))
#print(duplicate_cards)




def finalize(a, b):
    if not a:
        return b
    if not b:
        return a
    a = card_magus((), (), a, trick, finalize)
    b = card_magus((), (), b, trick, finalize)
    return a + b


def trick(a, b, card):
    if b == ():
        return a, b + (card, )
    elif compare_cards(b[0], card):
        return a + (b[0], ), (card, ) #smallest at the back, then swap to the front during finalise or vice versa
    else:
        return a + (card, ), b
    

        

    
##    if b == ():
##        return a, b + (card, )
##    elif compare_cards(b[0], card):
##        if a == ():
##            return a + (card, ), b
##        elif compare_cards(a[0], card):
##            return (card, ) + a, b
##        else:
##            return a + (card, ), b
##            
##    else:
##        return a, b + (card, )


# Uncomment the following line.
sorted_cards = card_magus((), (), ('TD', '4C', '6S', '9H', '3D', '5C', 'AH', 'KS', '2C', '7D', '8S', 'QC', 'JH'), trick, finalize)

print(sorted_cards)







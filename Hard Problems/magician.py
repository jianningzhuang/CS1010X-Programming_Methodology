def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
        print(output)
    return output

cards = ('AS', 'AC', 'TD', 'JC', 'AS', 'TD', 'QH')

a = () # Replace with your answer here.
b = cards 
c = lambda x,y: x + (y,) if b.count(y) == 1 else x # Replace with your answer here.

# DO NOT delete this line, otherwise the public test will fail.
# DO NOT call `card_magician` anywhere else than this line below.
# Uncomment the following line.
unique_deck = card_magician(a, b, c)
print(unique_deck)
print(card_magician(a, ('AS', 'AS', 'AC', 'AC'), c))

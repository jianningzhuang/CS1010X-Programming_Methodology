def make_word(string):
    result = ("Word", )
    current_word = ()
    for letter in string:
        current_word += (letter, )
    return result + (current_word, )

def is_word(obj):
    return type(obj) == tuple and obj != () and obj[0] == "Word"

def get_word(word):
    result = ""
    current_word = word[-1]
    for letter in current_word:
        result += letter
    return result

def delete(word, index):
    current_word = word[-1]
    if current_word[index:] == ():
        return word
    else:
        new_word = current_word[:index] + current_word[index + 1:]
        word += (new_word, )
    return word

def insert(word, index, letter):
    current_word = word[-1]
    if current_word[index - 1:] == ():
        return word
    else:
        new_word = current_word[:index] + (letter, ) + current_word[index:]
        word += (new_word, )
    return word

def undo(word):
    if word[2:] == ():
        return word
    else:
        return word[:-1]

def accept_all_changes(word):
    if word[2:] == ():
        return word
    else:
        return (word[0], ) + (word[-1], )

def equal(word1, word2):
    return word1[-1] == word2[-1]

    

w1 = make_word("blue")
w2 = delete(delete(w1, 2), 2)
w3 = insert(insert(insert(w2, 2, "k"), 2, "c"), 2, "a")

num = (9, 8, 7, 6, )
j = 0
for i in num:
    j += 1
print(j, "second")

        
        
##    try:
##        new_word = current_word[:index] + current_word[:index + 1:]
##    except TypeError:
##        return word
    
    

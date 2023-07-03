def digit_product(n):
    result = 1
    while n > 0:
        result *= n%10
        n = n//10
    return result

print(digit_product(1234))

def max_digit_product(n, k):
    stringify = str(n)
    max_value = None
    for i in range(len(stringify)-k + 1):
        test = stringify[i:i+k]
        value = digit_product(int(test))
        if max_value == None or value > max_value:
            max_value = value
    return max_value
        
    
print(max_digit_product(112311,2))

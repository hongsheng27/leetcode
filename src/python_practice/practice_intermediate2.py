import math
#  Write a function called "factorPrime" that takes an integer as input, and returns the prime factorization of the input.
# factorPrime(120); # returns "2 x 2 x 2 x 3 x 5"

def factorPrime(num):
    divisor_list = []
    for divisor in range(2, int(math.sqrt(num)) + 1):
        while num % divisor == 0:
            divisor_list.append(str(divisor))
            num //= divisor
    if num > 1: 
        divisor_list.append(str(num))
        
    return " x ".join(divisor_list)
            


print(factorPrime(120))
print(factorPrime(97))

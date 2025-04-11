# practice_intermediate.py
# Author: Will Liu
# Description: A collection of Python functions solving various problems, including sorting, prime checking, palindrome detection, and more.


# 1. Write a function called "mySort" that takes a list of integers as input 
#    and returns the sorted version of the input list. 
#    You are not allowed to use the built-in sorted() function.
# Example:
# mySort([17, 0, -3, 2, 1, 0.5]) -> [-3, 0, 0.5, 1, 2, 17]

def mySort(lst):
    """
    Sorts a list of numbers using bubble sort.
    """
    n = len(lst)
    while n > 1:
        is_move = False
        for i in range(n - 1):
            if(lst[i] > lst[i+1]): 
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_move = True
        if not is_move: break
        n -= 1
    print(lst)
    return lst

# Test cases:
# print(mySort([17, 0, -3, 2, 1, 0.5]))

# 2. Write a function called "isPrime" that takes an integer as input 
#    and returns a boolean value that indicates if the input number is prime.
# Example:
# isPrime(1) -> False
# isPrime(5) -> True
# isPrime(91) -> False
# isPrime(1000000) -> False

def isPrime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1: 
        print('false')
        return False
    for i in range(2, n):
        if not n % i: 
            print('false')
            return False
    print('true')
    return True

# Test cases:
# print(isPrime(1))  # False
# print(isPrime(5))  # True
# print(isPrime(91))  # False
# print(isPrime(1000000))  # False

# 3. Write a function called "palindrome" that checks if the input string is a palindrome.
# Example:
# palindrome("bearaeb") -> True
# palindrome("Whatever revetahW") -> True
# palindrome("Aloha, how are you today?") -> False

def palindrome(str):
    p1 = 0
    p2 = len(str) - 1
    
    while p1 <= p2: 
        if(str[p1] == str[p2]):
            p1 += 1
            p2 -= 1
        else:
            print('false')
            return 'false'
    print('true')
    return 'true'

# Test cases:
# print(palindrome("bearaeb"))  # True
# print(palindrome("Whatever revetahW"))  # True
# print(palindrome("Aloha, how are you today?"))  # False

# 4. Write a function called "pyramid" that takes an integer as input 
#    and prints a pyramid in the following pattern:
# Example:
# pyramid(1):
# *
# pyramid(2):
#  *
# ***
# pyramid(4):
#    *
#   ***
#  *****
# *******'

def pyramid(n):
    row_width = 1 + 2 * (n - 1)
    for i in range(1, n + 1):
        num_starts = i * 2 - 1
        spaces = ' ' * ((row_width - num_starts) // 2)
        stars = '*' * (num_starts)
        print(spaces + stars)

# Test cases:
pyramid(4)

# 5. Write a function called "inversePyramid" that draws a pyramid upside down.
# Example:
# inversePyramid(4):
# *******
#  *****
#   ***
#    *

def inversePyramid(n):
    row_width = 1 + 2 * (n - 1)
    for i in range(n, 0, -1):
        num_stars = i * 2 - 1
        stars = '*' * num_stars
        spaces = ' ' * ((row_width - num_stars) // 2)
        print(spaces + stars)

# Test cases:
# inversePyramid(4)

# 6. Given a list of ints, return True if the list contains a 3 next to a 3.
# Example:
# has_33([1, 5, 7, 3, 3]) -> True
# has_33([]) -> False
# has_33([4, 3, 2, 1, 0]) -> False

def has_33(lst):
    for i in range(len(lst) - 1): 
        if lst[i] == 3 and lst[i + 1] == 3:
            print('true')
            return True
    print('false')
    return False
            

# Test cases:
# print(has_33([1, 5, 7, 3, 3]))  # True
# print(has_33([]))  # False
# print(has_33([4, 3, 2, 1, 0]))  # False



# 7. Write a function that checks if a list contains a subsequence of 007.
# Example:
# spyGame([1, 2, 4, 0, 3, 0, 7]) -> True
# spyGame([1, 2, 5, 0, 3, 1, 7]) -> False

# my soltuon 1 
# def spyGame(lst):
#     result = ''
#     for ele in lst:
#         if ele == 0 or ele == 7:
#             result += str(ele)
#     print('007' in result)
#     return '007' in result

# my solution 2
# def spyGame2(lst):
#     result = ''.join((str(x) for x in lst if x == 7 or x == 0))
#     print('007' in result)
#     return '007' in result

def spyGame3(lst):
    string = '007'
    pointer_for_lst = 0
    pointer_for_str = 0

    while pointer_for_lst < len(lst):
        if lst[pointer_for_lst] == int(string[pointer_for_str]): 
            pointer_for_str += 1
            if pointer_for_str == len(string): return True
        pointer_for_lst += 1
    return False


# Test cases:
print(spyGame3([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame3([1, 2, 5, 0, 3, 1, 7]))  # False

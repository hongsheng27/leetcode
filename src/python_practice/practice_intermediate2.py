import math

# 1. factorPrime
# --------------------------
# Write a function called "factorPrime" that takes an integer as input,
# and returns its **prime factorization** in the format of a string joined by " x ".
# 
# Example:
# factorPrime(120) -> "2 x 2 x 2 x 3 x 5"
# factorPrime(97)  -> "97" (since 97 is a prime number)

def factorPrime(num):
    divisor_list = []
    for divisor in range(2, int(math.sqrt(num)) + 1):
        while num % divisor == 0:
            divisor_list.append(str(divisor))
            num //= divisor
    if num > 1: 
        divisor_list.append(str(num))
        
    return " x ".join(divisor_list)

# Test cases
# print(factorPrime(120))  # Expected: "2 x 2 x 2 x 3 x 5"
# print(factorPrime(97))   # Expected: "97"


# 2. intersection
# --------------------------
# Write a function called "intersection" that takes two lists of integers,
# and returns a new list containing only the **common elements** in both lists,
# without duplicates. The result should follow the order from the first list.
#
# Example:
# intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]) -> [3, 4]
# intersection([1, 1, 1], [1, 1, 1]) -> [1]
# intersection([1], [1]) -> [1]

# solution 1: two-pointer-like approach
def intersection(list1, list2): 
    point_1 = 0
    point_2 = 0
    result_list = []
    while point_1 < len(list1):
        if list1[point_1] == list2[point_2]: 
            if list1[point_1] not in result_list: 
                result_list.append(list1[point_1])
            point_1 += 1
            point_2 = 0
        elif point_2 >= len(list2) - 1:
            point_1 += 1
            point_2 = 0
        else:
            point_2 += 1
          
    print(result_list)
    return result_list

# solution 2: simple iteration
def intersection(list1, list2): 
    result_list = []
    for i in list1:
        if i in list2 and i not in result_list: 
            result_list.append(i)
          
    print(result_list)
    return result_list

# Test cases
# intersection([1, 1, 1], [1, 1, 1])                         # Expected: [1]
# intersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]) # Expected: [3, 4]
# intersection([1], [1])                                    # Expected: [1]


# 3. flatten
# --------------------------
# Write a function called "flatten" that flattens a nested list of arbitrary depth.
# All nested elements should be unpacked and returned as a single, flat list.
#
# Example:
# flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]])
# -> [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
# flatten([4, [1]]) -> [4, 1]

# solution : recursive flatten 
result = []
def flatten(my_list):
    for ele in my_list:
        if isinstance(ele, list):
            flatten(ele)
        else:
            result.append(ele)

    return result

# Test cases
print(flatten([4, [1]]))  
# Expected: [4, 1]

print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))  
# Expected: [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]

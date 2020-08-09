"""
Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""

def even(number):
    if number % 2 == 0:
        return {number : True}
    else:
        return {number : False}

numbers = list(range(1,21))
print(list(map(even,numbers)))

"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
A = [1, 5, 6]
B = [3, 5, 9]
C = [4, 10, 15]
"""
def add(number1,number2):
    return(number1+number2)

A = [1, 5, 6]
B = [3, 5, 9]

print(list(map(add,A,B)))

"""
Create a list of lists, these with multiple numbers to
be averaged
[
    [1, 2, 3],
    [9, 6, 1]
]
"""
def average(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum/len(numbers)

list1 = [
    [1, 2, 3],
    [9, 6, 1]
]

print(list(map(average, list1)))

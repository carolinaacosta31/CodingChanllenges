from functools import reduce
"""
Create a function that multiplies a sequence of
numbers.
"""
def multiply(num1, num2):
    return num1*num2

numbers = [1,2,3,4,5]

print(reduce(multiply, numbers))

"""
Create a function that takes a list of strings
and returns the sum of its characters.
"""
def char_quantity(word_a, word_b):
    word_a = len(word_a) if isinstance(word_a, str) else word_a
    return word_a + len(word_b)

strings = ['I','am','learning','to','code','with','python']

print(reduce(char_quantity, strings))

"""
This challenge can be a bit complicated, however
remember that in the functions you can perform
conditionals, take a list of numbers and return
the largest number.
"""
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

numbers = [4,7,99,1,43]

print(reduce(maximum, numbers))
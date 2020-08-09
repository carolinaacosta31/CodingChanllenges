"""
Use the lambda functions with the challenges of
map, filter and reduce.
"""
"""
Map
"""
"""
Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""
numbers = list(range(1,21))
print(list(map(lambda number: {number : True} if number % 2 == 0 else {number : False},numbers)))

"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
A = [1, 5, 6]
B = [3, 5, 9]
C = [4, 10, 15]
"""
A = [1, 5, 6]
B = [3, 5, 9]

print(list(map(lambda number1, number2: number1 + number2, A, B)))

"""
Create a list of lists, these with multiple numbers to
be averaged
[
    [1, 2, 3],
    [9, 6, 1]
]
"""
list1 = [
    [1, 2, 3],
    [9, 6, 1]
]

print(list(map(lambda numbers: sum(numbers)/len(numbers) , list1)))

"""
Filter
"""
"""
Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""
numbers = range(1,101)

print(list(filter(lambda number: number % 2 == 0, numbers)))

"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""
users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 15
    },
    {
        "name": "Jaime",
        "age": 18
    }
]

print(list(filter(lambda user: user["age"] < 18, users)))

"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""
numbers = range(-10,10)

print(list(filter(lambda number: number % 3 == 0 and number < 0,numbers)))

"""
Reduce
"""
from functools import reduce
"""
Create a function that multiplies a sequence of
numbers.
"""
numbers = [1,2,3,4,5]

print(reduce(lambda num1, num2: num1*num2, numbers))

"""
Create a function that takes a list of strings
and returns the sum of its characters.
"""
strings = ['I','am','learning','to','code','with','python']

print(reduce(lambda word_a,word_b: (len(word_a) if isinstance(word_a, str) else word_a) + len(word_b), strings))

"""
This challenge can be a bit complicated, however
remember that in the functions you can perform
conditionals, take a list of numbers and return
the largest number.
"""
numbers = [4,7,99,1,43]

print(reduce(lambda num1, num2: num1 if num1 > num2 else num2, numbers))
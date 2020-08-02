  
"""
Create a function that receives N numbers and returns
each of these multiplied by 2
"""

def multiply_by_two(*numbers):
    multiplied_list = [number*2 for number in numbers]
    print(multiplied_list)

numbers = [5, 4, 9, 7, 5, 3]
multiply_by_two(*numbers)

"""
Create a function that receives N arguments with your
personal information: name, age, phone, country, etc
Then print those values with their names
"""

def personal_information(**my_information):
    print(my_information)

info = {'name': 'Carolina', 'age': 35, 'phone': 3164713764, 'country': 'Colombia', 'city': 'Manizales', 'RH': 'O+'}

personal_information(**info)

"""
The Python print function receives positional arguments
and named arguments, the named arguments are used to alter
the way this print works:
sep = It indicates how all the values we pass will be separated
end = Indicates what you will put at the end of printing
Default Values:
sep = " "
end = "\n"
"""

values = ["Hello", "There","How","Are","You?"]
conf = {'sep' : ';' , 'end' : ' .... the end'}
print(*values, **conf)
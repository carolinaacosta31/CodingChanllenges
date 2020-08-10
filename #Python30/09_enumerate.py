"""
Create a list of 5 names and use the enumerate function to
display them as follows:
1. Name One
2. Name Two
...
5. Name Five
"""
names = ["Ana", "Beto", "Carla", "David", "Elena"]
for counter, element in enumerate(names, start=1):
    print('{}. {}'.format(counter,element))

"""
Use the enumerate function on a string (your name) and print
each character with its corresponding index
"""
name = "Carolina"
for counter, element in enumerate(name, start=1):
    print('{}. {}'.format(counter,element))

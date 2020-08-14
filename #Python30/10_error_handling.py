"""
Use try/except to catch an error, you can try to validate
what happens when we do
my_list = ["a", "b", "c"]
print(my_list[10])
"""
print('\n-------------------------------\n1)')
my_list = ["a", "b", "c"]
try:
    print(my_list[10])
except IndexError as err:
    print("An exception ocurred:", err)

"""
Cause an exception to be raised using the raise keyword and
print a message after you have finished catching the error
at finally.
"""
print('\n-------------------------------\n2)')
try:
  five_digits = "Helloooo"
  num = five_digits.isnumeric()
  if not five_digits.isnumeric() or len(five_digits)!=5:
    raise ValueError(f"{five_digits}: is not a valid code \n\nAnyway ...") 
except ValueError as err:
  print(err)
finally:
  print("Welcome to the game!")

"""
Use input function to request information to the user and in
the try/except structure catches multiple errors that can be
generated
"""
print('\n-------------------------------\n3)')
print('Enter the numerator:')
numerator = input()
print('Enter the denominator:')
denominator = input()

try:
  division = float(numerator) / float(denominator) 
  print('numerator / denominator = {}'.format(division))
except (ZeroDivisionError, ValueError) as err:
  print("An exception ocurred:", err)
finally:
  print('Thank you for participating!')
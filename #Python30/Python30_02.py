"""
Generate a sequence using the function range that
returns the following.
[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0,
10, 20, 30, 40, 50, 60, 70, 80, 90]
"""
print(list(range(-100,91,10)))

"""
Generate the previous sequence but in this case in
the opposite way.
"""
print(list(range(90,-101,-10)))

"""
This challenge can be a bit difficult, try to create a
function that returns a sequence of decimal numbers between
2 numbers, incremental only.
Here's a hint, use the while statement
"""

def floating_range(start, stop, step):
    
    element = start
    elements = [element]
    while element < stop-step:
        element = element + step
        element = round(element,2)
        elements.append(element) 

    return(elements)

print(floating_range(5, 10, 0.5))
print(floating_range(12, 15, 0.2))

"""
Create a class called Pizza that allows you to create different
types of them. When you create them, give them the price of the
pizza.
The class should calculate the size of the pizza based on the
price.
0 - 10 small
11 - 20 medium
21 - 30 large
"""

class Pizza:

    def __init__(self, ingredients, price):
        self.price = price    
        self.ingredients = ingredients
        self.size = self.calculate_size(price)

    @classmethod 
    def flavor_vegetarian(cls,price):
        ingredients = ['tomato', 'cheese', 'onion', 'mushrooms']
        return cls(ingredients, price)

    @classmethod 
    def flavor_chicken_mushrooms(cls,price):
        ingredients = ['cheese', 'chiken', 'mushrooms']
        return cls(ingredients, price)


    @staticmethod
    def calculate_size(price):
        if 0 <= price <= 10:
            size = 'small'
        elif 11 <= price <= 20:
            size = 'medium'
        elif price > 21:
            size = 'large'
        
        return size

vegetarian_pizza = Pizza.flavor_vegetarian(15)
print(vegetarian_pizza.size)
print(vegetarian_pizza.ingredients)

chicken_mushrooms_pizza = Pizza.flavor_chicken_mushrooms(25)
print(chicken_mushrooms_pizza.size)
print(chicken_mushrooms_pizza.ingredients)

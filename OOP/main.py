# import basic
# item = basic.items() # way to import a class from a file
'''
import will also run the progam basic.py
'''
import csv

class Item:
        
        discount = 20 # This is a class attribute as it is available for all for whole class
        all = []
        def __init__(self, name = 'Toy', price = 0, quantity = 0):
            assert price >= 0
            assert quantity >= 0
            self.name = name
            self.price = price
            self.quantity = quantity
            Item.all.append(self)

        def total_price(self):
            return self.quantity * self.price * (1 - self.discount/100)
        
        @classmethod # Classmethod can only be called from class. @<decorator>
        def from_csv(cls):
            with open('OOP/items.csv', 'r') as file:
                content = csv.DictReader(file) # arranging content as dictionary
                items = list(content) # making list of dictioary
                for item in items:
                    Item(
                        name = str(item.get('name')),
                        price = float(item.get('price')),
                        quantity = int(item.get('quantity')) 
                    )

        # StaticMethod makes a function instead of method. num is a parameter here instead of instace
        @staticmethod
        def is_integer(num):
            if isinstance(num, float): # Checks any new instance if it is float
                return num.is_integer() # if num is float it will check
            elif isinstance(num, int):
                return True
            else:
                return False
        def __repr__(self):
            # tells how to reprsent the informationin in print
            return f"Item({self.name}, {self.price}, {self.quantity})"


Item.from_csv()
'''
used CSV file for the data
item1 = item('Phone', 100, 1 )
item2 = item('Laptop', 1000, 2)
item3 = item('Keyboard', 10, 5)
item4 = item('Cable', 15, 10)
item5 = item('Mouse', 5, 8)
'''
print(Item.all)
print(Item.is_integer(7))


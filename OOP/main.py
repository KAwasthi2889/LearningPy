# import basic
# item = basic.items() # way to import a class from a file
'''
import will also run the progam basic.py
'''

class item:
        
        discount = 20 # This is a class attribute as it is available for all for whole class
        all = []
        def __init__(self, name = 'Toy', price = 0, quantity = 0):
            assert price >= 0
            assert quantity >= 0
            self.name = name
            self.price = price
            self.quantity = quantity
            item.all.append(self)

        def total_price(self):
            return self.quantity * self.price * (1 - self.discount/100)
        
        def __repr__(self):
            # tells how to reprsent the informationin in print
            return f"Item({self.name}, {self.price}, {self.quantity})"


item1 = item('Phone', 100, 1 )
item2 = item('Laptop', 1000, 2)
item3 = item('Keyboard', 10, 5)
item4 = item('Cable', 15, 10)
item5 = item('Mouse', 5, 8)

print(item.all)




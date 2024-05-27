class product:
    def total_product_price(self):
        return self.quantitiy * self.price
'''
we can also do
total_product_price(self, x, y):
return x * y 
and write 
item1.total_product_price(self, product.quantitiy, product.price)
'''
item1 = product()
item1.name = 'Phone'
item1.price = 100
item1.quantitiy = 10
print(item1.total_product_price())



item2 = product()
item2.name = 'Laptop'
item2.price = 1000
item2.quantitiy = 4
print(item2.total_product_price())



class items:
        
        discount = 20 # This is a class attribute as it is available for all for whole class
        all = []
        def __init__(self, name = 'Toy', price = 0, quantity = 0): # Here I have set default parameters that will execute if not assigned
# __init__ is a constructor is mainly used to store the parameters assigned
            assert price >= 0 # checks the condition before running
            assert quantity >= 0 , 'This is the message for assertion error for Laptop'
            self.name = name
            self.price = price
            self.quantity = quantity
            items.all.append(self) # all the instances are saved in all list

        def total_price(self):
            return self.quantity * self.price * (1 - self.discount/100)



item3 = items('Phone', 100, 10)
item4 = items('Laptop', 1000, 4)
print(f"The price of a single {item3.name} is ${item3.price} while the total for {item3.quantity} peices is ${item3.total_price()}")
print(f"The price of a single {item4.name} is ${item4.price} while the total for {item4.quantity} peices is ${item4.total_price()}")
item3.discount = 30 # at first it searches for discount at instance level, since it dosent find it there it goes for class level
print(item3.total_price())


item5 = items()
print(item5.name) # Toy
item4.has_numpad = 'True' # Assigned a new attribute unique to Laptop



print(items.discount) #Class attribute can be called by both, class and object
print(item4.discount)



# __dict__ calls all the attributes on same level
print(items.__dict__) # All the Class attribute can be shown here as dictionary
print(item4.__dict__) # All the Instance attributes are shown here as dictionary



print(items.all) # 5 instances are created with memory locations
# call all the names of instances
for instances in items.all:
    print(instances.name, end = ' ')
print()
# 1. Student Class – __str__() Create a Student class with name, roll_no, and marks. 
# Implement __str__() so that printing the 

class Student:
   def __init__(self,name,roll_no,marks):
      self.name=name
      self.roll_no=roll_no
      self.marks=marks

   def __str__(self):
       return f"Name:{self.name},Roll no{self.roll_no},marks{self.marks}"
   
student1=Student("sarthak", 88, 76)
print(student1)

# 2. Product Class – __eq__() Create a Product class with name and price. Implement __eq__() 
# to check whether two products have the same price. 

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __eq__(self, value):
        return self.price==value.price
    
product1=Product("pen",20)
product2=Product("pencil",20)

print(product1==product2)
   
   
   
# 3. Shopping Cart – __len__() Create a ShoppingCart class containing a list of products. 
# Implement __len__() so that len(cart) returns the number of products in the cart. 

class shoping:
    def __init__(self,product):
        self.product=product
    
    def __len__(self):
        return len(self.product)
    
product=shoping("sdfghjk")
print(len(product))


# 4. Bank Account – __str__() Create a BankAccount class with account holder name, account number,
# and balance. Implement __str__() to display account information when the object is printed.

class BankAccount:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance

    def __str__(self):
        return f"Account Holder Name{self.name},Account Number{self.number},Balance{self.balance}"
    
information=BankAccount("Gagandip pathare",1247500332,5000)
print(information)


# 5. Number Class – __add__() Create a Number class that stores one number.
# Implement __add__() so that two objects can be added 

class Number:
    def __init__(self,number):
        self.number=number

    def __add__(self, other):
        return self.number +other.number
    
num1=Number(20)
num2=Number(20)

print(num1+num2)


# 6. Create a Number class and implement: __add__()  __sub__()  
# __mul__()  __truediv__()  __mod__() 
        
        
class Number:
    def __init__(self,number):
        self.number=number

    def __add__(self, other):
        return self.number+other.number
    def __sub__(self, other):
        return self.number - other.number
    
    def __mul__(self, other):
        return self.number*other.number
    
    def __truediv__(self, other):
        return self.number/other.number
    
    def __mod__(self, other):
        return self.number% other.number
    
num1 = Number(20)
num2 = Number(10)

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
# 1. Create a Person parent class with name and age. Create a Student child class with roll_no and marks. 
# Use super() to initialize the parent attributes. 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,roll_no,marks):
        super().__init__(name,age)
        self.rollno=roll_no
        self.marks=marks
        
student1=Student("Gagandip",22,88,78)
print(student1.name)
print(student1.age)
print(student1.rollno)
print(student1.marks)

print()
# 2. Create a Vehicle parent class with a start() method. Create Car and Bike child classes and
# override the start() method with different behavior. 

class Vehicle:
    def Start(self):
        print("car is start")
        
class Car (Vehicle):
    def Start(self):
        print("car start with key")
        
class Bike(Vehicle):
    def Start(self):
        print("bike start ")
        
car=Car()
bike=Bike()
car.Start()
bike.Start()


# 3. Create an Employee parent class with name and salary. Create a Manager child class with an 
# additional department attribute. Display all details using constructors. 

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department

manager1=Manager("sarthak",50000,"Hr")
print(manager1.name)
print(manager1.salary)
print(manager1.department)


# 4. Create a BankAccount parent class with account_number and balance. Create a SavingsAccount child class 
# with an additional interest_rate. Use super() in the child constructor. 

class BankAccount:
    def __init__(self,account_number,balance):
        self.account=account_number
        self.balance=balance

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance,intrest_rate):
        super().__init__(account_number, balance)
        self.intrest=intrest_rate
        
bankaccount=SavingAccount(1247500332,850,5)
print(bankaccount.account)
print(bankaccount.balance)
print(bankaccount.intrest)

# 5. Create a Person parent class with a display() method. Create a Student child class that overrides 
# display() but also calls the parent display() using super()

class Company:

    def __init__(self, company_name):
        self.company = company_name

class Developer(Company):

    def __init__(self, company_name, programming_lang):
        super().__init__(company_name)
        self.programming = programming_lang

    def coding(self):
        print("coding")

class Tester(Company):

    def __init__(self, company_name, testing_tool):
        super().__init__(company_name)
        self.testing_tool = testing_tool

    def testing(self):
        print("testing")
developer1 = Developer("Infosys", "Python")
tester1 = Tester("Infosys", "Playwright")

print(developer1.company)
print(developer1.programming)
developer1.coding()

print(tester1.company)
print(tester1.testing_tool)
tester1.testing()


# 7. Bank Account
# Create a BankAccount class with a private attribute __balance. 
# Create get_balance() to view the balance. 
# Create set_balance() to update the balance only if the amount is valid.
# Create a withdraw() method with proper balance validation. 

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Withdraw ")
        else:
            print("no  balance in account")

account = BankAccount(5000)
print(account.get_balance())
account.set_balance(7000)
print(account.get_balance())
account.withdraw(2000)
print(account.get_balance())
account.withdraw(6000)


# 8. Student Marks
# Create a Student class with private attributes __name and __marks. 
# Create getter and setter methods for marks.  
# Allow marks only between 0 and 100.  
# Create a child class ExamStudent that inherits from Student 

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("no marks")


class ExamStudent(Student):

    def __init__(self, name, marks):
        super().__init__(name, marks)


student1 = ExamStudent("Gagan", 85)

print(student1.get_marks())
student1.set_marks(95)
print(student1.get_marks())

student1.set_marks(120)


# 9. Constructor + Private Data Create a User class with private __password. 
# Initialize it through the constructor.  
# Create get_password() and set_password().  
# Setter should update the password only if it contains at least 6 characters.

class User:

    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, password):
        if len(password) >= 6:
            self.__password = password
        else:
            print("Invalid password")


user1 = User("gagan123")

print(user1.get_password())

user1.set_password("python123")
print(user1.get_password())
user1.set_password("abc") 


# 10. Multilevel Inheritance + Getter/Setter
# Person → private age with getter/setter.  
# Employee → salary.  Manager → department.  Use super() at each level 

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


class Employee(Person):

    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary


class Manager(Employee):

    def __init__(self, age, salary, department):
        super().__init__(age, salary)
        self.department = department


manager1 = Manager(25, 50000, "IT")

print(manager1.get_age())
print(manager1.salary)
print(manager1.department)

manager1.set_age(30)
print(manager1.get_age())
# 1. Student Information System Create a Student class with: • name  • roll_no  • branch  • marks
# Create 3 student objects and 
# create a method display() to print their details. 

class Student:
    def __init__(self,name,roll_no,branch,marks):
        self.name=name
        self.roll_no=roll_no
        self.branch=branch
        self.marks=marks
        
    def display(self):
        print("Name:",self.name)
        print("roll_no:",self.roll_no)
        print("branch:",self.branch)
        print("marks",self.marks)
        print()
        
student1 = Student("Gagan", 101, "Computer", 85)
student2 =Student("sarthak",102,"python",86)
student3= Student("prathmesh",103,"java",88)
student4= Student("swapnil",104,"SQL",77)
student5= Student("Omkar",105,"Node js",89)

student1.display()
student2.display()
student3.display()
student4.display()
student5.display()



# 2. Employee Salary Create an Employee class with: • name  • employee_id  
# • salary  Create a method display_salary() that displays the employee's salary. 
# Create 3 employee objects. : Don't assign the values directly inside the class. 
# Pass them while creating objects. 

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display_salary(self):
        print("Employee_name",self.name)
        print("Employee_id",self.id)
        print("Employee_salary",self.salary)
        print()
        
employee1=Employee('Sarthak gite',234567,50000)
employee2=Employee("swapnil gandhale",234578,60000)
employee3=Employee("prathamesh bhagat",345677,80000)

employee1.display_salary()
employee2.display_salary()
employee3.display_salary()



# 3. Mobile Phone Create a Mobile class with: • brand  • model  • price  Create a method:
#     display_details() Create 3 mobile objects with different information. Expected concept: 
#         Constructor + objects.

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display_details(self):
        print("Brand Name:",self.brand)
        print("Model Name:",self.model)
        print("Mobile price:",self.price)
        print()
        
mobile1=Mobile("Samsung","A34",25000)
mobile2=Mobile("Vivo","X50",50000)
mobile3=Mobile("Iphone","17 pro",80000)

mobile1.display_details()
mobile2.display_details()
mobile3.display_details()
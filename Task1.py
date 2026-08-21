# 1. Create a Student Management System using Class and Object in Python. What to Do 
# 1. Create a class named Student.  
# 2. Create a constructor __init__() to initialize: 
#   o Student name  o Roll number  o Age  o Marks of 3 subjects 
#     3. Create a display_details() method to display all student information. 
#     4. Create a calculate_total() method to calculate the total marks.  
#     5. Create a calculate_percentage() method to calculate the percentage. 

#     6. Create a check_result() method:  o Student passes if marks 
#     in every subject are 35 or above.  o Otherwise, display FAIL. 

#     7. Create an update_marks() method to update the marks of a selected subject. 
class student:
    def __init__(self,name,roll,age,sub1,sub2,sub3):
        self.name=name
        self.roll = roll
        self.age=age
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    
    
    def display(self):
        print("student name is :",self.name)
        print("student roll no :",self.roll)
        print("student age is :",self.age)
        print("student sub1 mark :",self.sub1)
        print("student sub2 mark :", self.sub2)
        print("student sub3 mark :", self.sub3)
        print()
        
    
    def calculate_total(self):
        # print("total marks is :",self.sub1 + self.sub2 + self.sub3)
        # print()
        total = self.sub1 + self.sub2 + self.sub3
        print("Total Marks:", total)
        return total
        
    
    def calculate_percentage(self):
        total = self.sub1 + self.sub2 + self.sub3
        percentage = (total / 300) * 100
        print("your percentage",percentage)
        return percentage
        
    
    def check_result(self):
        # if self.sub1 >= 35:
        #     print("subject one pass")
        # else:
        #     self.sub1
        #     print("subject 1 is fail")
        
        # if self.sub2 >= 35:
        #     print("subject 2 pass")
            
        # else:
        #     self.sub2
        #     print("sub 2 is fail")
            
        # if self.sub3 >= 35:
        #     print("subject 3 pass")
        # else:
        #     self.sub3
        #     print("subject 3 fail")
        
        if self.sub1 >= 35 and self.sub2 >= 35 and self.sub3 >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")
    
    def update_mark(self,subject, marks):        
        # self.sub1 = s1
        # self.sub2 = s2
        # self.sub3 = s3
        # self.display()
        # self.calculate_total()
        # self.calculate_percentage()
        if subject==1:
            self.sub1=marks
          
        elif subject == 2:
            self.sub2 = marks
            
        elif subject==3:
            self.sub3=marks
        else:
            print("Invalid subject")
            print("marks update successfully")

    
obj1 = student("demo",55,60,4,22,22)
obj1.display()
obj1.calculate_total()
obj1.calculate_percentage()
obj1.check_result()
obj1.update_mark(3,22)

obj1.display()
obj1.calculate_total()
obj1.calculate_percentage()
obj1.check_result()

print()
print()

# 2. Create a Library Management System using Class and Object in Python.
# What to Do 1. Create a class named Book.  2. Create a constructor __init__() to initialize: 
# o Book name  o Book ID  o Author name  o Availability status  
# 3. Create a display_book() method to display book details. 
# 4. Create a issue_book() method:  o Check whether the book is available.  
# o If available, issue the book and change its status.  o If already issued, display an appropriate message.  
# 5. Create a return_book() method:  o Return the issued book.  o Change its availability status back to available. 
# 6. Create a check_availability() method to display whether the book is available or issued. 

class Book:
    def __init__(self,name,Id,author,status):
        self.name=name
        self.id= Id
        self.author=author
        self.status=status

    def display_book(self):
        print("Name of book:",self.name)
        print("Book Id number:",self.id)
        print("Author name:",self.author)
        print("Availability status:",self.status)
        
    def issue_book(self): 
     if self.status == True: 
        print("book is available") 
        self.status == False 
        print("book issue") 
     else: 
        print("Book is already issue")
                
    def return_book(self):
        if self.status==False:
            self.status==True
            print('book return succefully')
        else:
            print("book is not available")
        
obj2 = Book("end is the beginning",1234,"kusumagrah",True)
obj2.display_book()
obj2.issue_book()
obj2.return_book()

print()
print()



# 3. Create a simple Employee Management System using Class and Object in Python. What to Do 
# 1. Create a class named Employee.  2. Create a constructor __init__() to initialize: 
#     o Employee name  o Employee ID  o Department  o Basic salary  3. Create a display_details()
#     method to display employee information.  4. Create a calculate_salary() method:  o Add a fixed 
#     bonus of ₹5,000.  o Calculate and display the final salary.  5. Create a check_salary() method:
#         o If salary is ₹30,000 or above, display "Good Salary".  o Otherwise, display "Average Salary".
#         6. Create a menu-driven program:  o 1 → Display Details  o 2 → Calculate Salary 
#         o 3 → Check Salary  o 4 → Exit 

print()
print()

class Employee:
    def __init__(self,name,id,department,salary):
        self.name=name
        self.id=id
        self.department=department
        self.salary=salary
    
    def menu(self):
        choice = int(input("Enter your choice"))

        if choice==1:
            obj1.display_details()
    
        elif choice==2:
            obj1.calculate_salary()

        elif choice==3:
            obj1.check_salary()
    
        elif choice ==4:
            print("Exist")
        else:
            print("no choice option")
    

    def display_details(self):
        print("Employee Name:",self.name)
        print("Employee Id:",self.id)
        print("Department :",self.department)
        print("Basic salary:",self.salary)
        self.menu()
        
    def calculate_salary(self):
        final_salary=self.salary+5000
        print("final salary:",final_salary)
        self.menu()
        
    def check_salary(self):
        if self.salary>=30000:
            print("Good salary")
        else:
            print("average salary")
        self.menu()
        
obj1=Employee("Gagandip pathare",123456,"Hr",30000)
obj1.menu()

# obj1.display_details()
# obj1.calculate_salary()
# obj1.check_salary()


    

    

        






 
 
 
 
 
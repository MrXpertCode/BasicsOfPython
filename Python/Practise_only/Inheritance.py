# Single inheritance

class Employee:
    company = 'Google'

    def __init__(self , name):
        self.name = name

    def ShowDetails(self):
        print(f"Name is {self.name} and company is {Employee.company}")

# Boss class inhertate attributes and methods of Employee class
class Boss(Employee):
    # Overwriting attribute of class 'Employee'
    company = 'Apple'

    def info(self):
        print('Hello I am Boss')
 # Overwriting method of class 'ShowDetails'

    def ShowDetails(self):
        print("I have succssfully overwritten")

e = Employee('Sujan')
e.ShowDetails()


b = Boss('Samar')
b.ShowDetails()
print(b.company)
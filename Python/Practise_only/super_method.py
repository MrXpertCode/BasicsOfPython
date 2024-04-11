class Person:
    country = 'Nepal'
    
    def __init__(self):
        print("Intialize Person..\n")
    

    def TakeBreath(self):
        print("I am breathing\n")
    
class Employee(Person):
    company = 'Honda'

    def __init__(self):
        super().__init__()
        print("Intialze Employee..\n")

    def GetSalary(self):
        print(f'salary is {self.salary}')

    def TakeBreath(self):
        super().TakeBreath()
        print('I am Employee so I am luckily breathing\n')

class Programmer(Employee):
    company = 'Google'

    def __init__(self):
        super().__init__()
        print("Intialze person..\n")
    
    def GetSalary(self):
        super().TakeBreath()
        print("I am Programmer so I don't get salary++..\n")


pr = Programmer()



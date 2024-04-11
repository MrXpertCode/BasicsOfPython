class Person:
    country = 'Nepal'

    def TakeBreath(self):
        print("I am breathing")
    
class Employee(Person):
    company = 'Honda'

    def GetSalary(self):
        print(f'salary is {self.salary}')

    def TakeBreath(self):
        print('I am Employee so I am luckily breathing')

class Programmer(Employee):
    company = 'Google'

    def GetSalary(self):
        print("I am Programmer so I don't get salary++..")

p = Person()
e = Employee()
pr = Programmer()

pr.GetSalary()
# print(p.company) # Throws error
pr.TakeBreath()
print(pr.country)
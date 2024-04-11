class Employee:
    company = 'Apple'

    def show(self):
        print(f"Name is {self.name}, Comapany is {self.company}")

    @classmethod
    def changeClass(cls , newCompany):
        cls.company = newCompany

e = Employee()
e.name = 'Sujan'

e.show()
e.changeClass("Tesla")
e.show()

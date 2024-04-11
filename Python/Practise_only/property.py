class Employee:
    salary = 5000
    salaryBonus = 1000
    
    @property
    def TotalSalary(self):
        return self.salary + self.salaryBonus
    
    @TotalSalary.setter
    def TotalSalary(self , ChangeSalary):
         self.salary = ChangeSalary - self.salaryBonus



e = Employee()
print(e.TotalSalary)
print(e.salary)
e.TotalSalary = 5000
print(e.salary)
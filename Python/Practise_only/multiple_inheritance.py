# Multiple Inheritance

class Father:
    skin = 'Brown'
    level = 0

    def Addlevel(self):
        self.level = self.level + 1


class Mother:
    skin = 'White'

class Child(Father , Mother):
    pass

c = Child()
print(c.level)
c.Addlevel()
print(c.level)
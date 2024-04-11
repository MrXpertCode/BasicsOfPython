class Number:
    def __init__(self , num):
        self.num = num

    def __add__(self , num2):
        print("Let's add")
        print(self.num + num2.num)

n1 = Number(5)
n2 = Number(6)

n1 + n2

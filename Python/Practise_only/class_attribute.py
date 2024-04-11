class Item:

    def __init__(self , name:str , price : float , quanitity=0):


        # Ensuring that price and quantity should be greater or equall to zero
        assert price >= 0 ,f"Price should be greater or equall to zero you give-->{price}"
        assert quanitity >=0,f"Quantity should be greater or equall to zero you give-->{quanitity}"

        # Assigning object attribute
        self.name = name
        self.price = price
        self.quantity = quanitity

    # Calculating Total Price
    def totalPrice(self):
        return self.price * self.quantity
    
    

item1 = Item('I-phone' , 100 , 5)
print(item1.totalPrice())










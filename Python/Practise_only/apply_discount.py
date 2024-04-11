class Item:
    pay_rate = 0.8
    def __init__(self , name: str, quantity: float, price = 0 ):

        #Validating the arguments
        assert quantity >=0 , f"{quantity} quantity is not greater or equall to zero "
        assert price >=0 ,    f"{price} price is not greater or equall to zero "

        self.name = name
        self.quantity = quantity
        self.price = price

        # Calculating Total price
    def totalPrice(self):
            return self.quantity * self.price


phone = Item('I-phone' , 5 , 10 )
laptop = Item('Asus' ,10 , 10)

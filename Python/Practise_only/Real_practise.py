class Item:
    pay_rate = 0.8
    all = []
    def __init__(self , name: str, price: float, quantity = 0):
        
        assert price > 0, f"Price should be greater than zero, your input is {price}"
        assert quantity > 0, f"quantity should be greater than zero, your input is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def totalPrice(self):
        return self.price * self.quantity 
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    # Represents string for objects
    def __repr__(self):
        return f"(Item '{self.name}' ,'{self.price}' ,'{self.quantity}')"
    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
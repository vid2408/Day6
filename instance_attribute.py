class Monitor:
    def __init__(self, model, resolution, screensize, price):
        self.model = model
        self.resolution = resolution
        self.screensize = screensize
        self.price = price

    def getPrice(self):
        return f"This monitor has a price of {self.price}"

    def setDiscount(self, amount):
        self._discount = amount 

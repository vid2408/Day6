class Monitor:
    def __init__(self, model, resolution, screensize, price):
        self.model = model
        self.resolution = resolution
        self.screensize = screensize
        self.price = price

    def getPrice(self):
        return f"This monitor has a price of {self.price}"


monitor1 = Monitor("Samsung", "1920 x 1080", "24 inch", 129.99)
monitor2 = Monitor("Viewsonic", "1920 x 1080", "24 inch", 109.99)
monitor3 = Monitor("Dell", "1920 x 1080", "27 inch", 159.99)

print(monitor2.getPrice()) 

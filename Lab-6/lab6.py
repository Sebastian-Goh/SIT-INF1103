class product:
    def __init__(self, productid, name, price, stock):
        self.productid = productid
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
from Order import Order

class Orderdetails(Order):

    def __init__(self,customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode,
                 product_name,quantity,price,weight):

        super().__init__(customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode)

        self._product_name = product_name
        self._quantity = quantity
        self._price = price
        self._weight = weight

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
            self._price = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
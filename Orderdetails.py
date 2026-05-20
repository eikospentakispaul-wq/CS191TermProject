from Order import Order


class Orderdetails(Order):

    def __init__(self,customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode,address,
            product_name,quantity,price,weight):

        super().__init__(customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode,
                         address)

        self._product_name = product_name
        self._quantity = quantity
        self._price = price





    @property
    def product_name(self):
        return self._product_name

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price






    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @price.setter
    def price(self, value):
        self._price = value






    def to_dict(self):

        return {

            "Customer_ID": self.customer_ID,
            "Name": self.name,
            "Surname": self.surname,
            "Mail": self.mail,
            "Phone number": self.phonenumber,

            "Order_ID": self.order_ID,
            "City": self.city,
            "Country": self.country,
            "Zipcode": self.zipcode,
            "Address": self.address,

            "Product": self.product_name,
            "Quantity": self.quantity,
            "Price": self.price,

        }
class Orderdetails(Order):

    def __init__(self,
                 customer_ID,
                 name,
                 surname,
                 mail,
                 phonenumber,
                 order_ID,
                 city,
                 country,
                 zipcode,
                 product_name,
                 quantity,
                 price,
                 status):
        super().__init__(
            customer_ID,
            name,
            surname,
            mail,
            phonenumber,
            order_ID,
            city,
            country,
            zipcode
        )

        self._product_name = product_name
        self._quantity = quantity
        self._price = price
        self._status = status


from Customer import Customer
#

class Order(Customer):

    def __init__(
            self,
            customer_ID,
            name,
            surname,
            mail,
            phonenumber,
            order_ID,
            city,
            country,
            zipcode
    ):

        super().__init__(
            customer_ID,
            name,
            surname,
            mail,
            phonenumber
        )

        self._order_ID = order_ID
        self._city = city
        self._country = country
        self._zipcode = zipcode




    @property
    def order_ID(self):
        return self._order_ID

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @property
    def zipcode(self):
        return self._zipcode




    @order_ID.setter
    def order_ID(self, value):
        self._order_ID = value

    @city.setter
    def city(self, value):
        self._city = value

    @country.setter
    def country(self, value):
        self._country = value

    @zipcode.setter
    def zipcode(self, value):
        self._zipcode = value




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
            "Zipcode": self.zipcode
        }
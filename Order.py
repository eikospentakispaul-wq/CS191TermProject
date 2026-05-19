from Customer import Customer

class Order(Customer):

    def __init__(self, customer_ID, name, surname, mail,
                 phonenumber, order_ID, city, country, zipcode):

        super().__init__(customer_ID, name, surname, mail, phonenumber)

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
    def order_ID(self, order_ID):
        self._order_ID = order_ID

    @city.setter
    def city(self, city):
        self._city = city

    @country.setter
    def country(self, country):
        self._country = country

    @zipcode.setter
    def zipcode(self, zipcode):
        self._zipcode = zipcode

    def to_dict(self):
        return {
            "Customer_ID" : self._customer_ID,
            "Order_ID": self._order_ID,
            "City": self._city,
            "Country": self._country,
            "Zipcode": self._zipcode
        }
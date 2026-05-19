class Customer:

    def __init__(self,customer_ID,name,surname,mail,phonenumber):
        self._customer_ID = customer_ID
        self._name = name
        self._surname = surname
        self._mail = mail
        self._phonenumber = phonenumber

    @property
    def customer_ID(self):
        return self._customer_ID

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def mail(self):
        return self._mail

    @property
    def phonenumber(self):
        return self._phonenumber

    @name.setter
    def name(self,value ):
        self._name = value

    @surname.setter
    def surname(self,value):
        self._surname = value

    @mail.setter
    def mail(self,value):
        self._mail = value

    @phonenumber.setter
    def phonenumber(self,value):
        self._phonenumber = value

    def to_dict(self):
        return {
            "Customer_ID": self._customer_ID,
            "Name": self._name,
            "Surname": self._surname,
            "Mail": self._mail,
            "Phone number": self._phonenumber
        }
from Customer import Customer
from Orderdetails import Orderdetails
import json
import os

Apple_products = {
    "iphone 6": 300, "iphone 6 plus": 350, "iphone 6s": 400, "iphone 6s plus": 450, "iphone 7": 500, "iphone 7 plus": 550, "iphone 8": 600, "iphone 8 plus": 650,
    "iphone x": 700, "iphone xr": 750, "iphone xs": 800, "iphone xs max": 850, "iphone 11": 900, "iphone 11 pro": 1000, "iphone 11 pro max": 1100, "iphone 12 mini": 850,
    "iphone 12": 950, "iphone 12 pro": 1150, "iphone 12 pro max": 1300, "iphone 13 mini": 900, "iphone 13": 1000, "iphone 13 pro": 1200, "iphone 13 pro max": 1400, "iphone 14": 1100,
    "iphone 14 plus": 1200, "iphone 14 pro": 1400, "iphone 14 pro max": 1600, "iphone 15": 1200, "iphone 15 plus": 1300, "iphone 15 pro": 1500, "iphone 15 pro max": 1700, "iphone 16": 1300,
    "iphone 16 plus": 1400, "iphone 16 pro": 1600, "iphone 16 pro max": 1800, "iphone se 2020": 500, "iphone se 2022": 600, "ipad mini 4": 400, "ipad mini 5": 500, "ipad mini 6": 650,
    "ipad 7": 450, "ipad 8": 500, "ipad 9": 550, "ipad 10": 650, "ipad air 3": 700, "ipad air 4": 800, "ipad air 5": 900, "ipad pro 10.5": 850,
    "macbook pro 13 intel": 1500, "macbook pro 13 m1": 1700, "macbook pro 14 m1": 2200, "macbook pro 14 m2": 2500, "macbook pro 16 m1": 3000, "macbook pro 16 m2": 3500, "imac 21.5": 1300, "imac 24 m1": 1800,
    "mac mini intel": 900, "mac mini m1": 1100, "mac mini m2": 1300, "mac studio m1 max": 2500, "mac studio m1 ultra": 4000, "mac pro intel": 6000, "mac pro m2 ultra": 8000, "apple watch series 3": 250,
    "apple watch series 4": 300, "apple watch series 5": 350, "apple watch series 6": 400, "apple watch series 7": 500, "apple watch series 8": 600, "apple watch series 9": 700, "apple watch ultra": 1000, "apple watch ultra 2": 1200,
    "airpods 1": 120, "airpods 2": 180, "airpods 3": 250, "airpods pro 1": 320, "airpods pro 2": 380, "airpods max": 700, "homepod mini": 150, "homepod 1": 350,
    "homepod 2": 450, "apple tv hd": 200, "apple tv 4k 1st gen": 250, "apple tv 4k 2nd gen": 300, "apple tv 4k 3rd gen": 350, "magic mouse 1": 80, "magic mouse 2": 120, "magic keyboard 1": 100,
    "magic keyboard 2": 150, "magic trackpad 1": 100, "magic trackpad 2": 180, "pro display xdr": 6000, "studio display": 1800, "beats solo 3": 250, "beats studio 3": 350, "beats fit pro": 300,
    "beats studio pro": 450, "ipod touch 6": 250, "ipod touch 7": 350, "ipod nano 7": 200, "ipod shuffle 4": 120
}
#products_list = list(Apple_products.items())
#sorted_products = sorted(Apple_products.items(), key=lambda x: x[1])

#for product, price in sorted_products:
    #print(f"{product}: ${price}")


Customer_list = []

if os.path.exists("Customer_data.json"):

    with open("Customer_data.json", "r") as file:

        try:

            existing_data = json.load(file)

            for item in existing_data:

                Customer_list.append(

                    Customer(
                        item["Customer_ID"],
                        item["Name"],
                        item["Surname"],
                        item["Mail"],
                        item["Phone number"]
                    )
                )

        except json.JSONDecodeError:
            pass


#

Order_list = []

if os.path.exists("Order_data.json"):

    with open("Order_data.json", "r") as file:

        try:

            existing_data = json.load(file)

            for item in existing_data:

                Order_list.append(

                    Orderdetails(

                        item["Customer_ID"],
                        item["Name"],
                        item["Surname"],
                        item["Mail"],
                        item["Phone number"],

                        item["Order_ID"],
                        item["City"],
                        item["Country"],
                        item["Zipcode"],
                        item["Address"],

                        item["Product"],
                        item["Quantity"],
                        item["Price"],

                    )
                )

        except json.JSONDecodeError:
            pass


print("------ E-SHOP DATABASE ------\n")


Decision = int(
    input("How many customers would you like to save data for? : ")
)


###

for i in range(Decision):

    while True:

        try:

            customer_ID = input("Enter customer ID : ").strip()

            if not customer_ID.isdigit():
                raise ValueError(
                    "Customer ID must contain only numbers."
                )

            name = input("Name : ").strip()

            if not name.isalpha():
                raise ValueError(
                    "Name must contain only letters."
                )

            surname = input("Surname : ").strip()

            if not surname.isalpha():
                raise ValueError(
                    "Surname must contain only letters."
                )

            mail = input("Mail : ").strip()

            if "@" not in mail or "." not in mail:
                raise ValueError(
                    "Invalid email format."
                )

            phonenumber = input("Phone number : ").strip()

            if not phonenumber.isdigit():
                raise ValueError(
                    "Phone number must contain only digits."
                )


            c = Customer(customer_ID,name,surname,mail,phonenumber)


            Customer_list.append(c)


            customer_data = [
                x.to_dict() for x in Customer_list
            ]

            with open("Customer_data.json", "w") as file:

                json.dump(
                    customer_data,
                    file,
                    indent=4
                )

            print("\nCustomer added successfully.\n")

            break

        except ValueError as e:

            print(f"\nError: {e}\n")


print()






for i in range(Decision):

    while True:

        try:



            order_ID = input(
                "Enter order ID : "
            ).strip()

            if not order_ID.isdigit():
                raise ValueError(
                    "Order ID must contain only numbers."
                )

            country = input(
                "Country : "
            ).strip()

            if not country.isalpha():
                raise ValueError(
                    "Country must contain only letters."
                )

            city = input(
                "City : "
            ).strip()

            if not city.isalpha():
                raise ValueError(
                    "City must contain only letters."
                )

            zipcode = input(
                "Zip code : "
            ).strip()

            if not zipcode.isdigit():
                raise ValueError(
                    "Zip code must contain only numbers."
                )

            address = input(
                "Address : "
            ).strip()

            if not address.isalpha():
                raise ValueError(
                    "Address must contain only letters."
                )

            quantity = int(input(
                "Quantity : "
            ).strip())

            if quantity <= 0:
                raise ValueError(
                    "Quantity must be greater than 0."
                )

            price = 0
            product_name = " "

            for i in range(quantity):

                product_name = input(
                    "Product name : "
                ).strip().casefold()

                if product_name not in Apple_products:
                    raise ValueError(
                        "Product does not exist."
                    )


                price += Apple_products[product_name]








            od = Orderdetails(customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode,address,product_name,
                quantity,price)



            Order_list.append(od)


            order_data = [
                x.to_dict() for x in Order_list
            ]

            with open("Order_data.json", "w") as file:

                json.dump(
                    order_data,
                    file,
                    indent=4
                )

            print("\nOrder added successfully.\n")

            break

        except ValueError as e:

            print(f"\nError: {e}\n")
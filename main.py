from Customer import Customer
from Orderdetails import Orderdetails
import json
import os

product = {
    "MackBook Air M1" : "900$",
    "MacBook Air M2" : "1000$",
    "MackBook Air M3" : "1200$",
    "MackBook Air M4" : "1400$",
    "MackBook Pro" : "2000$",
    "iPad" : "800$",
    "iPad Pro" : "1000$",
    "iPhone 15" : "1000$",
    "iPhone 15 Pro" : "1200$",
    "iPhone 16" : "1200$",
    "iPhone 16 Pro" : "1400$",
    "iPhone 17" : "1600$",
    "iPhone 17 Pro" : "1200$",
 }


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
                        item["Weight"]
                    )
                )

        except json.JSONDecodeError:
            pass


print("------ COURIER DATABASE ------\n")


Decision = int(
    input("How many customers would you like to save data for? : ")
)




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

            customer_ID = input(
                "Enter customer ID : "
            ).strip()

            if not customer_ID.isdigit():
                raise ValueError(
                    "Customer ID must contain only numbers."
                )

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

            product_name = input(
                "Product name : "
            ).strip()

            if not product_name.isalpha():
                raise ValueError(
                    "Product name must contain only letters."
                )

            quantity = input(
                "Quantity : "
            ).strip()

            if not quantity.isdigit():
                raise ValueError(
                    "Quantity must contain only numbers."
                )

            price = input(
                "Price : "
            ).strip()

            if not price.isdigit():
                raise ValueError(
                    "Price must contain only numbers."
                )

            weight = input(
                "Weight : "
            ).strip()

            if not weight.isdigit():
                raise ValueError(
                    "Weight must contain only numbers."
                )


            od = Orderdetails(customer_ID,name,surname,mail,phonenumber,order_ID,city,country,zipcode,address,product_name,
                quantity,price,weight)



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
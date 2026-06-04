import matplotlib.pyplot as plt

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



products_list = list(Apple_products.items())
sorted_products = sorted(Apple_products.items(), key=lambda x: x[1])


def show_price_chart():
    # This function uses Matplotlib to display the 10 most expensive products.
    most_expensive_products = sorted(
        Apple_products.items(),
        key=lambda product: product[1],
        reverse=True
    )[:10]

    product_names = [product[0].title() for product in most_expensive_products]
    product_prices = [product[1] for product in most_expensive_products]

    plt.figure(figsize=(12, 6))
    plt.bar(product_names, product_prices)
    plt.title("Top 10 Most Expensive Apple Products")
    plt.xlabel("Product")
    plt.ylabel("Price (€)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("product_price_chart.png")
    print("Chart saved as product_price_chart.png")
    plt.show()


print("--------E-SHOP WAREHOUSE--------")

print("Choice 1 -products-")
print("Choice 2 -products sorted from lowest to highest-")
print("Choice 3 -Search products in warehouse-")
print("Choice 4 -Show product price chart-")
print("Choice 5 -Exit-")
print()


while True:
    choice = int(input())

    if choice == 1:
        for product,price in products_list:
            print(f'{product}: {price}')
    elif choice == 2:
        for product,price in sorted_products:
            print(f'{product}: {price}')
    elif choice == 3:
        search = input("Enter product name to search: ").lower()
        found = False

        for product, price in Apple_products.items():
            if search in product:
                print(f"{product}: {price}€")
                found = True

        if not found:
            print("No matching products found.")
    elif choice == 4:
        show_price_chart()
    elif choice == 5:
        print("You have exited the digital warehouse.")
        break
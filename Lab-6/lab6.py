import json


class product:
    def __init__(self, productid, name, price, stock):
        self._productid = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock += quantity

    def display_information(self):
        print(f"Product ID: {self._productid}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock} units")

    def to_dict(self):
        return {
            "id": self._productid,
            "item": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }


class inventory:
    def __init__(self, products):
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, productid):
        for product in self.__products:
            if int(product._productid) == int(productid):
                return product
        return None

    def display_inventory(self):
        for product in self.__products:
            product.display_information()
            print("-" * 20)


inventory_file = json.load(open("inventory.json", "r"))
inventory = inventory([])
for products in inventory_file:
    product_obj = product(products["id"], products["item"], products["price"], products["stock"])
    inventory.add_product(product_obj)

while True:
    print("\nInventory Management System")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.display_inventory()
    elif choice == "2":
        productid = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
        new_product = product(productid, name, price, stock)
        inventory.add_product(new_product)
        print(f"Product '{name}' added successfully.")
    elif choice == "3":
        productid = input("Enter product ID to update stock: ")
        product_to_update = inventory.search_product(productid)
        if product_to_update:
            quantity = int(input("Enter quantity to add (use negative for reduction): "))
            product_to_update.update_stock(quantity)
            print(f"Stock updated successfully for product ID '{productid}'.")
        else:
            print(f"Product with ID '{productid}' not found.")
    elif choice == "4":
        productid = input("Enter product ID to search: ")
        found_product = inventory.search_product(productid)
        if found_product:
            found_product.display_information()
        else:
            print(f"Product with ID '{productid}' not found.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

with open("inventory.json", "w") as f:
    json.dump([product.to_dict() for product in inventory._inventory__products], f, indent=4)
    

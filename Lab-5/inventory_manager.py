import json

def load_inventory_system():
    print("\n\n================================")
    print("Inventory Management System")
    print("================================")

    try:
        with open("inventory.json", "r") as json_file:
            inventory = json.load(json_file)
            print("Inventory loaded successfully.")
            return inventory
    except FileNotFoundError:
        print("No existing inventory found.")
        return {}

def save_inventory(inventory):
    with open("inventory.json", "w") as json_file:
        json.dump(inventory, json_file, indent=4)
    print("Inventory saved successfully.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"ID: {int(item['id'])}, Item: {item['item']}, Price: ${item['price']:.2f}, Stock: {item['stock']}")

def update_item(inventory):
    item_id = input("Enter item ID to update: ")
    if item_id not in [str(item['id']) for item in inventory]:
        print("Item ID not found.")
        return

    item_info = next(item for item in inventory if str(item['id']) == item_id)
    print(f"Current details - Item: {item_info['item']}, Price: ${item_info['price']:.2f}, Stock: {item_info['stock']}")

    new_name = input("Enter new item name (leave blank to keep current): ")
    new_price = input("Enter new item price (leave blank to keep current): ")
    new_stock = input("Enter new stock quantity (leave blank to keep current): ")

    if new_name:
        item_info['item'] = new_name
    if new_price:
        try:
            item_info['price'] = float(new_price)
        except ValueError:
            print("Invalid price input. Keeping current price.")
    if new_stock:
        try:
            item_info['stock'] = int(new_stock)
        except ValueError:
            print("Invalid stock input. Keeping current stock.")

    print(f"Item '{item_id}' updated successfully.")

def add_item(inventory):
    item_id = input("Enter item ID: ")
    if not any(item.get("id") == item_id for item in inventory):
        print("\nItem ID already exists. Please use a unique ID.")
        return

    item_name = input("Enter item name: ")
    try:
        item_price = float(input("Enter item price: "))
        item_stock = int(input("Enter item stock quantity: "))
    except ValueError:
        print("Invalid input for price or stock. Please enter numeric values.")
        return

    inventory.append({
        "item": item_name,
        "price": item_price,
        "stock": item_stock
    })
    print(f"Item '{item_name}' added successfully.")

def search_item(inventory):
    search_term = int(input("Enter item id to search: "))

    for item in inventory:
        if item["id"] == search_term:
            print("\nItem Found!")
            print(f"ID: {item["id"]}, Item: {item["item"]}, Price: {item["price"]}, Stock: {item["stock"]}")
            return

    print("\nItem not found!")
    

def exit_program(inventory):
    save_inventory(inventory)
    print("Exiting the program. Goodbye!")
    exit()

def display_menu():
    print("\nMenu:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Search Item")
    print("5. Save Inventory")
    print("6. Exit")


inventory = load_inventory_system()

while True:
    
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        view_inventory(inventory)
    elif choice == '2':
        add_item(inventory)
    elif choice == '3':
        update_item(inventory)
    elif choice == '4':
        search_item(inventory)
    elif choice == '5':
        save_inventory(inventory)
    elif choice == '6':
        exit_program(inventory)
    else:
        print("Invalid choice. Please select a valid option.")
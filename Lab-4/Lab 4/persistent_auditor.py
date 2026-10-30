def save_inventory(orders: list):
    with open("inventory.txt", "w") as file:
        file.write("Current Orders: \n\n")
        for i in range(len(orders)):
            file.write(f"{i+1}: {orders[i]}\n")

def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            print("\n\nLoading inventory from inventory.txt...")
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("No inventory found. Starting a new inventory.")

def get_valid_input(entry):
    if str(entry).isdigit() == False:
        if entry == "quit":
            return "quit"
        else:
            return "invalid"
    else:
        return entry

orders = []
item = ""
quantity = 0

while (True):
    item = input("Enter Item: ")
    quantity = input("Enter Quantity: ")
    status = get_valid_input(quantity)

    if status == "quit":
        break

    if status == "invalid":
        print("Invalid input. Please enter a valid quantity.")

        continue

    print("New Order Added: \n", f"{item}, {quantity}")
    orders.append(f"{item}, {quantity}")

save_inventory(orders)
print("Orders saved to inventory.txt")
load_inventory()
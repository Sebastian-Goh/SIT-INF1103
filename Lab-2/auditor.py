inventory = 0
user_input = 0

while(user_input != "quit"):
    user_input = input("Please key in stock value: ")
    if user_input.isdigit() == False:
        if user_input == "quit":
            break
        elif user_input.isdigit() == False:
            print("Please key in valid input.")
            continue
        else:
            print("Please key in valid input.")

    inventory += int(user_input)

    if inventory > 500:
        print("Overstock alert")
        break

print("Total Stock: ",inventory)
    
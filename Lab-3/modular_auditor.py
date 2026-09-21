# Defining Functions
def get_valid_input(entry):
    if str(entry).isdigit() == False:
        if entry == "quit":
            return "quit"
        else:
            return "invalid"
    else:
        return entry


def process_delivery(current_total, new_value):
    return (int(current_total) + int(new_value))


def calculate_tax(new_value):
    return int(new_value) * 0.1

def generate_report(total_units, failed_attempts):
    print("The total unit is: ", total_units)
    print("The failed attempts are: ", failed_attempts)

#main code
inventory = 0
total_units = 0
total_amount = 0
failed_attempts = 0
current_amount = 0
total_tax = 0

while(True):
    current_amount = input("What is the delivery amount: ")
    status = get_valid_input(current_amount)

    if status == "quit":
        break

    if status == "invalid":
        failed_attempts += 1
        total_units += 1

        continue
    else:
        total_units += 1

    total_amount = process_delivery(total_amount, status)

    total_tax += calculate_tax(status)

    generate_report(total_units, failed_attempts)

print("Total Amount: ", total_amount)
print("Total Tax: ", total_tax)
def get_valid_input(entry):
    if str(entry).isdigit() == False:
        if entry == "quit":
            return "quit"
        else:
            return "invalid"
    else:
        return entry


def process_delivery(current_total, new_value):
    return (current_total + new_value)


def calculate_tax(new_value):
    return new_value * 0.1

print(calculate_tax(79.5))
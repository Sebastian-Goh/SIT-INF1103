def get_valid_input(entry):
    if str(entry).isdigit() == False:
        if entry == "quit":
            return "quit"
        else:
            return "invalid"
    else:
        return entry


print(get_valid_input("hi"))
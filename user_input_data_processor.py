#Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
#Both should be at least 2 characters long. If not, print an error message

def validate_name_length(name, name_type):
    if len(name) < 2:
        print(f"Error: {name_type} must be at least 2 characters long.")
        return False
    return True

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

is_first_name_valid = validate_name_length(first_name, "First name")
is_last_name_valid = validate_name_length(last_name, "Last name")

if is_first_name_valid and is_last_name_valid:
    print("Both names are valid.")
else:
    print("Please try again with valid names.")


# Password Generator
# import modules
import random

# Password generator function

def password_generator():
    print("============= Welcome to Password Generator ================")
    # Password Length
    password_length = input("Enter the Password Length: ")
    while not password_length.isdigit():
        print("Alert!!!, Invalid input type only number")
        password_length = input("Enter the valid Password Length: ")
    # Converting password_length into integer
    selected_password_length = int(password_length)
    # Selection of characters for password
    def selected_characters(prompt):
        choice = input(prompt).strip().lower()
        while choice not in ["yes","no"]:
            print("Alert!!!, Invalid input, select only yes/no")
            choice = input(prompt).strip().lower()
        return choice
    
    lowerCase = selected_characters("Include lowerCase letters - yes/no: ")
    upperCase = selected_characters("Include upperCase letters - yes/no: ")
    digits = selected_characters("Include digits - yes/no: ")
    symbols = selected_characters("Include symbols - yes/no: ")

    # characters set
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!@#$%^&*()"

    # selected characters validations
    characters =""
    if lowerCase == "yes":characters+=lowercase
    if upperCase == "yes":characters+=uppercase
    if digits == "yes":characters+=numbers
    if symbols == "yes":characters+=special

    if not characters:
        print("Alert!!, you must choose at one character type!!")
        return
     
    # password generating
    password_box = []
    if lowerCase == "yes":password_box.append(random.choice(lowercase))
    if upperCase == "yes":password_box.append(random.choice(uppercase))
    if digits == "yes":password_box.append(random.choice(numbers))
    if symbols == "yes":password_box.append(random.choice(special))

    remaining_password = selected_password_length - len(password_box)
    for i in range(remaining_password):
        password_box.append(random.choice(characters))
    random.shuffle(password_box)
    final_password = "".join(password_box)
    print(f"Your final password: {final_password}")

password_generator()


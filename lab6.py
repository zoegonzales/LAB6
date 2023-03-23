#zoe gonzales

def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def password_encoder(password):
    new_pass = ''
    for num in password:
        new_pass += str(int(num) + 5)
    return new_pass

def password_decoder(password):
    decoded_password = ""
    for digit in password:
        # Convert the digit to an integer, add 3, and take the remainder divided by 10
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


while True:
    main()
    user_inp = int(input("\nPlease enter an option: "))
    if user_inp == 1:
        password = input("Please enter your password to encode: ")
        new_pass = password_encoder(password)
        print("Your password has been encoded and stored!")
    elif user_inp == 2:
        print(f"The encoded password is {new_pass}, and the original password is {password}.")
    elif user_inp == 3:
        break

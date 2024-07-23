
def encode(password):
    encoded = ''
    for i in range(len(password)):
        n = int(password[i])
        nn = (n + 3) % 10
        encoded = encoded + str(nn)
    return encoded

def decode(password):
    nums = []
    for i in password:
        num = int(i) - 3
        nums.append(str(num))
    decoded_pass = ''.join(nums)
    return decoded_pass

def main():
    encoded_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored! \n")
        elif option == '2':
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}. \n")
            else:
                print("No encoded password stored. Please encode a password first.")
        elif option == '3':
            break

if __name__ == "__main__":
    main()
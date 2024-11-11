name = input("Please tell me your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to the holiday, {}".format(name))
else:
    print("Sorry, try again later!")
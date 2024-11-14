options = ["Learn Python", "Learn Java", "Go swimming", "Go running", "Have dinner", "Have snack", "Go to bed", "Take shower", "Reading something", "Exit"]

print("Please chose your option from the list below:")

for i in range(1, len(options)):
    if options[i].casefold() == "exit":
       print("0. {}".format(options[i]))
    else:
         print("{}. {}".format(i, options[i]))

option_chased = 10

while option_chased != 0:
    option_chased = int(input())
    print("{}".format(options[option_chased - 1]))

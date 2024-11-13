low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start!")

guesses = 1
while True:
    guesses = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     " Enter h or l, or c if my guess was correct"
                     .format(guesses)).casefold()

    if high_low == "h":
        pass
    elif high_low == "l":
        pass
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
    else:
        print("Please enter h, l or c")
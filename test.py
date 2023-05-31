high = 100
low = 0
numguesses = 0

print('Please think of a number between 0 and 100!')

while low <= high:

    guess = int((high + low) / 2.0)
    print("Is your secret number" + str(guess) + " ?")
    user = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if user == 'h':
        high = guess
        numguesses += 1

    elif user == "l":
        low = guess

    elif user == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")


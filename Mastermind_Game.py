import random

# Generate a random 4-digit number
num = random.randrange(1000, 10000)

# Prompt the user to guess the number
n = int(input("Guess the 4 digit number: "))

# Check if the guess is correct
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    # Initialize the counter for the number of tries
    ctr = 0

    # Loop until the user guesses the number correctly
    while n != num:
        ctr += 1  # Increment the counter for each guess

        count = 0

        # Convert the guess and the number to strings for comparison
        n_str = str(n)
        num_str = str(num)

        # List to store correct digits
        correct = ['X'] * 4

        # Check each digit
        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct[i] = n_str[i]

        # Provide feedback to the user
        if count > 0:
            print(f"Not quite the number. But you did get {count} digit(s) correct!")
        else:
            print("None of the numbers in your input match.")

        # Prompt for the next guess
        n = int(input("Enter your next choice of numbers: "))

    # When the user guesses the number correctly
    ctr += 1  # Increment the counter for the final correct guess
    print("You've become a Mastermind!")
    print("It took you only", ctr, "tries.")

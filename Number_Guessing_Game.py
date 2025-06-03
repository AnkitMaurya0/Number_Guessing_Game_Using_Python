# Number Guessing Game

import random  # Step 1: import random module

secret_number = random.randint(1, 10)  # Step 2: choose a random number between 1 and 10

guess = None  # Step 3: initialize guess variable

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))  # Step 4: take input from user

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right.")

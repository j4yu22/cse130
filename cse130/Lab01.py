# 1. Name: 
#    Jay
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Let the user play a guessings game
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

# Game introduction.

# Prompt the user for how difficult the game will be. Ask for an integer.

# Generate a random number between 1 and the chosen value.

# Give the user instructions as to what he or she will be doing.

# Initialize the sentinal and the array of guesses.

# Play the guessing game.

    # Prompt the user for a number.

    # Store the number in an array so it can be displayed later.

    # Make a decision: was the guess too high, too low, or just right.

# Give the user a report: How many guesses and what the guesses where.

import random

def get_max():
    while True:
        max_input = input("Pick a positive integer: ")
        try:
            max_value = int(max_input)
            if max_value > 0:
                return max_value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("That's not a valid integer. Try again.")

def guess_game(max):
    target = random.randint(1, max)
    guesses = []

    while True:
        guess_input = input(f"Guess a number between 1 and {max}: ")
        try:
            guess = int(guess_input)
            guesses.append(guess)
            if guess < target:
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"You were able to find the number in {len(guesses)} guesses.")
                print(f"The numbers you guessed were: {guesses}")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print('This is the "guess a number" game.')
    print("You try to guess a random number in the smallest number of attempts.")
    max = get_max()
    guess_game(max)

if __name__ == "__main__":
    main()

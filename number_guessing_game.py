'''
Docstring for number_guessing_game
This program is an interactive number guessing game that allows the user
to customize the number range and the number of attempts. The program
uses input validation, error handling (try/except), loops, conditional
statements, and functions to ensure the game runs smoothly without crashing.
The user is prompted to enter their name, the desired number range, and 
the number of attempts. The program then generates a random number within
the specified range and allows the user to guess the number, providing
feedback on whether the guess is too low, too high, or correct. The game
continues until the user either guesses the number correctly or 
exhausts all attempts. After each round, the user is asked if they want to
 play again.

'''
# Import random module to generate a random number
import random

# Function to get a valid integer input with error handling


def get_valid_integer(prompt):
    while True:  # Loop until a valid integer is entered
        try:  # Try to convert the input to an integer
            return int(input(prompt))  # If successful, return the integer
        except ValueError:  # If a ValueError occurs, it means the input was not a valid integer
            # Prompt the user to enter a valid integer again
            print("Please enter a valid integer.")

# Function to get a valid 'y' or 'n' response from the user


def get_yes_no(prompt):  # Loop until a valid response is entered
    while True:
        # Get the user's response and convert it to lowercase
        response = input(prompt).lower()
        if response in ['y', 'n']:  # Check if the response is either 'y' or 'n'
            return response  # If valid, return the response
        else:
            # Prompt the user to enter a valid response again
            print("Please enter 'y' for yes or 'n' for no.")

# Function to play one round of the game


def play_game():

    # Ask for number range
    while True:  # Loop until a valid number range is entered
        low_number = get_valid_integer(
            # Get the lower bound of the number range from the user
            "Enter the lower bound of the number range: ")
        high_number = get_valid_integer(
            # Get the upper bound of the number range from the user
            "Enter the upper bound of the number range: ")
        if low_number < high_number:  # Check if the lower bound is less than the upper bound
            break
        else:  # If the lower bound is not less than the upper bound, prompt the user to enter a valid range again
            print("The lower bound must be less than the upper bound.")
# Ask for number of attempts
    # Get the number of attempts from the user
    max_attempts = get_valid_integer("Enter the number of attempts you want: ")
    while max_attempts <= 0:  # Check if the number of attempts is a positive integer
        print("Please enter a positive integer for attempts.")
        max_attempts = get_valid_integer(
            # If the number of attempts is not a positive integer, prompt the user to enter a valid number of attempts again
            "Enter the number of attempts you want: ")

# Generate random number
    target_number = random.randint(low_number, high_number)

# Track number of attempts
    attempts = 0

# Loop for user guesses
    while attempts < max_attempts:  # Loop until the user has used up all attempts
        guess = get_valid_integer(
            # Get the user's guess and display the current attempt number and total attempts
            f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
        attempts += 1

# Check if guess is too low or too high
        if guess < target_number:  # If the guess is less than the target number, inform the user that their guess is too low
            print("Too low! Try again.")
        elif guess > target_number:  # If the guess is greater than the target number, inform the user that their guess is too high
            print("Too high! Try again.")
        else:  # If the guess is equal to the target number, break out of the loop as the user has guessed correctly
            break
# Display success message if guessed correctly

# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game

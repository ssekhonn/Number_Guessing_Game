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

# Ask for number range

# Ensure low_number is less than high_number

# Ask for number of attempts

# Generate random number

# Track number of attempts

# Loop for user guesses

# Check if guess is too low or too high

# Display success message if guessed correctly

# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game

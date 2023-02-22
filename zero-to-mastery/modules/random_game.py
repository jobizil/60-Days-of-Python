
'''
You have been tasked to create a random number guessing game.
The game should generate a random number between 1 and 20 (inclusive).

Instructions:
- Ask user to pick range of numbers (min and max)
- Generate a random number between the min and max then store it in a variable
- Ask user to guess a number
- Compare user's guess to the random number generated
- If user guesses correctly, print "You win!"
- If user guesses incorrectly, print "You lose!"
'''

import sys
import random

try:
    min_number = int(sys.argv[1])
    max_number = int(sys.argv[2])

    if max_number <= min_number:
        print('Sorry, your maximum number must be higher than your minimum number')
    if min_number < 1:
        print('The minimum number you can enter should be 1')
    if max_number >= 21:
        print('The maximum number you can enter should be 20')

    print(
        f'Hello and welcome to our game \n You numbers will be generated between {min_number} and { max_number}')

    while True:
        try:
            user_input = int(
                input(f'Pick a number between {min_number} and {max_number} \n >>>'))

            # Generate a random int
            computer_guess = random.randrange(min_number, max_number, 1)

            # Compare User input to computer guess
            if computer_guess == user_input:
                print('You are rock! 🤘🏾')
                break

            elif (user_input < min_number):
                print('Your number choice is too small!')
            elif (user_input > max_number):
                print('Your number choice is too high!')

        except ValueError:
            print('Only numbers are allowed!')

        else:
            print('Incorrect guess, please try again!🙁')
except ValueError:
    # Handle invalid input
    print('Only numbers are allowed')

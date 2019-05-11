# A brief description of the project
# March 27, 2019
# CTI-110 P5HW1 - Random Number
# Robert Bush
#
# To import random, enables to pick number itself.
import random

# From number 1 to 100 with variable randomN (random number).
randomN = random.randint(1, 100)

# Give number from input to guess the number.
guess = int(input(" Enter a number between 1 to 100: "))

# To run while loop until the number is guessed.
while randomN != guess:

            # If the number is to low, print and try again.
            # input new number to guess again. 
            if guess < randomN:
                print("Too low, try again.")
                guess = int(input("Enter a number between 1 to 100:"))
            # else if number is to high than the randomN, print and try again.
            # input new number to guess again.
            elif guess > randomN:
                print("Too high, try again.")
                guess = int(input("Enter a number between 1 to 100:"))
                
# Once randomN guessed, print congratulate and start over to play again.
print("Congratulate! You guessed it.")
    

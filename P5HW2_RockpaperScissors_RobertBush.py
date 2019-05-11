# A brief description of the project
# March 28, 2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Robert Bush
#

import sys

u1 = input("What's your name?")
u2 = input("and your name?")
u1_a = ("% s, do you want to choose Rock, Paper, or Scissors?" % u1)
u2_a= ("% s, do you want to choose Rock, Paper, or Scissors?" % u2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
    sys.exit()
print(compare(u1_a, u2_a))
    

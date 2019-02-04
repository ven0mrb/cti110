# Debugging P3LAB
# 2-3-2019
# CTI-110 P3LAB - Debugging
# Robert Bush
#
# This program takes a number grade and outputs a letter grade
# system uses 10-point grading scale
# A= 90-100, B= 80-89, C= 70-79, D=60-69, F= 0-59
# TO DO: define the rest of the scores
#
def main():
    score = int(input('Enter the score:'))
    if score >= 90 and score <= 100:
        print('Your grade is A')
    elif score >= 80 and score <= 89:
        print('Your grade is B')
    elif score >= 70 and score <= 79:
        print('Your grade is C')
    elif score >= 60 and score <= 69:
        print('Your grade is D')
    else:
        print('Your grade is F')
main()

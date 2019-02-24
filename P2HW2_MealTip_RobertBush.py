# A brief description of the project
# 1-28-2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Robert Bush
#

# For Assignment P2HW2 (Python 2, Homework 2) you will create a program that calculates the
# total amount of a meal purchased at a restaurant.The program will ask the user to enter the
# charge for food and calculate the amount of the following tip percentages:
# 15%, 18%, 20%

# Enter the meal total purchased
# To put cost of the meal total without tip when asking for meal cost
meal = float(input('Enter the charge for food:'))

# Show the meal charge
print('Meal total is:', meal)

# Tips, 15, 18 and 20- List of the tip charge with the meal by the %
tip1 = 0.15*meal
tip2 = 0.18*meal
tip3 = 0.20*meal

# Print the Total of food purchased with tip
print('List of tip of 15%, 18%, and 20% with purchased of food total')
print('Tip 15%:', tip1)
print('Tip 18%:', tip2)
print('Tip 20%:', tip3)

# Total Tip with food purchased together listed
print('Food purcahsed with 15% total:', tip1 + meal)
print('Food purchased with 18% total:', tip2 + meal)
print('Food purchased with 20% total:', tip3 + meal)

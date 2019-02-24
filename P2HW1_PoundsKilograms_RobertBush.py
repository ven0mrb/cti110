# A brief description of the project
# 1-28-2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Robert Bush
#

#kg= lb/2.2046 as instructed on the blackboard assigment

# Enter the Pound(s) (lb) 
# To make an input for the pound(s) to be entered
pounds = float(input('Enter the pound(s):'))

# Converting
# After the pound(s) was entered, it is converted to Kilograms by the math opreation automatic  
kilograms = pounds *2.2046

#Converted to KG
# To show the kilogram as it's final that is converted from the pound(s).
print('The Kilograms is', kilograms)

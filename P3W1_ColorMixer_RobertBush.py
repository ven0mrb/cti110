# A brief description of the project
# 1-29-2019
# P3HW1 - Color Mixer
# Robert Bush
#


# c= color

#Color- Primary or secondary
c1 = input('What is your primary color? (red, blue, or yellow) :')
c2 = input('What is your secondary color? (red, blue, or yellow) :')

#Result of color
if c1 == "red" and c2 == "blue" or c1 == "blue" and c2 == "red":
    print("Result is purple")
elif c1 == "red" and c2 == "yellow" or c1 == "yellow" and c2 == "red":
    print("Result is orange")
elif c1 == "blue" and c2 == "yellow" or c1 == "yellow" and c2 == "blue":
    print("Result is green")

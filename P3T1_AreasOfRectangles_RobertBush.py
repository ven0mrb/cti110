# A brief description of the project
# 1-28-2019
# CTI-110 P3T1 - Areas of Rectangles
# Robert Bush
#

# Input the length and width of rectangle 1.
# Input the length and wwidth of rectangle 2.
# Calculate the area of rectangle 1.
# Calculate the area of rectangle 2.
# l= length  w= width
#

# Rectangle 1
l1 = int(input('Enter the length of rectangle 1:'))
w1 = int(input('Enter the width of rectangle 1:'))

# Rectangle 2
l2 = int(input('Enter the length of rectangle 2:'))
w2 = int(input('Enter the width of rectangle 2:'))

# Calculate area * rectangle (a= area)
a1 = l1 * w1
a2 = l2 * w2

# Determine which has the greater area.
if a1 > a2:
        print('Rectangle 1 has the greater area.')
elif a2 > a1:
        print('Rectangle 2 has the greater area.')
else:
        print('Both have the same area.')

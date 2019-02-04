# A brief description of the project
# 2-3-2019
# CTI-110  P3HW2 - MealTipTax 
# Robert Bush
#
# Asks the user to enter the total for the meal, tip and "fixed tax of 7%"
def main():
    meal = float(input('Enter the total for the meal:'))
    print('Total of food is:$', meal)
    tax = 0.7*meal
    total = tax + meal
    print('Sale tax 7% is:$', tax)
    print('Total of Food with Tax is: $', total)
    tip = float(input('Enter the tip 15%, 18%, or 20%:'))
    tip1 = 0.15*meal
    tip2 = 0.18*meal
    tip3 = 0.20*meal
    if tip == 15:
        print('Tip 15% is:$', tip1)
        print('Total of Food, Tax, and Tip:$', tip1 + total)
    elif tip == 18:
        print('Tip 18% is :$', tip2)
        print('Total of Food, Tax and Tip:$', tip2 + total)
    elif tip == 20:
        print('Tip 20% is:$', tip3)
        print('Total of Food, Tax, and Tip:$', tip3 + total)
    else:
        print('Unknown error')
main()

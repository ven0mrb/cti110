# A brief description of the project
# March 27, 2019
# CTI-110 P5T1_KilometerConverter 
# Robert Bush
#
# Miles = Kilometers x 0.6114

CONVERSION_FACTOR = 0.6214
# The main function gets a distance in kilometers and calls
# the show_miles function to covert it.
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometer equals', miles, 'miles.')

# Call the main function.
main()

    

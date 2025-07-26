from datetime import datetime, timedelta
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date to "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Display the formatted date
    print("Current Date and Time:", formatted_date)
display_current_datetime()
"""
 Part 2: Calculate a Future Date

Prompt the user to enter a number of days (as an integer).
Create a function with a name calculate_future_date and
saves the future date inside a future_date variable
Calculate what the date will be after adding the specified number of days to the current date.
Print the future date in a format like “YYYY-MM-DD”.   
"""
from datetime import datetime, timedelta

number_of_days = int(input("Enter the number of days: "))

def calculate_future_date():
    future_date = datetime.today() + timedelta(days=number_of_days)
    #formatted_date = future_date.strftime("%Y-%m-%d")
    #print("Future date:", formatted_date)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
calculate_future_date()

    

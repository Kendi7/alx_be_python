FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR= 9/5
'''
Implement Conversion Functions:

Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
Inside each function, use the respective global conversion factor to perform the conversion.
'''
# Define conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Take user input
temperature = float(input("Enter the temperature to convert: "))
temperature_validation = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

# Define conversion functions
def convert_to_celsius(temp):
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(temp):
    return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Determine which conversion to perform
if temperature_validation == 'F':
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted}°C")
elif temperature_validation == 'C':
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted}°F")
else:
    print("Invalid temperature. Please enter a numeric value")

    

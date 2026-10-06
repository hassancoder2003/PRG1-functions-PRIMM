def celsius_to_fahrenheit(celsius, fahrenheit):
    fahrenheit_calculation = (celsius * 9/5) + 32
    celsius_calculation = (fahrenheit - 32) / 1.8
    return celsius_calculation, fahrenheit_calculation


# Test the function
print(celsius_to_fahrenheit(0, 20))
print(celsius_to_fahrenheit(20, 40))
print(celsius_to_fahrenheit(100, 60))
print(celsius_to_fahrenheit(-40, -60))
print(celsius_to_fahrenheit(30, 50))

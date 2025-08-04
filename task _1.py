# Ask the user for temperature input
temp_input = input("Enter temperature (e.g., 37C or 98F): ").strip()

# Check if the last character is 'C' or 'F' (case-insensitive)
if temp_input[-1].upper() == 'C':
    # Convert Celsius to Fahrenheit
    celsius = float(temp_input[:-1])
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif temp_input[-1].upper() == 'F':
    # Convert Fahrenheit to Celsius
    fahrenheit = float(temp_input[:-1])
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

else:
    print("Invalid input. Please end the temperature with 'C' or 'F'.")

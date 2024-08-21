import math

# Demonstrating Math Built-in Functions with User Input

# Get a number from the user
number = float(input("Enter a number for math operations: "))

# Square root
sqrt_value = math.sqrt(number)
print(f"Square root of {number} is {sqrt_value}")

# Power
power_value = math.pow(number, 2)
print(f"{number} raised to the power 2 is {power_value}")

# Trigonometric functions
angle_degrees = float(input("Enter an angle in degrees for sine calculation: "))
angle = math.radians(angle_degrees)
sin_value = math.sin(angle)
print(f"Sine of {angle_degrees} degrees is {sin_value}")

# Logarithm (base e)
log_value = math.log(number)
print(f"Natural log of {number} is {log_value}")

# Ceiling and Floor
float_number = float(input("Enter a floating-point number for ceiling and floor operations: "))
ceil_value = math.ceil(float_number)
floor_value = math.floor(float_number)
print(f"Ceiling of {float_number} is {ceil_value}")
print(f"Floor of {float_number} is {floor_value}")

# Demonstrating String Built-in Functions with User Input

# Get a string from the user
text = input("\nEnter a string for string operations: ")

# Length of string
length = len(text)
print(f"Length of the string is {length}")

# Convert to uppercase
upper_text = text.upper()
print(f"Uppercase: {upper_text}")

# Remove whitespace
stripped_text = text.strip()
print(f"Stripped text: '{stripped_text}'")

# Find a substring
substring = input("Enter a substring to find in the string: ")
position = text.find(substring)
if position != -1:
    print(f"Position of '{substring}' in the string is {position}")
else:
    print(f"'{substring}' not found in the string.")

# Replace a substring
to_replace = input("Enter the substring to be replaced: ")
replacement = input("Enter the new substring: ")
replaced_text = text.replace(to_replace, replacement)
print(f"Replaced text: {replaced_text}")

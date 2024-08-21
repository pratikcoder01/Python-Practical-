# Define the functions as if they were in a package

# math_functions module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# string_functions module
def uppercase(s):
    return s.upper()

def lowercase(s):
    return s.lower()

# Main part of the script
def main():
    # Get user input for math functions
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        
        print(f"{x} + {y} = {add(x, y)}")
        print(f"{x} - {y} = {subtract(x, y)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    # Get user input for string functions
    text = input("Enter a string: ")
    print(f"Uppercase: {uppercase(text)}")
    print(f"Lowercase: {lowercase(text)}")

# Run the main function
if __name__ == "__main__":
    main()


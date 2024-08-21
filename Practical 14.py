    # calculator_module.py (The module code)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b

# Main program to use the above module

def main():
    print("Simple Calculator Using User-Defined Functions")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")

    choice = input("Enter the number corresponding to the operation: ")

    if choice == '1':
        result = add(a, b)
        print(f"The result of addition: {result}")
    elif choice == '2':
        result = subtract(a, b)
        print(f"The result of subtraction: {result}")
    elif choice == '3':
        result = multiply(a, b)
        print(f"The result of multiplication: {result}")
    elif choice == '4':
        try:
            result = divide(a, b)
            print(f"The result of division: {result}")
        except ValueError as e:
            print(e)
    elif choice == '5':
        result = power(a, b)
        print(f"The result of {a} raised to the power {b}: {result}")
    elif choice == '6':
        result = mod(a, b)
        print(f"The result of modulus: {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

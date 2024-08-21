def greet(name="Guest"):
    print(f"Hello, {name}!")

def power(base, exponent=2):
    return base ** exponent

def area_of_rectangle(length=1, width=1):
    return length * width

# Main Program
if __name__ == "__main__":
    # Demonstrating greet function
    print("Greeting Function:")
    name = input("Enter your name (or press Enter to use 'Guest'): ")
    greet(name)  # Use default if empty input
    print()

    # Demonstrating power function
    print("Power Function:")
    base = float(input("Enter the base number: "))
    exponent = input("Enter the exponent (or press Enter to use default exponent 2): ")
    exponent = float(exponent) if exponent else 2
    result = power(base, exponent)
    print(f"{base} raised to the power {exponent} is {result}")
    print()

    # Demonstrating area_of_rectangle function
    print("Rectangle Area Function:")
    length = input("Enter the length of the rectangle (or press Enter to use default length 1): ")
    width = input("Enter the width of the rectangle (or press Enter to use default width 1): ")
    length = float(length) if length else 1
    width = float(width) if width else 1
    area = area_of_rectangle(length, width)
    print(f"Area of rectangle with length {length} and width {width} is {area}")

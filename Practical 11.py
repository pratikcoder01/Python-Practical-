def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def swap(a, b):
    a, b = b, a
    return a, b

# Main Program
if __name__ == "__main__":
    # Factorial Calculation
    number = int(input("Enter a number to calculate its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")

    # Swapping Variables
    x = input("Enter the first value: ")
    y = input("Enter the second value: ")

    # Perform the swap
    x, y = swap(x, y)
    print(f"After swapping, first value is: {x}, second value is: {y}")


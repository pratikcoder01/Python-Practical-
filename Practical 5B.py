def for_loop_demo():
    # Building an equilateral triangle
    def build_equilateral_triangle():
        print("Equilateral Triangle Pattern:")
        height = 5  # You can change this value to adjust the height of the triangle
        for i in range(height):
            print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    
    build_equilateral_triangle()    

    # Printing a multiplication table
    print("\nMultiplication Table:")
    num = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    # Checking if a number is a palindrome
    num = input("\nEnter a number to check if it is a palindrome: ")
    if num == num[::-1]:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

for_loop_demo()     
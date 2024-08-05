def equivalent_resistors():
    # Accepting values of R1, R2, and R3 from the user
    R1 = float(input("Enter the value of R1: "))
    R2 = float(input("Enter the value of R2: "))
    R3 = float(input("Enter the value of R3: "))

    # Calculating equivalent resistance in series
    series_resistance = R1 + R2 + R3

    # Calculating equivalent resistance in parallel
    parallel_resistance = 1 / ((1 / R1) + (1 / R2) + (1 / R3))

    # Printing the results
    print(f"Equivalent resistance in series: {series_resistance} ohms")
    print(f"Equivalent resistance in parallel: {parallel_resistance} ohms")

# Calling the function
equivalent_resistors()

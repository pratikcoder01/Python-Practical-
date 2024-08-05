def calculate_voltage(current, resistance):
    return current * resistance

def calculate_resistance(voltage, current):
    return voltage / current

def calculate_current(voltage, resistance):
    return voltage / resistance

while True:
    print("1. Calculate Voltage")
    print("2. Calculate Resistance")
    print("3. Calculate Current")
    print("4. Exit Program")
    ask = input("> ")
    
    try:
        if ask == "1":
            i = float(input("Current (A): "))
            r = float(input("Resistance (Ω): "))
            print(f"Voltage = {calculate_voltage(i, r):.2f} V")
        elif ask == "2":
            v = float(input("Voltage (V): "))
            i = float(input("Current (A): "))
            print(f"Resistance = {calculate_resistance(v, i):.2f} Ω")
        elif ask == "3":
            v = float(input("Voltage (V): "))
            r = float(input("Resistance (Ω): "))
            print(f"Current = {calculate_current(v, r):.2f} A")
        elif ask == "4":
            break
        else:
            print("Not an option, try again.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")


def resistor_color_code():
    colors = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9
    }

    color = input("Enter the color: ").lower()

    value = colors.get(color, "Invalid color")

    if value != "Invalid color":
        print(f"The value for {color} is: {value}")
    else:
        print("Invalid color entered. Please enter a valid resistor color.")

resistor_color_code()

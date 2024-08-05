def check_frequency():
    frequency = float(input("Enter the frequency in Hz: "))

    if 20 <= frequency <= 20000:
        print("Audio frequency.")
    elif 3000 <= frequency <= 300000000000:
        print("Radio frequency.")
    else:
        print("Neither audio nor radio frequency.")

check_frequency()

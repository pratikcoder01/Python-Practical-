def radio_frequency_band():
    frequency = float(input("Enter the frequency in Hz: "))

    if 3e3 <= frequency < 30e3:
        print("Very Low Frequency (VLF)")
    elif 30e3 <= frequency < 300e3:
        print("Low Frequency (LF)")
    elif 300e3 <= frequency < 3e6:
        print("Medium Frequency (MF)")
    elif 3e6 <= frequency < 30e6:
        print("High Frequency (HF)")
    elif 30e6 <= frequency < 300e6:
        print("Very High Frequency (VHF)")
    elif 300e6 <= frequency < 3e9:
        print("Ultra High Frequency (UHF)")
    elif 3e9 <= frequency < 30e9:
        print("Super High Frequency (SHF)")
    elif 30e9 <= frequency < 300e9:
        print("Extremely High Frequency (EHF)")
    else:
        print("Frequency out of radio frequency range")

radio_frequency_band()

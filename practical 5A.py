def control_loops_demo():
    # Using a while loop
    print("While loop demonstration:")
    count = 0
    while count < 10:
        print(f"Count is {count}")
        count += 1

    #  do-while loop
    print("\nSimulated do-while loop demonstration:")
    count = 0
    while True:
        print(f"Count is {count}")
        count += 1
        if count >= 10:
            break

control_loops_demo()

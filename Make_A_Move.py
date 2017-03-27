def Make_A_Move():
    while True:
        while True:
            a = input()
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("\nOutside the board. Choose again")
                    continue
            except ValueError:
                print("\nNot a numver. Choose again")
                continue
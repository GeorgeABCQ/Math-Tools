def coprime(dev, num1, num2):
    try:
        from lib.mathtools.HCF import HCF
    except ModuleNotFoundError:
        try:
            from HCF import HCF
        except ModuleNotFoundError:
            print("Module HCF not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    if dev == False:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

    # check if num1 and num2 are numbers
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Invalid input.")
        if dev == False:
            input("Press enter to return to the main menu ... ")
        return 0
    if HCF(True, False, num1, num2, False) == 1:
        if dev == False:
            print(num1, "and", num2, "are coprime.")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return True
    else:
        if dev == False:
            print(num1, "and", num2, "are not coprime.")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return False

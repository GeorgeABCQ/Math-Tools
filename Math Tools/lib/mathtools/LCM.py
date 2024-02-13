def LCM(dev, num1, num2):
    try:
        from lib.mathtools.find_factor import find_factor
        from lib.mathtools.HCF import HCF
    except ModuleNotFoundError:
        try:
            from find_factor import find_factor
            from HCF import HCF
        except ModuleNotFoundError:
            print("Module find_factor or HCF not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    if dev == False:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Invalid input.")
        input("Press enter to return to the main menu ... ")
        return -2
    # find the factors of the numbers
    factors1 = find_factor(True, True, num1)
    factors2 = find_factor(True, True, num2)
    # find the common factors
    commonfactors = []
    for i in factors1:
        if i in factors2:
            commonfactors.append(i)
    # find the lowest common multiple
    LCM = int((num1 * num2) / int(HCF(True, False, num1, num2, False)))
    if dev == False:
        print("The lowest common multiple of", num1, "and", num2, "is", LCM, ".")
        input("Press enter to return to the main menu ... ")
        return 0
    else:
        return LCM

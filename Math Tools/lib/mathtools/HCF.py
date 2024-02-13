def HCF(dev, nostr, num1, num2, showall):
    try:
        from lib.mathtools.list_to_str import list_to_str
        from lib.mathtools.find_factor import find_factor
    except ModuleNotFoundError:
        try:
            from list_to_str import list_to_str
            from find_factor import find_factor
        except ModuleNotFoundError:
            print("The module 'list_to_str' or 'find_factor' is not found.")
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
        if dev == False:
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
    # find the highest common factor
    if dev == False:
        showall = input("Do you want to see all the common factors? (Y/N, default is no): ")

        # Ask if the user wants to see all the common factors

    if showall == "Y" or showall == "y" or showall == "yes" or showall == "Yes":
        if nostr == False:
            commonfactorsstr = list_to_str(commonfactors)
        if dev == False:
            if len(commonfactors) == 1:
                print("The common factors of", num1, "and", num2, "is", commonfactorsstr, ", so they are coprime.")
            else:
                print("The common factors of", num1, "and", num2, "are", commonfactorsstr, ".")
            input("Press enter to return to the main menu ... ")
            return 0
    HCF = max(commonfactors)
    if dev == False:
        if not(showall == "Y" or showall == "y" or showall == "yes" or showall == "Yes"):
            if HCF == 1:
                print("The highest common factor of", num1, "and", num2, "is", HCF, ", so they are coprime.")
            else:
                print("The highest common factor of", num1, "and", num2, "is", HCF, ".")
        input("Press enter to return to the main menu ... ")
        return 0
    else:
        return HCF

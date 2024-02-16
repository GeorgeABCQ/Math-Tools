def find_factor(dev, nostr, num): # When dev is True, the function will not ask for input, instead, it will use num. Nostr when True will not convert it to str. num is the number to find the factors.
    try:
        from lib.mathtools.list_to_str import list_to_str
    except ModuleNotFoundError:
        try:
            from list_to_str import list_to_str
        except ModuleNotFoundError:
            print("Module list_to_str is not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    if dev == False:
        num = input("Enter a number to find the factors: ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input.")
        input("Press enter to return to the main menu ... ")
        return 0
    # factorize the number
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    # convert the list to str
    if nostr == False:
        factorsstr = list_to_str(factors)
    if dev == False:
        if len(factors) == 1:
            print("The factors of", num, "is", factorsstr, ".")
        else:
            print("The factors of", num, "are", factorsstr, ".")
        input("Press enter to return to the main menu ... ")
        return 0
    else:
        return factors

def int_factorization(dev, nostr, num):
    try:
        from lib.mathtools.list_to_str_usingx import list_to_str_usingx
        from lib.mathtools.isprime import isprime
    except ModuleNotFoundError:
        try:
            from list_to_str_usingx import list_to_str_usingx
            from isprime import isprime
        except ModuleNotFoundError:
            print("Module list_to_str_usingx or isprime is not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    if dev == False:
        num = input("Enter a number to factorize: ")
    numdis = num
    try:
        num = int(num)
    except ValueError:
        print("Invalid input.")
        input("Press enter to return to the main menu ... ")
        return -2
    # factorize the number
    factors = []
    if isprime(True, num) == True:
        factors = [1, num]
    else:
        for i in range(2, num + 1):
            while num % i == 0:
                factors.append(i)
                num = num / i
    # convert the list to str
    if int(numdis) == 1:
        if dev == False:
            print("1 only has 1 factor, which is 1, so it cannot be factorized.")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return 1
    else:
        if nostr == False:
            factorsstr = list_to_str_usingx(factors)
        if dev == False:
            print(numdis, "=", factorsstr)
    if dev == False:
        input("Press enter to return to the main menu ... ")
        return 0
    else:
        return factors

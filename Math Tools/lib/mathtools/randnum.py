def randnum():
    import random
    try:
        from lib.mathtools.list_to_str import list_to_str
    except ModuleNotFoundError:
        try:
            from list_to_str import list_to_str
        except ModuleNotFoundError:
            print("The module list_to_str is not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    sort1 = False
    small = input("What's the smallest number you want to generate? (default is 1): ")

    #check if small is a number
    try:
        small = int(small)
    except ValueError:
        small = 1

    big = input("What's the largest number you want to generate? (default is 100): ")

    #check if big is a number
    try:
        big = int(big)
    except ValueError:
        big = 100

    #check if small is smaller than big
    if small > big:
        print("The smallest number is larger than the largest number.")
        input("Press enter to return to the main menu ... ")
        return 0
    
    times = input("How many random numbers do you want to generate? (default is 1): ")

    #check if times is a number
    try:
        times = int(times)
    except ValueError:
        times = 1
    
    # check if the user wants to sort the numbers
    if times > 1:
        sort1 = input("Do you want the numbers to be sorted? (Y/N, default is yes):")
        if sort1 == "N" or sort1 == "n" or sort1 == "no" or sort1 == "No":
            sort1 = False
        else:
            sort1 = True
            FSTB = input("Do you want the numbers to be from small to big(FSTB) or from big to small(FBTS)? (FSTB/FBTS, default is FSTB): ")
            if FSTB == "FBTS" or FSTB == "fbts":
                FSTB = False
            else:
                FSTB = True

    same = input("Do you want the same number can be generated multiple times? (Y/N, default is no): ")
    if same == "Y" or same == "y" or same == "yes" or same == "Yes":
        if big - small + 1 >= times:
            same = True
        elif big - small + 1 < times:
            print("The range is too small to generate that many numbers.")
            input("Press enter to return to the main menu ... ")
            return 0
    else:
        same = False

    randlist = []
    # return the random number
    for i in range(0, times):
        rand = random.randint(small, big)
        if same == False:
            while rand in randlist:
                rand = random.randint(small, big)
        randlist.append(rand)
    
    # sort the list
    if sort1 == True:
        if FSTB == True:
            randlist.sort()
        else:
            randlist.sort(reverse=True)
    
    # convert the list to str
    randstr = list_to_str(randlist)
    
    if times > 1:
        if big - small + 1 == times:
            print("The random numbers are", randstr, ". And they will always be.")
        else:
            print("The random numbers are", randstr, ".")
    else:
        if big - small + 1 == times:
            print("The random number is", randstr, ". And it will always be.")
        else:
            print("The random number is", randstr, ".")
    input("Press enter to return to the main menu ... ")
    return 0  

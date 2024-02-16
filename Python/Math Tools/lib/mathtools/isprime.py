def isprime(dev, num): # When dev is True, the function will not ask for input, instead, it will use the input from num. Return False means it is not a prime, True means it is a prime, 1 means it is not a prime or a composite, 0 means num is 0 and it cannot be defined, -1 means it cannot be defined as a prime number nor a composite number.
    if dev == False:
        num = input("Enter a number to check if it's prime: ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input.")
        if dev == False:
            input("Press enter to return to the main menu ... ")
        return -2
    
    # check if the number is prime
    if num > 1 and num == int(num):
        for i in range(2, num):
            if (num % i) == 0:
                if dev == False:
                    print(num, "is not a prime number.")
                    return False
                else:
                    return False
        # print the result
        if dev == False:
            print(num, "is a prime number.")
            input("Press enter to return to the main menu ... ")
            return True
        else:
            return True
    else:
        # exceptions
        if num == 1:
            if dev == False:
                print(num, "is not a prime number nor composite number.")
            else:
                return 1
        elif num == 0:
            if dev == False:
                print(num, "is not a prime number.")
            else:
                return 0
        else:
            if dev == False:
                print(num, "cannot be defined as a prime number nor a composite number.")
            else:
                return -1
    if dev == False:
        input("Press enter to return to the main menu ... ")
    return 0

import random

class Game:


    def guess_num():
        print("Welcome to the number guessing game!")
        bignum = input("Enter the largest number you want to guess (default is 100): ")

        # Check if bignum is a number
        try:
            bignum = int(bignum)
        except ValueError:
            bignum = 100
        print("I'm thinking of a number between 1 and", bignum, ".")
        guesstop = input("How much guesses do you want you to have? (0 for no limit, default is 20): ")

        # Check if guesstop is a number
        try:
            guesstop = int(guesstop)
        except ValueError:
            guesstop = 20
        print("Try to guess the number in as few attempts as possible.")

        number = random.randint(1, 100)
        guess = 0
        count = 0

        while guess != number and count != guesstop:
            guess = int(input("Enter your guess: "))
            count += 1
            # check if the guess is too high or too low (no equal because it is checked in the win or lose)
            if guess < number:
                print("The number", guess, "is too low!")
            elif guess > number:
                print("The number", guess, "is too high!")
        # check win or lose
        if guess == number:
            print("You've guessed it! The number was", number, ". It took you", count, "tries out of", guesstop, "tries.")
        else:
            print("You've run out of guesses! The number was", number, ".")



class Mathtools():

    
    def randnum():
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
        
        times = input("How many random numbers do you want to generate? (default is 1): ")

        #check if times is a number
        try:
            times = int(times)
        except ValueError:
            times = 1

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
                input("Press enter to continue ... ")
                Mathtools.randnum()
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
        randstr = devtools.list_to_str(randlist)
        
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
        return 0
    
    def isprime():
        num = input("Enter a number to check if it's prime: ")
        try:
            num = int(num)
        except ValueError:
            print("Invalid input. Please try again.")
            return 0
        
        # check if the number is prime
        if num > 1 and num != int(num):
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number.")
                    break
            # print the result
            else:
                print(num, "is a prime number.")
        else:
            # exceptions
            if num == 1:
                print(num, "is not a prime number nor composite number.")
            elif num == 0:
                print(num, "is not a prime number.")
            else:
                print(num, "cannot be defined as a prime number nor a composite number.")
        return 0


class devtools():

    def list_to_str(list):
        str1 = ""
        count = 0
        for i in list:
            i = str(i)
            count += 1
            if count == len(list):
                str1 = str1 + i
            else:
                str1 = str1 + i + ", "
        return str1


def menu():
    print("""
     -----Welcome to the Math Tools menu!-----
───────────────────────────────────────────────────
    Tools:                                        
    1. Random number generator
    2. Prime dectector
───────────────────────────────────────────────────
    Games:
    3. Guess the number
───────────────────────────────────────────────────
Notes:
- Type the number of the tool or game you want to use to use it.
- Type 'exit' to leave the program.
───────────────────────────────────────────────────""")
    
    goto = input("What would you like to do? ")
    
    try:
        goto = int(goto)
    except ValueError:
        if goto == "exit" or goto == "Exit" or goto == "EXIT":
            print("Goodbye!")
            return goto
        else:
            print("Invalid input. Please try again.")
            return 0
    return goto

# set menuuser to 0 to start the loop
menuuser = 0

# menu to program
while menuuser != "exit":
    menuuser = menu()
    if menuuser == 1:
        Mathtools.randnum()
        input("Press enter to continue ... ")
    elif menuuser == 2:
        Mathtools.isprime()
        input("Press enter to continue ... ")
    elif menuuser == 3:
        Game.guess_num()
        input("Press enter to continue ... ")
    elif menuuser == "exit":
        break

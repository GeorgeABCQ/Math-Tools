import random
import time

class Game:


    def guess_num():
        # Shows basic information
        score = 0
        print("Welcome to the number guessing game!")

        # Exit the game
        while True:
            print("If you win a game, you will get 1 point. If you lose, you will lose 1 point.")
            print("Type 'exit' to return to the main menu. Type 'score' to show your score. Type anything else to continue ... ")
            begin = input("Your choice: ")

            if begin == "exit":
                print("Your score is", score, ".")
                input("Press enter to return to the main menu ... ")
                return 0
            
            # Show the score
            elif begin == "score":
                print("Your score is", score, ".")

            # The game itself
            else:
                smallnum = input("Enter the smallest number you want to guess (default is 1): ")

                # Check if smallnum is a number
                try:
                    smallnum = int(smallnum)
                except ValueError:
                    smallnum = 1
                
                bignum = input("Enter the largest number you want to guess (default is 100 and the difference between the largest and the smallest must be greater than 10): ")

                # Check if bignum is a number
                try:
                    bignum = int(bignum)
                except ValueError:
                    bignum = 100
                
                # Check if the range is too small
                if bignum - smallnum + 1 <= 10:
                    print("The range is too small to guess.")
                    input("Press enter to return to the main menu ... ")
                    break

                print("I'm thinking of a number between", smallnum, "and", bignum, ".")
                time.sleep(0.5)
                guesstop = input("How much guesses do you want you to have? (0 for no limit, default is 20): ")

                # Check if guesstop is a number
                try:
                    guesstop = int(guesstop)
                except ValueError:
                    guesstop = 20
                print("Try to guess the number in as few attempts as possible.")

                number = random.randint(1, bignum)
                guess = 0
                count = 0

                while guess != number and count != guesstop:
                    guess = int(input("Enter your guess: "))
                    count += 1
                    # Check if the guess is too high or too low (no equal because it is checked in the win or lose section)
                    if guess < number:
                        print("The number", guess, "is too low!")
                    elif guess > number:
                        print("The number", guess, "is too high!")
                # Check for win or lose
                if guess == number:
                    print("You've guessed it! The number was", number, ". It took you", count, "tries out of", guesstop, "tries.")
                    score += 1
                else:
                    print("You've run out of guesses! The number was", number, ".")
                    score -= 1
                
                # Ask if the user wants to play again
                askexit = input("Do you want to play again? (Y/N): ")
                if askexit == "N" or askexit == "n" or askexit == "no" or askexit == "No":
                    print("Your score is", score, ".")
                    input("Press enter to return to the main menu ... ")
                    break

    
    def rps():
        # Show basic information
        print("Welcome to the Rock, Paper, Scissors game!")
        score = 0
        while True:
            print("If you win a game, you will get 1 point. If you lose, you will lose 1 point. If it's a tie, the score won't change.")
            print("Type 'score' to show your score. Type 'exit' to return to the main menu. Type anything else to start the game ...")
            userstart = input("Your choice: ")

            # Exit the game
            if userstart == "exit":
                print("Your score is", score, ".")
                input("Press enter to return to the main menu ... ")
                break
            
            # Show the score
            elif userstart == "score":
                print("Your score is", score, ".")
            # The game itself
            else:
                user = input("Choose rock, paper, or scissors: ")
                if user == "rock" or user == "paper" or user == "scissors" or user == "r" or user == "p" or user == "s":
                    comp = random.choice(["rock", "paper", "scissors"])
                    print("The computer chose", comp, ".")
                    if user == comp:
                        print("It's a tie!")
                    elif user == "rock" or user == "r":
                        if comp == "scissors":
                            print("You win!")
                            score += 1
                        else:
                            print("You lose!")
                            score -= 1
                    elif user == "paper" or user == "p":
                        if comp == "rock":
                            print("You win!")
                            score += 1
                        else:
                            print("You lose!")
                            score -= 1
                    elif user == "scissors" or user == "s":
                        if comp == "paper":
                            print("You win!")
                            score += 1
                        else:
                            print("You lose!")
                            score -= 1

                    # Ask if the user wants to play again
                    askexit = input("Do you want to play again? (Y/N): ")
                    if askexit == "N" or askexit == "n" or askexit == "no" or askexit == "No":
                        print("Your score is", score, ".")
                        input("Press enter to return to the main menu ... ")
                        break
                
                #Show the score
                elif user == "score":
                    print("Your score is", score, ".")
                
                elif user == "exit":
                    print("Your score is", score, ".")
                    input("Press enter to return to the main menu ... ")
                    break
        return 0


class Mathtools():

    
    def randnum():
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
        input("Press enter to return to the main menu ... ")
        return 0
    

    def isprime(dev, num): # When dev is True, the function will not ask for input, instead, it will use the input from num. Return False means it is not a prime, True means it is a prime, 1 means it is not a prime or a composite, 0 means num is 0 and it cannot be defined, -1 means it cannot be defined as a prime number nor a composite number.
        if dev == False:
            num = input("Enter a number to check if it's prime: ")
        try:
            num = int(num)
        except ValueError:
            print("Invalid input.")
            input("Press enter to return to the main menu ... ")
            return 0
        
        # check if the number is prime
        if num > 1 and num != int(num):
            for i in range(2, num):
                if (num % i) == 0:
                    if dev == False:
                        print(num, "is not a prime number.")
                    else:
                        return False
                    break
            # print the result
            else:
                if dev == False:
                    print(num, "is a prime number.")
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
    
    def find_factor(dev, nostr, num): # When dev is True, the function will not ask for input, instead, it will use num. Nostr when True will not convert it to str. num is the number to find the factors.
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
            factorsstr = devtools.list_to_str(factors)
        if dev == False:
            print("The factors of", num, "are", factorsstr, ".")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return factors
    

    def int_factorization(dev, nostr, num):
        if dev == False:
            num = input("Enter a number to factorize: ")
        numdis = num
        try:
            num = int(num)
        except ValueError:
            print("Invalid input.")
            input("Press enter to return to the main menu ... ")
            return 0
        # factorize the number
        factors = []
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
                factorsstr = devtools.list_to_str_usingx(factors)
            if dev == False:
                print(numdis, "=", factorsstr)
        if dev == False:
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return factors
        

    def HCF(dev, nostr, num1, num2, showall):
        if dev == False:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Invalid input.")
            input("Press enter to return to the main menu ... ")
            return 0
        # find the factors of the numbers
        factors1 = Mathtools.find_factor(True, True, num1)
        factors2 = Mathtools.find_factor(True, True, num2)
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
                commonfactorsstr = devtools.list_to_str(commonfactors)
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
                    print("The highest common factor of", num1, "and", num2, "are", HCF, ".")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return HCF
    

    def LCM(dev, num1, num2):
        if dev == False:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Invalid input.")
            input("Press enter to return to the main menu ... ")
            return 0
        # find the factors of the numbers
        factors1 = Mathtools.find_factor(True, True, num1)
        factors2 = Mathtools.find_factor(True, True, num2)
        # find the common factors
        commonfactors = []
        for i in factors1:
            if i in factors2:
                commonfactors.append(i)
        # find the lowest common multiple
        LCM = (num1 * num2) / Mathtools.HCF(True, num1, num2)
        if dev == False:
            print("The lowest common multiple of", num1, "and", num2, "is", LCM, ".")
            input("Press enter to return to the main menu ... ")
            return 0
        else:
            return LCM

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
    
    def list_to_str_usingx(list):
        str1 = ""
        count = 0
        for i in list:
            i = str(i)
            count += 1
            if count == len(list):
                str1 = str1 + i
            else:
                str1 = str1 + i + " x "
        return str1


def menu():
    print("""
                                     -----Welcome to the Math Tools menu!-----
  ╔═════════════════════════════════════════════════════╦════════════════════════════════════════════════════════════╗
  ║  Tools:                                             ║  Games:                                                    ║
  ║   1. Random number generator                        ║   7. Guess the number                                      ║
  ║   2. Prime dectector                                ║   8. Rock, Paper, Scissors                                 ║
  ║   3. find the factors                               ║                                                            ║
  ║   4. int factorization                              ║                                                            ║
  ║   5. find the highest common factor (HCF)           ║                                                            ║
  ║   6. find the lowest common multiple (LCM)          ║                                                            ║
  ╠═════════════════════════════════════════════════════╩════════════════════════════════════════════════════════════╣
  ║  Notes:                                                                                                          ║
  ║  - Type the number of the tool or game you want to use to use it.                                                ║
  ║  - Type 'exit' or press Ctrl+C or Alt+F4 to leave the program.                                                   ║
  ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""")
    
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
    elif menuuser == 2:
        Mathtools.isprime(False, 0)
    elif menuuser == 3:
        Mathtools.find_factor(False, False, 0)
    elif menuuser == 4:
        Mathtools.int_factorization(False, False, 0)
    elif menuuser == 5:
        Mathtools.HCF(False, False, 0, 0, False)
    elif menuuser == 6:
        Mathtools.LCM(False, 0, 0)
    elif menuuser == 7:
        Game.guess_num()
    elif menuuser == 8:
        Game.rps()
    elif menuuser == "exit":
        break

    print("""
















            """)

    # Check if the input is valid
    if type(menuuser) == int:
        if not(menuuser >= 1 and menuuser <= 5):
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
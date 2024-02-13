import random

class Game:


    def guess_num():
        # Shows basic information
        score = 0
        print("Welcome to the number guessing game!")
        print("Type 'exit' to return to the main menu. Type 'score' to show your score. Type anything else to continue ... ")
        begin = input("Your choice:")

        # Exit the game
        while True:
            if begin == "exit":
                print("Your score is", score, ".")
                input("Press enter to return to the main menu ... ")
                return 0
            
            # Show the score
            elif begin == "score":
                print("Your score is", score, ".")

            # The game itself
            else:
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
                    # Check if the guess is too high or too low (no equal because it is checked in the win or lose)
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
                else:
                    score += 1
                    begin = input("Type 'exit' to return to the main menu. Type 'score' to show your score. Type anything else to continue ... ")

    
    def rps():
        # Show basic information
        print("Welcome to the Rock, Paper, Scissors game!")
        print("Choose rock, paper, or scissors.")
        score = 0
        print("Type 'score' to show your score.")
        while True:
            userstart = input("Your choice: ")

            # Exit the game
            if userstart == "exit":
                print("Your score is", score, ".")
                input("Press enter to return to the main menu ... ")
                return 0
            
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
        input("Press enter to return to the main menu ... ")
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
    4. Rock, Paper, Scissors
───────────────────────────────────────────────────
Notes:
- Type the number of the tool or game you want to use to use it.
- Type 'exit' or press Ctrl+C or Alt+F4 to leave the program.
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
    elif menuuser == 2:
        Mathtools.isprime()
    elif menuuser == 3:
        Game.guess_num()
    elif menuuser == 4:
        Game.rps()
    elif menuuser == "exit":
        break

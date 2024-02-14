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
            print("You've guessed it! The number was", number, "and it took you", count, "tries out of", guesstop, "tries.")
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
        
        # return the random number
        return random.randint(small, big)


def menu():
    print("""
     -----Welcome to the Math Tools menu!-----
---------------------------------------------------
    Tools:
    1. Random number generator
---------------------------------------------------
    Games:
    2. Guess the number
    
(Type 'exit' to leave the program)""")
    
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
        Game.guess_num()
    elif menuuser == 2:
        Mathtools.randnum
    elif menuuser == "exit":
        break

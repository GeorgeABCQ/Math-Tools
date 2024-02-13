def guess_num():
    import random
    import time
    # Shows basic information
    score = 0
    print("Welcome to the number guessing game!")

    # Exit the game
    while True:
        print("If you win a game, you will get 1 point. If you lose, you will lose 1 point.")
        print("Type 'exit' to return to the main menu. Type 'score' to show your score. Type anything else to start the game ... ")
        begin = input("Your choice: ")

        if begin == "exit":
            print("Your score is", str(score), ".")
            input("Press enter to return to the main menu ... ")
            return 0
        
        # Show the score
        elif begin == "score":
            print("Your score is", str(score), ".")

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

            print("I'm thinking of a number between", str(smallnum), "and", str(bignum), ".")
            time.sleep(0.5)
            guesstop = input("How much guesses do you want you to have? (0 for no limit, default is 20): ")
            if guesstop == "0":
                guesstop = -1

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
                count += 1
                if guesstop != -1:
                    guess = input("guess " + str(count) + " out of " + str(guesstop) + " guesses. Please enter your guess: ")
                else:
                    guess = input("Please enter your guess: ")
                try:
                    guess = int(guess)
                except ValueError:
                    print("Invalid input.")
                    break
                # Check if the guess is too high or too low (no equal because it is checked in the win or lose section)
                if guess < number:
                    print("The number", str(guess), "is too low!")
                elif guess > number:
                    print("The number", str(guess), "is too high!")
            # Check for win or lose
            if guess == number:
                if guesstop != -1:
                    print("You've guessed it! The number was", str(number), ". It took you", str(count), "tries out of", str(guesstop), "tries. You win! +1 score.")
                else:
                    print("You've guessed it! The number was", str(number), ". It took you", str(count), "tries. You win! +1 score.")
                score += 1
            elif count == guesstop:
                print("You've run out of guesses! The number was", str(number), ". You've lost. -1 score.")
                score -= 1
            
            # Ask if the user wants to play again
            print("Your score is", str(score), ".")
            askexit = input("Do you want to play again? (Y/N): ")
            if askexit == "N" or askexit == "n" or askexit == "no" or askexit == "No":
                print("Your score is", str(score), ".")
                input("Press enter to return to the main menu ... ")
                break
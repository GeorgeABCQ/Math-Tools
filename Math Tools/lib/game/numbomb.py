def numbomb():
    import random
    print("Welcome to the number bomb game!")
    score = 0
    no = False
    while True:
        print("Type 'exit' to return to the main menu. Type 'rule' to show the rules. Type anything else to start the game ...")
        userstart = input("Your choice: ")
        if userstart == 'exit':
            input("Press enter to return to the main menu ... ")
            break
        elif userstart == 'rule':
            print("""The game is simple. You will try to not guess a number between 1 and 100 against a computer guessing randomly.
                    If you guess the number, you will lose 1 point. You will get 1 point if you don't guess the number in 10 attempts.
                    Each time you guess the number, the area you can guess will be smaller.""")
        else:
            bomb = random.randint(1, 100)
            guess = 0
            count = 0
            small = 1
            large = 100
            while count < 11:
                if no == False:
                    count += 1
                else:
                    no = False
                guess = input("This is your " + str(count) + " guess out of 10 guesses. Please enter your guess between " + str(small) + " and " + str(large) + " : ")
                try:
                    guess = int(guess)
                except ValueError:
                    print("Invalid input.")
                    no = True
                    continue
                if guess == bomb:
                    print("You've guessed the bomb! The number was", str(bomb), ".")
                    score -= 1
                    break
                elif guess < small or guess > large:
                    print("The number you typed is not in the range. Please type a number between", str(small), "and", str(large), ".")
                    no = True
                    continue
                elif guess != bomb:
                    print("You didn't guessed the bomb.")
                    if guess < bomb:
                        print("The bomb is higher than", str(guess), ".")
                        small = guess
                    elif guess > bomb:
                        print("The bomb is lower than", str(guess), ".")
                        large = guess
                
                comp = random.randint(small, large)
                print("The computer guessed", str(comp), ".")
                if comp == bomb:
                    print("The computer guessed the bomb! You won! +1 score. The number was", str(bomb), ".")
                    score += 1
                    break
                elif comp < bomb:
                    print("The computer didn't guessed the bomb. The bomb is higher than", str(comp), ".")
                    small = comp
                elif comp > bomb:
                    print("The computer didn't guessed the bomb. The bomb is lower than", str(comp), ".")
                    large = comp
            if count == 11:
                print("You've run out of guesses! The number was", str(bomb), ". You win! +1 score.")
                score += 1
            print("Your score is", str(score), ".")
            askexit = input("Do you want to play again? (Y/N): ")
            if askexit == "N" or askexit == "n" or askexit == "no" or askexit == "No":
                input("Press enter to return to the main menu ... ")
                break
    return 0
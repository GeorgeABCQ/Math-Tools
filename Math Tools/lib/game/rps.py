def rps():
    import random
    # Show basic information
    print("Welcome to the Rock, Paper, Scissors game!")
    score = 0
    count = 0
    count = 1
    no = False
    print("If you win a game, you will get 1 point. If you lose, you will lose 1 point. If it's a tie, the score won't change.")
    print("Type 'exit' to return to the main menu. Type anything else to start the game ...")
    userstart = input("Your choice: ")

    # Exit the game
    if userstart == "exit":
        print("Your score is", str(score), ".")
        input("Press enter to return to the main menu ... ")
        return 0

        # The game itself
    else:
        while True:
            user = input("Round " + str(count) + " . Choose rock, paper, or scissors: ")
            if user == "rock" or user == "paper" or user == "scissors" or user == "r" or user == "p" or user == "s":
                comp = random.choice(["rock", "paper", "scissors"])
                print("The computer chose", comp, ".")
                if user == comp:
                    print("It's a tie!")
                elif user == "rock" or user == "r":
                    if comp == "scissors":
                        print("You win! +1 score")
                        score += 1
                    else:
                        print("You lose! -1 score.")
                        score -= 1
                elif user == "paper" or user == "p":
                    if comp == "rock":
                        print("You win! +1 score")
                        score += 1
                    else:
                        print("You lose! -1 score.")
                        score -= 1
                elif user == "scissors" or user == "s":
                    if comp == "paper":
                        print("You win! +1 score")
                        score += 1
                    else:
                        print("You lose! -1 score.")
                        score -= 1
                else:
                    print("Invalid input. Please try again.")
                    no = True
                if no == False:
                    count += 1
                else:
                    no = False


                # Ask if the user wants to play again
                print("Your score is", str(score), ".")
                askexit = input("Do you want to play again? (Y/N): ")
                if askexit == "N" or askexit == "n" or askexit == "no" or askexit == "No":
                    print("Your score is", str(score), ".")
                    input("Press enter to return to the main menu ... ")
                    return 0
            
            #Show the score
            elif user == "score":
                print("Your score is", str(score), ".")
            
            elif user == "exit":
                print("Your score is", str(score), ".")
                input("Press enter to return to the main menu ... ")
                break
    return 0
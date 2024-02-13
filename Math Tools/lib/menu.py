def menu():
    import time
    print("""
                                     -----Welcome to the Math Tools menu!-----
  ╔═════════════════════════════════════════════════════╦════════════════════════════════════════════════════════════╗
  ║  Tools:                                             ║  Games:                                                    ║
  ║   1. Random number generator advanced               ║   10. Guess the number                                     ║
  ║   2. Prime dectector                                ║   11. Rock, paper, scissors                                ║
  ║   3. Find the factors                               ║   12. Number bomb                                          ║
  ║   4. Number factorization                           ║                                                            ║
  ║   5. Find the highest common factor (HCF)           ║                                                            ║
  ║   6. Find the lowest common multiple (LCM)          ║                                                            ║
  ║   7. Coprime detector                               ║                                                            ║
  ║   8. Basic calculator                               ║                                                            ║
  ║   9. Draw a graph                                   ║                                                            ║
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
            time.sleep(1)
            return goto
        else:
            return -2
    return goto

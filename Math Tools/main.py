# Import all of the modules
ModuleNotFound = False
try:
    from lib.game.guess_num import guess_num
    from lib.game.rps import rps
    from lib.game.numbomb import numbomb

    from lib.mathtools.calcaulator import calcaulator
    from lib.mathtools.coprime import coprime
    from lib.mathtools.find_factor import find_factor
    from lib.mathtools.HCF import HCF
    from lib.mathtools.int_factorization import int_factorization
    from lib.mathtools.isprime import isprime
    from lib.mathtools.LCM import LCM
    from lib.mathtools.randnum import randnum
    from lib.menu import menu
    from lib.mathtools.list_to_str import list_to_str
    from lib.mathtools.list_to_str_usingx import list_to_str_usingx
except ModuleNotFoundError:
    print("Error: One or more modules are missing. Please download the program again.")
    ModuleNotFound = True

# set menuuser to 0 to start the loop
if ModuleNotFound == False:
    menuuser = 0

    # menu to program
    while menuuser != "exit":
        menuuser = menu()
        if menuuser == 1:
            randnum()
        elif menuuser == 2:
            isprime(False, 0)
        elif menuuser == 3:
            find_factor(False, False, 0)
        elif menuuser == 4:
            int_factorization(False, False, 0)
        elif menuuser == 5:
            HCF(False, False, 0, 0, False)
        elif menuuser == 6:
            LCM(False, 0, 0)
        elif menuuser == 7:
            coprime(False, 0, 0)
        elif menuuser == 8:
            calcaulator()
        elif menuuser == 9:
            guess_num()
        elif menuuser == 10:
            rps()
        elif menuuser == 11:
            numbomb()
        elif menuuser == "exit":
            break

        print("""
















                """)

        # Check if the input is valid
        if type(menuuser) == int:
            if not(1 <= menuuser <= 11):
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

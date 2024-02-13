def calcaulator():
    import math
    try:
        from lib.mathtools.isprime import isprime
    except ModuleNotFoundError:
        try:
            from isprime import isprime
        except ModuleNotFoundError:
            print("The module 'isprime' is not found.")
            input("Press enter to return to the main menu ... ")
            return -2
    ans = None
    print("Welcome to the basic calculator!")
    while True:
        print("Type 'add' to add two numbers.")
        print("Type 'sub' to subtract two numbers.")
        print("Type 'mul' to multiply two numbers.")
        print("Type 'div' to divide two numbers.")
        print("Type 'exp' to find the power of a number.")
        print("Type 'sqrt' to find the square root of a number.")
        print("Type 'recip' to find the reciprocal of a number.")
        print("Type 'fact' to find the factorial of a number.")
        print("Type 'mod' to find the remainder of two numbers.")
        print("Type 'abs' to find the absolute value of a number.")
        print("Type 'log' to find the natrual logarithm of a number.")
        print("Type 'sin' to find the sine of a number.")
        print("Type 'cos' to find the cosine of a number.")
        print("Type 'tan' to find the tangent of a number.")
        print("Type 'prime' to check if a number is prime.")
        print("Type 'ans' to show the previous equation's answer.")
        print("Type 'exit' to return to the main menu.")
        choice = input("Your choice: ")
        if choice == "exit":
            break
        elif choice == "add":
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            ans = str(num1 + num2)
            print("The sum of", str(num1), "and", str(num2), "is", ans, ".")
        elif choice == "sub":
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            ans = str(num1 - num2)
            print("The difference between", str(num1), "and", str(num2), "is", ans, ".")
        elif choice == "mul":
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            ans = str(num1 * num2)
            print("The product of", str(num1), "and", str(num2), "is", ans, ".")
        elif choice == "div":
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            if num2 == 0:
                print("Cannot divide by 0.")
                break
            ans = str(num1 / num2)
            print("The quotient of", str(num1), "and", str(num2), "is", ans, ".")
        elif choice == "exp":
            num1 = input("Enter the base number: ")
            num2 = input("Enter the exponent: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            ans = str(num1 ** num2)
            print(str(num1), "to the power of", str(num2), "is", ans, ".")
        elif choice == "sqrt":
            num1 = input("Enter the number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            if num1 < 0:
                ans = str(-(num1) ** 0.5) + "i"
            else:
                ans = str(num1 ** 0.5)
            print("The square root of", str(num1), "is", ans, ".")
        elif choice == "recip":
            num1 = input("Enter the number: ")
            try:
                num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            if num1 == 0:
                print("Cannot divide by 0.")
                break
            ans = str(1 / num1)
            print("The reciprocal of", str(num1), "is", ans, ".")
        elif choice == "fact":
            num1 = input("Enter the number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = 1
            for i in range(1, num1 + 1):
                ans = ans * i
            ans = str(ans)
            print("The factorial of", str(num1), "is", ans, ".")
        elif choice == "mod":
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
                if num2 == int(num2):
                    num2 = int(num2)
                else:
                    num2 = float(num2)
            except ValueError:
                print("Invalid input.")
                break
            if num2 == 0:
                ans = "Cannot divide by 0."
                print(ans)
                break
            ans = str(num1 % num2)
            print("The remainder of", str(num1), "and", str(num2), "is", ans, ".")
        elif choice == "abs":
            num1 = input("Enter the number: ")
            try:
                if num1 == int(num1):
                    num1 = int(num1)
                else:
                    num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = abs(num1)
            print("The absolute value of", num1, "is", ans, ".")
        elif choice == "log":
            num1 = input("Enter the number: ")
            try:
                num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = math.log(num1)
            print("The natural logarithm of", num1, "is", ans, ".")
        elif choice == "sin":
            num1 = input("Enter the number: ")
            try:
                num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = math.sin(num1)
            print("The sine of", num1, "is", ans, ".")
        elif choice == "cos":
            num1 = input("Enter the number: ")
            try:
                num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = math.cos(num1)
            print("The cosine of", num1, "is", ans, ".")
        elif choice == "tan":
            num1 = input("Enter the number: ")
            try:
                num1 = float(num1)
            except ValueError:
                print("Invalid input.")
                break
            ans = math.tan(num1)
            print("The tangent of", num1, "is", ans, ".")
        elif choice == "prime":
            num1 = input("Enter the number: ")
            ans = isprime(True, num1)
            if ans == False:
                ans = str(num1) + " is not a prime number."
            elif ans == True:
                ans = str(num1) + " is a prime number."
            elif ans == 1:
                ans = str(num1) + " is not a prime number nor composite number."
            elif ans == 0 or ans == -1:
                ans = str(num1) + " cannot be defined as a prime number nor composite number."
            print(ans)
        elif choice == "exit":
            break
        elif choice == "ans":
            if ans == None:
                print("There is no previous equation's answer.")
            else:
                print("The previous equation's answer is:", ans)
        else:
            print("Invalid input.")
        input("Press enter to return to the selection menu ... ")
        print("""
















                """)
    return -2

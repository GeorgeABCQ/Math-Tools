def draw_graph(dev, eq):
    import sympy as sp
    if dev == False:
        eq = input("Enter the equation (^ is times. eq. 2*x + 3^2, DO NOT ADD y =): ")
        sym = input("Enter the variable (default is x): ")
    if len(sym) != 1:
        sym == 'x'
    try:
        x = sp.symbols(sym)
    except ValueError:
        x = sp.symbols('x')
    eq = sp.sympify(eq)
    try:
        sp.plot(eq, title="Graph of y = " + str(eq))
    except SyntaxError:
        print("Invalid equation.")
        input("Press enter to continue.")
        return -2
    except TypeError:
        print("sprt, log, sin, cos, tan, and other functions are not supported.")
        input("Press enter to continue.")
        return -2
    return 0

draw_graph(False, None)
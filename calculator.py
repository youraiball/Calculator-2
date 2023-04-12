"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

ops_w_2 = ["+", "-", "*", "/", "pow", "mod"]
quit_words = ["q", "quit", "Q", "Quit", "exit"]
while True:
    user_input = input("Enter your equation: ")
    tokens = user_input.split()

    if tokens[0] in quit_words:
        print("Have a nice day.")
        break

    if len(tokens) < 2 and tokens[0] not in quit_words:
        print("Incomplete input")
        continue
    elif len(tokens) == 2 or len(tokens) > 3:
        if tokens[0] in ops_w_2:
            print("This operation takes two numbers")
            continue

    if not tokens[1].isnumeric() or (tokens[0] in ops_w_2 and not tokens[2].isnumeric()):
        print("Pls enter an integer")
        continue

    if tokens[0] == "+":
        print(add(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "-":
        print(subtract(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "*":
        print(multiply(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "/":
        print(divide(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "square":
        print(square(float(tokens[1])))
    elif tokens[0] == "cube":
        print(cube(float(tokens[1])))
    elif tokens[0] == "pow":
        print(power(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == "mod":
        print(mod(float(tokens[1]), float(tokens[2])))
    else:
        print("Invalid Operator. Pls try again.")

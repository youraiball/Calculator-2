"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

ops_w_2 = ["+", "-", "*", "/", "pow", "mod"]
quit_words = ["q", "quit", "Q", "Quit", "exit"]

file = open("test.txt")
output_file = open("results.txt", "w")
has_not_quit = True
while has_not_quit:
    for line in file: #user_input = input("Enter your equation: ")
        print(line)
        tokens = line.strip().split()

        if tokens[0] in quit_words:
            print("Have a nice day.")
            has_not_quit = False
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

        result = None

        if tokens[0] == "+":
            result = add(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "-":
            result = subtract(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "*":
            result = multiply(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "/":
            result = divide(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "square":
            result = square(float(tokens[1]))
        elif tokens[0] == "cube":
            result = cube(float(tokens[1]))
        elif tokens[0] == "pow":
            result = power(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "mod":
            result = mod(float(tokens[1]), float(tokens[2]))
        else:
            result = "Invalid Operator. Pls try again."

        print(result)
        output_file.write(str(result) + "\n")

file.close()
output_file.close()

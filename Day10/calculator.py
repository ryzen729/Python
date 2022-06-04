logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))

    for symbols in operations:
        print(symbols)

    operation_symbol = input("Pick an operation form the line above: ")
    for k,v in operations.items():
        if k == operation_symbol:
            function_value = v
    answer = function_value(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    user_input = True
    while user_input:
        user_decide_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart.or 'e' to exit: ")
        if user_decide_input == "n":
            calculator()
        if user_decide_input == "e":
            user_input = False
            break
        operation_symbol = input("Pick another operation: ")
        num3 = int(input("What's the next number?: "))
        function_value = operations[operation_symbol]
        second_answer = function_value(answer,num3)
        print(f"{answer} {operation_symbol} {num3} = {second_answer}")
        answer = second_answer
        
calculator()  
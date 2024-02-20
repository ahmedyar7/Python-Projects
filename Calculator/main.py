from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    num1 = float(input("Enter the Number: "))
    for symbols in operations:
        print(symbols)

    flag = True
    while flag:

        operationSymbol = input("Enter The Operation Symbols: ")
        num2 = float(input("Enter the Second Number: "))

        calcFunction = operations[operationSymbol]
        answer = calcFunction(num1, num2)

        print(f"{num1} {operationSymbol} {num2} = {answer}")
        userInput = input(f"Do You want to Continue with {answer} y or n: ")

        if userInput == "y":
            num1 = answer
        else:
            flag = False
            calculator()


calculator()

# calculator_dp1

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b

def select_op(choice):
    if choice in ['+', '-', '*', '/', '^', '%']:
        try:
            first = input("Enter first number: ")
            if first == '$':
                return
            a = float(first)
        except ValueError:
            print("Not a valid number,please enter again")
            return

        try:
            second = input("Enter second number: ")
            if second == '$':
                return
            b = float(second)
        except ValueError:
            print("Not a valid number,please enter again")
            return

        try:
            if choice == '+':
                print(f"{a} + {b} = {add(a, b)}")
            elif choice == '-':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choice == '*':
                print(f"{a} * {b} = {multiply(a, b)}")
            elif choice == '/':
                print(f"{a} / {b} = {divide(a, b)}")
            elif choice == '^':
                print(f"{a} ^ {b} = {power(a, b)}")
            elif choice == '%':
                print(f"{a} % {b} = {remainder(a, b)}")
        except ZeroDivisionError:
            print("Something Went Wrong")
        except:
            print("Something Went Wrong")
    elif choice == '#':
        print("Done. Terminating")
        return 'terminate'
    elif choice == '$':
        return
    else:
        print("Unrecognized operation")

while True:
    print("Select operation.")
   

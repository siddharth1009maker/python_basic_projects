def add(a, b):
    answer = a+b
    print(f"The result of {a} + {b} is {answer}")


def sub(a, b):
    answer = a-b
    print(f"The result of {a} - {b} is {answer}")


def multiply(a, b):
    answer = a*b
    print(f"The result of {a} * {b} is {answer}")


def division(a, b):
    answer = a/b
    print(f"The result of {a} / {b} is {answer}")


while (True):
    print("A: Addition")
    print("B: Subtraction")
    print("C: Multiplication")
    print("D: Division")
    print("E: Exit")

    choice = input("Enter the choice: ")

    if (choice == 'a' or choice == 'A'):
        a = int(input("Enter the number"))
        b = int(input("Enter the number"))
        add(a, b)
    elif (choice == 'b' or choice == 'B'):
        a = int(input("Enter the number"))
        b = int(input("Enter the number"))
        sub(a, b)
    elif (choice == 'c' or choice == 'C'):
        a = int(input("Enter the number"))
        b = int(input("Enter the number"))
        multiply(a, b)
    elif (choice == 'd' or choice == 'D'):
        a = int(input("Enter the number"))
        b = int(input("Enter the number"))
        division(a, b)
    elif (choice == 'e' or choice == 'E'):
        break

# task 3
def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1' or choice == '+':
            result = num1 + num2
            op = '+'
        elif choice == '2' or choice == '-':
            result = num1 - num2
            op = '-'
        elif choice == '3' or choice == '*':
            result = num1 * num2
            op = '*'
        elif choice == '4' or choice == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                return
            result = num1 / num2
            op = '/'
        else:
            print("Invalid operation choice.")
            return

        print(f"{num1} {op} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    print("Welcome to the Calculator Program!")
    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 5:
            print("Goodbye!")
            break
        if choice > 5 or choice < 1:
            print("Invalid choice. Please try again.")
            print()
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        #else:
        #    print("Invalid choice. Please try again.")
        #    continue
        
        print(f"Result: {result:.2f}")
        print()

main()
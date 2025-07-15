# Welcome to our Fun Calculator 
# We're going to add, subtract, multiply, and divide two numbers like a boss! 😎

# So Step 1: we are going to define our variables. 
def num1():
    return float(input("Enter the first number: "))
def num2():
    return float(input("Enter the second number: "))

# Step 2: Let's do some math! 🧠
# We'll define functions for each operation so we can reuse them later.
def get_numbers():
    return num1(), num2()  # Get the two numbers from the user



def add(x, y): # type: ignore
    return x + y  # type: ignore #➕


def subtract(x, y):  # type: ignore
    return x - y  # type: ignore #➖


def multiply(x, y):  # type: ignore
    return x * y  # type: ignore #✖️


def divide(x, y):  # type: ignore
    if y == 0:
        return "Error! Division by zero."  # Avoiding math disasters! 😅
    return x / y  # type: ignore #➗

# Step 3: Now, let's ask the user what math operation they want to do!
def math_operation():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter the number of your choice (1-4): "))
    return choice


#step 4: Let's run the calculator!
def run_calculator():
    while True:
        choice = math_operation()
        if choice in [1, 2, 3, 4]:
            x, y = get_numbers()
            if choice == 1:
                print("Result:", add(x, y))
            elif choice == 2:
                print("Result:", subtract(x, y))
            elif choice == 3:
                print("Result:", multiply(x, y))
            elif choice == 4:
                print("Result:", divide(x, y))
        else:
            print("Invalid choice. Please select a valid operation.")
# Let's start the calculator!
if __name__ == "__main__":
    run_calculator()  # Start the calculator
# 🏁 And that's it! You've just made a mini-calculator! 😎

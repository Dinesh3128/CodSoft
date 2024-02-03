# Define the addition function
def add(x, y):
    return x + y

# Define the subtraction function
def subtract(x, y):
    return x - y

# Define the multiplication function
def multiply(x, y):
    return x * y

# Define the division function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Function to run the calculator
def calculator():
    while True:
        # Display the calculator menu
        print("Simple Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get the user's choice for the operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Validate the user's choice
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid input. Please enter a valid choice.")
            continue

        # Exit the program if the user chooses '5'
        if choice == '5':
            print("Exiting the program.")
            break

        # Get the user's input for two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            continue

        # Perform the selected operation and display the result
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

# Run the calculator function if the script is executed
if __name__ == "__main__":
    calculator()

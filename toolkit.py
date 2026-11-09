
# Personal Mini-Toolkit
# A program containing a calculator, a to-do list, and a number checker.


# Tool 1: Simple Calculator
# This tool performs basic mathematical calculations.
def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = first_number / second_number
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# This tool allows users to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' has been added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' has been removed.")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


# Tool 3: Number Checker
# This tool checks whether a number is even, odd, positive, negative, or zero.
def number_checker():
    print("\n--- NUMBER CHECKER ---")

    try:
        number = int(input("Enter a whole number: "))

        if number == 0:
            print("Your number is zero.")
        elif number > 0:
            print(f"{number} is a positive number.")
        else:
            print(f"{number} is a negative number.")

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main menu: keeps the program running until the user chooses Quit.
def main():
    print("Welcome to your Personal Mini-Toolkit!")
    print("Choose a tool to get started.")

    while True:
        print("\n====================================")
        print("       PERSONAL MINI-TOOLKIT")
        print("====================================")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Quit")
        print("====================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            simple_calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            number_checker()

        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit!")
            print("Goodbye and have a great day!")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please select 1, 2, 3, or 4.")


# Start the program.
if __name__ == "__main__":
    main()

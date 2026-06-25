import csv

filename = "expenses.csv"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            for row in reader:
                print(f"{row[0]} - ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found!")

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

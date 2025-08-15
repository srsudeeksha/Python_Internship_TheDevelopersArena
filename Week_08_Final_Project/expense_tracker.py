# week8_expense_tracker.py

import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    """Create CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Add a new expense entry."""
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Shopping, etc.): ")
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount < 0:
                print("❌ Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid amount. Enter a number.")
    description = input("Enter description: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    """Display all expenses."""
    if not os.path.exists(FILENAME):
        print("❌ No expenses found. Add some first.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))

def total_expenses():
    """Calculate and display total expenses."""
    if not os.path.exists(FILENAME):
        print("❌ No expenses found.")
        return

    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])

    print(f"💰 Total Expenses: ₹{total:.2f}")

def main():
    initialize_file()
    while True:
        print("\n📌 Daily Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("👋 Exiting. Have a great day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

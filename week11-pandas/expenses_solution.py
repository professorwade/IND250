import pandas as pd
import os
from datetime import datetime

# Configuration
FILE_NAME = "expenses.csv"

def initialize_df():
    """Ensures a CSV exists with the correct columns."""
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        # Define the structure of our tracker
        columns = ["Date", "Category", "Description", "Amount"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(FILE_NAME, index=False)
        return df

def edit_expense(location):
    df = pd.read_csv(FILE_NAME)
    row = df.iloc[location]

    row['Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp = input('Enter category [' + row['Category'] + '] : ')
    if temp != '':
        row['Category'] = temp
    temp = input('Enter Description [' + row['Description'] + '] : ')
    if temp != '':
        row['Description'] = temp
    temp = input('Enter Amount [' + str(row['Amount']) + '] : ')
    if temp != '':
        row['Amount'] = float(temp)

    df.iloc[location] = row
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Expense added successfully!")

def sort_expenses():
    df = pd.read_csv(FILE_NAME)
    sorted_df = df.sort_values(by='Amount')
    sorted_df.to_csv(FILE_NAME, index=False)

def average_expense():
    df = pd.read_csv(FILE_NAME)
    print("Average Expense: ", (df['Amount']).mean())

def add_expense(category, description, amount):
    """Appends a new expense to the CSV."""
    df = pd.read_csv(FILE_NAME)

    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Category": category,
        "Description": description,
        "Amount": float(amount)
    }

    # Append the new row and save
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Expense added successfully!")


def view_summary():
    """Displays data and basic stats using Pandas."""
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n📭 No expenses recorded yet.")
        return

    print("\n--- Current Expenses ---")
    print(df)

    # Use Pandas magic for a quick summary
    total = df["Amount"].sum()
    print(f"\n💰 Total Spent: ${total:.2f}")

    print("\n--- Spending by Category ---")
    print(df.groupby("Category")["Amount"].sum())

def main():
    initialize_df()

    while True:
        print("\n--- 📈 Expense Tracker CLI ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Edit Expense")
        print("4. Sort Expenses By Amount")
        print("5. Average Expense")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            cat = input("Enter Category (e.g., Food, Rent, Fun): ")
            desc = input("Short Description: ")
            amt = input("Amount: ")
            add_expense(cat, desc, amt)
        elif choice == "2":
            view_summary()
        elif choice == "3":
            location = input("Enter expense number: ")
            edit_expense(int(location))
        elif choice == "4":
            sort_expenses()
        elif choice == "5":
            average_expense()     
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
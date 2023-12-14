import sqlite3
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option: ")
    print("1. Enter expense")
    print("2. View expenses summary")


    choice = int(input())
    if choice == 1:
        date = input("Please enter the date (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")
        cur.execute("select distinct Category from expenses")

        categories = cur.fetchall()

        print("Select category: ")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}, {category[0]}")
        print(f"{len(categories) + 1}. New category")

        cat_choice = int(input())
        if cat_choice == len(categories) + 1:
            category = input("Enter category name: ")
        else:
            category = categories[cat_choice - 1][0]
        
        price = float(input("Enter price: "))

        cur.execute("insert into expenses (Date, Description, Category, Price) values (?, ?, ?, ?)", (date, description, category, price))

        conn.commit()

    elif choice == 2:
        print("Select an option:")
        print("1. View all expenses")
        print("2. View monthly expenses")

        view_choice = int(input())

        if view_choice == 1:
            cur.execute("select * from expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)

        elif view_choice == 2:
            print("Select an option:")
            print("1. Sum")
            print("2. By category")
            monthly_choice = int(input())

            if monthly_choice == 1:
                month = input("Enter month (MM): ")
                year = input("Enter year (YYYY): ")
                cur.execute("select sum(Price), strftime('%m', Date), strftime('%Y', Date) from expenses where strftime('%m', Date) = ? and strftime('%Y', Date) = ? group by Date", (month, year))
                expenses = cur.fetchall()
                for expense in expenses:
                    print(f"Total: ${expense[0]:.2f}, Month: {month}, Year: {year}")

            elif monthly_choice == 2:
                month = input("Enter month (MM): ")
                year = input("Enter year (YYYY): ")
                cur.execute("select Category, sum(Price) from expenses where strftime('%m', Date) = ? and strftime('%Y', Date) = ? group by Category", (month, year))
                expenses = cur.fetchall()
                for expense in expenses:
                    print(f"Category: {expense[0]}, Total: ${expense[1]:.2f}")

            else:
                exit()

        else:
            exit()

    elif choice > 2 or choice < 1:
        print("Choose only between 1 and 2!")

    repeat = input("Anything else to add(y/n)?: ")
    if repeat.lower() != "y":
        break

cur.close()
conn.close()
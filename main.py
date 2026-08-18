from datetime import datetime  
from storage import save_expenses,load_expenses
from reports import generate_pdf_report


expenses =load_expenses()

while True:
    print("\n-----Expense Tracker-----")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expense")
    print("4. Generate PDF Report")
    print("5. Exit")

    choice = input("Enter your choice from the following option")

    if choice == '1':
        print("Adding Expense...")
        while True:
            try:
                amount=float(input("Enter the amount : "))
                break
            except ValueError:
                print("Enter a valid amount in figures!!")
        while True:
            category = input("Enter the category :").strip()
            if category:
                break
            else:
                print("Category cannot be empty")
                continue
        while True:
            payment_method= input("enter the payment method(UPI/NETBANKING/CREDIT CARD/DEBIT CARD/CASH): ").strip().lower()
            if payment_method not in ["upi","netbanking","credit card","debit card","cash"]:
                print("enter valid payment method..")
            else:
                break
        while True:
            description = input("enter description of the expense:").strip()
            if not description:
                print("enter valid description..")
            else:    
                break
        date= datetime.now().strftime("%d-%m-%Y")  

        new_expense = {
            "amount": amount,
            "category": category,
            "payment_method": payment_method,
            "description": description,
            "date": date
            }

        expenses.append(new_expense)
        save_expenses(expenses)
        print(expenses)
        print("Expense Added Successfully!" )
        

    elif choice == '2':
        print("Removing Expense...")
        while True:
            try:
                n = int(input("enter the index number of the expense to remove:"))
            
                expense_to_remove=n-1
                if 0 <= expense_to_remove < len(expenses):
                    expenses.pop(n-1)
                    save_expenses(expenses)
                    print("Expense Removed Successfully!")
                    break   
                else:
                    print("Invalid index!")
            except ValueError:
                print("enter valid number!")


    elif choice == '3':
        print("Viewing Expense...")

        if not expenses:
            print("no expense added!!")
        else:
            total= 0.0
            for index, exp in enumerate(expenses):
                print("\n", f"{index + 1}.\n date: {exp['date']} \n category: {exp['category']} \n payment_method: {exp.get('payment_method', 'N/A')} \n amount: {exp['amount']} \n description: {exp['description']}")
                total += exp['amount']
            print("\n-x-x-x-x-x-x-x-x-x-x-x-")
            print("Total Expenses: ", total) 

    elif choice =='4':
        generate_pdf_report(expenses)

    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

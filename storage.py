import csv

def save_expenses(expenses_list):
    fields = ["amount", "category","payment_method", "description", "date"]
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses_list)

def load_expenses():
    loaded_list = []
    try:
        with open("expenses.csv","r") as f:
            for row in csv.DictReader(f):
                row["amount"] = float(row["amount"])
                loaded_list.append(row)
    except FileNotFoundError:
        print("No Data Found!")
    return loaded_list
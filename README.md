# Expense Manager

A simple command-line expense tracker written in Python. Add, view, and remove expenses, with data saved to a CSV file and exportable as a PDF report.

## Features

- **Add Expense** — Record an amount, category, payment method, description, and date (auto-filled with today's date).
- **Remove Expense** — Delete an expense by its list index.
- **View Expenses** — List all recorded expenses along with a running total.
- **Generate PDF Report** — Export all expenses into a formatted PDF (`expense_report.pdf`).
- **Persistent Storage** — Expenses are automatically saved to and loaded from `expenses.csv`.

## Project Structure

```
expense-manager-main/
├── main.py          # CLI entry point and menu loop
├── storage.py        # Handles reading/writing expenses to CSV
├── reports.py         # Generates the PDF expense report
├── expenses.csv        # Expense data (auto-created/updated)
└── README.md
```

## Requirements

- Python 3.7+
- [fpdf2](https://pypi.org/project/fpdf2/) (for PDF report generation)

## Installation

1. Clone or download this repository.
2. Install the required dependency:

   ```bash
   pip install fpdf2
   ```

## Usage

Run the app from the project directory:

```bash
python main.py
```

You'll see a menu with the following options:

```
-----Expense Tracker-----
1. Add Expense
2. Remove Expense
3. View Expense
4. Generate PDF Report
5. Exit
```

### 1. Add Expense
Enter the amount, category, payment method (UPI / Netbanking / Credit Card / Debit Card / Cash), and a description. The date is set automatically to the current date.

### 2. Remove Expense
Enter the index number of the expense (as shown in "View Expense") to delete it.

### 3. View Expense
Displays all recorded expenses with their date, category, payment method, amount, and description, plus the total amount spent.

### 4. Generate PDF Report
Creates `expense_report.pdf` in the project directory, containing a table of all expenses and the total.

### 5. Exit
Closes the application.

## Data Storage

Expenses are stored in `expenses.csv` with the following columns:

| Column         | Description                              |
|----------------|-------------------------------------------|
| amount         | Expense amount                           |
| category       | Expense category (e.g., food, travel)    |
| payment_method | Payment method used                      |
| description    | Short description of the expense         |
| date           | Date the expense was recorded (DD-MM-YYYY) |

The file is created automatically the first time you add an expense, and is updated after every add or remove operation.

## Notes

- Amounts must be entered as valid numbers; invalid input is rejected with a prompt to re-enter.
- Payment method input is case-insensitive and must match one of: `upi`, `netbanking`, `credit card`, `debit card`, `cash`.
- The PDF report will not be generated if there are no expenses recorded.

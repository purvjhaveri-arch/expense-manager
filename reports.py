from fpdf import FPDF
from pathlib import Path

def generate_pdf_report(expenses):
    if not expenses:
        print("No expenses to export!")
        return

    # 1. Create the PDF object
    pdf = FPDF()
    pdf.add_page()

    # 2. Set title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, text="Expense Report", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5) # Add a small blank line

    # 3. Set font for the table headers
    pdf.set_font("Arial", style="B", size=10)
    pdf.cell(30, 8, "Date", border=1)
    pdf.cell(35, 8, "Category", border=1)
    pdf.cell(30, 8, "Amount", border=1)
    pdf.cell(40, 8, "Payment", border=1)
    pdf.cell(55, 8, "Description", border=1)
    pdf.ln() # Move to the next line

    # 4. Set font for the table rows and loop through expenses
    pdf.set_font("Arial", size=9)
    total = 0.0
    for exp in expenses:
        pdf.cell(30, 8, str(exp["date"]), border=1)
        pdf.cell(35, 8, str(exp["category"]), border=1)
        pdf.cell(30, 8, f"${exp['amount']:.2f}", border=1)
        pdf.cell(40, 8, str(exp.get("payment_method", "N/A")), border=1)
        pdf.cell(55, 8, str(exp["description"]), border=1)
        pdf.ln()
        total += exp["amount"]

    # 5. Print total row
    pdf.set_font("Arial", style="B", size=10)
    pdf.ln(3)
    pdf.cell(200, 8, f"Total: ${total:.2f}", align="R")

    # 6. Save the PDF beside the project files.
    report_path = Path(__file__).resolve().parent / "expense_report.pdf"
    pdf.output(str(report_path))
    print(f"PDF report saved as '{report_path}'!")

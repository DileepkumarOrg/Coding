import tkinter as tk
def calculate_payment():
    amount = int(amount_entry.get())
    downpayment = int(DownPyment_entry.get())
    principle = amount-downpayment
    interest = float(interest_entry.get()) / 100
    years = int(years_entry.get())

    monthly_interest = interest / 12
    months = years * 12
    factor = ((1 + monthly_interest) ** months * monthly_interest) / ((1 + monthly_interest) ** months - 1)
    monthly_payment = principle * factor

    result_label.config(text=f"Monthly Payment: {monthly_payment:.2f}")


# Create the main window
root = tk.Tk()
root.title("EMI Calculator")

# Create the input fields
amount_label = tk.Label(root, text="Loan Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

DownPayment_label = tk.Label(root, text="Down Payment:")
DownPayment_label.grid(row=1, column=0, padx=10, pady=10)
DownPayment_entry = tk.Entry(root)
DownPayment_entry.grid(row=1, column=1, padx=10, pady=10)

interest_label = tk.Label(root, text="Interest Rate (%):")
interest_label.grid(row=2, column=0, padx=10, pady=10)
interest_entry = tk.Entry(root)
interest_entry.grid(row=2, column=1, padx=10, pady=10)

years_label = tk.Label(root, text="Loan Term (years):")
years_label.grid(row=3, column=0, padx=10, pady=10)
years_entry = tk.Entry(root)
years_entry.grid(row=3, column=1, padx=10, pady=10)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create the result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()

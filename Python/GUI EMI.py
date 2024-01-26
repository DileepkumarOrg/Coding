from tkinter import *

def calculate_EMI():
    principle = float(principle_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 1200
    duration = float(duration_entry.get())
    EMI = "{:.2f}".format(principle * interest_rate * (1 + interest_rate) ** duration / ((1 + interest_rate) ** duration - 1))
    result_label.config(text="EMI: Rs. " + str(EMI))

window = Tk()
window.title("EMI Calculator")

principle_label = Label(window, text="Principle amount (in Rs.): ")
principle_label.grid(row=0, column=0)

principle_entry = Entry(window)
principle_entry.grid(row=0, column=1)

interest_rate_label = Label(window, text="Interest rate (in % per annum): ")
interest_rate_label.grid(row=1, column=0)

interest_rate_entry = Entry(window)
interest_rate_entry.grid(row=1, column=1)

duration_label = Label(window, text="Duration (in months): ")
duration_label.grid(row=2, column=0)

duration_entry = Entry(window)
duration_entry.grid(row=2, column=1)

result_label = Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

calculate_button = Button(window, text="Calculate EMI", command=calculate_EMI)
calculate_button.grid(row=3, column=0)

window.mainloop()

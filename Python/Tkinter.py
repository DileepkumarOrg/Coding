from tkinter import *

window = Tk()
window.title("Billing System")
window.geometry("250x350")
window.configure(bg="Light Green")  # Use configure() method to set window background color

Label(window, text="Product code").grid(row=0, column=0)
Entry(window).grid(row=0, column=1)
Product = 'Product Code'
Label(window, text=Product).grid(row=0, column=2)  # Use Label() to display text label on the window

Label(window, text="Cost").grid(row=1, column=0)
Entry(window).grid(row=1, column=1)

Label(window, text="Discount").grid(row=2, column=0)
Entry(window).grid(row=2, column=1)

Label(window, text="Final cost").grid(row=3, column=0)
Entry(window).grid(row=3, column=1)

Button(window, text="Pay").grid(row=4, column=0)
Button(window, text="Cancel", command=window.destroy).grid(row=4, column=1)

window.mainloop()

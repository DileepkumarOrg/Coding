from tkinter import *

def calculate_total():
    # Get the price and quantity of each item
    shirt_price = float(shirt_price_entry.get())
    shirt_quantity = int(shirt_quantity_entry.get())
    trouser_price = float(trouser_price_entry.get())
    trouser_quantity = int(trouser_quantity_entry.get())
    saree_price = float(saree_price_entry.get())
    saree_quantity = int(saree_quantity_entry.get())

    # Calculate the total cost of the items
    total = shirt_price * shirt_quantity + trouser_price * trouser_quantity + saree_price * saree_quantity

    # Display the total cost in the output label
    total_label.configure(text=f"Total cost: {total:.2f} INR")

# Create the main window
window = Tk()
window.title("Online Billing for Clothes")
window.geometry("400x250")

# Create the widgets for entering the details of the items
shirt_label = Label(window, text="Shirt")
shirt_label.grid(row=0, column=0, padx=10, pady=5)
shirt_price_entry = Entry(window)
shirt_price_entry.grid(row=0, column=1, padx=10, pady=5)
shirt_quantity_entry = Entry(window)
shirt_quantity_entry.grid(row=0, column=2, padx=10, pady=5)

trouser_label = Label(window, text="Trouser")
trouser_label.grid(row=1, column=0, padx=10, pady=5)
trouser_price_entry = Entry(window)
trouser_price_entry.grid(row=1, column=1, padx=10, pady=5)
trouser_quantity_entry = Entry(window)
trouser_quantity_entry.grid(row=1, column=2, padx=10, pady=5)

saree_label = Label(window, text="Saree")
saree_label.grid(row=2, column=0, padx=10, pady=5)
saree_price_entry = Entry(window)
saree_price_entry.grid(row=2, column=1, padx=10, pady=5)
saree_quantity_entry = Entry(window)
saree_quantity_entry.grid(row=2, column=2, padx=10, pady=5)

# Create the button for calculating the total cost
calculate_button = Button(window, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=3, column=1, padx=10, pady=10)

# Create the label for displaying the total cost
total_label = Label(window, text="Total cost: 0.00 INR")
total_label.grid(row=4, column=1, padx=10, pady=5)

# Start the GUI event loop
window.mainloop()

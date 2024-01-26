
from tkinter import*

def addition():
    num1 = int(number1.get())
    num2 = int(number2.get())




window = Tk()
window.title("Addition")

number1 = label(window, text="Enter number 1")
number1.grid(row=0, column=0)


number2 = label(window, text="Enter number 2")
number2.grid(row=1, column=0)


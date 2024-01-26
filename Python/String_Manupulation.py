import tkinter as tk
from PIL import ImageTk, Image

# create a window
window = tk.Tk()

# open image file
image = Image.open('image.png')

# convert image to Tkinter PhotoImage object
photo = ImageTk.PhotoImage(image)

# create a Canvas widget to display the image
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.pack()

# start the GUI event loop
window.mainloop()

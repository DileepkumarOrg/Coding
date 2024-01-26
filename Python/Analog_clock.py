import tkinter as tk
import time

def update_clock():
    # Update digital clock
    current_time = time.strftime('%H:%M:%S')
    digital_clock.config(text=current_time)
    
    # Update analog clock
    current_datetime = time.localtime()
    hours = current_datetime.tm_hour
    minutes = current_datetime.tm_min
    seconds = current_datetime.tm_sec
    
    angle_seconds = seconds * 6
    angle_minutes = (minutes * 6) + (seconds * 0.1)
    angle_hours = (hours * 30) + (minutes * 0.5)
    
    canvas.delete('all')
    canvas.create_line(center_x, center_y, center_x + radius * 0.8 * math.sin(math.radians(angle_hours)), center_y - radius * 0.8 * math.cos(math.radians(angle_hours)), width=8, fill='black')
    canvas.create_line(center_x, center_y, center_x + radius * 0.9 * math.sin(math.radians(angle_minutes)), center_y - radius * 0.9 * math.cos(math.radians(angle_minutes)), width=4, fill='black')
    canvas.create_line(center_x, center_y, center_x + radius * 0.95 * math.sin(math.radians(angle_seconds)), center_y - radius * 0.95 * math.cos(math.radians(angle_seconds)), width=2, fill='red')
    
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title('Analog and Digital Clock')
root.geometry('400x300')

# Create canvas for analog clock
radius = 100
center_x = 200
center_y = 150
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Create digital clock label
digital_clock = tk.Label(root, font=('Helvetica', 36))
digital_clock.pack(pady=10)

# Start clock
update_clock()

# Run the program
root.mainloop()

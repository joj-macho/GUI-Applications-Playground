# tk_canvas_items.py
from tkinter import *

# Root Widget Creation
root = Tk()
root.title('Canvas Items')

# Canvas Widget
canvas_widget = Canvas(root, width=400, height=300, bg='white')
canvas_widget.pack()

# Draw a line on the canvas
canvas_widget.create_line(50, 50, 200, 50, fill='red', width=3)

# Draw a rectangle on the canvas
canvas_widget.create_rectangle(50, 100, 200, 200, outline='blue', fill='yellow')

# Display text on the canvas
canvas_widget.create_text(300, 150, text='Canvas Text', fill='green', font=('Arial', 16))

# Draw an oval on the canvas
canvas_widget.create_oval(250, 50, 350, 150, outline='purple', fill='cyan')

# Draw a polygon on the canvas
canvas_widget.create_polygon(100, 250, 150, 350, 200, 300, outline='orange', fill='pink')

# Draw an arc on the canvas
canvas_widget.create_arc(300, 250, 400, 350, start=0, extent=180, outline='brown', fill='yellow')

# Display a bitmap on the canvas
canvas_widget.create_bitmap(200, 200, bitmap='error')

# Embed a label widget within the canvas
label = Label(canvas_widget, text='Embedded Label')
canvas_widget.create_window(350, 200, window=label)

# Event Loop
root.mainloop()

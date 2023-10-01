from tkinter import *

# Root Widget Creation
root = Tk()
root.title('Canvas')

# Canvas Widget
canvas_widget = Canvas(root, width=300, height=200, bg = 'blue')
canvas_widget.pack() 

# Event Loop
root.mainloop()
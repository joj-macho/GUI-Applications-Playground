from tkinter import *
from math import sin, cos, pi
from time import localtime

def main():
    '''Main function to create the Tkinter window and start the clock.'''

    # Create a Tkinter root window
    root = Tk()
    root.title('Analog Clock')

    # Set the dimensions of the canvas
    canvas_width = 300
    canvas_height = 300

    # Create a canvas to draw the clock
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    # Draw the initial clock
    draw_clock(canvas, canvas_width, canvas_height)

    # Update the clock every second
    update_clock(canvas, canvas_width, canvas_height)

    # Start the Tkinter event loop
    root.mainloop()


def draw_clock(canvas, width, height):
    '''Draw the analog clock face with hour labels and clock hands.'''

    # Draw clock face at center of widget
    x_center = width / 2
    y_center = height / 2
    
    # Clock dimensions
    clock_radius = 0.9 * min(x_center, y_center)
    adjusted_radius = 0.9 * clock_radius
    hour_hand_length = 0.5 * min(x_center, y_center)
    minute_hand_length = 0.7 * min(x_center, y_center)

    # Draw clock face/circle
    canvas.create_oval(x_center - clock_radius, y_center - clock_radius,
                       x_center + clock_radius, y_center + clock_radius, outline='black', width=2)

    # Draw hour labels
    for i in range(1, 13):
        angle = pi / 6 * i
        x = x_center + adjusted_radius * sin(angle)
        y = y_center - adjusted_radius * cos(angle)
        canvas.create_text(x, y, text=str(i))


    # Get current time
    t = localtime()
    t_s = t[5]  # seconds
    t_m = t[4] + t_s / 60  # minutes
    t_h = t[3] % 12 + t_m / 60  # hours [0,12]

    # Draw hour hand
    angle = pi / 6 * t_h
    x = x_center + hour_hand_length * sin(angle)
    y = y_center - hour_hand_length * cos(angle)
    canvas.create_line(x_center, y_center, x, y, arrow=LAST, fill='black', width=4)

    # Draw minute hand
    angle = pi / 30 * t_m
    x = x_center + minute_hand_length * sin(angle)
    y = y_center - minute_hand_length * cos(angle)
    canvas.create_line(x_center, y_center, x, y, arrow=LAST, fill='black', width=2)

    # Draw second hand
    angle = pi / 30 * t_s
    x = x_center + minute_hand_length * sin(angle)
    y = y_center - minute_hand_length * cos(angle)
    canvas.create_line(x_center, y_center, x, y, arrow=LAST, fill='red')


def update_clock(canvas, width, height):
    '''Update the analog clock every second.'''

    # Clear the canvas
    canvas.delete(ALL)
    # Draw the clock
    draw_clock(canvas, width, height)
    # Schedule the update after 1000 milliseconds (1 second)
    canvas.after(1000, update_clock, canvas, width, height)


if __name__ == '__main__':
    main()

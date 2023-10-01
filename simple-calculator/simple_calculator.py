from tkinter import *
import tkinter as tk

# Constants for styling
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#63839c'


def main():
    '''Main function to create and run the simple calculator application.'''
    
    root = tk.Tk()
    root.title('Simple Calculator')

    # Content Frame
    main_frame = tk.Frame(root, borderwidth=4, bd=4, bg=MAIN_BG)
    main_frame.pack(expand=YES, fill=BOTH)

    # Entry Widget
    display = StringVar()
    display_entry = Entry(main_frame, relief=RIDGE, justify='right', textvariable=display, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 24))
    display_entry.pack(side=TOP, expand=YES, fill=BOTH)

    # Clear Button
    clear_button_frame = calculator_frame(root, TOP)
    button(clear_button_frame, LEFT, 'C', lambda button_obj=display: button_obj.set(''))

    # Equal Button
    equal_button_frame = calculator_frame(root, BOTTOM)
    button(equal_button_frame, LEFT, '=', lambda button_obj=display:  calculate(root, button_obj))

    # Operator and Number Buttons
    for num_button in ("789/", "456*", "123-", "0.+"):
        operator_num_frame = calculator_frame(root, TOP)
        for i in num_button:
            button(operator_num_frame, LEFT, i, lambda button_obj=display, q=i: button_obj.set(button_obj.get() + q))
    
    root.mainloop()


def calculator_frame(source, side):
    '''Create a frame for buttons with specified background color.'''

    frame_obj = Frame(source, borderwidth=4, bd=4, bg=MAIN_BG)
    frame_obj.pack(side=side, expand=YES, fill=BOTH)
    return frame_obj


def button(source, side, text, command=None):
    '''Create a button with specified text, command, and background color.'''

    button_obj = Button(source, text=text, command=command, bg=BTN_BG, font=('Arial', 24))
    button_obj.pack(side=side, expand=YES, fill=BOTH)
    return button_obj


def calculate(root, display):
    '''Calculate the result and display it in the entry field.'''

    try:
        result = eval(display.get())
        display.set(result)
    except ZeroDivisionError:
        display.set('ERROR: Division by zero')
    except Exception as e:
        display.set('ERROR')


if __name__ == "__main__":
    main()

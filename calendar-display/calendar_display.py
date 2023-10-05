import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import date

# Constants for styling
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#4E944F'


def main():
    '''Main function to create and run the calendar application.'''
    
    global window, month_var, year_var, month_box, year_box, current_month, current_year, calendar_input

    window = tk.Tk()
    window.geometry('500x600')
    window.title('Calendar Display')
    window.configure(bg=MAIN_BG)

    # Header Frame
    header_frame = tk.Frame(window, bg=MAIN_BG)
    header_frame.pack(expand=True, fill="both")

    # Entry Frame
    entry_frame = tk.Frame(window, bg=MAIN_BG)
    entry_frame.pack(expand=True, fill="both")

    # Integer variables for month and year
    month_var = tk.IntVar(entry_frame)
    year_var = tk.IntVar(entry_frame)
    current_month = date.today().month
    current_year = date.today().year
    month_var.set(current_month)
    year_var.set(current_year)

    month_label = tk.Label(entry_frame, text='Month:', bg=MAIN_BG, fg=LABEL_FG)
    month_label.place(x=120, y=0)
    year_label = tk.Label(entry_frame, text='Year:', bg=MAIN_BG, fg=LABEL_FG)
    year_label.place(x=275, y=0)
    
    # Spin Box widget for selecting the month
    month_box = tk.Spinbox(entry_frame, from_=1, to=12, width="4", textvariable=month_var)
    month_box.place(x=180, y=0)
    # Spin Box widget for selecting the year
    year_box = tk.Spinbox(entry_frame, from_=0000, to=3000, width="5", textvariable=year_var)
    year_box.place(x=325, y=0)

    # Result Frame
    result_frame = tk.Frame(window, bg=MAIN_BG)
    result_frame.pack(expand=True, fill="both")

    calendar_input = tk.Text(result_frame, width=21, height=8, relief=tk.RIDGE, borderwidth=2)
    calendar_input.pack(expand=False, fill=None)

    # Button Frame
    btn_frame = tk.Frame(window, bg=MAIN_BG)
    btn_frame.pack(expand=True, fill="both")

    # Show Button
    show_btn = tk.Button(btn_frame, text="Show", bg=BTN_BG, fg=LABEL_FG, command=show_calendar)
    show_btn.place(x=140, y=0)

    # Reset Button
    reset_btn = tk.Button(btn_frame, text="Reset", bg=BTN_BG, fg=LABEL_FG, command=reset_calendar)
    reset_btn.place(x=210, y=0)

    # Exit Button
    exit_btn = tk.Button(btn_frame, text="Exit", bg=BTN_BG, fg="red", command=exit_program)
    exit_btn.place(x=285, y=0)

    window.mainloop()


def show_calendar():
    '''Show the calendar based on user input.'''

    try:
        year = int(year_var.get())
        month = int(month_var.get())
        calendar_output = calendar.month(year, month)
        calendar_input.delete(1.0, 'end')
        calendar_input.insert('end', calendar_output)
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter valid numeric values for year and month.')


def reset_calendar():
    '''Reset the displayed calendar.'''
    
    calendar_input.delete(1.0, 'end')
    month_var.set(current_month)
    year_var.set(current_year)
    month_box.config(textvariable=month_var)
    year_box.config(textvariable=year_var)


def exit_program():
    '''Exit the application.'''

    window.destroy()


if __name__ == "__main__":
    main()

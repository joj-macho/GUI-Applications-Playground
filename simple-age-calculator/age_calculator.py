from tkinter import *
from datetime import date

# Color CONSTANTS
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#4E944F'


def main():
    '''Main function to create the tkinter window and initiate the age calculation.'''

    global window

    # MAIN WINDOW
    window = Tk()
    window.geometry('400x300+200+200')
    window.title('Age Calculator')
    window.config(bg=MAIN_BG)
    
    # HEADER FRAME
    # Label Widgets
    name_label = Label(text='Name', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
    name_label.grid(row=1, column=0, padx=50)

    year_label = Label(text='Year', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
    year_label.grid(row=2, column=0)

    month_label = Label(text='Month', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
    month_label.grid(row=3, column=0)

    day_label = Label(text='Day', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
    day_label.grid(row=4, column=0)

    # variable declaration + Entry Widgets
    global name_val, year_entry, month_entry, day_entry
    name_val = StringVar()
    name_entry = Entry(window, textvariable=name_val, bg=ENTRY_BG, fg=ENTRY_FG)
    name_entry.grid(row=1, column=1, padx=20, pady=8)

    year_val = StringVar()
    year_entry = Entry(window, textvariable=year_val, bg=ENTRY_BG, fg=ENTRY_FG)
    year_entry.grid(row=2, column=1, pady=8)

    month_val = StringVar()
    month_entry = Entry(window, textvariable=month_val, bg=ENTRY_BG, fg=ENTRY_FG)
    month_entry.grid(row=3, column=1, pady=8)

    day_val = StringVar()
    day_entry = Entry(window, textvariable=day_val, bg=ENTRY_BG, fg=ENTRY_FG)
    day_entry.grid(row=4, column=1, pady=8)

    # BUTTON FRAME
    calculate_btn = Button(text='Calculate', command=calculate_age, bg=BTN_BG)
    calculate_btn.grid(row=5, column=1, pady=10)

    # Run application
    window.mainloop()


def calculate_age():
    '''This function calculates the age of a person using the datetime module.'''

    # current date
    current_date = date.today()

    # get birthdate
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))

    # calculate age: dob-currentdate
    age = current_date.year - birth_date.year
    
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1

    # show results
    Label(window, text=f'{name_val.get()}\'s age is {age} years.', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12)).grid(row=6, column=1)
    

if __name__ == "__main__":
    main()

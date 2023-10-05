from tkinter import *

# Constants for styling
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#63839c'


def main():
    '''Main function to create and run the temperature converter application.'''
    
    root = Tk()
    root.title('Temperature Converter')

    # Content Frame
    main_frame = Frame(root, bg=MAIN_BG)
    main_frame.pack()

    # Entry Widgets for Temperature Input and Selection
    temp_label = Label(main_frame, text='Temperature:', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    temp_label.grid(row=0, column=0, padx=10, pady=5)
    temp_entry = Entry(main_frame, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    temp_entry.grid(row=0, column=1, padx=10, pady=5)

    from_label = Label(main_frame, text='From:', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    from_label.grid(row=1, column=0, padx=10, pady=5)
    from_var = StringVar(value='Celsius')
    from_menu = OptionMenu(main_frame, from_var, 'Celsius', 'Fahrenheit')
    from_menu.config(bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    from_menu.grid(row=1, column=1, padx=10, pady=5)

    to_label = Label(main_frame, text='To:', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    to_label.grid(row=2, column=0, padx=10, pady=5)
    to_var = StringVar(value='Fahrenheit')
    to_menu = OptionMenu(main_frame, to_var, 'Celsius', 'Fahrenheit')
    to_menu.config(bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    to_menu.grid(row=2, column=1, padx=10, pady=5)

    # Convert Button
    convert_button = Button(main_frame, text='Convert', bg=BTN_BG, font=('Arial', 18),
                            command=lambda: convert_temperature(temp_entry.get(), from_var.get(), to_var.get(), result_var))
    convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    # Result Frame
    result_var = StringVar()
    result_label = Label(main_frame, textvariable=result_var, fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()


def convert_temperature(temp_str, from_unit, to_unit, result_var):
    '''Convert temperature and update the result variable.'''

    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    try:
        temperature = float(temp_str)
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                result = celsius_to_fahrenheit(temperature)
            else:
                result = temperature
        else:
            if to_unit == 'Celsius':
                result = fahrenheit_to_celsius(temperature)
            else:
                result = temperature

        result_var.set(f'Result: {result:.2f} {to_unit}')

    except ValueError:
        result_var.set('ERROR: Invalid input')


if __name__ == "__main__":
    main()

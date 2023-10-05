from tkinter import *

# Constants for styling
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#63839c'

# Conversion factors
CONVERSION_FACTORS = {
    'Gram (g)': 1,
    'Kilogram (kg)': 0.001,
    'Milligram (mg)': 1000,
    'Pound (lb)': 0.00220462,
    'Ounce (oz)': 0.035274,
    'Metric Ton (ton)': 1e-6
}

def main():
    '''Main function to create and run the weight converter application.'''
    
    root = Tk()
    root.title('Weight Converter')

    # Content Frame
    main_frame = Frame(root, bg=MAIN_BG)
    main_frame.pack()

    # Entry Widgets for Weight and Unit
    weight_label = Label(main_frame, text='Weight:', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    weight_label.grid(row=0, column=0, padx=10, pady=5)
    weight_entry = Entry(main_frame, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    weight_entry.grid(row=0, column=1, padx=10, pady=5)

    unit_label = Label(main_frame, text='Unit:', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    unit_label.grid(row=1, column=0, padx=10, pady=5)
    # Creating a dropdown menu for selecting the unit of conversion
    unit_var = StringVar(value=list(CONVERSION_FACTORS.keys())[0])
    unit_menu = OptionMenu(main_frame, unit_var, *sorted(CONVERSION_FACTORS.keys(), key=lambda x: CONVERSION_FACTORS[x]))
    unit_menu.config(bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    unit_menu.grid(row=1, column=1, padx=10, pady=5)

    # Convert Button
    convert_button = Button(main_frame, text='Convert', bg=BTN_BG, font=('Arial', 18),
                            command=lambda: convert_weight(weight_entry.get(), unit_var.get(), display_frame))
    convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Result Frame
    display_frame = Frame(root, bg=MAIN_BG)
    display_frame.pack()

    root.mainloop()

def convert_weight(weight, unit, display_frame):
    '''Convert weight to all available weight units and display the results.'''

    try:
        weight = float(weight)

        # Convert weight to grams if it's not in grams
        selected_unit_conversion = CONVERSION_FACTORS[unit]
        weight_in_grams = weight / selected_unit_conversion

        results = {unit: weight_in_grams * unit_conversion for unit, unit_conversion in CONVERSION_FACTORS.items()}

        # Clear any previous result labels
        for widget in display_frame.winfo_children():
            widget.destroy()
            
        # Display the converted mass for each unit
        for i, (unit, result) in enumerate(results.items()):
            result_label = Label(display_frame, text=f'{unit}: {result:.6f}', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
            result_label.grid(row=i, column=0, padx=10, pady=2, sticky='w')

    except ValueError:
        # Display an error message if input is invalid
        error_label = Label(display_frame, text='ERROR: Invalid input', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
        error_label.grid(row=0, column=0, padx=10, pady=2, sticky='w')


if __name__ == "__main__":
    main()

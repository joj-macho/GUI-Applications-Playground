from tkinter import *

# Constants for styling
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#63839c'


def main():
    '''Main function to create and run the BMI calculator application.'''
    
    root = Tk()
    root.title('BMI Calculator')

    # Content Frame
    main_frame = Frame(root, borderwidth=4, bd=4, bg=MAIN_BG)
    main_frame.pack(side=TOP, expand=YES, fill=BOTH)

    # Entry Widgets for Height and Weight
    height_label = Label(main_frame, text='Height (cm):', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    height_label.pack(side=TOP, fill=BOTH)
    height_entry = Entry(main_frame, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    height_entry.pack(side=TOP, fill=BOTH)

    weight_label = Label(main_frame, text='Weight (kg):', fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 18))
    weight_label.pack(side=TOP, fill=BOTH)
    weight_entry = Entry(main_frame, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 18))
    weight_entry.pack(side=TOP, fill=BOTH)

    # Calculate Button
    calculate_button = Button(main_frame, text='Calculate BMI', bg=BTN_BG, font=('Arial', 24), command=lambda: calculate_bmi(height_entry.get(), weight_entry.get(), display))
    calculate_button.pack(side=LEFT, expand=YES, fill=BOTH)

    # Display BMI Result
    display = StringVar()
    result_label = Label(root, textvariable=display, fg=LABEL_FG, bg=MAIN_BG, font=('Arial', 24))
    result_label.pack(side=TOP, fill=BOTH)

    root.mainloop()


def calculate_bmi(height, weight, display):
    '''Calculate BMI and display the result with classification.'''

    try:
        height_cm = float(height)
        weight_kg = float(weight)

        bmi = weight_kg / ((height_cm / 100) ** 2)
        classification = classify_bmi(bmi)
        display.set(f'Your BMI is: {bmi:.2f}\nYou are {classification}')
    except ValueError:
        display.set('ERROR: Invalid input')


def classify_bmi(bmi):
    '''Classify BMI based on given ranges.'''

    if bmi < 16:
        return 'Severely Thin'
    elif 16 <= bmi < 17:
        return 'Moderately Thin'
    elif 17 <= bmi < 18.5:
        return 'Mildly Thin'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    elif 30 <= bmi < 35:
        return 'Obese Class I'
    elif 35 <= bmi < 40:
        return 'Obese Class II'
    else:
        return 'Obese Class III'


if __name__ == "__main__":
    main()

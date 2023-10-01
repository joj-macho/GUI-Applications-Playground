import tkinter as tk
from time import strftime


def main():
    '''Main function to create the tkinter window and start the digital clock.'''

    # Create the main window
    global root
    root = tk.Tk()
    root.title('Digital Clock')

    # Create a label to display the time
    global label
    label = tk.Label(root, font=('Arial', 48), background='black', foreground='white')
    label.pack(padx=20, pady=20)

    # Update the time initially and then every second
    update_time()

    # Start the tkinter main loop
    root.mainloop()


def update_time():
    '''Update the displayed time every second.'''
    
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)  # Update every second


if __name__ == "__main__":
    main()

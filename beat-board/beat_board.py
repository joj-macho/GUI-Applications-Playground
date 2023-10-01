from tkinter import *
from playsound import playsound
from threading import Thread

# Sound locations
sound_locations = [
    './beat-board/assets/Kick.wav',
    './beat-board/assets/hiHat.wav',
    './beat-board/assets/snare.wav',
    './beat-board/assets/Pad1.wav',
    './beat-board/assets/Pad2.wav',
    './beat-board/assets/Pad3.wav',
    './beat-board/assets/Pad4.wav',
    './beat-board/assets/Pad5.wav',
    './beat-board/assets/Pad6.wav'
]


def main():
    '''Main function to create and run the beat board application.'''
    
    global main_window
    main_window = Tk()
    main_window.resizable(False, False)
    main_window.title('Beat Board')

    create_layout(main_window, sound_locations)

    main_window.mainloop()


def play_sound(sound_location):
    '''Play a sound using the playsound library.'''

    def play():
        playsound(sound_location)

    sound_thread = Thread(target=play)
    sound_thread.start()


def create_buttons(frame, sound_locations):
    '''Create buttons for each sound and bind them to play the corresponding sound.'''

    button_texts = ["Kick", "Hi-Hat", "Snare", "Pad 1", "Pad 2", "Pad 3", "Pad 4", "Pad 5", "Pad 6"]
    bind_keys = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']

    for i in range(len(button_texts)):
        button = Button(text=button_texts[i], height=5, width=10)
        frame.bind(bind_keys[i], lambda event, loc=sound_locations[i]: play_sound(loc))
        button.bind("<Button-1>", lambda event, loc=sound_locations[i]: play_sound(loc))
        button.grid(row=i // 3, column=i % 3)


def create_layout(main_window, sound_locations):
    '''Create the layout of the beat board application.'''

    # Creates the Frame
    frame_a = Frame(master=main_window, width=500, height=500, bg="black")
    frame_a.grid(rowspan=3, columnspan=3)
    frame_a.focus_set()

    create_buttons(frame_a, sound_locations)


if __name__ == "__main__":
    main()

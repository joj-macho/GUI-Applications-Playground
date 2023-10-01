##########################################
# Import Modules
##########################################
from tkinter import *
from tkinter import messagebox


##########################################
# CONSTANTS
##########################################
# Colors
MAIN_BG = '#2D4263'
ENTRY_BG = '#191919'
LABEL_FG = '#ECDBBA'
ENTRY_FG = 'white'
BTN_BG = '#4E944F'

##########################################
# UI Setup
##########################################
# ----------------------------
        # MAIN WINDOW
# ----------------------------
window = Tk()
window.geometry('650x400+200+300')
window.title('Address Book')
window.config(bg=MAIN_BG)
# ----------------------------
        # HEADER SECTION
# ----------------------------
# Details in Phonebook: Name, Phone Number, email, address(city, zip code)
leftFrame = Frame(window, bg=MAIN_BG)
leftFrame.pack(expand=True, fill=BOTH, side=LEFT)

detailsFrame = Frame(leftFrame, bg=MAIN_BG)
detailsFrame.pack(padx=15 ,pady=20)
# header
titleLabel = Label(detailsFrame, text='Address Book', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 18))
titleLabel.grid(row=0, column=1, pady=15)

# Name input
nameVar = StringVar()
nameLabel = Label(detailsFrame, text='Name:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
nameLabel.grid(row=1, column=0, sticky=W, pady=8)

nameEntry = Entry(detailsFrame, textvariable=nameVar, width=35, bg=ENTRY_BG, fg=ENTRY_FG)
nameEntry.grid(row=1, column=1)

# Phone number input
phoneVar = StringVar()
phoneLabel = Label(detailsFrame, text='Phone:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
phoneLabel.grid(row=2, column=0, sticky=W, pady=8)

phoneEntry = Entry(detailsFrame, textvariable=phoneVar, width=35, bg=ENTRY_BG, fg=ENTRY_FG)
phoneEntry.grid(row=2, column=1)

# Email input
emailVar = StringVar()
emailLabel = Label(detailsFrame, text='Email:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
emailLabel.grid(row=3, column=0, sticky=W)

emailEntry = Entry(detailsFrame, textvariable=emailVar, width=35, bg=ENTRY_BG, fg=ENTRY_FG)
emailEntry.grid(row=3, column=1)

# Address input: incl. City, street name, zip code
cityVar = StringVar()
cityLabel = Label(detailsFrame, text='City:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
cityLabel.grid(row=4, column=0, sticky=W, pady=8)

cityEntry = Entry(detailsFrame, textvariable=cityVar, width=35, bg=ENTRY_BG, fg=ENTRY_FG)
cityEntry.grid(row=4, column=1)

# detailFrame = Frame(window)
# detailFrame.pack()
streetVar = StringVar()
streetLabel = Label(detailsFrame, text='Street:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
streetLabel.grid(row=5, column=0, sticky=W, pady=8)

streetEntry = Entry(detailsFrame, textvariable=streetVar, width=35, bg=ENTRY_BG, fg=ENTRY_FG)
streetEntry.grid(row=5, column=1)

zipVar = StringVar()
zipLabel = Label(detailsFrame, text='Zip:', fg=LABEL_FG, bg=MAIN_BG, font=('monospace', 12))
zipLabel.grid(row=6, column=0, sticky=W)

zipEntry = Entry(detailsFrame, textvariable=zipVar, bg=ENTRY_BG, fg=ENTRY_FG)
zipEntry.grid(row=6, column=1)

# Display Contact Textbox
displayFrame = Frame(window)
displayFrame.pack( side=LEFT, padx=10 ,pady=20)

listboxItem = Listbox(displayFrame, height=14, width=30, bg=ENTRY_BG, fg=ENTRY_FG)
listboxItem.pack(fill=BOTH, expand=True)




##########################################
# FUNCTIONS
##########################################
contactList = [
    ['John Reese', '022132225', 'johnreese@email.com', 'New York', 'Library St', '552']
]

def selectContact():
    '''This function points curser on contact'''
    return int(listboxItem.curselection()[0])

def selectContacts():
    '''This function responds on clicking contact'''
    contactList.sort()
    listboxItem.delete(0, END)
    for i in contactList:
        # print(i)
        listboxItem.insert(END, i[0])

def addContact():
    contactList.append([nameVar.get(), phoneVar.get(), emailVar.get(), cityVar.get(), streetVar.get(), zipVar.get()])

    selectContacts()


def viewContact():
    name, number, email, city, street, zipCode = contactList[selectContact()]

    nameVar.set(name)
    phoneVar.set(number)
    emailVar.set(email)
    cityVar.set(city)
    streetVar.set(street)
    zipVar.set(zipCode)

def deleteContact():
    del contactList[selectContact()]
    
    selectContacts()

def exitApp():
    closeApp = messagebox.askyesno('Exit', 'Do you want to Exit App?')
    # If sure then close app
    if closeApp > 0:
        window.destroy()

# selectContacts()


# ----------------------------
        # BUTTON SECTION
# ----------------------------

btnFrame = Frame(leftFrame)
btnFrame.pack(padx=15 ,pady=20)

addBtn = Button(btnFrame, text='Add', command=addContact, bg=BTN_BG)
addBtn.grid(row=1, column=1)

viewBtn = Button(btnFrame, text='View', command=viewContact, bg=BTN_BG)
viewBtn.grid(row=1, column=2)

deleteBtn = Button(btnFrame, text='Delete', command=deleteContact, bg=BTN_BG)
deleteBtn.grid(row=1, column=3)

exitBtn = Button(btnFrame, text='Exit', command=exitApp, bg=BTN_BG, fg='red')
exitBtn.grid(row=1, column=4)


# Run application
window.mainloop()
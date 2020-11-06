#Importing the necessary modules/packages for this program/application
import tkinter
import tkinter.font as tkFont
import sys
import ast
from tkinter import messagebox
from tkinter import *

#Initialize the Intro Window
user_input = tkinter.Tk()

#Sets the position and size of the application
user_input.geometry('210x75+0+0')

#Gives title to application
user_input.title("Username?")

#Change the icon of the application
user_input.iconbitmap("./images/PalPadSprite.ico")

v1 = StringVar()
v2 = StringVar()

#Checks if username was saved before
def checkName(string_to_search):
    global contactpos 
    # Open the file in read only mode
    with open('username.txt', 'r') as read_obj:
        # Read all lines in the file one by one
        for position, line in enumerate(read_obj):
            # For each line, check if line contains the string
            if string_to_search in line:
                contactpos = position
                return string_to_search
    return ""

def getContacts():
    global contacts
    with open('contacts.txt', 'r') as read_obj:
        contacts = read_obj.readlines(contactpos)
        contacts = ast.literal_eval(contacts[0])
        print(contacts)

#Used to destroy the intro window, and allow
#the main window to run
def enter():
    global contacts
    #Checking if name have been filled
    if len(username.get()) > 0:
        if v1.get() == checkName(v1.get()):
            print("Welcome Back!")
            getContacts()
    else:
        #Alerts User that name has not been filled out 
        messagebox.showerror("Error", "Name has not been filled")

    user_input.destroy()

#The procedure for the close button on the intro window
def close():
    sys.exit()

#Setting up the title/question
username_title = tkinter.Label(user_input, text="What is your first name?")
username_title.pack()

#Setting the Username Entry 
username = tkinter.Entry(user_input, width=30, textvariable = v1)
username.pack()

#Setting up the Enter Button
enterButton = tkinter.Button(user_input, text = "Enter", command = enter)
enterButton.pack()

#Will completely destroy the program >:)
user_input.protocol('WM_DELETE_WINDOW', close)

#Runs the Tkinter event loop
user_input.mainloop()

#Initialize the GUI/Application
gui = tkinter.Tk()

#Gives title to application
gui.title('Contact Book')

#Sets the position and size of the application
gui.geometry('500x500+0+0')

#Change the icon of the application
gui.iconbitmap("./images/PalPadSprite.ico")

#Changes style and font of text
title_fontStyle = tkFont.Font(family = "Lucida Grande", size = 24, weight = tkFont.BOLD, underline = True)
contact_fontStyle = tkFont.Font(family = "Times", size = 14)

#Initializing the list for the Contacts
if v1.get() == checkName(v1.get()):
    contacts = contacts
else:
    contacts = []


#Used whenever the Listbox needs to be updated
def updateList():
    global contact_list
    contact_list.delete(0, END)
    for i in range(len(contacts)):
        contact_list.insert(END, contacts[i][0] + " (" + str(contacts[i][1]) + ")")

#The procedure for the 'Add' button when it is clicked
def add():
    #Checking if requirements have been filled
    if len(name.get()) > 0 and len(num.get()) > 0:
        #Checking if Phone Number is a number
        try:
            int(num.get())
            contacts.append([name.get(), int(num.get())])
            updateList()
        except ValueError:
            #Alerts User that phone number is invalid
            messagebox.showerror("Error", "Invalid Phone Number") 
    else:
       #Alerts User that not all requirements have been filled out 
       messagebox.showerror("Error", "Requirements have not been filled")
    
    add_contact.destroy()

#The procedure for the 'Remove' button when it is clicked     
def remove():
    #Storing the response into a vairable, if 'yes' then remove contact
    response = messagebox.askyesno("Remove Contact?", "Are you sure you want to remove this contact?")
    if response == 1:
        contacts.pop(list(contact_list.get(0, END)).index(contact_list.get(ANCHOR)))
        updateList()
        select_contact.destroy()

#The pop-up window for the 'Plus' button when it is clicked
def AddContact():
    #Setting up pop-up window like main window
    global add_contact
    add_contact = tkinter.Toplevel(gui)
    add_contact.title("Add Contact")
    add_contact.geometry("300x200")
    add_contact.iconbitmap("./images/PalPadSprite.ico")

    #Setting up the Label and Entry for the 'Name' of the contact
    global name
    name = tkinter.Entry(add_contact, width = 20)
    name.place(x = 112.5, y = 75)

    name_label = tkinter.Label(add_contact, text = "Name: ")
    name_label.place(x = 10, y = 75)

    #Setting up the Label and Entry for the 'Phone Number' of the contact
    global num
    num = tkinter.Entry(add_contact, width = 20)
    num.place(x = 112.5, y = 125)

    num_label = tkinter.Label(add_contact, text = "Phone Number: ")
    num_label.place(x = 10, y = 125)

    #Setting up the button to add the contact, using the procedure 'add()'
    addButton = tkinter.Button(add_contact, text = "Add", bg = "white", fg = "blue", width = 5, command = add)
    addButton.pack()

#The pop-up window when a contact has been double-clicked
def selectContact(event):
    #Setting up pop-up window like main window
    global select_contact
    select_contact = tkinter.Toplevel(gui)
    select_contact.title("Contact")
    select_contact.geometry("333x333")
    select_contact.iconbitmap("./images/PalPadSprite.ico")

    #Setting up Label for Contact name
    contact_name = tkinter.Label(select_contact, text = contacts[list(contact_list.get(0, END)).index(contact_list.get(ANCHOR))][0])
    contact_name.place(x = 333/2, y = 166, anchor = "center")

    #Setting up Message button, but doesn't do anything, just graphical purposes
    msg = tkinter.Button(select_contact, text = "Message", fg = "blue", borderwidth = 0)
    msg.place(x = 333/2 - 83.25, y = 225, anchor = "center")

    #Setting up Call button, but doesn't do anything, just graphical purposes
    call = tkinter.Button(select_contact, text = "Call", fg = "blue", borderwidth = 0)
    call.place(x = 333/2, y = 225, anchor = "center")

    #Setting up the 'Remove' button, using the procedure 'remove()'
    removeButton = tkinter.Button(select_contact, text = "Remove", fg = "blue", borderwidth = 0, command = remove)
    removeButton.place(x = 333/2 + 83.25, y = 225, anchor = "center")


''' The two sorting algorithms are used to sort either the names 
or the phone numbers of the contact list. It takes the list and 
separates it into three different lists. It then chooses a random
item and compares either the name or the number with the items
of the contact list. After sorting them into different lists, it
returns the all three lists in order from smallest to greatest.
'''
def num_sort(array):
    from random import randint
   
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)][1]

    for item in array:
        if item[1] < pivot:
            low.append(item)
        elif item[1] == pivot:
            same.append(item)
        elif item[1] > pivot:
            high.append(item)

    return num_sort(low) + same + num_sort(high)

def name_sort(array):
    from random import randint

    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)][0]

    for item in array:
        if item[0] < pivot:
            low.append(item)
        elif item[0] == pivot:
            same.append(item)
        elif item[0] > pivot:
            high.append(item)

    return name_sort(low) + same + name_sort(high)

#The procedure whenever one of the Radio Buttons in 'sortContacts()' is selected
def sortList(value):
    global contacts
    if value == 1:
        #Sort by Name
        contacts = name_sort(contacts)
    else:
        #Sort by Number
        contacts = num_sort(contacts)
    updateList()

#The pop-up window when the 'Sort' button is clicked
def sortContacts():
    #Setting up pop-up window like main window
    global sort_contact
    sort_contact = tkinter.Toplevel(gui)
    sort_contact.title("Sort")
    sort_contact.geometry("200x200")
    sort_contact.iconbitmap("./images/PalPadSprite.ico")

    #Used to get the value of whichever button is selected
    global sort
    sort =  IntVar()

    #Setting up Radio Buttons to give user options for
    #how they want to sort their contacts
    tkinter.Radiobutton(sort_contact, text = "Name", variable = sort, value = 1, command = lambda: sortList(sort.get())).place(x = 0, y = 0)
    tkinter.Radiobutton(sort_contact, text = "Number", variable = sort, value = 2, command = lambda: sortList(sort.get())).place(x = 0, y = 50)

#The procedure to save username and contacts
def saveContacts():
    #Open their separate files and add them
    with open('username.txt', 'a') as userfile:
        userfile.write(v1.get())
    with open('contacts.txt', 'a') as contactfile:
        contactfile.write(str(contacts))

   
#Setting up the Title label
title = tkinter.Label(gui, text = v1.get() + "'s Contacts", font = title_fontStyle)
title.place(x = 250, y = 25, anchor = "center")

#Setting the Plus Button (Add Contact)
img = tkinter.PhotoImage(file = "./images/AddContact.png")
plus_img = tkinter.Label(image = img)
plus = tkinter.Button(gui, image = img, command = AddContact, borderwidth = 0)
plus.place(x = 350, y = 350)

#Setting up the Sort button
sortButton = tkinter.Button(gui, text = "Sort", command = sortContacts)
sortButton.place(x = 0, y = 0)

#Setting up the Save Button
saveButton = tkinter.Button(gui, text = "Save", command = saveContacts)
saveButton.place(x = 465, y = 0)

#Setting up the Frame for scrollbar and Listbox
list_frame = Frame(gui)
scroll_bar = Scrollbar(list_frame, orient = VERTICAL)

contact_list = tkinter.Listbox(list_frame, font = contact_fontStyle, fg = "blue", height = 18, width = 31, yscrollcommand = scroll_bar.set)
contact_list.bind('<Double-1>', selectContact)

scroll_bar.config(command = contact_list.yview)
scroll_bar.pack(side = RIGHT, fill = Y)
list_frame.place(x = 5, y = 75)
contact_list.pack()

#Cannot resize the window
gui.resizable(False, False)

#Runs the Tkinter event loop
gui.mainloop()
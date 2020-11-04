import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *

#Initialize the GUI/Application
gui = tkinter.Tk()

#Gives title to application
gui.title('Contact Book')

#Sets the position and size of the application
gui.geometry('500x500+0+0')

#Change the icon of the application
gui.iconbitmap("PalPadSprite.ico")

#Changes style and font of text
title_fontStyle = tkFont.Font(family = "Lucida Grande", size = 24, weight = tkFont.BOLD, underline = True)
contact_fontStyle = tkFont.Font(family = "Times", size = 14)

contacts = []

def add():
    if len(name.get()) > 0 and len(num.get()) > 0:
        try:
            int(num.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Phone Number")
            raise 
        global contact_list
        contacts.append([name.get(), num.get()])
        contact_list.delete(0, END)
        for i in range(len(contacts)):
            contact_list.insert(END, contacts[i][0] + " (" + contacts[i][1] + ")")
    else:
       messagebox.showerror("Error", "Requirements have not been filled")
    
    add_contact.destroy()
        
def remove():
    response = messagebox.askyesno("Remove Contact?", "Are you sure you want to remove this contact?")
    if response == 1:
        contacts.pop(list(contact_list.get(0, END)).index(contact_list.get(ANCHOR)))
        contact_list.delete(ANCHOR)
        select_contact.destroy()
        #print(list(contact_list.get(0, END)).index(contact_list.get(ANCHOR)))

def AddContact():
    #Setting up pop-up window like main window
    global add_contact
    add_contact = tkinter.Toplevel(gui)
    add_contact.title("Add Contact")
    add_contact.geometry("300x200")
    add_contact.iconbitmap("PalPadSprite.ico")

    global name
    name = tkinter.Entry(add_contact, width = 20)
    name.place(x = 112.5, y = 75)

    name_label = tkinter.Label(add_contact, text = "Name: ")
    name_label.place(x = 10, y = 75)

    global num
    num = tkinter.Entry(add_contact, width = 20)
    num.place(x = 112.5, y = 125)

    num_label = tkinter.Label(add_contact, text = "Phone Number: ")
    num_label.place(x = 10, y = 125)

    addButton = tkinter.Button(add_contact, text = "Add", bg = "white", fg = "blue", width = 5, command = add)
    addButton.pack()

def selectContact(event):
    global select_contact
    select_contact = tkinter.Toplevel(gui)
    select_contact.title("Contact")
    select_contact.geometry("333x333")
    select_contact.iconbitmap("PalPadSprite.ico")

    contact_name = tkinter.Label(select_contact, text = contacts[list(contact_list.get(0, END)).index(contact_list.get(ANCHOR))][0])
    contact_name.place(x = 333/2, y = 166, anchor = "center")

    msg = tkinter.Button(select_contact, text = "Message", fg = "blue", borderwidth = 0)
    msg.place(x = 333/2 - 83.25, y = 225, anchor = "center")

    call = tkinter.Button(select_contact, text = "Call", fg = "blue", borderwidth = 0)
    call.place(x = 333/2, y = 225, anchor = "center")

    removeButton = tkinter.Button(select_contact, text = "Remove", fg = "blue", borderwidth = 0, command = remove)
    removeButton.place(x = 333/2 + 83.25, y = 225, anchor = "center")

def num_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_list = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element.
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element. Do this only if the element is 
        # smaller than its adjacent values.
        while j >= 0 and array[j][1] > array[i][1]:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # the specified element in its correct location
        array[j + 1] = key_list

    return array

def name_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_list = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element 
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element. Do this only if the element is 
        # smaller than its adjacent values.
        while j >= 0 and array[j][0] > array[i][0]:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # the specified element in its correct location
        array[j + 1]= key_list

    return array

def sortList(value):
    global contacts
    if value == 1:
        #Sort by Name
        contacts = name_sort(contacts)
    else:
        #Sort by Number
        contacts = num_sort(contacts)
    
    print(contacts)
    
    #myList = [[Name,Num],[Name,Num],[Name,Num],[Name,Num],[Name,Num]]
    #myList.sort() --> sorts by Name

def sortContacts():
    global sort_contact
    sort_contact = tkinter.Toplevel(gui)
    sort_contact.title("Sort")
    sort_contact.geometry("200x200")
    sort_contact.iconbitmap("PalPadSprite.ico")

    global sort
    sort =  IntVar()
    sort.set(1)

    tkinter.Radiobutton(sort_contact, text = "Name", variable = sort, value = 1, command = lambda: sortList(sort.get())).place(x = 0, y = 0)
    tkinter.Radiobutton(sort_contact, text = "Number", variable = sort, value = 2, command = lambda: sortList(sort.get())).place(x = 0, y = 50)
    
    #contacts.sort(key = sortList)

username_title = tkinter.Label(gui, text = "Sanjeev's Contacts", font = title_fontStyle)
username_title.place(x = 250, y = 25, anchor = "center")

img = tkinter.PhotoImage(file = "AddContact.png")
plus_img = tkinter.Label(image = img)
plus = tkinter.Button(gui, image = img, command = AddContact, borderwidth = 0)
plus.place(x = 350, y = 350)

sortButton = tkinter.Button(gui, text = "Sort", command = sortContacts)
sortButton.place(x = 0, y = 0)

'''
list_frame = Frame(gui)
scroll_bar = Scrollbar(list_frame, orient = VERTICAL)

contact_list = tkinter.Listbox(list_frame, font = contact_fontStyle, fg = "blue", height = 18, width = 31, yscrollcommand = scroll_bar.set)
contact_list.bind('<Double-1>', selectContact)

scroll_bar.config(command = contact_list.yview)
scroll_bar.pack(side = RIGHT, fill = Y)
list_frame.pack()
contact_list.place(x = 5, y = 75)
'''
contact_list = tkinter.Listbox(gui, font = contact_fontStyle, fg = "blue", height = 18, width = 31)
contact_list.bind('<Double-1>', selectContact)
contact_list.place(x = 5, y = 75)

#Cannot resize the window
gui.resizable(False, False)
gui.mainloop()
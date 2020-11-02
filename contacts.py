import tkinter
import tkinter.font as tkFont
from tkinter import messagebox

contacts = []

#Initialize the GUI/Application
gui = tkinter.Tk()

#Gives title to application
gui.title('Contact Book')

#Sets the position and size of the application
gui.geometry('500x500+0+0')

#Change the icon of the application
gui.iconbitmap("PalPadSprite.ico")

#Changes style and font of text
title_fontStyle = tkFont.Font(family = "Lucida Grande", size = 24, weight=tkFont.BOLD)
contact_fontStyle = tkFont.Font(family = "Times", size = 14)

def add():
    if len(name.get()) > 0 and len(num.get()) > 0:
        contacts.append(str(name.get()))
        #print(contacts)
        for i in range(len(contacts)):
            contacts_list = tkinter.Label(gui, text = contacts[i], font = contact_fontStyle)
            contacts_list.place(x = 5, y = 75 + i*20 )
        add_contact.destroy()
    else:
       messagebox.showerror("Error", "Requirements have not been filled")
        
    

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

def selectContact():
    global select_contact
    select_contact = tkinter.Toplevel(gui)
    select_contact.title("Add Contact")
    select_contact.geometry("300x200")
    select_contact.iconbitmap("PalPadSprite.ico")

username_title = tkinter.Label(gui, text = "Sanjeev's Contacts", font = title_fontStyle)
#username_title .grid(row=0, column=250)
username_title.place(x = 112.5, y = 0)

img = tkinter.PhotoImage(file = "AddContact.png")
plus_img = tkinter.Label(image = img)
plus = tkinter.Button(gui, image = img, command = AddContact, borderwidth = 0)
plus.place(x = 350, y = 350)

#Cannot resize the window
gui.resizable(False, False)
gui.mainloop()
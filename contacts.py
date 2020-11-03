import tkinter
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import IntVar

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
title_fontStyle = tkFont.Font(family = "Lucida Grande", size = 24, weight = tkFont.BOLD, underline = True)
contact_fontStyle = tkFont.Font(family = "Times", size = 14)

contact_list = tkinter.Button(gui)

def add():
    contactx = 5
    contacty = 75
    if len(name.get()) > 0 and len(num.get()) > 0:
        try:
            int(num.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid Phone Number")
            raise 
        global contact_list
        contacts.append([name.get(), num.get()])
        contacts.sort()
        #print(contacts)
        contact_list.destroy()
        for i in range(len(contacts)):
            contact_list = tkinter.Button(gui, text = contacts[i][0] + " (" + contacts[i][1] + ")", font = contact_fontStyle, fg = "blue", command = selectContact, borderwidth = 0)
            contact_list.place(x = contactx, y = contacty + i*30 )
        add_contact.destroy()
    else:
       messagebox.showerror("Error", "Requirements have not been filled")
        
def remove():
    response = messagebox.askyesno("Remove Contact?", "Are you sure you want to remove this contact?")
    #if response == 1:
    #    contacts.remove()
    

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
    select_contact.title("Contact")
    select_contact.geometry("333x333")
    select_contact.iconbitmap("PalPadSprite.ico")

    contact_name = tkinter.Label(select_contact, text = "-Contact Name-")
    contact_name.place(x = 117.5, y = 166)

    msg = tkinter.Button(select_contact, text = "Message", fg = "blue", borderwidth = 0)
    msg.place(x = 66, y = 225)

    call = tkinter.Button(select_contact, text = "Call", fg = "blue", borderwidth = 0)
    call.place(x = 333/2 - 10, y = 225)

    removeButton = tkinter.Button(select_contact, text = "Remove", fg = "blue", borderwidth = 0, command = remove)
    removeButton.place(x = 222, y = 225)

def sortContacts():
    global sort_contact
    sort_contact = tkinter.Toplevel(gui)
    sort_contact.title("Sort")
    sort_contact.geometry("200x200")
    sort_contact.iconbitmap("PalPadSprite.ico")

    sort =  IntVar()
    sort.get()

    tkinter.Radiobutton(sort_contact, text = "Name", variable = sort, value = 1).place(x = 0, y = 0)
    tkinter.Radiobutton(sort_contact, text = "Number", variable = sort, value = 2).place(x = 0, y = 50)

username_title = tkinter.Label(gui, text = "Sanjeev's Contacts", font = title_fontStyle)
username_title.place(x = 112.5, y = 0)

img = tkinter.PhotoImage(file = "AddContact.png")
plus_img = tkinter.Label(image = img)
plus = tkinter.Button(gui, image = img, command = AddContact, borderwidth = 0)
plus.place(x = 350, y = 350)

sortButton = tkinter.Button(gui, text = "Sort", command = sortContacts)
sortButton.place(x = 0, y = 0)

#Cannot resize the window
gui.resizable(False, False)
gui.mainloop()
import tkinter
import tkinter.font as tkFont

gui = tkinter.Tk()

#Gives title to application
gui.title('Contact Book')

#Sets the position and size of the application
gui.geometry('500x500+0+0')

#Change the icon of the application
gui.iconbitmap("PalPadSprite.ico")

def add():
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

def select():
    pass

#Changes style and font of text
title_fontStyle = tkFont.Font(family = "Lucida Grande", size = 24)

username_title = tkinter.Label(gui, text = "Sanjeev's Contacts", font = title_fontStyle)
#username_title .grid(row=0, column=250)
username_title.place(x = 112.5, y = 0)

contacts = []

img = tkinter.PhotoImage(file = "AddContact.png")
plus_img = tkinter.Label(image = img)
plus = tkinter.Button(gui, image = img, command = add, borderwidth = 0)
plus.place(x = 350, y = 350)


gui.resizable(False, False)
gui.mainloop()
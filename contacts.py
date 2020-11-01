import tkinter
import tkinter.font as tkFont
from PIL import ImageTk, Image
#Need to install Pillow by using pip install

def add():
    pass

def select():
    pass

gui = tkinter.Tk()

#Gives title to application
gui.title('Contact Book')

#Sets the position and size of the application
gui.geometry('500x500+0+0')

#Change the icon of the application
gui.iconbitmap("PalPadSprite.ico")


#Changes style and font of text
title_fontStyle = tkFont.Font(family="Lucida Grande", size=24)

username_title = tkinter.Label(gui, text="Sanjeev's Contacts", font=title_fontStyle)
#username_title .grid(row=0, column=250)
username_title.place(x=112.5, y=0)

contacts = []

img = ImageTk.PhotoImage(Image.open("AddContact.png"))
plus = tkinter.Label(gui, image=img)
#plus.image = img
plus.place(x=350, y=350)
#tkinter.Label(image=img).grid(row=390, column=390)


#To add any image
#img = ImageTk.PhotoImage(Image.open(""))

'''#This is for later use
name = tkinter.Entry(gui, width=20)
name.pack()

def username():
    title = name.get() + "'s Contacts"
    Name = tkinter.Label(gui, text=title)
    Name.pack()

add = tkinter.Button(gui, text="Continue", command=username, fg="white", bg="blue")
add.pack()
'''


gui.resizable(False, False)
gui.mainloop()
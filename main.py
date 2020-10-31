import tkinter

gui = tkinter.Tk()
gui.title('Contact Book')
gui.geometry('500x500+0+0')
gui.iconbitmap("./PalPadSprite.ico")

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



gui.mainloop()
import tkinter

gui = tkinter.Tk()

count = 0

def click():
    global count
    count += 1
    Count = tkinter.Label(gui, text=str(count))
    Count.pack()

add = tkinter.Button(gui, text="Add Contact", command=click, fg="white", bg="blue")
add.pack()

gui.title('Contact Book')
gui.geometry('500x500+0+0')
gui.mainloop()
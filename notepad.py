from tkinter import *
from tkinter.messagebox import showinfo, askquestion
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetype=[("All Files", "*.*"), ("Text Document", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("File saved")

    else:
        # save a new file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def cuttext():
    textarea.event_generate("<<Cut>>")


def copytext():
    textarea.event_generate("<<Copy>>")


def pastetext():
    textarea.event_generate("<<Paste>>")


def hellp():
    value = askquestion("Help", "Did you face any problem??")
    if value == "no":
        msg = "Really happy to see that"
    else:
        msg = "Go to contact info and let the company know throught mail"
    showinfo("Help", msg)


def about():
    showinfo("About Creator", "This is created as a 1st version of Notepad by Sparsh Saxena")


def contact():
    showinfo("Contacts", "Please contact company at xyz@gmail.com")


if __name__ == '__main__':
    # basics of tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("588x686")

    # add text area
    textarea = Text(root, font="lucdia 14")
    file = None  # this file points to the file which is opened in teh text editor which is currently none
    textarea.pack(expand=True, fill=BOTH)

    # menu bar
    menubar = Menu(root)

    # file menu starts
    filemenu = Menu(menubar, tearoff=0)
    # to add new file
    filemenu.add_command(label="New", command=newfile)
    # to open a already existing file
    filemenu.add_command(label="Open", command=openfile)
    # to save the current file
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    # to exit the app
    filemenu.add_command(label="Exit", command=quit)
    # add.cascade will add all the abouve labels under the file menu
    menubar.add_cascade(label="File", menu=filemenu)
    # file menu ends

    # edit menu starts
    editmenu = Menu(menubar, tearoff=0)
    # to give feature of cut, copy, paste
    editmenu.add_command(label="Cut", command=cuttext)
    editmenu.add_command(label="Copy", command=copytext)
    editmenu.add_command(label="Paste", command=pastetext)
    menubar.add_cascade(label="Edit", menu=editmenu)
    # edit menu ends

    # help menu starts
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=hellp)
    helpmenu.add_command(label="Contact Info", command=contact)
    helpmenu.add_separator()
    helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # help menu endsl

    root.config(menu=menubar)

    # adding scrollbarfrom tut22
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    # ending scrollbar

    root.mainloop()

from tkinter import *
import os
from tkinter.messagebox import *
from tkinter.filedialog import *



class Notepad():
    root = Tk()
    root.title("Notepad")

    width = 500
    height = 500
    TextArea = Text(root)
    Menubar = Menu(root)

    FileMenu = Menu(Menubar, tearoff = 0)
    EditMenu = Menu(Menubar, tearoff = 0)
    HelpMenu = Menu(Menubar, tearoff = 0)

    __file = None

    def __init__(self, **kwargs):
        self.TextArea.grid()

        self.FileMenu.add_command(label = "New", command = self.NewFile)
        self.FileMenu.add_command(label="Open", command = self.OpenFile)
        self.FileMenu.add_command(label="Save", command = self.SaveFile)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command = self.QuitNotepad)
        self.Menubar.add_cascade(label = "File", menu = self.FileMenu)

        self.EditMenu.add_command(label = "Cut", command = self.__Cut)
        self.EditMenu.add_command(label="Copy", command = self.__Copy)
        self.EditMenu.add_command(label="Paste", command = self.__Paste)
        self.Menubar.add_cascade(label = "Edit", menu = self.EditMenu)

        self.HelpMenu.add_command(label = "About Notepad", command = self.AboutNotepad)
        self.Menubar.add_cascade(label = "Help", menu = self.HelpMenu)

        self.root.config(menu = self.Menubar)

    def QuitNotepad(self):
            self.root.destroy()

    def AboutNotepad(self):
            showinfo("About", "This Notepad is Created by Shubham Jain")

    def OpenFile(self):
            self.__file = askopenfilename()

            if self.__file == "":
                self.__file = None
            else:
                self.root.title(os.path.basename(self.__file) + " - Notepad")
                self.TextArea.delete(1.0,END)
                file = open(self.__file,"r")
                self.TextArea.insert(1.0, file.read())
                file.close()

    def NewFile(self):
            self.root.title("Untitled - Notepad")
            self.TextArea.delete(1.0, END)


    def SaveFile(self):

            if self.__file == None:                       #Saveing the file
                self.__file = asksaveasfilename(filetypes=[("All Files", "*.*")])

                if self.__file == "":
                    self.__file = None
                else:
                    file = open(self.__file, "w")
                    file.write(self.TextArea.get(1.0, END))
                    file.close()
                    self.root.title(os.path.basename(self.__file) + " - Notepad")

            else:                                         #content vahin rehege
                file = open(self.__file, "w")
                file.write(self.TextArea.get(1.0, END))
                file.close()

    def __Cut(self):
            self.TextArea.event_generate("<<Cut>>")

    def __Copy(self):
            self.TextArea.event_generate("<<Copy>>")

    def __Paste(self):
            self.TextArea.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

notepad = Notepad()
notepad.run()

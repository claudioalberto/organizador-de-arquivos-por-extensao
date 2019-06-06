from tkinter import *
from tkinter.filedialog import askdirectory
import os
import core
import getpass

user = getpass.getuser()

# current_path = core.set_folder_to_organize('C:\\Users\\cafgd\\Desktop')




class Application():
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.label1 = Label(self.widget1, text="Organizador de Arquivos por Extensão", pady="10px", font=("Sans Serif", 14)).pack(side=TOP)
        self.label2 = Label(self.widget1, text="Pasta Selecionada:", pady="5px", font=("Sans Serif", 9)).pack(side=TOP)
        self.label3 = Label(self.widget1, text='', pady="3px", font=("Sans Serif", 9)).pack(side=TOP)
        self.btn_select_folder = Button(self.widget1, text="Selecione a pasta", padx="15px", pady="10px", command=self.askdirectory).pack()
        self.btn_organize_folder = Button(self.widget1, text="Organizar a pasta", padx="15px", pady="10px").pack(anchor=CENTER)

    def changeCurrentPath(self, path):
        self.current_path = path
        self.label3 = str(self.current_path)
        return path

    def askdirectory(self):
        global current_path
        self.filename = askdirectory(title="Selecione uma pasta")
        self.directory = os.path.split(self.filename)[0]
        current_path.set(self.directory)
        # self.changeCurrentPath(self.directory)
        print(current_path.get())
        return self.directory








root = Tk()
root.geometry('400x300')
Application(root)
root.title('Organizador de Arquivos por Extensão')










root.mainloop()




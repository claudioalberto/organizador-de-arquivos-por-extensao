from tkinter import *


windows = Tk()
windows.geometry('400x300')
windows.title('Organizador de Arquivos por Extensão')
label = Label(windows, text="Organizador de Arquivos por Extensão", pady="20px", font=("Sans Serif", 14)).pack(side=TOP)
btn_select_folder = Button(windows, text="Selecione a pasta", padx="15px", pady="10px").pack()
btn_organize_folder = Button(windows, text="Organizar a pasta", padx="15px", pady="10px").pack(anchor=CENTER)



windows.mainloop()




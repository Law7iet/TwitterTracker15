'''
Created on 3 dic 2020

@author: L
'''

from tkinter import *
from tkcalendar import Calendar, DateEntry
#from tkinter import ttk
#from tkmacosx import Button 
#from graphics.button import *

class Window():
    
    language = ["it", "en", "fr", "de", "es"]
    type = ["mixed", "popular", "recent"]
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x200")
        
        # ELEMENTS
        AA = Label(self.root, text = "Parola Chiave:")
        BA = Label(self.root, text = "Lingua:")
        CA = Label(self.root, text = "Tipo:")
        DA = Label(self.root, text = "N" + chr(186) + " di elementi:")
        EA = Label(self.root, text = "Data inizio:")
        FA = Label(self.root, text = "Data fine:")

        input_parola = Entry(self.root, width = 5)
        var_lingua = (StringVar(self.root))
        var_lingua.set(self.language[0])
        input_lingua = OptionMenu(self.root, var_lingua, *self.language)
        var_tipo = (StringVar(self.root))
        var_tipo.set(self.type[0])
        input_tipo = OptionMenu(self.root, var_tipo, *self.type)
        input_numero = Entry(self.root, width = 10)
        input_inizio = DateEntry(self.root, width = 8)
        input_inizio._top_cal.overrideredirect(False)
        input_fine = DateEntry(self.root, width = 8)
        input_fine._top_cal.overrideredirect(False)

        # GRID
        AA.grid(row = 0, column = 0, sticky = W)
        BA.grid(row = 1, column = 0, sticky = W)
        CA.grid(row = 2, column = 0, sticky = W)
        DA.grid(row = 3, column = 0, sticky = W)
        EA.grid(row = 4, column = 0, sticky = W)
        FA.grid(row = 5, column = 0, sticky = W)
        
        input_parola.grid(row = 0, column = 1)
        input_lingua.grid(row = 1, column = 1, sticky = E)
        input_lingua.config(width = 5)
        input_tipo.grid(row = 2, column = 1, sticky = E)
        input_tipo.config(width = 10)
        input_numero.grid(row = 3, column = 1, sticky = E)
        input_inizio.grid(row = 4, column = 1)
        input_fine.grid(row = 5, column = 1)
        
    def run(self):
        self.root.mainloop()
        
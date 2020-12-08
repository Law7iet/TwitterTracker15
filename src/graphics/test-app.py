'''
THIS IS A TEST FILE
ECLISPE CAN'T SEE THIS FILE BECAUSE I DIDN'T IMPORT IT
TO SEE THE RESULT RUN MAINAPPLICATION.PY
'''


import tkinter as tk
from tkinter import ttk
import tkmacosx as tkmac

class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Creazione oggetto tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        # Definizione della grandezza della finestra
        self.geometry("1000x1000")
        # Titolo finestra
        tk.Tk.wm_title(self, "Porcodio")
        # Insieme degli oggetti (?)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}
        # Inizializzazione delle pagine
        for f in (StartPage, PageOne, PageTwo):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        # Mostra per default la pagina 1
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# classe della prima pagina
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina iniziale")
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = ttk.Button(self, text = "Ricerca tweets", command = lambda: controller.show_frame(PageOne))
        button.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = ttk.Button(self, text = "Ricerca tweets utente", command = lambda: controller.show_frame(PageTwo))
        button.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina 1")
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(StartPage))
        button.pack()
        label = tk.Label(self, text = "ciao")
        label.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina 2")
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(StartPage))
        button.pack()

app = MainApplication()
app.mainloop()

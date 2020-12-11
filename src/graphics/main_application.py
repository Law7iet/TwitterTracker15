import tkinter as tk
from tkinter import ttk
#from graphics import page_0, page_1, page_2
import page_0, page_1, page_2

class Main_application(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Creazione oggetto tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        # Titolo finestra
        tk.Tk.wm_title(self, "Titolo")
        # Grandezza della finestra
        self.geometry("500x500")
        # Tema/Stile
#        s = ttk.Style(self)
#        s.theme_use('clam')

        # Creazione del contenitore di tutti gli elementi
        # Il background non si vede perche' viene completamente coperto dalle altre finestre
        container = tk.Frame(self, background = "red")
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # Inizializzazione delle pagine
        self.frames = {}
        for f in (page_0.Page_0, page_1.Page_1, page_2.Page_2):
            frame = f(container, self)
            self.frames[f] = frame
            # span unifica le righe/colonne, lo si usa per coprire le righe/colonne delle altre finestre
            # al momento ci sono 2 colonne e 9 righe da coprire
            frame.grid(row = 0, column = 0, columnspan = 2, rowspan = 9, sticky = "nsew")
        # Mostra per default la pagina 0
        self.show_frame(page_0.Page_0)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
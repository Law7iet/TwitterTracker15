import tkinter as tk
from tkinter import ttk
import tkmacosx as tkmac
import page_0, page_1, page_2

class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Creazione oggetto tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        # Titolo finestra
        tk.Tk.wm_title(self, "Titolo")
        # Definizione della grandezza della finestra
        self.geometry("1000x1000")
        # Creazione del contenitore di tutti gli elementi
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # Inizializzazione delle pagine
        self.frames = {}
        for f in (page_0.Page_0, page_1.Page_1, page_2.Page_2):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        # Mostra per default la pagina 0
        self.show_frame(page_0.Page_0)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = MainApplication()
app.mainloop()

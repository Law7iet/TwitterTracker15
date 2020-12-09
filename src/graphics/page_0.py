import tkinter as tk
from tkinter import ttk
import tkmacosx as tkmac
import page_1, page_2

# classe della prima pagina
class Page_0(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina iniziale")
        label.grid(sticky = "nsew")
        label.grid_rowconfigure(0, weight=1)
        label.grid_columnconfigure(0, weight=1)
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets", command = lambda: controller.show_frame(page_1.Page_1))
        button.grid(row = 1, column = 0, sticky = tk.E)
        button.grid_rowconfigure(1, weight = 1)
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets utente", command = lambda: controller.show_frame(page_2.Page_2))
        button.grid(row = 2, column = 0, sticky = tk.E)
        button.grid_rowconfigure(2, weight = 1)

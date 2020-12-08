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
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets", command = lambda: controller.show_frame(page_1.Page_1))
        button.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets utente", command = lambda: controller.show_frame(page_2.Page_2))
        button.pack()
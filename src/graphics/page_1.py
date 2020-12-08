import tkinter as tk
from tkinter import ttk
import tkmacosx as tkmac
import page_0

class Page_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina 1")
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(page_0.Page_0))
        button.pack()
        label = tk.Label(self, text = "ciao")
        label.pack()
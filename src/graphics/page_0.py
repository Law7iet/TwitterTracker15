import tkinter as tk
import tkmacosx as tkmac
#from graphics import page_1, page_2
import page_1, page_2

# classe della prima pagina
class Page_0(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background = 'yellow')
        self.pack(side = "top", fill = "both", expand = True)
        # Titolo
        label = tk.Label(self, text="Pagina iniziale", bg = "green")
        label.grid(row = 0, sticky = "nsew")
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets", command = lambda: controller.show_frame(page_1.Page_1))
        button.grid(row = 1, sticky = "nsew")
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Ricerca tweets utente", command = lambda: controller.show_frame(page_2.Page_2))
        button.grid(row = 2, sticky = "nsew")
        # Proporzionale alla finestra
        tk.Grid.columnconfigure(self, 0, weight = 1)
        tk.Grid.rowconfigure(self, 0, weight = 1)
        tk.Grid.rowconfigure(self, 1, weight = 1)
        tk.Grid.rowconfigure(self, 2, weight = 1)
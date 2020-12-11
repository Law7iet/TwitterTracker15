import tkinter as tk
import tkmacosx as tkmac
#from graphics import page_0
import page_0

class Page_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Titolo
        label = tk.Label(self, text="Pagina 2")
        label.pack()
        # Bottone per rendirizzare alla pagina/frame corretta
        button = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(page_0.Page_0))
        button.pack()
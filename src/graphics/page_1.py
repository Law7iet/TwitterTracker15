import tkinter as tk
#from tkinter import ttk
import tkmacosx as tkmac
#from graphics import page_0
import page_0
from twitter.twitter_handler import Twitter_handler
import tkcalendar

class Page_1(tk.Frame):
    
    language = ["it", "en", "fr", "de", "es"]
    filter = ["mixed", "popular", "recent"]
    ricerca = Twitter_handler() 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "yellow")

        # Lo stile per il calendario
#        stile = ttk.Style(parent)
#        stile.theme_use('clam')
        
        # Titolo
        self.title = tk.Label(self, text = "Ricerca dei tweets", bg = "orange")
        # Descrizioni del form
        self.descr_parola_chiave = tk.Label(self, text = "Parola Chiave:")
        self.descr_coordinate = tk.Label(self, text = "Coordinate:")
        self.descr_raggio = tk.Label(self, text = "Raggio:")
        self.descr_lingua = tk.Label(self, text = "Lingua:")
        self.descr_filtro = tk.Label(self, text = "Filtro:")
        self.descr_numero = tk.Label(self, text = "Numero:")
        self.descr_data_inizio = tk.Label(self, text = "Dal giorno:")
        self.descr_data_fine = tk.Label(self, text = "Al giorno:")
        # Campi da compilare
        self.parola_chiave = tk.Entry(self)
        self.coordinate = tk.Entry(self)
        self.raggio = tk.Entry(self)
        self.lingua = tk.StringVar(self)
        self.lingua.set(self.language[0])
        self.menu_lingua = tk.OptionMenu(self, self.lingua, *self.language)
        self.filtro = tk.StringVar(self)
        self.filtro.set(self.filter[0])
        self.menu_filtro = tk.OptionMenu(self, self.filtro, *self.filter)
        self.numero = tk.Entry(self)
        self.data_inizio = tkcalendar.DateEntry(self)
        self.data_inizio._top_cal.overrideredirect(False)
        self.data_fine = tkcalendar.DateEntry(self)
        self.data_fine._top_cal.overrideredirect(False)
        # Bottoni
        self.cerca = tkmac.Button(self, text = "Cerca", command = self.check)
        self.pag_0 = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(page_0.Page_0))
        
        # Grid
        self.title.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        self.descr_parola_chiave.grid(row = 1, column = 0, sticky = "nsw")
        self.parola_chiave.grid(row = 1, column = 1, sticky = "nse")
        self.descr_coordinate.grid(row = 2, column = 0, sticky = "nsw")
        self.coordinate.grid(row = 2, column = 1, sticky = "nse")
        self.descr_raggio.grid(row = 3, column = 0, sticky = "nsw")
        self.raggio.grid(row = 3, column = 1, sticky = "nse")
        self.descr_lingua.grid(row = 4, column = 0, sticky = "nsw")
        self.menu_lingua.grid(row = 4, column = 1, sticky = "nse")
        self.descr_filtro.grid(row = 5, column = 0, sticky = "nsw")
        self.menu_filtro.grid(row = 5, column = 1, sticky = "nse")
        self.descr_numero.grid(row = 6, column = 0, sticky = "nsw")
        self.numero.grid(row = 6, column = 1, sticky = "nse")
        self.descr_data_inizio.grid(row = 7, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 7, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 8, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 8, column = 1, sticky = "nse")
        self.cerca.grid(row = 9, column = 0, columnspan = 2, sticky = "nsew")
        # Layout
        tk.Grid.columnconfigure(self, 0, weight = 1)
    
    def get(self):
        geocodifica = self.coordinate.get() + "," + self.raggio.get()
        tweets = self.ricerca.search(self.parola_chiave.get(), geocodifica, self.lingua.get(), self.filtro.get(), int(self.numero.get()), self.data_inizio.get_date(), self.data_fine.get_date())
        i = 1
        for tweet in tweets:
            print(i)
            print(tweet["text"])
#            print(tweet["created_at"])
#            print(tweet["place"]["full_name"])
#            print(tweet["place"]["bounding_box"]["coordinates"][0])
            i += 1
        return tweets
    
    def check(self):
        # Stampa i valori ottenuti e il loro tipo
#         print(str(type(self.parola_chiave.get())) + " " + self.parola_chiave.get())
#         print(str(type(self.coordinate.get())) + " " + self.coordinate.get())
#         print(str(type(self.raggio.get())) + " " + self.raggio.get())
#         print(str(type(self.lingua.get())) + " " + self.lingua.get())
#         print(str(type(self.filtro.get())) + " " + self.filtro.get())
#         print(str(type(self.numero.get())) + " " + self.numero.get())
#         print(str(self.data_inizio.get_date()))
#         print(str(self.data_fine.get_date()))
        
        # Controlla il numero, le coordinate e il raggio
        if (self.numero.get()).isdigit() == False:
            # Il campo numero deve essere un intero
            # Crea pop-up
            return None
        self.get()
        
    
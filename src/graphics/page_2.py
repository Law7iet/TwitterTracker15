import tkinter as tk
import tkmacosx as tkmac
import tkcalendar
from twitter.twitter_handler import Twitter_handler
import page_0 # OPPPURE from graphics import page_0

class Page_2(tk.Frame):
    
    language = ["it", "en", "fr", "de", "es"]
    filter = ["mixed", "popular", "recent"]
    ricerca = Twitter_handler() 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Lo stile per il calendario
#        stile = ttk.Style(parent)
#        stile.theme_use('clam')
        
        # Titolo
        self.titolo = tk.Label(self, text = "Ricerca dei tweets di un utente")
        # Descrizioni del form
        self.descr_id_utente = tk.Label(self, text = "ID utente:")
        self.descr_data_inizio = tk.Label(self, text = "Dal giorno:")
        self.descr_data_fine = tk.Label(self, text = "Al giorno:")
        # Campi da compilare
        self.id_utente = tk.Entry(self)
        self.data_inizio = tkcalendar.DateEntry(self)
        self.data_inizio._top_cal.overrideredirect(False)
        self.data_fine = tkcalendar.DateEntry(self)
        self.data_fine._top_cal.overrideredirect(False)
        # Bottoni
        self.cerca = tkmac.Button(self, text = "Cerca", command = self.check)
        self.pag_0 = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(page_0.Page_0))
        
        # Grid
        self.titolo.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        self.descr_id_utente.grid(row = 1, column = 0, sticky = "nsw")
        self.id_utente.grid(row = 1, column = 1, sticky = "nse")
        self.descr_data_inizio.grid(row = 2, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 2, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 3, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 3, column = 1, sticky = "nse")
        self.cerca.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew")
        self.pag_0.grid(row = 5, column = 0, columnspan = 2, sticky = "nsew")
        # Layout
        tk.Grid.columnconfigure(self, 0, weight = 1)

    def get(self):
        list_tweets = self.ricerca.search_user(self.id_utente.get(), self.data_inizio.get_date(), self.data_fine.get_date())
        for tweets in list_tweets:
            i = 1
            for tweet in tweets:
                print(i)
                print(tweet["text"])
                print(tweet["created_at"])
    #            print(tweet["place"]["full_name"])
    #            print(tweet["place"]["bounding_box"]["coordinates"][0])
                i += 1
        return list_tweets
    
    def check(self):
        # Stampa i valori ottenuti e il loro tipo
#         print(str(type(self.id_utente.get())) + " " + self.id_utente.get())
#         print(str(type(self.numero.get())) + " " + self.numero.get())
#         print(str(self.data_inizio.get_date()))
#         print(str(self.data_fine.get_date()))
        self.get()
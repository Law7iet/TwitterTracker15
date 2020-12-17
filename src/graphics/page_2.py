import tkinter as tk
import tkmacosx as tkmac
import tkcalendar
from twitter.twitter_handler import Twitter_handler
from utility.loader import Loader
from tkinter.filedialog import askopenfile

class Page_2(tk.Frame):

    caricatore = Loader()
    ricerca = Twitter_handler()
    tweets = []

    def __init__(self, parent, controller):
        # Import locale per evitare dipendenze circolari
        from graphics.page_0 import Page_0

        # Inizializzazione del frame
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
        self.seleziona = tkmac.Button(self, text = "Seleziona", command = self.select)
        self.carica = tkmac.Button(self, text = "Carica Tweets", command = self.load)
        self.salva = tkmac.Button(self, text = "Salva", command = self.save)
        self.pag_0 = tkmac.Button(self, text = "Torna alla Home", command = lambda: controller.show_frame(Page_0))

        # Grid
        self.titolo.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        self.descr_id_utente.grid(row = 1, column = 0, sticky = "nsw")
        self.id_utente.grid(row = 1, column = 1, sticky = "nse")
        self.descr_data_inizio.grid(row = 2, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 2, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 3, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 3, column = 1, sticky = "nse")
        self.cerca.grid(row = 4, column = 0, columnspan = 2, sticky = "nsew")
        self.seleziona.grid(row = 5, column = 0, columnspan = 2, sticky = "nsew")
        self.carica.grid(row = 6, column = 0, sticky = "nsew")
        self.salva.grid(row = 6, column = 1, sticky = "nsew")
        self.pag_0.grid(row = 7, column = 0, columnspan = 2, sticky = "nsew")
        # Layout
        tk.Grid.columnconfigure(self, 0, weight = 1)
        tk.Grid.columnconfigure(self, 1, weight = 1)

    def get(self):
        list_tweets = self.ricerca.search_user(self.id_utente.get(), self.data_inizio.get_date(), self.data_fine.get_date())

        return list_tweets

    def check(self):
        # Stampa i valori ottenuti e il loro tipo
#         print(str(type(self.id_utente.get())) + " " + self.id_utente.get())
#         print(str(type(self.numero.get())) + " " + self.numero.get())
#         print(str(self.data_inizio.get_date()))
#         print(str(self.data_fine.get_date()))
        self.get()

    def select(self):
        f = askopenfile(mode = 'r', filetypes = [('JSON Files', '*.json')])
        self.caricatore.set(f.name)

    def load(self):
        self.tweets = self.caricatore.load()
        self.print_tweets()

    def save(self):
        self.caricatore.store(self.tweets)

    def print_tweets(self):
        i = 1
        for tweets in list_tweets:
            print(i)
            j = 1
            for tweet in tweets:
                print(i)
                print(tweet["text"])
                print(tweet["created_at"])
#                print(tweet["place"]["full_name"])
#                print(tweet["place"]["bounding_box"]["coordinates"][0])
                j += 1
            i += 1

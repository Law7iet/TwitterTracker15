import tkinter as tk
import tkmacosx as tkmac
import tkcalendar
import list_tweets as listtw
from twitter.twitter_handler import Twitter_handler
from utility.loader import Loader
from utility.others import address_to_coordinates
from tkinter.filedialog import askopenfile
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL


class Form():

    caricatore = Loader()
    language = ["it", "en", "fr", "de", "es"]
    # popular non funziona
    filter = ["mixed", "recent"]
    ricerca = Twitter_handler()
    tweets = []

    def __init__(self):
        # Inizializzazione del frame
        self.container = tk.Frame()

        # Lo stile per il calendario
        stile = ttk.Style(self.container)
        stile.theme_use('clam')

        # Titolo
        self.titolo = tk.Label(self.container, text = "Ricerca dei tweets", bg = "orange")
        # Bottoni scelta tipologia form (parola chiave, persona/multipersona)
        self.button_parolachiave = tkmac.Button(self.container, text = "Ricerca Parola Chiave",state=DISABLED, command=self.check_state)
        self.button_persona = tkmac.Button(self.container, text = "Ricerca per Persona", command=self.check_state)
        # Descrizioni del form
        self.descr_parola_chiave = tk.Label(self.container, text = "Parola Chiave:")
        self.descr_coordinate = tk.Label(self.container, text = "Città, stato:")
        self.descr_raggio = tk.Label(self.container, text = "Raggio in km:")
        self.descr_lingua = tk.Label(self.container, text = "Lingua:")
        self.descr_filtro = tk.Label(self.container, text = "Filtro:")
        self.descr_numero = tk.Label(self.container, text = "Numero:")
        self.descr_data_inizio = tk.Label(self.container, text = "Dal giorno:")
        self.descr_data_fine = tk.Label(self.container, text = "Al giorno:")
        # Campi da compilare
        self.parola_chiave = tk.Entry(self.container)
        self.coordinate = tk.Entry(self.container)
        self.raggio = tk.Entry(self.container)
        self.lingua = tk.StringVar(self.container)
        self.lingua.set(self.language[0])
        self.menu_lingua = tk.OptionMenu(self.container, self.lingua, *self.language)
        self.filtro = tk.StringVar(self.container)
        self.filtro.set(self.filter[0])
        self.menu_filtro = tk.OptionMenu(self.container, self.filtro, *self.filter)
        self.numero = tk.Entry(self.container)
        self.data_inizio = tkcalendar.DateEntry(self.container)
        self.data_inizio._top_cal.overrideredirect(False)
        self.data_fine = tkcalendar.DateEntry(self.container)
        self.data_fine._top_cal.overrideredirect(False)
        # Bottoni
        self.cerca = tkmac.Button(self.container, text = "Cerca", command = self.check)
        self.seleziona = tkmac.Button(self.container, text = "Seleziona", command = self.select)
        self.carica = tkmac.Button(self.container, text = "Carica Tweets", command = self.load)
        self.salva = tkmac.Button(self.container, text = "Salva", command = self.save)

        # Grid
        self.titolo.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        self.button_parolachiave.grid(row = 1, column = 0, sticky = "nsew")
        self.button_persona.grid(row = 1, column = 1, sticky = "nsew")
        self.descr_parola_chiave.grid(row = 2, column = 0, sticky = "nsw")
        self.parola_chiave.grid(row = 2, column = 1, sticky = "nse")
        self.descr_coordinate.grid(row = 3, column = 0, sticky = "nsw")
        self.coordinate.grid(row = 3, column = 1, sticky = "nse")
        self.descr_raggio.grid(row = 4, column = 0, sticky = "nsw")
        self.raggio.grid(row = 4, column = 1, sticky = "nse")
        self.descr_lingua.grid(row = 5, column = 0, sticky = "nsw")
        self.menu_lingua.grid(row = 5, column = 1, sticky = "nse")
        self.descr_filtro.grid(row = 6, column = 0, sticky = "nsw")
        self.menu_filtro.grid(row = 6, column = 1, sticky = "nse")
        self.descr_numero.grid(row = 7, column = 0, sticky = "nsw")
        self.numero.grid(row = 7, column = 1, sticky = "nse")
        self.descr_data_inizio.grid(row = 8, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 8, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 9, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 9, column = 1, sticky = "nse")
        self.cerca.grid(row = 10, column = 0, columnspan = 2, sticky = "nsew")
        self.seleziona.grid(row = 11, column = 0, columnspan = 2, sticky = "nsew")
        self.carica.grid(row = 12, column = 0, sticky = "nsew")
        self.salva.grid(row = 12, column = 1, sticky = "nsew")
        # Layout
        tk.Grid.columnconfigure(self.container, 0, weight = 1, uniform = 'equispaziato')
        tk.Grid.columnconfigure(self.container, 1, weight = 1, uniform = 'equispaziato')

    def get(self):
        tmp1 = address_to_coordinates(self.coordinate.get())
        tmp2 = self.raggio.get()
        try:
            geocodifica = str(tmp1[1]) + "," + str(tmp1[0]) + "," + str(tmp2) + "km"
        except:
            geocodifica = 'NULL'
        self.tweets = self.ricerca.search(self.parola_chiave.get(), geocodifica, self.lingua.get(), self.filtro.get(), int(self.numero.get()), self.data_inizio.get_date(), self.data_fine.get_date())
        self.print_tweets()

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

    def get_person(self):
        self.tweets = self.ricerca.search_user(self.parola_chiave.get(), self.data_inizio.get_date(), self.data_fine.get_date())
        self.print_tweets_person()
        return self.tweets

    def check_person(self):
        # Stampa i valori ottenuti e il loro tipo
#         print(str(type(self.id_utente.get())) + " " + self.id_utente.get())
#         print(str(type(self.numero.get())) + " " + self.numero.get())
#         print(str(self.data_inizio.get_date()))
#         print(str(self.data_fine.get_date()))
        self.get()

    def print_tweets_person(self):
        i = 1
        for tweets in self.tweets:
            print(i)
            j = 1
            for tweet in tweets:
                print(j)
                print(tweet["id"])
                print(tweet["text"])
                print(tweet["created_at"])
                print(tweet["place"]["full_name"])
                print(tweet["place"]["bounding_box"]["coordinates"][0])
                j += 1
            i += 1

        lista = listtw.ListTweets(self.tweets)
        lista.build_list_person()
        lista.open_window()

    def select(self):
        f = askopenfile(mode = 'r', filetypes = [('JSON Files', '*.json')])
        self.caricatore.set(f.name)

    def load(self):
        self.tweets = self.caricatore.load()
        self.print_tweets()

    def save(self):
        self.caricatore.store(self.tweets)

    def print_tweets(self):
#        i = 1
#        for tweet in self.tweets:
#            print(i)
#            print(tweet["text"])
#            print(tweet["created_at"])
#            i += 1

        lista = listtw.ListTweets(self.tweets)
        lista.build_list()
        lista.open_window()

    def check_state(self):
        if self.button_parolachiave['state'] == 'disabled':
            self.button_parolachiave['state'] = NORMAL
            self.button_persona['state'] = DISABLED
            self.show_persona()
        else:
            self.button_persona['state'] = NORMAL
            self.button_parolachiave['state'] = DISABLED
            self.show_parolaChiave()

    def show_parolaChiave(self):

        self.descr_parola_chiave['text']='Parola Chiave:'
        self.descr_parola_chiave.grid(row = 2, column = 0, sticky = "nsw")
        self.parola_chiave.grid(row = 2, column = 1, sticky = "nse")
        self.descr_coordinate.grid(row = 3, column = 0, sticky = "nsw")
        self.coordinate.grid(row = 3, column = 1, sticky = "nse")
        self.descr_raggio.grid(row = 4, column = 0, sticky = "nsw")
        self.raggio.grid(row = 4, column = 1, sticky = "nse")
        self.descr_lingua.grid(row = 5, column = 0, sticky = "nsw")
        self.menu_lingua.grid(row = 5, column = 1, sticky = "nse")
        self.descr_filtro.grid(row = 6, column = 0, sticky = "nsw")
        self.menu_filtro.grid(row = 6, column = 1, sticky = "nse")
        self.descr_numero.grid(row = 7, column = 0, sticky = "nsw")
        self.numero.grid(row = 7, column = 1, sticky = "nse")
        self.descr_data_inizio.grid(row = 8, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 8, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 9, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 9, column = 1, sticky = "nse")
        self.seleziona.grid(row = 11, column = 0, columnspan = 2, sticky = "nsew")
        self.carica.grid(row = 12, column = 0, sticky = "nsew")
        self.salva.grid(row = 12, column = 1, sticky = "nsew")

        self.cerca['command'] = self.check

    def show_persona(self):
        self.descr_parola_chiave['text']='Nome Utente:'
        self.descr_coordinate.grid_forget()
        self.coordinate.grid_forget()
        self.descr_raggio.grid_forget()
        self.raggio.grid_forget()
        self.descr_lingua.grid_forget()
        self.menu_lingua.grid_forget()
        self.descr_filtro.grid_forget()
        self.menu_filtro.grid_forget()
        self.descr_numero.grid_forget()
        self.numero.grid_forget()
        self.descr_data_inizio.grid(row = 3, column = 0, sticky = "nsw")
        self.data_inizio.grid(row = 3, column = 1, sticky = "nse")
        self.descr_data_fine.grid(row = 4, column = 0, sticky = "nsw")
        self.data_fine.grid(row = 4, column = 1, sticky = "nse")
        self.seleziona.grid_forget()
        self.carica.grid_forget()
        self.salva.grid_forget()
        
        self.cerca['command'] = self.get_person

    def get_container(self):
        return self.container

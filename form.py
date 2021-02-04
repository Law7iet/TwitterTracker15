import tkinter as tk
#import tkmacosx as tkmac
import tkcalendar

import list_tweets as listtw
from mappa_person import Mappa_Person
from mappa_noperson import Map_Noperson
from Tools import Tools
from twitter.twitter_handler import Twitter_handler
from Word_cloud import Word_cloud
from utility.loader import Loader
from utility.others import address_to_coordinates
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from tkinter.filedialog import askopenfile
from tweetChart import TweetChart

class Form():

    caricatore = Loader()
    tweetChart = TweetChart()
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
#        self.button_parolachiave = tkmac.Button(self.container, text = "Ricerca Parola Chiave",state=DISABLED, command=self.check_state)
#        self.button_persona = tkmac.Button(self.container, text = "Ricerca per Persona", command=self.check_state)
        self.button_parolachiave = tk.Button(self.container, text = "Ricerca Parola Chiave",state=DISABLED, command=self.check_state)
        self.button_persona = tk.Button(self.container, text = "Ricerca per Persona", command=self.check_state)
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
#        self.cerca = tkmac.Button(self.container, text = "Cerca", command = self.check)
#        self.carica = tkmac.Button(self.container, text = "Carica Tweets", command = self.load)
#        self.salva = tkmac.Button(self.container, text = "Salva", command = self.save)
        self.cerca = tk.Button(self.container, text = "Cerca", command = self.check)
        self.carica = tk.Button(self.container, text = "Carica Tweets", command = self.load)
        self.salva = tk.Button(self.container, text = "Salva", command = self.save)

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
        self.carica.grid(row = 12, column = 0, sticky = "nsew")
        self.salva.grid(row = 12, column = 1, sticky = "nsew")
        # Layout
        tk.Grid.columnconfigure(self.container, 0, weight = 1, uniform = 'equispaziato')
        tk.Grid.columnconfigure(self.container, 1, weight = 1, uniform = 'equispaziato')

    #funzione per la ricerca dei tweets con parola chiave
    def get(self):
        tmp1 = address_to_coordinates(self.coordinate.get())
        tmp2 = self.raggio.get()
        try:
            geocodifica = str(tmp1[1]) + "," + str(tmp1[0]) + "," + str(tmp2) + "km"
        except:
            geocodifica = 'NULL'
        self.tweets = self.ricerca.search(self.parola_chiave.get(), geocodifica, self.lingua.get(), self.filtro.get(), int(self.numero.get()), self.data_inizio.get_date(), self.data_fine.get_date())

        self.set_tools(True)


    def check(self):

        # Controlla il numero, le coordinate e il raggio
        if (self.numero.get()).isdigit() == False:
            # Il campo numero deve essere un intero
            # Crea pop-up
            return None
        self.get()
    
    #funzione per la ricerca dei tweet tramite persona
    def get_person(self):
        self.tweets = self.ricerca.search_user(self.parola_chiave.get(), self.data_inizio.get_date(), self.data_fine.get_date())
        self.set_tools(False)
        return self.tweets

    #funzione per caricamento tweets da file json
    def load(self):
        
        f = askopenfile(mode = 'r', filetypes = [('JSON Files', '*.json')])
        self.caricatore.set(f.name)
        
        self.tweets = self.caricatore.load()
       
       
        self.set_tools(True, file_name=f.name)

    #funzione per salvataggio tweets
    def save(self):
        self.caricatore.store(self.tweets)

    #gestione bottoni form
    def check_state(self):
        if self.button_parolachiave['state'] == 'disabled':
            self.button_parolachiave['state'] = NORMAL
            self.button_persona['state'] = DISABLED
            self.show_persona()
        else:
            self.button_persona['state'] = NORMAL
            self.button_parolachiave['state'] = DISABLED
            self.show_parolaChiave()
            
    #gestisce i bottoni nel form per la ricerca per parola chiave
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
        self.carica.grid(row = 12, column = 0, sticky = "nsew")
        self.salva.grid(row = 12, column = 1, sticky = "nsew")

        self.cerca['command'] = self.check
        
    #gestione dei bottoni del form per la ricerca per persona
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
        self.cerca['command']=self.get_person
        self.carica.grid_forget()
        self.salva.grid_forget()

    #ritorna il form
    def get_container(self):
        return self.container
    
    #setta i vari tools per l'analisi dei tweet con i tweets ricercati
    def set_tools(self, mode, file_name=""):
        
        print(self.tweets)
        lista = listtw.ListTweets(self.tweets)
        wordcloud = Word_cloud(self.ricerca.extend_lang(self.lingua.get()))
         
        if file_name == "":
            print("ciao")
           # word_cloud_format = self.ricerca.get_tweets_for_wordcloud(self.parola_chiave.get(), self.lingua.get(), self.filtro.get(), self.data_inizio.get_date(), self.data_fine.get_date(), int(self.numero.get()))       
           # wordcloud.generate_wordcloud(1,word_cloud_format)
          #  self.tweetChart.barChart(tweets=self.tweets)
           # self.tweetChart.pieChart(tweets=self.tweets)
        else:
            
            wordcloud.generate_wordcloud(2, file_name)
            self.tweetChart.barChart(file_name=file_name)
            self.tweetChart.pieChart(file_name=file_name)
       
        
        if mode == True:
             
            Map_Noperson(self.tweets)
            lista.build_list()
            
            
        else:
            Mappa_Person(self.tweets)
            lista.build_list_person()
           
            
        
        Tools(lista)

        

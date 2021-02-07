import tkinter as tk
from sys import platform
if platform == "darwin":
    from tkmacosx import Button as bt
else:
    from tkinter import Button as bt
import tkcalendar
from view import list_tweets as listtw
from view.mappa_person import Mappa_Person
from view.mappa_noperson import Map_Noperson
from utility.tools import Tools
from twitter.twitter_handler import Twitter_handler
from view.Word_cloud import Word_cloud
from utility.loader import Loader
from utility.geography import address_to_coordinates
from utility.geography import address
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
from tkinter.filedialog import askopenfile
from view.tweetChart import TweetChart
from datetime import datetime, timedelta

class Form():

    caricatore = Loader()
    tweetChart = TweetChart()
    language = ["it", "en", "fr", "de", "es"]
    filter = ["mixed", "recent", "popular"]
    ricerca = Twitter_handler()
    tweets = []

    def __init__(self):
        # Inizializzazione del frame
        self.container = tk.Frame()

        # Lo stile per il calendario
        stile = ttk.Style(self.container)
        stile.theme_use('clam')

        # Titolo
        self.titolo = tk.Label(self.container, text = "Ricerca dei tweets", fg = "white", bg = "blue")
        # Bottoni scelta tipologia form (parola chiave, persona/multipersona)
        self.button_parolachiave = bt(self.container, text = "Ricerca Parola Chiave",state=DISABLED, command=self.check_state)
        self.button_persona = bt(self.container, text = "Ricerca per Persona", command=self.check_state)
        # Descrizioni del form
        self.descr_parola_chiave = tk.Label(self.container, text = "Parola Chiave:")
        self.descr_coordinate = tk.Label(self.container, text = "Località:")
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
        self.data_inizio.set_date(datetime.now() - timedelta(7))
        self.data_inizio._top_cal.overrideredirect(False)
        self.data_fine = tkcalendar.DateEntry(self.container)
        self.data_fine.set_date(datetime.now() + timedelta(1))
        self.data_fine._top_cal.overrideredirect(False)
        # Bottoni
        self.cerca = bt(self.container, text = "Cerca", command = self.check)
        self.carica = bt(self.container, text = "Carica Tweets", command = self.load)
        self.salva = bt(self.container, text = "Salva", command = self.save)

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

    # Funzione per la ricerca dei tweets con parola chiave
    def get(self):
        tmp1 = address_to_coordinates(self.coordinate.get())
        tmp2 = self.raggio.get()
        try:
            geocodifica = str(tmp1[1]) + "," + str(tmp1[0]) + "," + str(tmp2) + "km"
        except:
            geocodifica = 'NULL'
        self.tweets = self.ricerca.search(self.parola_chiave.get(), geocodifica, self.lingua.get(), self.filtro.get(), float(self.numero.get()), self.data_inizio.get_date(), self.data_fine.get_date())
        self.set_tools(True)

    # Funzione che controlla che i parametri in input siano tutti corretti
    # Se non sono corretti, esce un popup
    def check(self):
        # Parola chiave
        if self.parola_chiave.get() == "":
            tk.messagebox.showinfo('Errore nell\'input','La parola chiave non è stata inserita.')
        # Numero dei tweet
        elif (self.numero.get()).isdigit() == False:
            tk.messagebox.showinfo('Errore nell\'input','Il numero di tweet inserito non è un numero.')
        elif int(self.numero.get()) <= 0:
            tk.messagebox.showinfo('Errore nell\'input','Il numero di tweet inserito è invalido.')
        # Località e raggio
        elif self.coordinate.get() != "" and self.raggio.get() == "":
            tk.messagebox.showinfo('Errore nell\'input','Hai inserito la località ma non il raggio.')
        elif self.coordinate.get() == "" and self.raggio.get() != "":
            tk.messagebox.showinfo('Errore nell\'input','Hai inserito il raggio ma non la località.')
        # Località e Raggio vuoto
        elif self.coordinate.get() == "" and self.raggio.get() == "":
            self.get()
        # C'è la località
        else:
            # Località
            if address_to_coordinates(self.coordinate.get()) == -1:
                tk.messagebox.showinfo('Errore nell\'input','Località non trovata.')
            elif address_to_coordinates(self.coordinate.get()) == -2:
                tk.messagebox.showinfo('Errore nell\'input','Errore nella ricerca della località.')
            # Raggio
            else:
                try:
                    if float(self.raggio.get()) <= 0:
                        tk.messagebox.showinfo('Errore nell\'input','Il raggio inserito è invalido.')
                    else:
                        result = tk.messagebox.askquestion('Località','La località indicata è: ' + address(self.coordinate.get()))
                        if result == 'yes':
                            self.get()                        
                except:
                    tk.messagebox.showinfo('Errore nell\'input','Il raggio inserito non è un numero.')       
                    
    # Funzione per la ricerca dei tweet tramite persona
    def get_person(self):
        self.tweets = self.ricerca.search_user(self.parola_chiave.get(), self.data_inizio.get_date(), self.data_fine.get_date())
        if self.tweets == -1:
            tk.messagebox.showinfo('Errore nell\'input','L\'ID utente è errato.')
            return []
        else:
            self.set_tools(False)
            return self.tweets

    # Funzione per caricamento tweets da file json
    def load(self):
        f = askopenfile(mode = 'r', filetypes = [('JSON Files', '*.json')])
        self.caricatore.set(f.name)
        self.tweets = self.caricatore.load()
        self.set_tools(True, file_name=f.name)

    # Funzione per salvataggio tweets
    def save(self):
        self.caricatore.store(self.tweets)

    # Gestione dei bottoni nel form
    def check_state(self):
        if self.button_parolachiave['state'] == 'disabled':
            self.button_parolachiave['state'] = NORMAL
            self.button_persona['state'] = DISABLED
            self.show_persona()
        else:
            self.button_persona['state'] = NORMAL
            self.button_parolachiave['state'] = DISABLED
            self.show_parolaChiave()
            
    # Attivazione dei bottoni nel form per la ricerca per parola chiave
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
        
    # Attivazione dei bottoni del form per la ricerca per persona
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

    # Ritorna il form
    def get_container(self):
        return self.container
    
    # Imposta i vari tools per l'analisi dei tweet con i tweets ricercati
    def set_tools(self, mode, file_name=""):
        
        if self.tweets:
            # Ci sono i tweet
            lista = listtw.ListTweets(self.tweets)
            wordcloud = Word_cloud(self.ricerca.extend_lang(self.lingua.get()))
            
            if file_name == "":
                word_cloud_format = self.ricerca.get_tweets_for_wordcloud(self.tweets)       
                wordcloud.generate_wordcloud(1,word_cloud_format)
                self.tweetChart.barChart(tweets=self.tweets)
                self.tweetChart.pieChart(tweets=self.tweets)
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

        else:
            # La ricerca non ha trovato tweet
            tk.messagebox.showinfo('Errore nell\'output','Non sono stati trovati tweet.')
        

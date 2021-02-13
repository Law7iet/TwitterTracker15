import json
from tkinter.filedialog import askopenfile
import os

# Classe responsabile del caricamento e scaricamento dei tweet raccolti
class Loader():

    # Inizializza il costruttore, selezionando il file Tweets.json come default
    # Se non esiste il file lo crea, altrimenti usa quello esistente
    # INPUT: niente
    # OUTPUT: niente
    def __init__(self):
        self.file_name = 'Tweets.json'
        self.data = {}
        try:
            f = open(os.path.dirname(__file__) + '/../' + self.file_name)
        except IOError:
            f = open(os.path.dirname(__file__) + '/../' + self.file_name, 'w+')
            f.write(
'''{
    "Tweets": []
}''')
            f.close()
            f = open(os.path.dirname(__file__) + '/../' + self.file_name)
        finally:
            self.data = json.load(f)
            f.close()

    # Cambia il file da utilizzare
    # Cambia anche le informazioni in data
    # INPUT: una stringa
    # OUTPUT: niente
    def set(self, file_name):
        self.file_name = file_name
        f = open(self.file_name)
        self.data = json.load(f)
        f.close()

    # Ritorna le informazioni del file
    # INPUT: niente
    # OUTPUT: una lista di tweet (dizionari)
    def load(self):
        return self.data['Tweets']

    # Inserisce nel file selezionato i tweet passati per paremtro
    # Non inserisce eventuali duplicati
    # INPUT: una lista di tweet (dizionari)
    # OUTPUT: niente
    def store(self, tweets):
        f = askopenfile(mode = 'r', filetypes = [('JSON Files', '*.json')])
        self.set(f.name)
        tmp = self.data['Tweets']
        for tweet in tweets:
            copy = False
            for element in tmp:
                if element['id'] == tweet['id']:
                    copy = True
            if copy == False:
                tmp.append(tweet)
        self.data['Tweets'] = tmp
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent = 4)

    # Cancella tutti i dati del file selezionato
    # INPUT: niente
    # OUTPUT: niente
    def clean(self):
        with open(self.file_name, 'w') as f:
            f.open('{ "Tweets": [] }')

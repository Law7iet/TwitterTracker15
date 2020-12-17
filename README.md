# Progetto di Ingegneria del software 2020
## Struttura del Progetto
```
IngSw2020
|- src
|   |- graphics
|   |   |- __init__.py
|   |   |- main_application.py
|   |   |- page_0.py
|   |   |- page_1.py
|   |   |- page_2.py
|   |
|   |- twitter
|   |   |- __init__.py
|   |   |- twitter_app_credentials.py
|   |   |- twitter_handler.py
|   |
|   |- utility
|   |   |- __init__.py
|   |   |- converter.py
|   |   |- loader.py
|   |   |- others.py
|   |
|   |- main.py
|   |- test.py
|   |- Tweets.json
|
|- README.md
```
Dove:
- `README.py` è il seguente documento, indica la struttura, i file presenti ed eventuali annotazioni
- `src` è il folder contente tutti i codici sorgente
    - `graphics` è il modulo contente la parte grafica
        - `main_application.py` è l'applicazione principale
        - `page_0.py` è la pagina home
        - `page_1.py` è la pagina per la ricerca dei tweet
        - `page_2.py` è la pagina per la ricerca dei tweet degli utenti
    - `twitter` è il modulo contente la parte della raccolta dei tweet
        - `twitter_app_credentials.py` è il file contenente le credenziali per l'accesso alle API di Twitter
        - `twitter_handler.py` è l'oggetto che ricerca i tweet
    - `utility` è un modulo contente oggetti di utilità
        - `converter.py` è la classe che converte alcuni oggetti di *Tweepy* in tipi di Python e viceversa
        - `loader.py` è la classe che carica/scarica nel file `Tweet.json` i tweet
        - `other.py` funzioni per le coordinate e geolocalizzazione (da realizzarlo in oggetti)
    - `main.py` è il file principale da eseguire
    - `test.py` è il file contente le funzioni da provare localmente (senza GUI).
    - `Tweets.json` contiene i tweet raccolti.

### tweepy.models.status
Tale oggetto (che viene ritornato dalle funzioni di ricerca) può essere convertito in un dizionario in formato json mediante il metodo con l'oggetto `Converter`.
Le chiavi che lo compongono sono descritte in questo [link](https://www.geeksforgeeks.org/python-status-object-in-tweepy/). Le chiavi più importanti sono:
- *created_at*, data di creazione;
- *id*, l'identificativo dello status;
- *text*, il testo;
- *entities*, allegati come hashtags (*entities['hashtags']*), URL,..
- *user*, l'utente che ha pubblicato lo status;
- *place*, *geo* e *coordinates*, per la geolocalizzazione;
- *retweet_count* e *favorite_count*, come misure di valutazione.

### LE COORDINATE SONO DI TIPO [LONGITUDINE, LATITUDINE]
### converter va dentro others
### link ad un tweet sapendo il suo id: twitter.com/anyuser/status/id
### Loader
Classe con attributi:
- file_name, il path del nome del file
- data, i dati del file
Metodi:
- costruttore, apre un file di default e lo usa come contenitore di tweet; se non esiste lo crea, altrimenti lo utilizza (non sovrascrive i vecchi dati)
- set, seleziona il file e inserisce in "data" i dati del file
- load, prende in input i tweet da caricare nel file. I duplicati non vengono caricati.

# file.json
E' una raccolta di tweet che segue la seconda struttura:
{'Tweets' = [
		{tweet},
		{tweet},
		{tweet}
	]
}


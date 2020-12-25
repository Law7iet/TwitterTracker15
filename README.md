# Progetto di Ingegneria del software 2020
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

### file.json
E' una raccolta di tweet che segue la seconda struttura:
{'Tweets' = [
		{tweet},
		{tweet},
		{tweet}
	]
}

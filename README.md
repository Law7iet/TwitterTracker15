# Progetto di Ingegneria del software 2020

## Struttura del Progetto
```
IngSw2020
|- src
|   |- twitter
|   |   |- __init__.py
|   |   |- Twitter_app_credentials.py
|   |   |- Twitter_handler.py
|   |
|   |- utility
|   |   |- converter
|   |   |   |- __init__.py
|   |   |   |- Converter.py
|   |   |
|   |   |- loader
|   |   |   |- __init__.py
|   |   |   |- Loader.py
|   |   |
|   |   |- __init__.py
|   |
|   |- Test.py
|   |- Tweets.json
|
|- README.md
```
Dove:
- `Tweets.json` contiene i tweet raccolti.
- `Test.py` è il file *main* da eseguire.
- `twitter` è un modulo contenente la classe `Twitter_handler.py` che ricerca tweets, e `Twitter_app_credentials.py`, che contiene le infomazioni per il login.
- `utility` è un package contente due moduli:
    - `converter`, che contiene la classe `Converter.py`, utile per convertire degli oggetti complessi in tipi di Python.
    - `loader`, che contiene la classe `Loader.py`, ed è l'oggetto responsabile del caricamentento e conservazione dei tweet raccolti.

### api.search
Ricerca gli ultimi post

### Tweet ID
I tweet sono detti anche status.
Hanno ID unici che rappresentano

### Coordinate
Su Google, possono essere in diversi formati:
- DMS (gradi, minuti e secondi): `xx°xx'xx″ yy°yy'yy″`
- DDM (gradi e minuti decimali): `xx xx.xx, yy yy.yy`
- DD (gradi decimali): `xx.xx, yy.yy`
Di default il primo valore è N e il secondo è E.
Nelle API di Tweepy userò il formato DD nella seguente sintassi:
```
geocode='xx.xx,yy.yy,z'
```
dove `z` indica il raggio e l'unità di misura `xkm`.

Quando si cercando "tutti" i tweets, per efficienza si cercano solamente i primi 100.

### tweepy.models.status
Tale oggetto (che viene ritornato dalle funzioni di ricerca) può essere convertito in un dizionario in formato json mediante il metodo `_json`.
Le chiavi che lo compongono sono descritte in questo [link](https://www.geeksforgeeks.org/python-status-object-in-tweepy/). Le chiavi più importanti sono:
- *created_at*, data di creazione;
- *id*, l'identificativo dello status;
- *text*, il testo;
- *entities*, allegati come hashtags (*entities['hashtags']*), URL,..
- *user*, l'utente che ha pubblicato lo status;
- *place*, *geo* e *coordinates*, per la geolocalizzazione;
- *retweet_count* e *favorite_count*, come misure di valutazione.

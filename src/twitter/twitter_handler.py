from utility.others import is_in
import tweepy
from twitter import twitter_app_credentials as credentials

# E' la classe che si occupa di cercare i tweet usando le API di Twitter
class Twitter_handler():

    # Inizializza le credeziali
    # INPUT: niente
    # OUTPUT: niente
    def __init__(self):
        self.auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
        self.auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        self.api = tweepy.API(self.auth)

    # Converte l'oggetto tweepy.cursor.ItemIterator in una lista di dizionari
    # Ogni elemento di tipo dizionario nella lista e' un tweet
    # INPUT: l'oggetto tweepy.cursor.ItemIterator
    # OUTPUT una lista composta da dizionari
    def convert_ItemIterator_to_list(self, tweets):
        tweets_list = []
        for tweet in tweets:
            tweets_list.append(tweet._json)
        return tweets_list

    # Cerca i tweets con una certa stringa
    # INPUT: una sequenza di strighe; le stringhe sono la parola chiave, la lingua, il filtro, il numero, la data d'inizio e fine di ricerca
    # OUTPUT: una lista di dizionari, che rappresentano il JSON dei vari tweet
    def search_string(self, content, language, res_type, counts, date_since, date_until):
        tweets = tweepy.Cursor(self.api.search, q = content, lang = language, result_type = res_type, since = date_since, until = date_until).items(counts)
        tweets = self.convert_ItemIterator_to_list(tweets)
        return tweets

    # Cerca i tweets con una certa stringa
    # INPUT: una sequenza di strighe; le stringhe sono la parola chiave, la geocodifica, la lingua, il filtro, il numero, la data d'inizio e fine di ricerca
    # OUTPUT: una lista di dizionari, che rappresentano il JSON dei vari tweet
    def search_geo(self, content, geo, language, res_type, counts, date_since, date_until):
        tweets = tweepy.Cursor(self.api.search, q = content, geo = geo, lang = language, result_type = res_type, since = date_since, until = date_until).items(100)
        tweets = self.convert_ItemIterator_to_list(tweets)
        geolocated_tweets = []
        geo = geo.split(',')
        # controlla se il tweet è all'interno dell'area
        for tweet in tweets:
            if tweet["place"] != None:
                place = tweet["place"]
                coordinates = place["bounding_box"]
                if coordinates["coordinates"] != None:
                    coordinates = (coordinates["coordinates"])[0]
                    if is_in([geo[1], geo[0]], geo[2], coordinates) == True and len(geolocated_tweets) < int(counts):
                        geolocated_tweets.append(tweet)

        return geolocated_tweets

    # Funzione di smistamento: in base agli argomenti ottenuti dal form chiama la specifica funzione di ricerca
    # INPUT: una sequenza arbitraria di valori
    # OUTPUT: in base ai paramentri, ritorna il valore di una funzione di ricerca
    def search(self, *args):
        if args[1] == 'NULL':
            return self.search_string(args[0], args[2], args[3], args[4], args[5], args[6])
        else:
            return self.search_geo(args[0], args[1], args[2], args[3], args[4], args[5], args[6])

    # Ricerca i tweets di un singolo utente, oppure di un gruppo di utenti
    # INPUT: l'id dell'utente o degli utenti separati da una virgola e le date di inizo e di fine
    # OUTPUT: una lista di liste di dizionari; la prima lista ha come elementi i differenti utenti, la seconda lista è l'insieme dei tweet di un utente e il dizionario rappresenta un tweet di tipo JSON
    def search_user(self, identifiers, data_inizio, data_fine):
        # setup
        data_inizio = str(data_inizio)
        data_fine = str(data_fine)
        data_inizio = data_inizio.split('-')
        data_fine = data_fine.split('-')
        identifiers = identifiers.split(', ')
        list_tweets = []
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

        for identifier in identifiers:
            tweets = self.api.user_timeline(identifier, count = 200)
            tweets = self.convert_ItemIterator_to_list(tweets)
            # cancella i vecchi tweet
            i = 0
            flag = True
            while i < len(tweets) and flag:
                tmp = tweets[i]
                tmp = tmp['created_at'].split()
                month = months[tmp[1]]
                if int(tmp[5]) < int(data_inizio[0]):
                    flag = False
                elif int(tmp[5]) == int(data_inizio[0]):
                    if int(month) < int(data_inizio[1]):
                        flag = False
                    elif int(month) == int(data_inizio[1]):
                        if int(tmp[2]) < int(data_inizio[2]):
                            flag = False
                i += 1
            tweets = tweets[0:(i - 1)]

            # cancella i tweet recenti
            i = 0
            flag = True
            while i < len(tweets) and flag:
                tmp = tweets[i]
                tmp = tmp['created_at'].split()
                month = months[tmp[1]]
                if int(tmp[5]) > int(data_inizio[0]):
                    flag = False
                elif int(tmp[5]) == int(data_inizio[0]):
                    if int(month) > int(data_inizio[1]):
                        flag = False
                    elif int(month) == int(data_inizio[1]):
                        if int(tmp[2]) > int(data_inizio[2]):
                            flag = False
                i += 1
            tweets = tweets[(i - 1):]

            # aggiunge i tweet nella lista principale
            list_tweets.append(tweets)

        return list_tweets

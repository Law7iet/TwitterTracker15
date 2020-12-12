import utility.converter as cv
import utility.loader as ld
import twitter.twitter_handler as th
   
convertitore = cv.Converter()
caricatore = ld.Loader('Tweets.json')
ricerca = th.Twitter_handler()
  
stringa = '#IngSw2020'
falconara = '43.6242,13.404,20km'
bologna = '44.5075,11.3514,10km'
vuoto = ','
lingua = 'it'
filtro = 'recent'
numero = 10
data_inizio = '2020-12-04'
data_fine = '2020-12-11'

id = 'FNATIC'
id = 'xLalisaxx'
id = 'Law_2885'
    
tweets = ricerca.search(stringa, falconara, lingua, filtro, numero, data_inizio, data_fine)
#tweets = ricerca.search_user(id, data_inizio_tupla)
    
tmp = 1
for element in tweets:
    print(tmp)
    print(element["text"])
    print(element["created_at"])
    tmp += 1

caricatore.store(tweets)
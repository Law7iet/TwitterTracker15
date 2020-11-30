import utility.converter.Converter as cv
import utility.loader.Loader as ld
import twitter.Twitter_handler as th

convertitore = cv.Converter()
caricatore = ld.Loader('Tweets.json')
ricerca = th.Twitter_handler()

stringa = '#IngSw2020'
lingua = 'it'
geolocalizzazione_x = '43.6242'
geolocalizzazione_y = '13.404'
area = '10'
misura = 'km'
data_inizio = {'2020', '11', '23'}
data_fine = {'2020', '11', '28'}
elementi = 5
result_type = 'recent'

tweets = ricerca.search(stringa, lingua, result_type, elementi, data_inizio, data_fine)
for element in tweets:
    print(element["text"])
#caricatore.store(tweets)

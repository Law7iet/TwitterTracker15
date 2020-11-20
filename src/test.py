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
data_inizio = {'2020', '11', '18'}
data_fine = {'2020', '11', '19'}
elementi = 2
    
#tweets = ricerca.search_geo(stringa, lingua, geolocalizzazione_x, geolocalizzazione_y, area, misura, elementi)
tweets = ricerca.search_string(stringa, lingua, elementi)
caricatore.store(tweets)

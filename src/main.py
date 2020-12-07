'''
Created on 3 dic 2020

@author: L
'''

if __name__ == '__main__':
    import utility.converter as cv
    import utility.loader as ld
    import twitter.twitter_handler as th
    
    convertitore = cv.Converter()
    caricatore = ld.Loader('Tweets.json')
    ricerca = th.Twitter_handler()
    
    stringa = '#IngSw2020'
    lingua = 'it'
    falconara = '43.6242,13.404,2km'
    bologna = '44,5075,11,3514,20km'
    data_inizio_tupla = ('2020', '11', '20')
    data_inizio = '2020-11-29'
    data_fine = '2020-12-07'
    elementi = 20
    result_type = 'recent'
    
    id = 'FNATIC'
    id = 'xLalisaxx'
    id = 'Law_2885'
    
    tweets = ricerca.search(stringa, falconara, lingua, result_type, elementi, data_inizio, data_fine)
    #tweets = ricerca.search_user(id, data_inizio_tupla)
    
    tmp = 1
    for element in tweets:
        print(tmp)
        print(element["text"])
        print(element["place"]["full_name"])
        print(element["place"]["bounding_box"]["coordinates"][0])
        tmp += 1
    
    print(len(tweets))
#    caricatore.store(tweets)
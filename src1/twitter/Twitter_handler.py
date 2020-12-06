'''
Created on 20 nov 2020

@author: L
'''

from utility.converter import Converter as cv
import tweepy
import Twitter_app_credentials as credentials

class Twitter_handler(object):
    
    convertitore = ''
    tweets = []
    auth = ''
    api = ''
    
    # Create the authentication
    # Create the object convertitore
    def __init__(self):
        self.auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
        self.auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        self.api = tweepy.API(self.auth)
        self.convertitore = cv.Converter()
        
    # Search tweets based on the string passed in input
    # INPUT: ...
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_string(self, content, language, type, counts, date_since, date_until):
        #tweets = tweepy.Cursor(self.api.search, q = content, lang = language, result_type = type, since = date_since, until = date_until).items(counts)
        tweets = tweepy.Cursor(self.api.search, q = content, lang = language, result_type = type).items(counts)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets

    # Search tweets based on the geolocation
    # INPUT: ...
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_geo(self, content, geo, lang, result_type, items, since, until):
        tweets = tweepy.Cursor(self.api.search, q = content, geo = geo, result_type = result_type, since = since, until = until).items(items)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets
    
    def search(self, *args):
        if len(args) == 6:
            return self.search_string(args[0], args[1], args[2], args[3], args[4], args[5])
        elif len(args) == 7:
            return self.search_geo(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        else:
            print('Errore.')
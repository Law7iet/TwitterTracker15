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
    # INPUT: the string to search, the language and the number of tweets
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_string(self, content, lang, items):
        tweets = tweepy.Cursor(self.api.search, q = content, lang = lang, result_type = 'recent').items(items)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets

    # Search tweets based on the geolocation
    # INPUT: the string to search, the language, the coordinates in decimal degrees, the range of the area, the measure unit and the number of tweets
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_geo(self, content, lang, coordinate_x, coordinate_y, area, measure, items):
        coordinate = str(coordinate_x) + ',' + str(coordinate_y) + ',' + str(area) + measure
        tweets = tweepy.Cursor(self.api.search, q = content, lang = lang, geocode = coordinate, result_type = 'recent').items(items)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets
    
    # Search tweets based on the time:
    # INPUT the string to search, the language, 2 Python tuples {YYYY, MM, DD}, cointaining the dates in numbers and the number of tweets
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_date(self, content, lang, start, end, items):
        date_since = str(start[0]) + '-' + str(start[1]) + '-' + str(start[2])
        date_until = str(end[0]) + '-' + str(end[1]) + '-' + str(end[2])
        tweets = tweepy.Cursor(self.api.search, q = content, lang = lang, since = date_since, until = date_until, result_type = "recent").items(items)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets
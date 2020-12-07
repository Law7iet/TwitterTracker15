'''
Created on 3 dic 2020

@author: L
'''

from utility.converter import Converter
from utility.others import is_in
import tweepy
import twitter_app_credentials as credentials


class Twitter_handler():

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
        self.convertitore = Converter()

    # Search tweets based on the string passed in input
    # INPUT: ...
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_string(self, content, language, res_type, counts, date_since, date_until):
        tweets = tweepy.Cursor(self.api.search, q = content, lang = language, result_type = res_type, since = date_since, until = date_until).items(counts)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)
        return tweets

    # Search tweets based on the geolocation
    # INPUT: ...
    # OUTPUT: a list of dict, cointaing the tweets in JSON
    def search_geo(self, content, geo, language, res_type, counts, date_since, date_until):
        print(content)
        print(geo)
        print(language)
        print(res_type)
        print(counts)
        print(date_since)
        print(date_until)
        tweets = tweepy.Cursor(self.api.search, q = content, geo = geo, lang = language, result_type = res_type, since = date_since, until = date_until).items(counts)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)

        geolocated_tweets = []
        geo = geo.split(',')
        
        for tweet in tweets:
            if tweet["place"] != None:
                place = tweet["place"]
                coordinates = place["bounding_box"]
                if coordinates["coordinates"] != None:
                    coordinates = (coordinates["coordinates"])[0]
                    if is_in([geo[1], geo[0]], geo[2], coordinates) == True:
                        geolocated_tweets.append(tweet)
                        
        return geolocated_tweets

    def search(self, *args):
        if len(args) == 6:
            return self.search_string(args[0], args[1], args[2], args[3], args[4], args[5])
        elif len(args) == 7:
            return self.search_geo(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        else:
            print('Errore.')

    # Search an user tweets posted after a given date
    # INPUT: the user id and a date
    # OUTPUT: a list of dict, coinaining the tweets in JSON
    def search_user(self, identifier, data_inizio, data_fine):
        tweets = self.api.user_timeline(identifier, count=200)
        tweets = self.convertitore.convert_to_Status_list(tweets)
        tweets = self.convertitore.convert_to_dict_list(tweets)

        # delete old tweets
        i = 0
        flag = True
        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
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
        
        # delete recent tweets
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
        
        return tweets

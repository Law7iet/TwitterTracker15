import json
import tweepy
import twitter_app_credentials as credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

import utils

# Search tweets based on the geolocation
# INPUT:
# OUTPUT: a list of tweepy.models.Status
def search_geo(content, language, coordinate_x, coordinate_y, area, measure, items):
    
    # TO-DO transform coordate to DD format
    # DD format is a string: xx.xx
    
    #coordinates = coordinate_x + ',' + coordinate_y + ',' + area + measure

    tweets = tweepy.Cursor(api.search, q=content, lang=language, geocode='41.87839,12.48634,1000km').items(5)
    return utils.convert_to_list(tweets)

# Search tweets based on the time:
# INPUT 
# OUTPUT
def search_date(content, start_day, start_month, start_year, end_day, end_month, end_year, items):
    since = str(start_year) + '-' + str(start_month) + '-' + str(start_day)
    until = str(end_year) + '-' + str(end_month) + '-' + str(end_day)
    tweets = tweepy.Cursor(api.search, q=content, since=since, until=until).items(items)
    return utils.convert_to_list(tweets)

# Covert a tweet in a json string
# INPUT: a list of tweepy.models.Status object
# OUTPUT: a json file
def convert_to_str_json(tweet):
    return json.dumps(tweet._json, indent=4, separators=(',', ': '))
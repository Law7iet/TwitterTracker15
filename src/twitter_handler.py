import json
import tweepy
import twitter_app_credentials as credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

import utils.Converter as cv
y = cv.Converter()

# Search tweets based on the geolocation
# INPUT:
# OUTPUT: a list of tweepy.models.Status
def search_geo(coordinate_x, coordinate_y, area, items):
    # TO-DO transform coordate to DD format
    # DD format is a string: xx.xx
    coordinate = str(coordinate_x) + ',' + str(coordinate_y) + ',' + str(area) + 'km'
    tweets = tweepy.Cursor(api.search, geocode=coordinate).items(items)
    return y.convert_to_list(tweets)

# Search tweets based on the time:
# INPUT 2 Python tuples {YYYY, MM, DD}, cointaining the dates in numbers
# OUTPUT a list of tweepy.models.Status
def search_date(content, start, end, items):
    date_since = str(start[0]) + '-' + str(start[1]) + '-' + str(start[2])
    date_until = str(end[0]) + '-' + str(end[1]) + '-' + str(end[2])
    tweets = tweepy.Cursor(api.search, q=content, since=date_since, until=date_until, result_type="recent").items(items)
    return y.convert_to_list(tweets)

# Covert a tweet in a json string
# INPUT: a list of tweepy.models.Status object
# OUTPUT: a json file
def convert_to_str_json(tweet):
    return json.dumps(tweet._json, indent=4, separators=(',', ': '))
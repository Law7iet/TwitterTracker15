# Test tweepy
import tweepy
import twitter_app_credentials as credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

# Test twitter_handler
#import twitter_handler

tweets = tweepy.Cursor(api.search, q='#IngSw2020').items(5)

# Test loader
import loader.Loader as ld
x = ld.LOADER('Tweets.json')
test = x.load()
print(test)

import utils.Converter as cv
y = cv.Converter()
array = y.convert_to_list(tweets)
aaa = []
for element in array:
    aaa.append(y.convert_to_dict_json(element))

x.store(aaa)
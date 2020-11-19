# Test tweepy
import tweepy
import twitter_app_credentials as credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

# Test twitter_handler
import twitter_handler as th

inizio = (2020, 11, 16)
fine = (2020, 11, 17)
items = 3
# coordinate di Bologna https://www.google.com/search?client=safari&rls=en&q=bologna+coordinate+geografiche&ie=UTF-8&oe=UTF-8
coordinate_x ='44.5075'
coordinate_y = '11.3514'
area = '20'

#tweets = tweepy.Cursor(api.search, q='#IngSw2020', since='2020-11-16', until='2020-11-18', result_type='recent').items(items)
#tweets = y.convert_to_list(tweets)

#tweets = th.search_date('contenuto', inizio, fine, items)
tweets = th.search_geo(coordinate_x, coordinate_y, area, items)

# Test loader
import loader.Loader as ld
import utils.Converter as cv

x = ld.Loader('Tweets.json')
y = cv.Converter()

test = x.load()

tmp = []
for element in tweets:
    tmp.append(y.convert_to_dict_json(element))
x.store(tmp)
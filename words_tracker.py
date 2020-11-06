# Words tracker on Twitter

import tweepy
import twitter_app_credentials as credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

# Putting tweepy.API methods inside Cursor (e.g. API.search);
# Excluded retweets and replies;
# Geocoding: longitude, latitude, radius
public_tweets = tweepy.Cursor(api.search, q='virus -filter:retweets -filter:replies', lang='it', geocode='41.87839,12.48634,1000km').items(3)

i = 1
for tweet in public_tweets:
    print(i)
    print (tweet.text)
    i = i+1
        
    

    
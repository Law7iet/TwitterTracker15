class Converter(object):

    def __init__(self):
        '''
        Constructor
        '''
    
    # Convert a tweepy.cursor.ItemIterator to a Python list
    # INPUT a tweepy.cursor.ItemIterator object
    # OUTPUT a list of tweepy.models.Status
    def convert_to_Status_list(self, tweets):
        tweets_list = []
        for tweet in tweets:
            tweets_list.append(tweet)
        return tweets_list
    
    # Convert a tweepy.cursor.ItemIterator to a Python list
    # INPUT a tweepy.cursor.ItemIterator object
    # OUTPUT a list of tweepy.models.Status
    def convert_to_dict_list(self, tweets):
        tweets = self.convert_to_Status_list(tweets)
        tweets_list = []
        for tweet in tweets:
            tmp = tweet._json
            tweets_list.append(tmp)
        return tweets_list
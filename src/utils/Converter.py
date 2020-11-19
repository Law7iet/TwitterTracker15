class Converter():

    def __init__(self):
        '''
        Constructor
        '''
    
    # convert a tweepy.cursor.ItemIterator to a Python list
    # INPUT a tweepy.cursor.ItemIterator onject
    # OUTPUT a list of tweepy.models.Status
    def convert_to_list(self, tweets):
        tweets_list = []
        for tweet in tweets:
            tweets_list.append(tweet)
        return tweets_list

    # Convert a tweet in a json dictionary
    # INPUT: a tweepy.models.Status object
    # OUTPUT: a json dict
    def convert_to_dict_json(self, tweet):
        return tweet._json
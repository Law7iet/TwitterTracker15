import json

class Loader():

    file_name = 'str'
    data = {}

    # Set the correct file name
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.data = json.load(f)

    # Load (return) the stored json data
    # OUTPUT: Python array
    def load(self):
        return self.data['Tweets']
        
    # Store tweets in the original file, appending it
    # It deletes duplicates
    # INPUT: Python array
    def store(self, tweets):
        tmp = self.data['Tweets']
        for tweet in tweets:
            copy = False
            for element in tmp:
                if element['id'] == tweet['id']:
                    copy = True
            if copy == False:
                tmp.append(tweet)
        self.data['Tweets'] = tmp
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
        
    # Clean the tweets in Tweets.json
    def clean(self):
        with open(self.file_name, 'w') as f:
            f.open('{ "Tweets": [] }')
# Word cloud creation from tweets 

import os
import nltk
from nltk.corpus import stopwords  
import re
from wordcloud import WordCloud
import json

class Word_cloud: 
      
    # Stopwords (the first attribute of the constructor) must be a set for WordCloud to function
    # Go to your folder: nltk_data/corpora/stopwords 
    # Open the file and add or remove other stopwords
    # Better to add them at the end so that it doesn't mix with the original dataset
    # INPUT: lang must be a full string for language, e.g.: 'italian', 'english', letters NOT capital.
 
    def __init__(self, lang):
        self.stop_words = set(stopwords.words(lang)) 
        self.text_from_json = ""
        self.final_text = ""
        self.cleaned_text = ""
        self.json_string = ""
    
    # Removing https pattern from the text with regular expressions
    def remove_https_pattern(self, text):
        self.cleaned_text = re.sub(r'https?://\S+','', text)
        return self.cleaned_text
    
    # Making the JSON file a string 
    def json_to_string(self, json_file):
        with open(json_file) as fileobj:
            # First create a dictionary 
            dict_tweets = json.loads(fileobj.read())
            # Then get only the "Tweets" field
            data = dict_tweets["Tweets"]
            # Cycle through the objects in the dictionary and get the text only
            for tweet in data:
                self.json_string += tweet["text"] + " "
        return self.json_string
    
    def generate_wordcloud(self, mode, tweets):    
        # mode = 1 means simple search wordcloud 
        if(mode == 1):
            self.final_text = self.remove_https_pattern(tweets) 
            
        # mode = 2 means JSON wordcloud        
        elif(mode == 2):
            self.text_from_json = self.json_to_string(tweets)
            self.final_text = self.remove_https_pattern(self.text_from_json)
        
        # Generate the wordcloud 
        wordcloud = WordCloud(stopwords=self.stop_words, background_color="black").generate(self.final_text)
        # Display the generated wordcloud in a PNG image
        wordcloud.to_file(os.path.dirname(__file__) + "/../wordcloud.jpeg")
  
    
   

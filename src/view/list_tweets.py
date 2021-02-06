'''
Created on 19 dic 2020

@author: andreamancini
'''
'''
Classe della Lista dei Tweet
'''
class ListTweets(list):
    '''
    classdocs
    '''
    html = "<div id='listatweet' style='display:none;'>\n"
    user_tweets = []
    
    def __init__(self, tweet=None):
        
        #inizializza i tweet ricevuti
        super().__init__(tweet)
        self.user_tweets = tweet
        
    #costruisce l'html per la lista dei tweet dalla ricerca per persona
    def build_list_person(self):
        
        for tweets in self.user_tweets:
            
            for tweet in tweets:
                    
                self.html +='<blockquote class="twitter-tweet tw-align-center" tw-align-center data-lang="en"><p lang="en" dir="ltr" style="vertical-align: middle;"><a href="https://twitter.com/vitadiste/status/'+str(tweet['id'])+'?ref_src=twsrc%5Etfw"></a>'
                self.html +='</blockquote>\n'
    
        self.html += "</div>\n"
        self.html += '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n'
    
    #costuisce l'html per la lista dei tweet dalla ricerca per parola chiave
    def build_list(self):
        
            
        for tweet in self.user_tweets:
                    
            self.html +='<blockquote class="twitter-tweet tw-align-center" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/vitadiste/status/'+str(tweet['id'])+'?ref_src=twsrc%5Etfw"></a>'
            self.html +='</blockquote>\n'
    
        self.html += "</div>\n"
        self.html += '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>\n'
        
    #restituisce l'html della lista
    def get_list(self):
        
        return self.html
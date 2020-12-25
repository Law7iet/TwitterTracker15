'''
Created on 19 dic 2020

@author: andreamancini
'''
import webview


class ListTweets(list):
    '''
    classdocs
    '''
    html = "<html>\n"+"<body>\n"
    user_tweets = []

    def __init__(self, tweet=None):

        super().__init__(tweet)
        self.user_tweets = tweet


    def build_list_person(self):

        for tweets in self.user_tweets:

            for tweet in tweets:

                self.html +='<blockquote class="twitter-tweet" tw-align-center data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/vitadiste/status/'+str(tweet['id'])+'?ref_src=twsrc%5Etfw"></a>'
                self.html +='</blockquote>\n'

        self.html += "</body>\n"
        self.html += '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'


    def build_list(self):


        for tweet in self.user_tweets:

            self.html +='<blockquote class="twitter-tweet" tw-align-center data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/vitadiste/status/'+str(tweet['id'])+'?ref_src=twsrc%5Etfw"></a>'
            self.html +='</blockquote>\n'

        self.html += "</body>\n"
        self.html += '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

    def open_window(self):

#        print(self.html)
        webview.create_window("list_tweets.html",html=self.html, width=800, height=600, resizable=True,fullscreen=False)
        webview.start()

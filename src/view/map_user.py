# these liarbries are used for solo map:
import os
import folium
from folium.plugins import MarkerCluster
import random # get a random color code

class Map_user(list):
    # return result stored in nested list of search_user for map:
    # return type of each user: (user_name, id, text, coordinates, url_of_pictures, created_time)
    user_tweets = []
    def __init__(self, tweet=None):

        super().__init__(tweet)
        self.user_tweets = tweet
        self.FunDraw(self.person_to_list())

    def person_to_list(self):
        L=[] # to save all tweets get from tweepy
        for tweet in self.user_tweets:
            if (tweet["place"]):
                l=[] #list for one person
                l.append(tweet["user"]["screen_name"])
                l.append(tweet['id'])
                l.append(tweet["text"])
                point=tweet["place"]["bounding_box"]["coordinates"][0]
                points=self.coordinate_calculator(point)
                l.append(points)
                if ('entities' in tweet.keys()):
                    if ('media' in tweet['entities'].keys()):
                        l.append(tweet['entities']['media'][0]['media_url_https'])
                    else:
                        l.append(None)
                l.append(tweet["created_at"])
                L.append(l)
        return (L)

    # function to calculate the coordinate. Wirten by Han, i've just made a little chang, now it return the coordinates in way reversed
    def coordinate_calculator(self,coordinates):
        bottom_left = coordinates[0]
        bottom_right = coordinates[1]
        top_right = coordinates[2]
        top_left = coordinates[3]

        if bottom_left == bottom_right == top_right == top_left:
            # it's a place, so the coordinates are the same
            return [float(bottom_left[1]), float(bottom_left[0])]
        else:
            # it's a city, there're 4 different coordinates
            longitude = (float(bottom_left[0]) + float(bottom_right[0])) / 2
            latitude = (float(bottom_right[1]) + float(top_right[1])) / 2
            return [latitude,longitude]

    # get a random color (type: #FFFFFF)
    # used in tracks of person
    def randomcolor(self):
            colorNumber  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            color = ""
            for i in range(6):
                color+=colorNumber[random.randint(0,14)]
            return "#"+color

    # generate an empty map
    # maybe is useless
    def generaMap(self):
        m = folium.Map(location=[44.4933,11.3432])
        m.add_child(folium.LatLngPopup()) #when click in map, show the corrispond coordinates
        m.save(os.path.dirname(__file__) + "/../mappa.html")
        return m

    # return the numbers of all user_name, no duplicated
    def ids(self, dati):
        l=[]
        for i in dati:
            l.append(i[0])
        L=[]
        [L.append(i) for i in l if not i in L]
        return L

    # ['Law_2885', 'Non sta nevicando.', [43.62071365, 13.375032650000001], None, 'Wed Dec 02 14:25:45 +0000 2020']
    # type if Datii[name, id, text, coordinate,picture_url, created_at]
    def FunDraw(self, datas):
        x2=[i[3]for i in datas] #all the coord
        if (len(x2)==0):
            m=self.generaMap()
            return m
        else:
            m = folium.Map(location=datas[0][3])
            for dati in datas:
                # print(dati[2])
                marker_cluster = MarkerCluster().add_to(m)
                # print(dati[2])
                html= '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
                html+='<blockquote class="twitter-tweet" tw-align-center data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/vitadiste/status/'+str(dati[1])+'?ref_src=twsrc%5Etfw"></a>'
                html+='</blockquote>'
                iframe = folium.IFrame(html,width=600,height=400,ratio='20%')
                popup = folium.Popup(iframe,max_width=1000)
                folium.Marker(dati[3],popup=popup, tooltip=dati[5]).add_to(marker_cluster)
                folium.PolyLine(x2, color=self.randomcolor(),weight=5).add_to(m)
                m.add_child(folium.LatLngPopup()) #when click in map, show the corrispond coordinates
                m.save(os.path.dirname(__file__) + "/../mappa.html")
        m.save(os.path.dirname(__file__) + "/../mappa.html")
        return m

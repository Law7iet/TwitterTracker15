import folium
from folium.plugins import MarkerCluster
import os


class Map_Noperson(list):
   
    tweets = None
    def __init__(self, tweet_list=None):
        
        super().__init__(tweet_list)
        self.tweets = self.search_to_list(tweet_list)
        self.Map(self.tweets)
        
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
        
    
    # return type: (text, coordinates, url_of_pictures, created_time,id)
    def search_to_list(self,tweets):
        L=[] #list
        for tweet in tweets:
            if(tweet["place"]):
                l=[]
                # print(tweet["text"])
                l.append(tweet["text"])
                point=tweet["place"]["bounding_box"]["coordinates"][0]
                points=self.coordinate_calculator(point)
                # print(points)
                l.append(points)
                if ('entities' in tweet.keys()):
                    if ('media' in tweet['entities'].keys()):
                        # print(tweet['entities']['media'][0]['media_url_https'])
                        l.append(tweet['entities']['media'][0]['media_url_https'])
                    else:
                        l.append(None)
                # print(tweet["created_at"])
                l.append(tweet["created_at"])
                l.append(tweet["id"])
                # l.append(',')
                L.append(l)
    
        return(L)
    
    def generaMap(self):
        m = folium.Map(location=[44,14]) 
        m.save(os.path.dirname(__file__) + "/../mappa.html")
        return m
    
    # type of [text, coordinates, url_of_pictures, created_time,id]
    def Map(self,datas):
        
        m=self.generaMap()
        
#        print("Dati;",datas)
        for dati in datas:
            
            
            marker_cluster = MarkerCluster().add_to(m)
            # print(dati[2])
            html= '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'
            html+='<blockquote class="twitter-tweet tw-align-center" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/vitadiste/status/'+str(dati[4])+'?ref_src=twsrc%5Etfw"></a>'
            html+='</blockquote>'
            iframe = folium.IFrame(html,width=600,height=400,ratio='20%')
            popup = folium.Popup(iframe,max_width=1000)
            folium.Marker(dati[1],popup=popup, tooltip=dati[3]).add_to(marker_cluster)
        #if non pictures, then show in popup just text
            m.add_child(folium.LatLngPopup()) #when click in map, show the corrispond coordinates
            m.save(os.path.dirname(__file__) + "/../mappa.html")
        m.save(os.path.dirname(__file__) + "/../mappa.html")
        return m

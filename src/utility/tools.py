import os.path
import webview
from bs4 import BeautifulSoup
from view.list_tweets import List_tweets

# Classe per creazione della finestra web con i vari tools per l'analisi
class Tools(List_tweets):

    listatweet=""

    # Parte finale da aggiungere all'html
    endHtml = '''
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
</body>
</html>'''

    def __init__(self, listtweet=None):

        super().__init__(listtweet)
        self.listatweet = listtweet

        # Parte iniziale dell'html
        self.html = '''
<html>
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    '''

        # Aggiunta dell'head del file html della mappa al mio nuovo html
        self.add_map('head')
        self.html +="</head>"

        # html della navbar e degli elementi wordcloud, piechart, barchart
        self.html += '''
    <body>
        <nav class="navbar navbar-expand-lg navbar-light mx-auto bg-dark">
          <form class="container-fluid justify-content-centers">
            <button class="btn btn-primary" id="mappa" type="button" onclick="show_map()">Mappa</button>
            <button class="btn btn-primary" id="list" type="button" onclick="show_list()"disabled>Lista Tweets</button>
            <button class="btn btn-primary" id="wordcloud" type="button" onclick="show_word_cloud()">WordCloud</button>
            <button class="btn btn-primary button_chart" type="button" onclick="show_chart()">Tweet Chart</button>

          </form>
        </nav>
        <img src="wordcloud.jpeg" id="wc_image" alt=" WordCloud "style="display:none; width:80%; margin: 20 auto auto auto;">
        <img src="piechart.jpeg" class="chartTweet" alt=" Pie Chart "style="display:none; width:80%; margin: 20 auto auto auto;">
        <img src="barchart.jpeg" class="chartTweet" alt=" Bar Chart "style="display:none; width:80%; margin: 20 auto auto auto;">
'''
        # Aggiungo all'html la lista dei tweet
        self.html += self.listatweet.get_list()
        # Aggiungo il body della mappa al mio html
        self.add_map('body')

        # Aggiungo le funzioni per gestire la navbar (js)
        self.script_navbar()

        # Aggiungo gli script della mappa al mio html
        self.add_map('script')

        self.html += self.endHtml
        # Sovrascrivo il mio html nel file creato dalla mappa
        htmlfile = open(os.path.dirname(__file__) + "/../mappa.html", "w")
        htmlfile.write(self.html)
        htmlfile.close()

        webview.create_window("Analisi Tweet", url="mappa.html", width=800, height=600, resizable=True,fullscreen=False)

        # Lancio il browser
        webview.start()

        # Crea funzioni per gestione navbar
    def script_navbar(self):

        self.html += "<script>\n"
        self.html += '''
function set_button(button){

    switch(button){
        case "list":
            document.getElementById('list').disabled = true;
            document.getElementById('mappa').disabled = false;
            document.getElementById('wordcloud').disabled = false;
            document.getElementsByClassName('button_chart')[0].disabled = false;
            break;

        case "map":
            document.getElementById('list').disabled = false;
            document.getElementById('mappa').disabled = true;
            document.getElementById('wordcloud').disabled = false;
            document.getElementsByClassName('button_chart')[0].disabled = false;
            break;

        case "wordcloud":
            document.getElementById('list').disabled = false;
            document.getElementById('mappa').disabled = false;
            document.getElementById('wordcloud').disabled = true;
            document.getElementsByClassName('button_chart')[0].disabled = false;
            break;
        case "tweetchart":
            document.getElementById('list').disabled = false;
            document.getElementById('mappa').disabled = false;
            document.getElementById('wordcloud').disabled = false;
            document.getElementsByClassName('button_chart')[0].disabled = true;
            break;

    }
}'''
        self.html += '''
function show_list(){

    if(document.getElementById('wc_image').style.display !== 'none')
        document.getElementById('wc_image').style.display = 'none';

    else if ( document.getElementsByClassName('folium-map')[0].style.visibility === 'visible'){
        document.getElementsByTagName("BODY")[0].style.overflowY = 'scroll';
        document.getElementsByClassName('folium-map')[0].style.visibility = 'hidden';
    }
    else {
        document.getElementsByClassName('chartTweet')[0].style.display = 'none';
        document.getElementsByClassName('chartTweet')[1].style.display = 'none';

    }
    document.getElementById('listatweet').style.display = 'block';

    set_button('list');

}

'''
        self.html += '''
function show_map(){

    if(document.getElementById('listatweet').style.display === 'block')
        document.getElementById('listatweet').style.display = 'none';
    else if (document.getElementById('wc_image').style.display === 'block')
        document.getElementById('wc_image').style.display = 'none';
    else {
        document.getElementsByClassName('chartTweet')[0].style.display = 'none';
        document.getElementsByClassName('chartTweet')[1].style.display = 'none';

    }

    document.getElementsByClassName('folium-map')[0].style.visibility = 'visible';
    document.getElementsByTagName("BODY")[0].style.overflowY = 'hidden';

    set_button('map');

}
'''
        self.html +='''
function show_word_cloud(){

    if(document.getElementById('listatweet').style.display === 'block')
        document.getElementById('listatweet').style.display = 'none';
    else if ( document.getElementsByClassName('folium-map')[0].style.visibility === 'visible'){
        document.getElementsByTagName("BODY")[0].style.overflowY = 'scroll';
        document.getElementsByClassName('folium-map')[0].style.visibility = 'hidden';
    }
    else {
        document.getElementsByClassName('chartTweet')[0].style.display = 'none';
        document.getElementsByClassName('chartTweet')[1].style.display = 'none';

    }
    document.getElementById('wc_image').style.display = 'block';
    set_button('wordcloud');

}

'''
        self.html +='''
function show_chart(){

    if(document.getElementById('listatweet').style.display === 'block')
        document.getElementById('listatweet').style.display = 'none';
    else if (document.getElementsByClassName('folium-map')[0].style.visibility === 'visible'){
        document.getElementsByTagName("BODY")[0].style.overflowY = 'scroll';
        document.getElementsByClassName('folium-map')[0].style.visibility = 'hidden';
    }
    else
        document.getElementById('wc_image').style.display = 'none';
        
    document.getElementsByClassName('chartTweet')[0].style.display = 'block';
    document.getElementsByClassName('chartTweet')[1].style.display = 'block';
    set_button('tweetchart');
}

'''
        self.html += "</script>\n"

    # Funzione per gestire l'integrazione della mappa al mio html
    def add_map(self, tag):

        with open(os.path.dirname(__file__) + "/../mappa.html") as fp:
            soup = BeautifulSoup(fp, features="html5lib")

        if tag == 'head':

            head = soup.find("head").findChildren()
            for child in head:

                if str(child).find('bootstrap') == -1 and str(child).find('meta') == -1:
                    self.html += str(child)+'\n'

        elif tag == 'body':
            div_map = soup.find("div")
            
            
            div_map['style'] = 'visibility: hidden;'
            self.html += str(div_map)+'\n'

        elif tag == 'script':

                script = soup.find_all("script")
                self.html += str(script[len(script) - 1])

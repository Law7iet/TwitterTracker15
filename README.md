# Progetto di Ingegneria del software 2020
- OS: Linux e MacOS
- Python version 3.9.1
- Packages:
    - bs4
    - datetime
    - folium
    - html5lib
    - json
    - math
    - matplotlib
    - nltk
    - numpy
    - os
    - re
    - requests
    - sys
    - tkcalendar
    - tkinter
    - tweepy
    - urllib
    - webview
    - wordcloud
    Inoltre bisogna eseguire il seguente codice per installare una componente di `nltk`:
    ```
    python -m nltk.downloader stopwords
    ```


## Struttura del codice
`App.py` è il programma da eseguire.\n
I folder contengono funzioni e classi per il programma, ed è diviso in 3 cartelle:
- `twitter` contenente la parte di programma che interagisce con Twitter
- `utility` contenente funzioni utili al programma
- `view` contenente i modi per visualizzare le ricerche

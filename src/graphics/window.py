'''
Created on 3 dic 2020

@author: L
'''

from tkinter import *
from tkinter import ttk
from tkcalendar import *
#from graphics.button import *

from twitter.twitter_handler import Twitter_handler as tw

class Window():
    
    language = ["it", "en", "fr", "de", "es"]
    type = ["mixed", "popular", "recent"]
    
    def __init__(self):
        
        self.ricerca = tw()
        
        self.root = Tk()
        self.root.geometry("400x300")
        
        stile = ttk.Style(self.root)
        stile.theme_use('clam')
        
        # ELEMENTS
        self.obj01 = Label(self.root, text = "Parola Chiave:")
        self.obj02 = Entry(self.root)
        self.obj03 = Label(self.root, text = "Lingua:")
        self.lingua = StringVar(self.root)
        self.lingua.set(self.language[0])
        self.obj04 = OptionMenu(self.root, self.lingua, *self.language)
        self.obj05 = Label(self.root, text = "Data di inizio:")
        self.obj06 = DateEntry(self.root, width = 12, background = "darkblue", foreground = "white", borderwidth = 2)
        self.obj06._top_cal.overrideredirect(False)
        self.obj07 = Label(self.root, text = "Data di inizio:")
        self.obj08 = DateEntry(self.root, width = 12, background = "darkblue", foreground = "white", borderwidth = 2)
        self.obj08._top_cal.overrideredirect(False)
        self.obj09 = Label(self.root, text = "Filtro:") 
        self.tipo = StringVar(self.root)
        self.tipo.set(self.type[0])
        self.obj10 = OptionMenu(self.root, self.tipo, *self.type)
        self.obj11 = Label(self.root, text = "Numero di tweet:")
        self.obj12 = Entry(self.root)
        self.obj13 = Label(self.root, text = "Coordinate")
        self.obj14 = Entry(self.root)
        
        # BUTTON
        invio = Button(self.root, text = "Invio", fg = "black", command = self.get)
        
        # GRID
        self.obj01.grid(row = 0, column = 0, sticky = W)
        self.obj02.grid(row = 0, column = 1, sticky = E)
        self.obj03.grid(row = 1, column = 0, sticky = W)
        self.obj04.grid(row = 1, column = 1, sticky = E)
        self.obj05.grid(row = 2, column = 0, sticky = W)
        self.obj06.grid(row = 2, column = 1, sticky = E)
        self.obj07.grid(row = 3, column = 0, sticky = W)
        self.obj08.grid(row = 3, column = 1, sticky = E)
        self.obj09.grid(row = 4, column = 0, sticky = W)
        self.obj10.grid(row = 4, column = 1, sticky = E)
        self.obj11.grid(row = 5, column = 0, sticky = W)
        self.obj12.grid(row = 5, column = 1, sticky = E)
        self.obj13.grid(row = 6, column = 0, sticky = W)
        self.obj14.grid(row = 6, column = 1, sticky = E)
        
        invio.grid(row = 7)

    def get(self):
        data01 = self.obj06.get()
        data01 = data01.split('/')
        data01 = data01[1] + '-' + data01[0] + '-' + data01[2]
        data02 = self.obj08.get()
        data02 = data02.split('/')
        data02 = data02[1] + '-' + data02[0] + '-' + data02[2]
        print(self.obj02.get())
        print(self.lingua.get())
        print(type(str(self.obj06.get_date())))
        print(str(self.obj06.get_date()))
        print(self.obj08.get_date())
        print(self.tipo.get())
        print(self.obj12.get())
        print(self.obj14.get())

        tweets = self.ricerca.search(self.obj02.get(), self.obj14.get(), self.lingua.get(), self.tipo.get(), int(self.obj12.get()), str(self.obj06.get_date()), str(self.obj08.get_date()))

        print(tweets)
        i = 1
        for tweet in tweets:
            print(i)
            print(tweet["text"])
            print(tweet["created_at"])
            print(tweet["place"]["full_name"])
            print(tweet["place"]["bounding_box"]["coordinates"][0])
            i += 1
        
    def run(self):
        self.root.mainloop()
        
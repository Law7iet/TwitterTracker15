# import utility.converter as cv
# import utility.loader as ld
# import twitter.twitter_handler as th
   
# convertitore = cv.Converter()
# caricatore = ld.Loader('Tweets.json')
# ricerca = th.Twitter_handler()
#   
# stringa = '#IngSw2020'
# falconara = '43.6242,13.404,20km'
# bologna = '44.5075,11.3514,10km'
# vuoto = ','
# lingua = 'it'
# filtro = 'recent'
# numero = 10
# data_inizio = '2020-12-04'
# data_fine = '2020-12-11'
# 
# id = 'FNATIC'
# id = 'xLalisaxx'
# id = 'Law_2885'
#     
# tweets = ricerca.search(stringa, falconara, lingua, filtro, numero, data_inizio, data_fine)
# #tweets = ricerca.search_user(id, data_inizio_tupla)
#     
# tmp = 1
# for element in tweets:
#     print(tmp)
#     print(element["text"])
#     print(element["created_at"])
#     tmp += 1
# 
# caricatore.store(tweets)

# ------------------------------------
# from tkinter import * 
# from tkinter.ttk import *
# 
# # importing askopenfile function 
# # from class filedialog 
# from tkinter.filedialog import askopenfile 
# 
# root = Tk() 
# root.geometry('200x100') 
# 
# # This function will be used to open 
# # file in read mode and only Python files 
# # will be opened 
# def open_file(): 
#     file = askopenfile(mode ='r') 
#     if file is not None: 
#         content = file.read() 
#         print(content) 
# 
# btn = Button(root, text ='Open', command = lambda: open_file()) 
# btn.pack(side = TOP, pady = 10) 
# 
# mainloop()
##file = askopenfile(mode ='r', filetypes =[('Python Files', '*.docx')]) 

#----------------------------------------

from utility.loader import Loader
from twitter.twitter_handler import Twitter_handler

ricerca = Twitter_handler()
tweets = ricerca.search('#IngSw2020', ',', 'it', 'recent', 25, '2020-12-8', '2020-12-15')

x = Loader()
x.set("/Users/L/Desktop/Università/3 anno/Ingegneria del Software/Progetto/IngSw2020/src/Tweets.json")
x.store(tweets)
x.set("/Users/L/Desktop/Università/3 anno/Ingegneria del Software/Progetto/IngSw2020/src/tmp.json")
print(x.data)


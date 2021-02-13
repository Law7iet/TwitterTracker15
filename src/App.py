from utility import form as form
import tkinter as tk
import os

class Application(tk.Frame):

    def __init__(self, root=None):
        
        super().__init__(root)
        self.root = root
        self.grid()
        self.build()
        
    def build(self):
        
        self.form = form.Form()
        self.form.get_container().grid(row=0, column=0)

#root = tk.Tk().title("Tweets Analysis Team15")
root = tk.Tk()
root.title("Tweet Analysis Team 15")
root.resizable(width=False, height=False)
app = Application(root=root)
app.mainloop()

# Delete used files
path = os.path.dirname(__file__)
if os.path.exists(path + "/barchart.jpeg"):
    os.remove(path + "/barchart.jpeg")
if os.path.exists(path + "/piechart.jpeg"):
    os.remove(path + "/piechart.jpeg")
if os.path.exists(path + "/wordcloud.jpeg"):
    os.remove(path + "/wordcloud.jpeg")
if os.path.exists(path + "/mappa.html"):
    os.remove(path + "/mappa.html")
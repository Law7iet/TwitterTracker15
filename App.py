import form as form
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, root=None):
        
        super().__init__(root)
        self.root = root
        self.grid()
        self.build()
        
    def build(self):
        
        self.form = form.Form()
        self.form.get_container().grid(row=0, column=0)

root = tk.Tk().title("Tweets Analysis Team15")
app = Application(root=root)
app.mainloop()

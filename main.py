from  tkinter import *

#root = Tk()
#root.title('hello world')
#root.geometry('650x400')
#label = Label(text = 'List magazine')
#label.pack()
#root.mainloop()

# Пока не будем использовать наследование, обойдемся композицией.
	
class App():
    def __init__(self, root):
        self.root = root
        self.root.title('hello world')
        self.root.geometry('650x400')
        # label
        self.label = Label(text = 'List magazine')
        self.label.pack()
        # frame/контейнер
        self.frame = Frame()
        # Button
        self.button = Button(self.frame, text='Next', command=None)
        self.button.pack()
        self.frame.pack()
        # Listbox
        self.listbox = Listbox()
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        [self.listbox.insert(END, i) for i in range(110)]
        # SCROLLBAR
        self.scroll = Scrollbar(orient="vertical", command = self.listbox.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # для взаиможействия со scrollbar
        self.listbox.config(yscrollcommand=self.scroll.set)

         

root = Tk()
app = App(root)
print(app.__dict__)
root.mainloop()

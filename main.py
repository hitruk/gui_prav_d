from  tkinter import *
from  data import Db

#root = Tk()
#root.title('hello world')
#root.geometry('650x400')
#label = Label(text = 'List magazine')
#label.pack()
#root.mainloop()

# Пока не будем использовать наследование, обойдемся композицией.
	
#p = Db()
#print(p.__dict__)
#sql = p.query_parent()
#print(p.get_res(sql))

class App():
    p = Db()
    sql = p.query_parent()
    data = p.get_res(sql)
    def __init__(self, root):
        # windows
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
        #[self.listbox.insert(END, i) for i in range(110)]
        [self.listbox.insert(END, i) for i in self.data]
        # SCROLLBAR
        self.scroll = Scrollbar(orient="vertical", command = self.listbox.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # для взаиможействия со scrollbar
        self.listbox.config(yscrollcommand=self.scroll.set)
    def op(self):
        print(self.data) 

root = Tk()
app = App(root)
print(app.__dict__)
root.mainloop()

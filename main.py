from  tkinter import *
from  data import Db

# Пока не будем использовать наследование, обойдемся композицией.
	
class App(Db):
    #p = Db()
    #p.query_child(id_parent)
    #p.query_parent()
    #data = p.get_res()
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
        self.button = Button(self.frame, text='Next', command=self.click_next_button)
        self.button.pack()
        self.frame.pack()
        # Listbox
        self.listbox = Listbox()
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

        #[self.listbox.insert(END, i) for i in range(110)]
        # получаем данные из таблицы parent
        #[self.listbox.insert(END, i) for i in self.p.get_res()]

        # переопределить запрос sql 
        self.query_parent()
        
        [self.listbox.insert(END, i) for i in self.get_res()]
        print(self.listbox.size())
        # SCROLLBAR
        self.scroll = Scrollbar(orient="vertical", command = self.listbox.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
        # для взаиможействия со scrollbar
        self.listbox.config(yscrollcommand=self.scroll.set)
            
    def _create_dict(self):
        # создаем словарь {index_listbox: id_table}
        list_index = self.listbox.get(0, END)
        dict_f = {}
        for i in (range(len(list_index))):
            dict_f[i] = list_index[i]  
        print(dict_f)
        return dict_f

    def click_next_button(self):
        # получаем index из списка элементов
        index_el = self.listbox.curselection()
        if index_el == ():
            print('Выберите пункт из списка')
        else:    
            # получаем текст по индексу
            list_index_id = self._create_dict()
            text = list_index_id[(index_el[0])][1]
            print(f'text: {text}')
            id_parent = list_index_id[(index_el[0])][0]
            print(f'id_parent: {id_parent}')
            # замена текста в заголовке
            self.label['text'] = text
            # переопределить sql для таблицы child  
            self.query_child(str(id_parent))
            # очищаю окно от данных
            self.listbox.delete(0, END)
            # загружаю данные в окно из таблицы child
            [self.listbox.insert(END, i) for i in self.get_res()]
            # удалить кнопку            
            self.button.pack_forget()
            # добавляем кнопку
            self.button = Button(self.frame, text='Next=>', command=self.click_next_two)
            self.button.pack()
            self.button = Button(self.frame, text='Back')
            self.button.pack()
#Можно при помощи компоновщика .grid() добавлять объект и временно удалять при помощи .grid_remove()
    def click_next_two(self):
        print('ura')
root = Tk()
app = App(root)
#print(app.__dict__)
#app._create_dict()
#app.click_next_button()
#app._get_parent_data()
root.mainloop()

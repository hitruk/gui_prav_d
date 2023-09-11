from  tkinter import *
from data import Db

# Пока не будем использовать наследование модуля tkinter, обойдемся композицией.
	
class App(Db):
    #p = Db()
    #p.query_child(id_parent)
    #p.query_parent()
    #data = p.get_res()

    def __init__(self, root):
        #history cooki
        self._history = {}
         
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
        self.button_next = Button(self.frame, text='Next_1', command=self.click_next_button)
        self.button_next.pack()
        self.frame.pack()
        # Listbox
        self.listbox = Listbox()
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        # переопределить запрос sql 
        self.query_parent()
        [self.listbox.insert(END, i) for i in self.get_res()]
        # запись в истории
        self._history['parent_page'] = self.listbox.get(0, END) 
        print(f'self._history: {self._history}')
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
        #print(dict_f)
        return dict_f


    # Parent Page 
    def click_next_button(self):
        # получаем index из списка элементов
        index_el = self.listbox.curselection()
        if index_el == ():
            print('Выберите пункт из списка')
        else:    
            # создатьсловарь соответствие индексу-идентификатора
            list_index_id = self._create_dict()
            # получаем текст по индексу
            text = list_index_id[(index_el[0])][1]
            # замена текста в заголовке
            self.label['text'] = text
            # очищаю окно от данных
            self.listbox.delete(0, END)
            # получить id_parent,  sql для таблицы child  
            id_parent = list_index_id[(index_el[0])][0]
            # переопределить sql для таблицы child  
            self.query_child(str(id_parent))
            # загружаю данные в окно из таблицы child
            [self.listbox.insert(END, i) for i in self.get_res()]
            # запись в историю
            self._history['child'] = self.listbox.get(0, END)
            # переопределяем кнопку next_button
            self.button_next['text'] = 'Next_2'
            self.button_next['command'] = self.click_next_two
            # добавим кнопку button_back
            self.button_back = Button(self.frame, text='Back_1', command=self.return_parent_page)
            self.button_back.pack()


    # Return parent page
    def return_parent_page(self):
        # Убираем кнопку
        self.button_back.pack_forget()
        # переопределяем кнопку next_button
        self.button_next['text'] = 'Next_1'
        self.button_next['command'] = self.click_next_button
        # очищаю окно от данных
        self.listbox.delete(0, END)
        # замена текста в заголовке
        self.label['text'] = 'List magazine'
        # Загрузка данных из истории
        [self.listbox.insert(END, i) for i in self._history['parent_page']]


    # Page child 
    def click_next_two(self):
        # получаем index из списка элементов
        index_el = self.listbox.curselection()
        if index_el == ():
            print('Выберите пункт из списка')
        else:
            # получаем индексы всех элементов
            index_el = self.listbox.curselection()
            # получаем текст по индексу
            list_index_id = self._create_dict()
            text = list_index_id[(index_el[0])][1]
            print(f'text: {text}')
            id_child = list_index_id[(index_el[0])][0]
            print(f'id_child: {id_child}')
            # замена текста в заголовке
            self.label['text'] = text
            # очищаем окно от данных
            self.listbox.delete(0, END)

            # переопределить запрос sql 
            self.query_grandchild(id_child)

            # загружаю данные в окно из таблицы parent
            [self.listbox.insert(END, i) for i in self.get_res()]
 
            # запись в историю
            self._history['grandchild'] = self.listbox.get(0, END)
            print(self._history)

            # Удаляем кнопку 
            self.button_next.pack_forget()

            # переопределяем кнопку Back_button
            self.button_back['text'] = 'Back_2'
            self.button_back['command'] = self.back_button_two


    # return page child   
    def back_button_two(self):
        
        # переопределяем кнопку next_button
        self.button_back['text'] = 'Back_1'
        self.button_back['command'] = self.return_parent_page

        # добавляем кнопку
        self.button_next['text'] = 'Next_2'
        self.button_next['command'] = self.click_next_two
        self.button_next.pack()

        #очищаю окно от данных
        self.listbox.delete(0, END)

        # Зaгрузка данных из истории
        [self.listbox.insert(END, i) for i in self._history['child']]
        # замена текста в заголовке
        # self.label['text'] = 'List magazine'


root = Tk()
app = App(root)
root.mainloop()

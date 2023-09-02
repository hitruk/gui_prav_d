
  

from config import config
import psycopg2
import string

class Db:

     params = config()
     list_sql = ['select version()', 'select id, title from parent']

     def __init__(self):
         self.conn = None 
         self.cur = None
         self.__sql = '''select version()'''

     def _open_conn_cur(self):
         self.conn = psycopg2.connect(**self.params)
         self.cur = self.conn.cursor()
         return self.cur
  
     def _close(self):
         self.conn.close()
         self.conn = None
         self.cur = None  

     def query_parent(self):
         self.__sql = '''select id, title from parent'''

     def query_child(self, id_parent):
         self.__sql =  ''' select title from child where id_parent = %s ''' 
         # строка
         # число из двух символов
         # может состоять из 1,2,3,4,5,6,7,8,9,0
         # проверка на диапазон(не реализовывал)
         # возможно надо заменить isinstance() 
         if isinstance(id_parent, str) and len(id_parent) <= 2:
            if all(i in string.digits for i in id_parent):
                self.__sql = [''' select title from child where id_parent = %s ''', id_parent]
         else:
             self.__sql = None

     def get_res(self):
         try:
             cur = self._open_conn_cur()
             if self.__sql == None:
                 return   
             elif isinstance(self.__sql, list):
                 cur.execute(self.__sql[0], (self.__sql[1],))
             else:
                 cur.execute(self.__sql)
             res = cur.fetchall()
             print(res)
             cur.close()
             return res
         except(Exception, psycopg2.DatabaseError) as error:
             print(error)
         finally:
             if self.conn is not None:
                 self._close()

#p = Db()
#print(p.__dict__)
#p.query_child('1')
#p.get_res()
#p.query_parent()
#p.get_res()

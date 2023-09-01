# получить список строк из таблицы parent
  

from config import config
import psycopg2

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

     def query_child(self):
         self.__sql =  ''' select title from child where id_parent = %s ''' 

     # возможно это лишнее
     #def _check_sql(self):
     #    if sql not in self.list_sql:
     #        sql = None
     #        print('Недопустимый запрос')
     #    return sql       

     def get_res(self, *args):
         #if self._check_sql(self.__sql) is None:
         #    return 
         # делать обработку на ошибки: то есть должна быть одна строка, тип данных строка, только цифры и т.д. 
         id_parent = args
         print(id_parent)        
         try:
             cur = self._open_conn_cur()
             if id_parent is not None:
                 cur.execute(self.__sql, (id_parent))
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

p = Db()
#print(p.__dict__)
p.query_child()
p.get_res('13')


# получить список строк из таблицы parent
  

from config import config
import psycopg2

class Db:

     params = config()
     list_sql = ['select version()', 'select id, title from parent']

     def __init__(self):
         self.conn = None 
         self.cur = None

     def _open_conn_cur(self):
         self.conn = psycopg2.connect(**self.params)
         self.cur = self.conn.cursor()
         return self.cur
  
     def _close(self):
         self.conn.close()
         self.conn = None
         self.cur = None  
     def query_version(self):
         sql = ''' select version() '''
         return sql

     def query_parent(self):
         sql = '''select id, title from parent'''
         return sql

     def query_child(self):
         sql =  ''' select title from child where id_parent '''
         return sql
 
     def _check_sql(self):
         if sql in self.list_sql:
             return sql
         else:
             print('Недопустимый запрос')
                 

     def get_res(self, sql):
         # sql = '''select*from parent'''
         if self._check() is None:
             return 
         try:
             cur = self._open_conn_cur()
             cur.execute(sql)
             res = cur.fetchall()
             #print(res)
             cur.close()
             return res
         except(Exception, psycopg2.DatabaseError) as error:
             print(error)
         finally:
             if self.conn is not None:
                 self._close()

p = Db()
print(p.__dict__)
sql = p.query_parent()
print(p.get_res(sql))






# Данный код необходимо реализовать через ООП
# 
def get_parent_table():
    """ """
    sql = ''' select id, title from parent '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        base_title = cur.fetchall()
        #  print(base_title)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return base_title


def get_child_table(parent_id):
    """ """
    sql = ''' select title from child where id_parent '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select*from child where id_parent=%s", (parent_id,))
        child_data= cur.fetchall()
        print(child_data)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return child_data
#get_child_table(parent_id='58')


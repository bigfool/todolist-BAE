# _*_ coding:utf-8 _*_
import web
import web.db
from bae.core import const

#your dbname in BAE
dbname = "your dbname"

db = web.database(
    dbn='mysql',
    host=const.MYSQL_HOST,
    port=int(const.MYSQL_PORT),
    user=const.MYSQL_USER,
    passwd=const.MYSQL_PASS,
    db=dbname
)

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    return db.insert('todo', titel=text)

def del_todo(id):
    db.delete('todo', where='id=$id', vars=locas())

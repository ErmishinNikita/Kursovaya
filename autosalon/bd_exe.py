import math
import sqlite3
from autosalon import app
import time

menu = [{'name': 'Главная', 'url': 'index'}, {'name': 'Блюда', 'url': 'dishes'}, {'name': 'Помощь', 'url': 'help'},
        {'name': 'Контакт', 'url': 'contact'}, {'name': 'Авторизация', 'url': 'login'},
        {'name': 'Регистрация', 'url': 'reg'}]

bd_userdata = [{'username': 'test', 'psw': 'test'}, {'username': 'root', 'psw': 'pass'},
               {'username': 'log', 'psw': 'psw'}]

posts = [{'title': 'test', 'post_message': 'test'}, {'title': 'Что то о постах', 'post_message': 'пост'},
         {'title': 'Чек пост', 'post_message': 'Чеееек'}]


def connect_db():
    '''создание соединения с бд'''
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    '''Вспомогательная функция для создания таблицы'''
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


class FDataBase:
    def __init__(self, db1):
        self.__db = db1
        self.__cursor = db1.cursor()

    def add_menu(self, usluga, zena):
        try:
            self.__cursor.execute("insert into uslugi values(NULL, ?, ?)", (usluga, zena))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления меню в БД" + str(e))
            return False
        return True

    def add_users(self, username, psw):
        try:
            self.__cursor.execute("insert into users values(NULL, ?, ?)", (username, psw))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления меню в БД" + str(e))
            return False
        return True

    def add_auto(self, fio, contact, auto):
        try:
            self.__cursor.execute("insert into uslugi values(NULL, ?, ?, ?)", (fio, contact, auto))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления меню в БД" + str(e))
            return False
        return True

    def add_admin(self, login, password):
        try:
            self.__cursor.execute("insert into admin values(NULL, ?, ?)", (login, password))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления меню в БД" + str(e))
            return False
        return True

    def add_model(self, name, foto, price, max_speed, loshad, razgon, rashod):
        try:
            self.__cursor.execute("insert into model2 values(NULL, ?, ?, ?, ?, ?, ?, ?)",
                                  (name, foto, price, max_speed, loshad, razgon, rashod))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления меню в БД" + str(e))
            return False
        return True

    def getAdmin(self):
        sql = 'SELECT * FROM admin'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')

    def get_zakaz(self):
        sql = 'SELECT * FROM uslugi'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')
        return ()

    def get_model2(self):
        sql = 'SELECT * FROM model2'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')
        return ()

    def get_model2top3(self):
        sql = 'SELECT * FROM model2 ORDER BY id LIMIT (3)'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')
        return ()

    def del_menu(self, id=0):
        if id == 0:
            self.__cursor.execute("delete from mainmenu ")
            self.__db.commit()
        else:
            self.__cursor.execute(f"delete from mainmenu where id={id}")

    def getMenu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')
        return ()

    def getUser(self):
        sql = 'SELECT * FROM users'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')

    def getUserById(self):
        sql = 'SELECT login FROM users WHERE users.id'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')

    def getModelById(self, id):
        sql = 'SELECT * FROM model2 WHERE id = ?'
        try:
            self.__cursor.execute(sql, (id,))
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')

    def getUsl(self):
        sql = 'SELECT * FROM uslugi'
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res: return res;
        except:
            print('Ошибка чтения бд')
        return ()

    def deuUserById(self, id):
        if id == 0:
            self.__cursor.execute("delete from users ")
            self.__db.commit()
        else:
            self.__cursor.execute(f"delete from users where id={id}")
            self.__db.commit()


if __name__ == "__main__":
    db = connect_db()
    db = FDataBase(db)
    # create_db()
    # db.add_admin("admin", "admin")
    print(db)

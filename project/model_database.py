import sqlite3
from project import app, DB_NAME

class Database:
    @staticmethod
    def conn():
        conn = None
        try:
            conn = sqlite3.connect(DB_NAME)
        except sqlite3.Error as e:
            print("Ошибка подключения к БД" + str(e))
        return conn


    @staticmethod
    def create_db():
        conn = Database.conn()
        with app.open_resource("sq_db.sql", "r") as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def add_idea(name: str, descrip: str, image: str):
        conn = Database.conn()
        cursor = conn.cursor()
        query = "INSERT INTO ideas (name, description, image) VALUES(NULL, ?, ?, ?)"
        try:
            cursor.execute(query, (name, descrip, image))
            conn.commit()
            print("Идея добавлена")
            return True
        except sqlite3.Error as e:
            print("Ошибка получения доступа к БД" + str(e))
            return None
        finally:
            conn.close()


    @staticmethod
    def check_idea(name: str):
        conn = Database.conn()
        cursor = conn.cursor()
        query = "SELECT * FROM ideas WHERE name LIKE = ?"
        try:
            cursor.execute(query, (name,))
            conn.commit()
            print("Идея добавлена")
            return True
        except sqlite3.Error as e:
            print("Ошибка получения доступа к БД" + str(e))
            return None
        finally:
            conn.close()

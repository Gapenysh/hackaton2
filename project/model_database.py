import sqlite3
from project import app, DB_NAME, DB_NAME_TEAMS
from project.model_user import Resume

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
    def conn_row():
        conn = None
        try:
            conn = sqlite3.connect(DB_NAME_TEAMS)
            conn.row_factory = sqlite3.Row
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
    def create_db_for():
        conn = Database.conn_row()
        with app.open_resource("sq_db.sql", "r") as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def add_resume(name: str, role: str, skills: str):
        conn = Database.conn()
        cursor = conn.cursor()
        query = "INSERT INTO resumes (name, role, skills) VALUES(?, ?, ?)"
        try:
            cursor.execute(query, (name, role, skills))
            conn.commit()
            print("Информация добавлена в БД")
            return True
        except sqlite3.Error as e:
            print("Ошибка получения доступа к БД" + str(e))
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all_resumes():
        conn = Database.conn()
        cursor = conn.cursor()
        query = "SELECT id, name, role, skills FROM resumes"
        try:
            cursor.execute(query)
            # Получаем результаты запроса
            results = cursor.fetchall()
            # Преобразуем результаты запроса в список словарей
            resumes = Resume.create_dict_resume(results)
            conn.commit()
            print("Информация передана")
            return resumes
        except sqlite3.Error as e:
            print("Ошибка получения доступа к БД" + str(e))
            return None
        finally:
            conn.close()




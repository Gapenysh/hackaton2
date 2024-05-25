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
    def add_resume(name: str, role: str, skills: str):
        conn = Database.conn()
        cursor = conn.cursor()
        query = "INSERT INTO resumes (name, role, skills) VALUES(NULL, ?, ?, ?)"
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
            resumes = []
            for result in results:
                id, name, role, skills = result
                skills = skills.split(",")  # Предполагаем, что навыки хранятся в виде строки с разделителем-запятой
                resume = {"id": id,
                          "name": name,
                          "role": role,
                          "skills": skills}
                resumes.append(resume)
            conn.commit()
            print("Информация передана")
            return resumes
        except sqlite3.Error as e:
            print("Ошибка получения доступа к БД" + str(e))
            return None
        finally:
            conn.close()




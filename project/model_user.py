from project import app


class Resume:
    @staticmethod
    def create_dict_resume(results):
        resumes = []
        for result in results:
            id, name, role, skills = result
            skills = skills.split(",")  # Предполагаем, что навыки хранятся в виде строки с разделителем-запятой
            resume = {"id": id,
                      "name": name,
                      "role": role,
                      "skills": skills}
            resumes.append(resume)

        return resumes


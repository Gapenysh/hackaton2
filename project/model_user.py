from project import app


class Resume:
    @staticmethod
    def create_dict_resume(results):
        resumes = []
        for result in results:
            id, name, role, skills = result
            resume = {"id": id,
                      "name": name,
                      "role": role,
                      "skills": skills}
            resumes.append(resume)

        return resumes

    @staticmethod
    def create_dict_teams(results):
        teams = []
        for result in results:
            id, name, size, roles = result
            team = {"id": id,
                      "name": name,
                      "size": size,
                      "roles": roles}
            teams.append(team)

        return teams


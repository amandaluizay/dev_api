from flask_restful import Resource

list_habilidades = ['python', 'java', 'php', 'django']


class Habilidades(Resource):
    def get(self):
        return list_habilidades

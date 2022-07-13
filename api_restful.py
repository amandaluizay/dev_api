from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

devs = [
    {'id': '1',
     'nome': 'Rafael',
     'habilidades': ['Python', 'Flask']
     },
    {'id': '1',
     'nome': 'Amanda',
     'habilidades': ['Python', 'Dkangp']
     }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucesso'}


class Lista_Desenvolvedores(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        devs.append(dados)
        return ({'status': 'sucesso'})


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Lista_Desenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)

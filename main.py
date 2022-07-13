from flask import *
import json

app = Flask(__name__)

devs = [
    {'nome': 'Rafael',
      'habilidades': ['Python', 'Flask']
     },
     {'nome': 'Amanda',
      'habilidades': ['Python', 'Dkangp']
     }
]

#devolve um dev pelo id e também o deleta pelo id
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status' : 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'sucesso'})


@app.route('/dev', methods=['POST', 'GET'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        return jsonify({'status': 'sucesso'})


if __name__ == '__main__':
    app.run(debug=True)

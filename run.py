from flask import Flask, jsonify, request
import json
app = Flask(__name__)


# lista de desenvolverdores
desenvolvedores = [
    {
        'id':'0',
        'nome': 'Anselmo',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id':'1',
        'nome': 'Priscila',
        'habilidades': ['Python', 'Django']
    }
]

# devolve um desenvolvedor pelo ID , Alterar e Excluir 
@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        response = desenvolvedores[id]
        return jsonify(response)
    elif request.method == 'PUT':
        #Realiza uma alteração
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': ' sucesso', 'mensagem': 'Registro excluido com Sucesso'})
    

@app.route("/dev/", methods=['POST', 'GET'])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'stauts': 'Sucesso', 'mensagem': 'Registro inserido '})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)




if __name__ == '__main__':
    app.run(debug=True)



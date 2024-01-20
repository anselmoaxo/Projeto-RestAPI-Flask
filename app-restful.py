from flask import Flask, request, json
from flask_restful import Resource, Api


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


app = Flask(__name__)
api = Api(app)


class Desenvolvedor(Resource):
    def get(self, id):
        response = desenvolvedores[id]
        return response
    
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': ' sucesso', 'mensagem': 'Registro excluido com Sucesso'}
    
    
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return {'stauts': 'Sucesso', 'mensagem': 'Registro inserido '}
    
    def get(self):
        return desenvolvedores
    
    
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
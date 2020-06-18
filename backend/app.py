from flask import Flask
from flask import jsonify as json
from partidos import ColetadorPartidos
from coletador import Coletador
app = Flask(__name__)

# Rota principal
@app.route('/', methods=['GET'])
def dadosParaPesquisa():
    
    coletandoPartidos = ColetadorPartidos()
    
    response = json({
        "partidos": coletandoPartidos.getPartidos()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Rota partido
@app.route('/partido/<idPartido>')
def rotaPartido(idPartido):
    
    dadosPartido = ColetadorPartidos()
    response = json(
        {
            "dados": dadosPartido.getDadosPartido(idPartido)
        }
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
from flask import Flask
from flask import jsonify as json
from ufs import ColetadorUfs
from partidos import ColetadorPartidos
from coletador import Coletador
app = Flask(__name__)

# Rota principal
@app.route('/', methods=['GET'])
def dadosParaPesquisa():
    
    coletandoUfs = ColetadorUfs()
    coletandoPartidos = ColetadorPartidos()
    
    response = json({
        "ufs": coletandoUfs.getUfs(),
        "partidos": coletandoPartidos.getPartidos()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Rota composta por partido e estado
@app.route('/pesquisandoDeputados')
def coletandoDeputadoPorEstadoEParido():
    pass

# Rota partido
@app.route('/partido/<siglaPartido>')
def rotaPartido(siglaPartido):
    
    dadosPartido = Coletador().coletaPartido(siglaPartido)
    
    return json(
        {
            "messagem": "Acessando rota de partidos",
            "de": "Admin",
            "partidoDados": dadosPartido
        }
    )

# Rota estado
@app.route('/estado/<siglaEstado>')
def rotaEstado(siglaEstado):
    
    dadosEstado = Coletador().coletaEstado(siglaEstado)
    
    return json(
        {
            "messagem": "Acessando rota de estado",
            "de": "Admin",
            "estadoDados": dadosEstado
        }
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
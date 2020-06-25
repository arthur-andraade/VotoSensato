from flask import jsonify as json
from flask import request
from .partidos import ColetadorPartidos
from .deputados import ColetadorDeputado

def init_app(app):
    
    @app.route('/', methods=['GET'])
    def dadosParaPesquisa(): 
        coletandoPartidos = ColetadorPartidos()
        response = json({
            "partidos": coletandoPartidos.getPartidos()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # Rota para dados do partido SELECIONADO
    @app.route('/partido/<idPartido>', methods=['GET'])
    def rotaPartido(idPartido: int):
        dadosPartido = ColetadorPartidos()
        response = json(
            {
                "dados": dadosPartido.getDadosPartido(idPartido)
            }
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @app.route('/filtro')
    def rotaFiltro():
        partido = request.args.get('partido')
        uf = request.args.get('uf')
        filtro = ColetadorDeputado()
        
        response = json({
            "membrosFiltrado": filtro.getDeputadoPorEstado(uf, partido)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
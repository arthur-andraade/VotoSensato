from flask import jsonify as json
from flask import request
from .partidos import ColetadorPartidos
from .deputados import ColetadorDeputado

def init_app(app):
    '''
        ROTA de inicio, 
        fornece as siglas do 
        partido para o front-end
    '''
    @app.route('/', methods=['GET'])
    def dadosParaPesquisa(): 
        coletandoPartidos = ColetadorPartidos()
        response = json({
            "partidos": coletandoPartidos.getPartidos()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


    '''
        ROTA que pega
        um partido específico e retorna
        dados sobre ele
    '''
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

    '''
        ROTA que filtra, pegando deputados por 
        ESTADO do partido selecionado
    '''
    @app.route('/filtro', methods=['GET'])
    def rotaFiltro():
        partido = request.args.get('partido')
        uf = request.args.get('uf')
        filtro = ColetadorDeputado()
        
        response = json({
            "membrosFiltrado": filtro.getDeputadoPorEstado(uf, partido)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
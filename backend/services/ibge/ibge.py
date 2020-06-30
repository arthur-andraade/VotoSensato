from .ufs import ColetadorUfs
from flask import jsonify as json

def init_app(app):
    """ 
        Consumindo API do IBGE,
        e enviando ufs para o 
        front-end.
    """    
    @app.route('/ufs')
    def consutandoIBGE():
        coletandoUfs = ColetadorUfs()
        response = json({
            "siglas": coletandoUfs.getUfs()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

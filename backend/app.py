import services.camara_deputados.api_camara as camaraDeputados
import services.ibge.ibge as ibge
from flask import Flask


def create_app():
    app = Flask(__name__)
    camaraDeputados.init_app(app)
    ibge.init_app(app)
    return app
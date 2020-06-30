import requests
from .utils.aux import formataMembro as formatador
class ColetadorDeputado():
    
    def __init__(self):
        self.url = "https://dadosabertos.camara.leg.br/api/v2/deputados"
        
    def getDeputadoPorEstado(self, uf: str, partido: str):
        #url = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido={0}&siglaUf={1}".format(partido,uf)
        dadosFiltrado = requests.get(f'{self.url}?siglaPartido={partido}&siglaUf={uf}').json()['dados']
        dadosFiltradoFormatado = formatador(dadosFiltrado)
        return dadosFiltradoFormatado
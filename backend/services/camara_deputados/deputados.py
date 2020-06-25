import requests

class ColetadorDeputado():
    
    def __init__(self):
        self.url = "https://dadosabertos.camara.leg.br/api/v2/deputados"

    def formataDados(self, dados):
        dadosFormatados = []
        for membro in dados:
            dadosMembro = {}
            dadosMembro['id'] = membro['id']
            dadosMembro['nome'] = membro['nome']
            dadosMembro['uf'] = membro['siglaUf']
            dadosMembro['image'] = membro['urlFoto']
            dadosMembro['email'] = membro['email']
            dadosFormatados.append(dadosMembro)
        return dadosFormatados
    
    def getDeputadoPorEstado(self, uf: str, partido: str):
        #url = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido={0}&siglaUf={1}".format(partido,uf)
        dadosFiltrado = requests.get(f'{self.url}?siglaPartido={partido}&siglaUf={uf}').json()['dados']
        dadosFiltradoFormatado = self.formataDados(dadosFiltrado)
        return dadosFiltradoFormatado
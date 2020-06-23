import requests

class ColetadorPartidos():
    
    def __init__(self):
        self.partidos = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=33').json()
        self.partidosFormatados = []
        
        for partido in self.partidos['dados']:
            dictPartido = {
                'id': 0, 
                'sigla': ' '
            }
            dictPartido['id'] = partido['id']
            dictPartido['sigla'] = partido['sigla']
            
            self.partidosFormatados.append(dictPartido)

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
    
    def getPartidos(self):
        return self.partidosFormatados
    
    def getDadosPartido(self, idPartido):
        url = 'https://dadosabertos.camara.leg.br/api/v2/partidos/{0}'.format(idPartido)
        # Pegando dados sobre o PARTIDO
        dadosPartido = requests.get(url).json()['dados']
        dadosPartidoFormatado = {}
        dadosPartidoFormatado['sigla'] = dadosPartido['sigla']
        dadosPartidoFormatado['nome'] = dadosPartido['nome']
        dadosPartidoFormatado['logo'] = dadosPartido['urlLogo']
        dadosPartidoFormatado['totalPosse'] = dadosPartido['status']['totalPosse']
        dadosPartidoFormatado['totalMembros'] = dadosPartido['status']['totalMembros']
        dadosPartidoFormatado['situacao'] = dadosPartido['status']['situacao']
        
        # Pegando dados sobre MEMBROS do PARTIDO
        url += '/membros?itens=100'
        dadosMembrosPartido = requests.get(url).json()['dados'] 
        dadosPartidoFormatado['membros'] = self.formataDados(dadosMembrosPartido)
        return dadosPartidoFormatado
    
    def getDeputadoPorEstado(self, uf, partido):
        url = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaPartido={0}&siglaUf={1}".format(partido,uf)
        dadosFiltrado = requests.get(url).json()['dados']
        dadosFiltradoFormatado = self.formataDados(dadosFiltrado)
        return dadosFiltradoFormatado
    
    
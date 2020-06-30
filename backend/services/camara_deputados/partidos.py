import requests
from .utils.aux import formataMembro as formatador
class ColetadorPartidos():
    
    def __init__(self):
        self.partidos = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=33').json()
        self.partidosFormatados = []
        
        for partido in self.partidos['dados']:
            dictPartido = {}
            dictPartido['id'] = partido['id']
            dictPartido['sigla'] = partido['sigla']
            
            self.partidosFormatados.append(dictPartido)
    
    def getPartidos(self):
        return self.partidosFormatados
    
    def getDadosPartido(self, idPartido: int):
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
        dadosPartidoFormatado['membros'] = formatador(dadosMembrosPartido)
        return dadosPartidoFormatado
    
    
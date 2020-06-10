import requests

class ColetadorPartidos():
    
    def __init__(self):
        self.partidos = requests.get('https://dadosabertos.camara.leg.br/api/v2/partidos?itens=33').json()
        self.partidosFormatados = []
        
        for partido in self.partidos['dados']:
            self.partidosFormatados.append(partido['sigla'])
        
    def getPartidos(self):
        return self.partidosFormatados
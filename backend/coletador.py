#   "COLERTADOR DE DADOS"
import requests
import xmltodict
import pandas as pd

class Coletador():
    
    def __init__(self):
        self.acessandoApi = requests.get("https://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados")
        self.conteudoRequisicao = self.acessandoApi.content
        self.converteParaDict = xmltodict.parse(self.conteudoRequisicao)
        
        self.indexNomesDeputados = [] #  Index do DataFrame
        self.dadosCadaParlamentar = {} # Coluna com seus respectivos dados

        
        self.dados = self.converteParaDict['deputados']['deputado']
        for key,value in self.dados[0].items():
            self.dadosCadaParlamentar['{0}'.format(key)] = []  

        # Coletando dados de cada deputado
        for deputado in self.dados:
            self.indexNomesDeputados.append(deputado['nomeParlamentar'])
            for coluna in self.dadosCadaParlamentar:
                self.dadosCadaParlamentar[coluna].append(deputado[coluna])

        # Criando DataFrame
        self.dataFrame = pd.DataFrame(self.dadosCadaParlamentar)
        self.dataFrame.index = self.indexNomesDeputados
    
    def coletaPartido(self,partido):
        
        dadosDeputadosPorPartido = self.dataFrame[self.dataFrame['partido'] == partido].to_dict("dict")
        return dadosDeputadosPorPartido
        
    def coletaEstado(self,estado):
        dadosDeputadosPorEStado = self.dataFrame[self.dataFrame['uf'] == estado].to_dict("dict")
        return dadosDeputadosPorEStado
    
    
    def coletaDeputado(self,nomeDeputado):
        keys = list(self.dadosCadaParlamentar.keys())
        dadosDeputado = self.dataFrame.loc[nomeDeputado].tolist()
        dadosDeputado.append(keys)
        return dadosDeputado


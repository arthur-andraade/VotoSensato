import requests

# Pegando UF de cada estado na API DO IBGE
class ColetadorUfs():
    
    def __init__(self):
        self.ufs = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome').json()
        self.ufsFormatado = []
        for uf in self.ufs:
            self.ufsFormatado.append(uf['sigla'])
    
    def getUfs(self):
        return self.ufsFormatado
    

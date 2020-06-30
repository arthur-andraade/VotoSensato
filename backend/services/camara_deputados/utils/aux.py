'''
    FUNÇÃO que formata dados de acordo com o front-end precisa
    sobre os deputados
'''
def formataMembro(dados):
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
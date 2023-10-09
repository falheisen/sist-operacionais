class Job():
    def __init__(self, id, chegada, memoria, duracao, entradas, saidas):
        self.id = id
        self.chegada = chegada 
        self.memoria = memoria
        self.duracao = duracao 
        self.entradas = entradas
        self.saidas = saidas

    def __repr__(self):
        return f'''
Job: {self.id}
Instante de chegada: {self.chegada} 
Memoria ocupada: {self.memoria}
Duracao do processamento: {self.duracao}
Entradas: {self.entradas}
Saidas: {self.saidas}
    '''
class Processos():
    def __init__(self, id, chegada, estrutura, previsao, acessos, duracao):
        self.id = id
        self.chegada = chegada #Instante de chegada
        self.estrutura = estrutura #Estrutura do job (árvore dos segmentos que o constituem, e tamanho de cada segmento)
        self.previsao = previsao #Número total previsto de entradas, saídas e acessos a arquivos para cada segmento
        self.acessos = acessos #Identificação dos acessos a serem feitos pelo job nos arquivos
        self.duracao = duracao #Tempo máximo previsto de uso da CPU
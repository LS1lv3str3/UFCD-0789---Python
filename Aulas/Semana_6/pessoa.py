'''
A class é criar a forma de um conceito
O objeto é o conteudo da class

Exemplo:
Class é a forma do carro Óbjeto é um carro mercesdes, amarelo ou bentley preto
'''

from dataclasses import dataclass #dataclass é uma class para dados (data)

@dataclass
class Pessoa:
    
    #Atributos - é o que define o objeto
    nome: str
    idade: int
    genero: str
    
    
    
    #Métodos
    
    def envelhecer(self, anos: int = 1):
        self.idade += anos # self.idade = self.idade + anos
    pass
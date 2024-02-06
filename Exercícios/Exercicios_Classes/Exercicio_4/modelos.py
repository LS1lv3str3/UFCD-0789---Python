'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.    
'''

class Pessoa:
    
    def __init__(self, nome:str, idade:int, peso:float, altura:float):
        
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos:int = 1):
        
        self.idade += anos
        
    
    def emagrecer(self, ema:float = 1.0):
        
        self.peso -= ema
        
    
    def engordar(self, engo:float = 1.0):
        
        self.peso += engo
        
    
    def crescer(self, cres:float = 0.5):
        
        self.altura += cres
        
        return self.altura
    
    
        
    
        
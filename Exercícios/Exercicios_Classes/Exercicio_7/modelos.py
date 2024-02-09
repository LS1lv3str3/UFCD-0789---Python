'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade 
    Métodos:
        Alterar Nome, 
        Fome, 
        Saúde 
        Idade; 
    
    Retornar Nome, Fome, Saúde e Idade 
    Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi:
        este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. 
'''

class Tamagotshi:
    
    def __init__(self, nome:str, fome:str = "0 -> Sem Fome", saude:str = "Excelente", idade:int = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def novo_nome(self, novo_nome):
        self.nome = novo_nome
    
    def fome_level(self, nivel_fome:str):
        self.fome = nivel_fome
    
    def level_saude(self, nivel_saude:str):
        self.saude = nivel_saude
    
    def nova_idade(self, anos=1):
        self.idade += anos
        
    
        
    
    
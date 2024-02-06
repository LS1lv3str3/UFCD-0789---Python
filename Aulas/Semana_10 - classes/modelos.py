'''
Class é uma forma de representar alguma coisa concreta ou nao.

Deve-se criar classes para criar objetos
'''
from dataclasses import dataclass

@dataclass
class Fruta:
    cor: str
    tamanho: float
    formato: str = None
    nome: str = None
    idade: int = 1
    textura: str = None
    comestivel: bool = True
    
    #Com valores predefinidos os objetos que constituem essas classes podem reter apenas os atributos nao-definidos ou todos os atributos
    def envelhecer(self, anos: int = 1): #self é usado para quando houver algum objeto desta class a condição ser atribuida a esse objeto 
        self.idade += anos
        
        if self.idade > 5: 
            self.comestivel = False
            
'''
Criar Class com o __init__
'''           
            
class Gato:
    
    def __init__(self, nome : str, idade: int):   #Cria a class 
        self.nome = nome #O self vai fazer atribuição à class por exemplo self.nome vai atribuir o nome ao objeto
        self.idade = idade
        
        
    def envelheceer(self, anos: int = 1):
        self.idade += anos
        
    def __str__(self):
        return f"Gato(nome='{self.nome}', idade={self.idade})"
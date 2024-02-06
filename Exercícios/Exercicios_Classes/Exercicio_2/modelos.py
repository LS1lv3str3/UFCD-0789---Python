'''
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
'''

class Quadrado:
    
    def __init__(self, lado:int):
        
        self.lado = lado
        
    def mudarLado (self, ladoNovo:int):
        
        self.lado = ladoNovo
    
    def calcArea(self):
        
        area = self.lado ** 2
        
        return print(f"A area do novo Quadrado é {area}")
        
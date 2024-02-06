'''
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. 
'''

class Retangulo:
    
    def __init__(self, ladoA:int, ladoB:int):
        
        self.ladoA = ladoA
        self.ladoB = ladoB
        
    def mudarLados(self, novo_ladoA : int , novo_ladoB : int):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB
    
    def calcArea(self):
        
        area = self.ladoA * self.ladoB
        return area
        
        

    def calcPer(self):
        
        perimetro = (self.ladoA * 2) + (self.ladoB * 2)
        return perimetro
        
        
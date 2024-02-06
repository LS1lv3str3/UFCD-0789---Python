'''
Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor 
'''
from modelos import *

bola = Bola("Vermelho", "Esfera", "Tecido")

print(bola.cor)

bola.trocaCor(nova_cor = "Laranja" )

bola.mostraCor()
                
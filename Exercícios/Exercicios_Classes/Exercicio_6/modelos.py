'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar:
    o número do canal;
    aumentar ou diminuir o volume. 
    Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. 
'''

class TV:
    def __init__(self, canal, volume:int = 0, power:int = 0):
        self.power = power
        self.canal = canal
        self.volume = volume
    
    def ligarTV(self, change_power):
        self.power = change_power
    
    def diminuir_volume(self, new_volume):
        self.volume = new_volume
        
    def aumentar_volume(self, new_volume):
        self.volume = new_volume
        
    def aumentar_canal(self,new_canal):
        self.canal = new_canal

    def diminuir_canal(self,new_canal):
        self.canal = new_canal
    
    
        
        
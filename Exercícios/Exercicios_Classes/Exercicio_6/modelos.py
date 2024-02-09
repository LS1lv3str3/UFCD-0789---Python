'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar:
    o número do canal;
    aumentar ou diminuir o volume. 
    Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. 
'''

class TV:
    def __init__(self, canal, volume:int = 0):
        self.canal = canal
        self.volume = volume
    
    def new_volume(self, new_volume):
        
        if new_volume in range(0,26):
            self.volume = new_volume
            return print(f"Volume atualizado para {self.volume}")
        else:
            print("Introduziste um valor de volume invalido.")
            
    def new_canal(self,new_canal):
        if new_canal in range(1,101):  
            self.canal = new_canal
            return print(f"Volume atualizado para {self.volume}")
            
        

    
    
        
        
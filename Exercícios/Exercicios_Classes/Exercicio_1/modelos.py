class Bola:
    
    def __init__(self, cor: str, circunferencia:str, material:str):
        
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocaCor (self , nova_cor:str):
        self.cor = nova_cor
        
    def mostraCor (self):
        return print(f"A nova cor é {self.cor}")
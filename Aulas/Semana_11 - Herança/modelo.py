class Pessoa:
    def __init__(self, nome: str, telefone: int):
        self.nome = nome
        self.tefone = telefone
        
    def mudar_telefone(self, novo_telefone):
        self.telefone = novo_telefone
        
    def get_info(self): #publico
        return f"nome: {self.nome} telefone: {self.tefone}"
    
    def _get_info2(self): #protected
        pass
    
    def __get_info3(self): #privated
        pass
        
        

class Aluno(Pessoa): #Herança em Python: Alunbos vai receber tudo da class de Pessoa que não sejam privados
    
    
    def __init__(self, nome: str, telefone: int, turma: str):
        super().__init__(nome, telefone)
        self.turma = turma

    def myFunc(self):
        super()._get_info2()
    
    def get_info(self): #publico
        return f"{super().get_info()}, turma: {self.turma}"
    
    
    
    
    
al = Aluno("Carlos", "212153", "TPSI1223")
print(al.nome)


al.get_info()
al._get_info2()
al.myFunc()

print(al.get_info())


"""
ENUM

"""

from enum import Enum

class estacoes_ano(Enum):
    verao = "Verão"
    primavera = "Primavera"
    outono = "Outono"
    inverno = "Inverno"
    
print(estacoes_ano.verao) #O Enum permite que criemos classes e consigamos atribuir "Caracteristicas a essa class"
print(estacoes_ano.verao.name)


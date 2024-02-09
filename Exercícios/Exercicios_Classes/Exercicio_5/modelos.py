'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: 
    número da conta, 
    nome do correntista 
    saldo
     
    Os métodos são os seguintes: 
    alterarNome 
    depósito 
    saque
    No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. 
'''

class ContaCorrente:
    def __init__(self, nome:str, numero:int, saldo:float = 0):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        
    def alterarnome(self, novo_nome):
        self.nome = novo_nome
        
    def deposito(self, deposito):
        if deposito < 0:
            print("Introduza um valor válido para deposito")
        
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito Autorizado.\nSaldo Atualizado --> {self.saldo}€")
    
    def levantamento(self, levantamento):
        if levantamento <= self.saldo:
            self.saldo -= levantamento
            print(f"Levantamento Autorizado.\nSaldo Atualizado --> {self.saldo}€")
        
        else:
            print(f"Tentativa de levantamento recusado.\nSaldo Atual --> {self.saldo}€")
            
    
    
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
        self.saldo += deposito
    
    def levantamento(self, levantamento):
        self.saldo -= levantamento
    
    
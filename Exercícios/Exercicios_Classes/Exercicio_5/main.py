from modelos import *

nome =str(input("Qual o seu nome? Nome --> "))
numero = int(input("Digite o numero da sua Conta --> "))

conta_1 = ContaCorrente(nome, numero)

print(conta_1.nome)
print(conta_1.numero)

questao_1 = str(input("Deseja alterar o nome da sua conta? S --> Sim | N --> Não\nResposta --> "))

if questao_1.lower() == 's':
    novo_nome = str(input("Qual o novo nome da sua conta corrente?\nNovo nome --> "))
    conta_1.alterarnome(novo_nome)
    print(f"A sua conta Corrente agora tem o nome de {conta_1.nome}")

questao_2 = int(input("Pressione:\n1 -> Depósito | 2 -> Levantamento | Qualquer outra ação -> Cancelar Operação\n--> "))

if questao_2 == 1:
    deposito = int(input("Qual a quantia que deseja depositar?\nDepósito --> "))
    conta_1.deposito(deposito)
    print(f"O valor depositado foi {deposito}€\nSaldo Atual --> {conta_1.saldo}€")
    
elif questao_2 == 2 and conta_1.saldo:
    levantamento = int(input("Qual a quantia que deseja levantar?\nLevantamento --> "))
    
    if levantamento < conta_1.saldo:
        print("Levantamento Autorizado")
        conta_1.levantamento(levantamento)
        print(f"Saldo atual -- > {conta_1.saldo}")
    
    else:
        print("Levantamento Não Autorizado por saldo insuficiente")

else:
    print("Operação Cancelada por sua ordem!")
    
        
        
    



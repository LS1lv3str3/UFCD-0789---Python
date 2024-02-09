from modelos import *

create = str(input("Desejas criar uma conta?\nS --> Sim | N --> Não\nResposta --> "))

contas = []

while create.lower() == 's':
    
    nome = str(input("Qual o seu nome? Nome --> "))
    numero = int(input("Digite o numero da sua Conta --> "))

    new_conta = ContaCorrente(nome, numero)
    contas.append(new_conta)


    questao_1 = str(input("Deseja alterar o nome da sua conta? S --> Sim | N --> Não\nResposta --> "))

    if questao_1.lower() == 's':
        novo_nome = str(input("Qual o novo nome da sua conta corrente?\nNovo nome --> "))
        new_conta.alterarnome(novo_nome)
        print(f"A sua conta Corrente agora tem o nome de {new_conta.nome}")

    questao_2 = int(input("Pressione:\n1 -> Depósito | 2 -> Levantamento | Qualquer outra ação -> Cancelar Operação\n--> "))

    if questao_2 == 1:
        deposito = int(input("Qual a quantia que deseja depositar?\nDepósito --> "))
        new_conta.deposito(deposito)
        
    elif questao_2 == 2 and new_conta.saldo:
        levantamento = int(input("Qual a quantia que deseja levantar?\nLevantamento --> "))
        new_conta.levantamento(levantamento)

    else:
        print("Operação Cancelada por sua ordem!")
        
    continuar = input("Deseja criar mais contas?\nS --> Sim | N --> Não")
    
    if continuar.lower() != 's':
        break
    
print(contas[0].nome)
print(contas[0].saldo)
        
    



'''

Faça um Programa para um caixa eletrônico.
O programa deverá:
        perguntar ao usuário a valor do saque;
        informar quantas notas de cada valor serão fornecidas. 
            As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
            O valor mínimo é de 10 reais e o máximo de 600 reais. 
        O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 

'''
levantamento = int(input("Quanto dinheiro deseja levantar? "))

def check_levantamento(levantamento):
    return 10 < levantamento < 600


def tipo_notas(valor_leva):
    
    notas_100 = valor_leva // 100
    valor_leva %= 100
        
    notas_50 = valor_leva // 50
    valor_leva %= 50

    notas_10 = valor_leva // 10
    valor_leva %= 10
        
    notas_5 = valor_leva // 5
    valor_leva %= 5
       
    notas_1 = valor_leva // 1
        
    print(f"Seão dispensadas: \n {notas_100} notas de 100€ \n {notas_50} notas de 50€ \n {notas_10} notas de 10€ \n {notas_5} notas de 5€ \n {notas_1} notas de 1€ ")

if check_levantamento(levantamento):
    
    print(f"Valor de Levantamento: {levantamento}€")
    tipo_notas(levantamento)
else:
    print("Só é permitido levantamentos entre 10€ e 600€")


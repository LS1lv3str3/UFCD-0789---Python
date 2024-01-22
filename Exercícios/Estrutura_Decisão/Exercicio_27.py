'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00:
        receberá ainda um desconto de 10% sobre este total. 
        
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 
'''

peso_Mor = float(input("Peso MORANGOS: "))
peso_Maca = float(input("Peso MAÇÃS: "))

def totalMorango():
    
    if peso_Mor <= 5:
        preco_Mor = peso_Mor * 2.50
        
        return preco_Mor
    
    if peso_Mor > 5:
        preco_Mor = peso_Mor * 2.20
        
        return preco_Mor
    
def totalmaca():
    
    if peso_Maca <= 5:
        preco_Maca = peso_Maca * 1.80
        
        return preco_Maca
    
    if peso_Maca > 5:
        preco_Maca = peso_Maca * 1.50
        
        
        return preco_Maca

preco_Total = totalmaca() + totalMorango()
peso_Total = peso_Mor + peso_Maca

if preco_Total > 25 or peso_Total > 8:
    
    preco_Final = preco_Total * 0.9
    print(f"Peso Morangos : {peso_Mor}kg \nPeso Maças: {peso_Maca}kg \nPeso Total: {peso_Total}kg\n Valor final = {preco_Final}")

else:
    print(f"Peso Morangos : {peso_Mor}kg \nPeso Maças: {peso_Maca}kg \nPeso Total: {peso_Total}kg\n Valor final = {preco_Total}")
    
    
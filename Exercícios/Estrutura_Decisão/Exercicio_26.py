'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
    
    Escreva um algoritmo que leia o número de litros vendidos
    o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
    calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 


def tipoCombustivel():
        
    while True:  
        tipo = str(input("Que tipo de combustivél queres? A - Álcool | G - Gasolina \n Tipo de Combustivél: "))       
        if tipo.lower() == 'a':
            tipo_Select = "Álcool"
            
            break
                    
        elif tipo.lower()== 'g':
            
            tipo_Select = "Gasolina"
            break
                       
        else:
            print("Por favor, selecione apenas 'A' para Álcool ou 'G' para Gasolina.")
    
    return tipo_Select 
'''
   
def gasolineira():
    
    while True:  
        tipo = str(input("Que tipo de combustivél queres? A - Álcool | G - Gasolina \n Tipo de Combustivél: "))       
        if tipo.lower() == 'a':
            tipo_Select = "Álcool"
            
            break
                    
        elif tipo.lower()== 'g':
            
            tipo_Select = "Gasolina"
            break
                       
        else:
            print("Por favor, selecione apenas 'A' para Álcool ou 'G' para Gasolina.")
    
    qty_Litros = float(input("Quantos litros queres comprar? \n Quantidade de litros: "))
    
    preco_Alcool = qty_Litros * 1.90
    preco_Gasolina = qty_Litros * 2.50
    
    if tipo_Select == "Álcool" and qty_Litros <= 20:
        
        preco_Total = preco_Alcool * 0.97
        preco_Total_Round = round(preco_Total, 2)
        preco_Litro = preco_Total / qty_Litros
        preco_Litro_Round = round(preco_Litro, 2)
        
        return preco_Total_Round, preco_Litro_Round, tipo_Select
    
    elif tipo_Select == "Álcool" and qty_Litros > 20:
        
        preco_Total = preco_Alcool * 0.95
        preco_Total_Round = round(preco_Total, 2)
        preco_Litro = preco_Total / qty_Litros
        preco_Litro_Round = round(preco_Litro, 2)
        
        return preco_Total_Round, preco_Litro_Round, tipo_Select

    elif tipo_Select == "Gasolina" and qty_Litros <= 20:
        
        preco_Total = preco_Gasolina * 0.96
        preco_Total_Round = round(preco_Total, 2)
        preco_Litro = preco_Total / qty_Litros
        preco_Litro_Round = round(preco_Litro, 2)
        
        return preco_Total_Round, preco_Litro_Round, tipo_Select
    
    elif tipo_Select == "Gasolina" and qty_Litros > 20:
        
        preco_Total = preco_Gasolina * 0.94
        preco_Total_Round = round(preco_Total, 2)
        preco_Litro = preco_Total / qty_Litros
        preco_Litro_Round = round(preco_Litro, 2)
        
        return preco_Total_Round, preco_Litro_Round, tipo_Select

result = gasolineira()
print(f"Tipo de combustivél: {result[2]} \n Preço por Litro c/ desconto: {result[1]}$ \n Preço Total = {result[0]}$")
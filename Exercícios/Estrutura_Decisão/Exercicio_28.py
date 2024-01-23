'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção
    Porém não há limites para a quantidade de carne por cliente. 
    Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário
 gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 
'''

resp = str(input("Você tem cartão Tabajara? \n Digite S - SIM ou N - Não \n Resposta: "))

tipo = str(input("Produtos Inluidos na promoção: File Duplo | Alcatra | Picanha \n Escreva o tipo de carne em promoção que deseja comprar: "))

qty_Kilos = (float(input(f"Qauntos kilos desa levar de {tipo}? \n Kg = ")))

tipos_carne = ["File Duplo", "Alcatra", "Picanha"]

def verificarCartão(resp: str):
    
    if resp.lower() == 's':   
        return 0.95
    
    else:
        return 1

def tiposCarne (tipo: str):
    
    if tipo.lower() == tipos_carne[0].lower():
        return tipos_carne[0]
    
    if tipo.lower() == tipos_carne[1].lower():
        return tipos_carne[1]
    
    if tipo.lower() == tipos_carne[2].lower():
        return tipos_carne[2]
    
    

   
def pagamento(valor: float):
    
    if qty_Kilos <= 5 and tiposCarne(tipo) == tipos_carne[0]:
        
        valor = qty_Kilos * 4.90
        valor = round(valor, 2)
        
        return valor
    
    if qty_Kilos > 5 and tiposCarne(tipo) == tipos_carne[0]:
        
        valor = qty_Kilos * 5.80
        valor = round(valor, 2)
        
        return valor
    
    if qty_Kilos <= 5 and tiposCarne(tipo) == tipos_carne[1]:
        
        valor = qty_Kilos * 5.90
        valor = round(valor, 2)
        
        return valor
    
    if qty_Kilos > 5 and tiposCarne(tipo) == tipos_carne[1]:
        
        valor = qty_Kilos * 6.80
        valor = round(valor, 2)
        
        return valor
    
    if qty_Kilos <= 5 and tiposCarne(tipo) == tipos_carne[2]:
        
        valor = qty_Kilos * 6.90
        valor = round(valor, 2)
        
        return valor
    
    if qty_Kilos > 5 and tiposCarne(tipo) == tipos_carne[2]:
        
        valor = qty_Kilos * 5.90
        valor = round(valor, 2)
        
        return valor

if verificarCartão(resp) == 0.95:
    print(f"Valor S/ Disconto: {pagamento(tiposCarne(tipo))}€ \n Valor C/ Disconto: {pagamento(tiposCarne(tipo)) * verificarCartão(resp)}€")
    
else:
    print(f"{pagamento(tiposCarne(tipo))}€")



'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 
'''

def decompor(num):

    if 0 < num < 1000:
        cent = num // 100
        deze = (num % 100) // 10
        uni = num % 10

        resultado = f"O {num} é constituido por: \n"
        
        if cent >= 0:
            
            resultado += f"Centenas = {cent} \n"
            
        if deze >= 0:
            
            resultado += f"Dezenas = {deze} \n"
            
        if uni >= 0:
            
            resultado += f"Unidades = {uni} \n"
            
        print(resultado)
    else:
        print("Introduz um numero entre 1 e 999")
        

teste = [326, 300 , 100, 320, 310 ,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 , 16]  

for num in teste:
    decompor(num) 
       
        


        

     
    
    
    
    
    
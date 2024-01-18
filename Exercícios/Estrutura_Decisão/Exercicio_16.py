'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma:
                                        ax2 + bx + c

O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
'''
import math

InputDoUtilizador = [
    float(input("Digite o valor a:")),
    float(input("Digite o valor b:")),
    float(input("Digite o valor c:"))
]

if InputDoUtilizador[0] == 0:
    print("A função não é uma equação de 2 grau")
    
    

def Calculo_Delta(valores):
    
    delta = valores[1]**2 + 4*valores[0]*valores[2]
    
    if delta > 0:
        raiz_1 = (-valores[1] - math.sqrt(delta)) / 2*valores[0]
        raiz_2 = (-valores[1] + math.sqrt(delta)) / 2*valores[0]
        
        raiz_1 = round(raiz_1, 2)
        raiz_2 = round(raiz_2, 2)
        
        return raiz_1, raiz_2
    
    if delta == 0:
        raiz_1 = -valores[1] / 2*valores[0]
        raiz_1 = round(raiz_1, 2)
        
        return raiz_1
    
    else:
        print("A solução não tem solução nos numeros Reais.")


print(f"{Calculo_Delta(InputDoUtilizador)} são as soluções da tua função")     

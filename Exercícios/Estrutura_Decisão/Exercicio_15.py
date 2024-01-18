'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 
'''
inputDoUtilizador =[
    float(input("Introduz o comprimento do Lado do Triangulo 1: ")),
    float(input("Introduz o comprimento do Lado do Triangulo 2: ")),
    float(input("Introduz o comprimento do Lado do Triangulo 3: ")),
]

def verificar_triangulo(lados):
    return ((lados[0] + lados[1]) > lados [2] and (lados[0] + lados[2]) > lados [1] and (lados[1] + lados[2]) > lados [0])

def tipotriangulo(lados):
    if lados[0] == lados[1] == lados[2]:
        return 'Triuangulo Equílatero'
    
    if lados[0] != lados[1] != lados[2] != lados[0]:
        return 'Triangulo Escaleno'
    
    else:
        return ' Triângulo Isósceles'


if verificar_triangulo(inputDoUtilizador):
    print(tipotriangulo(inputDoUtilizador))
    
else:
    print("Não é um Triângulo")
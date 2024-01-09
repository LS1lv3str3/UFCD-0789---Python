"""
Continuação da semana 2 
"""
"""
if

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é par!")

elif numero % 5 == 0:
    print("O numero não é par mas é divisivél por 5")

elif numero % 3 == 0:
    print("O numero não é par mas é divisivél por 3")

else:
    print("O numero não é par")

No if é possivel utilizar and ou or, por exemplo:

if numero % 2 == 0 and numero % 5 == 0 or numero == 42
    print("O numeor é par e divisivél por 5")

"""

"""
match é o switch case, vai verificar se o valor atribuido na variavél vai ao encontro com os meus cases

nota = 20

match nota:
    case 10:
        print("A nota é 10")

    case 15:
        print("A nota é 15")
    case _:
        print("Outra nota!")
"""

"""
funções

Define-se as variaveis com a seguinte sintaxe dev nome_da_variavel ():
pass é utilizado para designar um bloco vazio

def ola_mundo():
    print("Ola Mundo")

ola_mundo()
ola_mundo()
ola_mundo()

def ola_mundo_2(nome:str):
    print(f"Ola Mundo, {nome}")

ola_mundo_2("João")
ola_mundo_2("Rita")
ola_mundo_2("Maria")

---------------------------------------------

O return é como se o valor ficasse guardado para ser usado mais tarde, utilizando o comando print()

def ola_mundo_3(nome: str):
    return f"Ola Mundo, {nome}"

print(ola_mundo_3("João"))
print(ola_mundo_3("Maria"))
print(ola_mundo_3("Rita"))

Sem o comando print não devolve nada 

---------------------------------------------

Exercicio formula resolvente 

-b +- raiz(b^2 -4ac)/2a 

import math 

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def div_zero(a:float): #Verifica se o 2a = 0
    if a == 0.0:
        return True
    
    return False

def calc_int_raiz(a: float, b: float, c: float): 
    int_raiz = (b * b) - (4 * a * c)
    if int_raiz >= 0.0: # Verifica se o calculo da raiz é >=0
        return int_raiz
    else:
        return False

def fresolv(a: float, b: float, c: float):
    i = calc_int_raiz(a, b, c)
    if div_zero(a) or (i < 0): #Verifica as condições de exclusão
        return False
    
    raiz = math.sqrt(i)

    x1 = (-b + raiz) / a * 2
    x2 = (-b - raiz) / a * 2

    return f"X1 = {x1}\nX2 = {x2}"

print(fresolv(a, b, c))
"""
import math 

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

def div_zero(a:float): #Verifica se o 2a = 0
    if a == 0.0:
        return True
    
    return False

def calc_int_raiz(a: float, b: float, c: float): 
    int_raiz = (b * b) - (4 * a * c)
    if int_raiz >= 0.0: # Verifica se o calculo da raiz é >=0
        return int_raiz
    else:
        return False

def fresolv(a: float, b: float, c: float):
    i = calc_int_raiz(a, b, c)
    if div_zero(a) or (i < 0): #Verifica as condições de exclusão
        return False
    
    raiz = math.sqrt(i)

    x1 = (-b + raiz) / a * 2
    x2 = (-b - raiz) / a * 2

    return f"X1 = {x1}\nX2 = {x2}"

print(fresolv(a, b, c))
    


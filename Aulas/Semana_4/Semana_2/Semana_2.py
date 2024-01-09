#Criar variaveis
"""
idade = 20
ano_curr = 2023
nome = "Lucas"
"""

#comando print
"""
print(f"O {nome} tem {idade} anos")

"""
#Operações com variaveis

"""
+ - / * % (modulo ou resto da divisão inteira) ** (potência)
para fazer a divisão inteira são //
"""

"""
a = 6
b = 2

print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(a / b) # Divisão décimal
print(a // b) # Divisão inteira
print(a % b) # Resto/modulo da divisão = 0

a = 5
b = 2

print(a / b) # Divisão décimal = 2.5
print(a // b) # Divisão inteira = 2
print(a % b) # Resto/modulo da divisão resto = 1

a = 3
b = 2

print(a ** b)

"""

#Input

"""
idade_input = input("Qual é o seu idade: ")
nome_input = input("Qual é o seu nome: ")

print(f"O nome inserido foi {nome_input} e tem {idade_input} anos.")

"""

#converter tipos de dados
"""
idade_input = input("Qual é o seu idade: ")
nome_input = input("Qual é o seu nome: ")
idade_input_int = int(idade_input)
ano_int = int("2023")
ano_nasc = ano_int - idade_input_int

print(f"O nome inserido foi {nome_input} e tem {idade_input} anos e nasceu {ano_nasc}.")

"""
"""
Condições: < > <= >= == !=
if True:
    print("Dentro do bloco")
    
print("Fora do bloco")

if not - se nao

and - e

or - ou

"""

num_a = 10
num_b = 15
num_c = 20

if not num_a < num_b: # equivalente a num_a > num_b
    print("True")
elif (num_a > num_b) or (num_c > num_a): # else if
    print("False")
else:
    print("else") 
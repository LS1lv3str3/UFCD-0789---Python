'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = input("Qual é o seu sexo? M ou F: ")

if sexo == 'M' or sexo == 'm':
    print("M - Masculino")
elif sexo == 'F' or sexo == 'f':
    print("F - Feminimo")
else:
    print("Sexo Inválido")
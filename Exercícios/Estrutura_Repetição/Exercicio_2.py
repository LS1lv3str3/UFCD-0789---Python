'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
'''

username = str(input("Username \n"))
password = str(input("Password \n"))

while password.lower() == username.lower():
    print("Coloque uma password diferente do seu username")
    username = str(input("Username: \n"))
    password = str(input("Password: \n"))
print("Registo efetuado com sucesso! ")
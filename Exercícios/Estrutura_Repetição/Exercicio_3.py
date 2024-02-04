'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''

not_register = True

while not_register:
    nome = str(input("Por favor insere o teu nome: "))
    if len(nome) < 3:
        print("Só são aceites nomes com mais do que 3 caracteres.")
    
    while True:
        idade = int(input("\nInsere a tua idade: "))
        if 0 < idade < 150:
            break
        
        else: 
            print("Por favor, insira uma idade válida entre os 0 e os 150 anos.")
    
    while True:        
        sexo = str(input("\nQual o teu sexo? M --> Masculino | F --> Feminino \n Sexo: "))
        if sexo.lower() == 'm' or sexo.lower() == 'f':
            break
        else:
            print("Por favor introduz apenas 'M' para Masculino ou 'F' para Feminino")
    
    while True:
        estado = str(input("\nQual o teu estado civil:\nSolteiro --> S\nCasado --> C\nDicosiádo --> D\nViúvo(a) --> V\n\nEstado Civil: "))
        if estado.lower() == 's' or estado.lower() == 'c' or estado.lower() == 'd' or estado.lower() == 'v':
            break
        else:
            print("Por favor insira apenas uma das opções apresentadas na lista de cima.")
    
    while True:
        salario = float(input("\nQual é o teu salário?\nSalário: "))
        if salario > 0:
            break
        else:
            print("Por favor só é aceite salários superiores a 0")
        
    not_register = False

print("\nRegisto efetuado com sucesso")
    

    
       
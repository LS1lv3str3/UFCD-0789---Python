'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. 
'''



def operacao():
    num_1 = float(input("Introduza o 1º numero: "))
    num_2 = float(input("Introduza o 2º numero: "))
    opr = str(input(f"Qual a operação que deseja efetuar entre o {num_1} e {num_2}: \n Operação: "))
    
    if opr == '+':
        
        soma = num_1 + num_2
        round_soma = round(soma)

        if soma % 2 == 0 and soma > 0 and soma == round_soma:
            print(f"Resultado = {soma} \n {soma} é um numero par, positivo e inteiro")
        else:
            print(f"Resultado = {soma} \n {soma} é um numero impar, negativo e décimal")

    if opr == '-':
        
        sub = num_1 - num_2
        round_sub = round(sub)
        
        if sub % 2 == 0 and sub > 0 and sub == round_sub:
            print(f"Resultado = {sub} \n {sub} é um numero par, posditivo e inteiro")
        else:
            print(f"Resultado = {sub} \n {sub} é um numero impar, negativo e décimal")
            
    if opr == '*':
        multi = num_1 * num_2
        round_multi = round(multi)
        
        if multi % 2 == 0 and multi > 0 and multi == round_multi:
            print(f"Resultado = {multi} \n {multi} é um numero par, posditivo e inteiro")
        else:
            print(f"Resultado = {multi} \n {multi} é um numero impar, negativo e décimal")
        
    
    if opr == '/':
        divi = num_1 / num_2
        divi_round = round(divi)
        
        if divi % 2 == 0 and divi > 0 and divi == divi_round:
            print(f"Resultado = {divi} \n {divi} é um numero par, posditivo e inteiro")
        else:
            print(f"Resultado = {divi} \n {divi} é um numero impar, negativo e décimal")

operacao()
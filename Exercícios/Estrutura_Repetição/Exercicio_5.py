'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

'''
not_calc = True

while not_calc:
    
    pop_A = int(input("Qual a população do pais A: "))
    tx_cresc_A = float(input("Qual a taxa de crescimento do pais A: "))

    pop_B = int(input("Qual a população do pais B: "))
    tx_cresc_B = float(input("Qual a taxa de crescimento do pais B: "))

    tx_cresc_A = (tx_cresc_A / 100) + 1
    tx_cresc_B = (tx_cresc_B / 100) + 1

    validation = pop_A < pop_B
    anos = 0
    if pop_A < pop_B:
        while pop_A < pop_B:
                            
                pop_A = pop_A * tx_cresc_A
                pop_B = pop_B * tx_cresc_B
                
                anos = anos + 1
                not_calc = False
            
        print(f"Serão precisos {anos} anos para a populção ser igual à população do pais B")
    else:
        print("Os dados introduzidos mostram que a população do Pais A já é igual ou superior que a população do pais B.\n Introduz novamente os dados.")
        


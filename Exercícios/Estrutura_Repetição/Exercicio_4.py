'''
Supondo que:
    Ppopulação de um país A seja:
    Da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
    
    População de B seja:
    200000 habitantes com uma taxa de crescimento de 1.5%. 
    
    Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
'''

pop_A = 80000
tx_cresc_A = 1.03

pop_B = 200000
tx_cresc_B = 1.015

anos = 0

while pop_A < pop_B:
    
    pop_A = pop_A * tx_cresc_A
    pop_B = pop_B * tx_cresc_B
    
    anos = anos + 1
print(f"Serão precisos {anos} anos")
    
    
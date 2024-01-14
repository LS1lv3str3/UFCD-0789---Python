'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 
'''

tamanho_arq = float(input("Quantos MB tem o teu ficheiro? "))
velocidade_int = float(input("Qual a tua velocidade de internet em Mbps? "))

velocidade_download = (tamanho_arq / velocidade_int) * 60

print(f"O seu arquivo vai demorar {velocidade_download} minutos a fazer o download")
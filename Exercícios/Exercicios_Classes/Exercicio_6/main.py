from modelos import *

tv1 = TV(4)
print(tv1.canal)
print(tv1.power)
print(tv1.volume)
power = int(input("Deseja ligar a TV? 0 --> Desligado | 1 --> Ligado\n"))

canais = range(1,101)
volumeTV = range(0,26)

if power == 1:
    tv1.ligarTV(power)
    print("TV TURN ON")
    
    questao_1 = str(input("Se deseja mudar de canal pressione + --> Aumentar | - --> Diminuir\n--> "))
    
    while questao_1 == '+' and tv1.canal == 100:
        print("O teu serviço nao permite que visualizes mais de 100 canais")
        questao_1 = str(input("Se deseja mudar de canal pressione + --> Aumentar | - --> Diminuir\n--> "))
    
    if questao_1 == "+":
        
        new_canal = int(input("Canal --> "))
        
        if new_canal in canais:
            tv1.aumentar_canal(new_canal)
            print(f"Estás transmitir o canal {tv1.canal}")
    
    while questao_1 == '-' and tv1.canal == 1:
        print("Estás no canal 1 só consegues aumentar o canal")
        questao_1 = str(input("Se deseja mudar de canal pressione + --> Aumentar | - --> Diminuir\n--> "))

    if questao_1 == "-":
        
        new_canal = int(input("Canal --> "))
        
        if new_canal in canais:
            tv1.diminuir_canal(new_canal)
            print(f"Estás transmitir o canal {tv1.canal}")    
        
    questao_2 = str(input("Se desejas aumentar ou diminuir o volume pressiona - --> Diminuir | + --> aumentar"))
    
    while questao_2 == '-' and tv1.volume == 0:
        print("Estas sem som só podes aumentar o volume!")
        questao_2 = str(input("Se desejas aumentar ou diminuir o volume pressiona - --> Diminuir | + --> aumentar"))
        
    if questao_2 == '-':
        
        while new_volume not in volumeTV or new_volume < 0 or new_volume > tv1.volume:
            new_volume = int(input(f"O volume nãop pode ser ajustado para o que desejas colaca um entre {tv1.volume} - 0 \n Nivel de Volume --> "))
        tv1.diminuir_volume(new_volume)
        print(f"Volume ajustado para {tv1.volume}")
        
    while questao_2 == '+' and tv1.volume == 25:
        print("Estas sem som só podes aumentar o volume!")
        questao_2 = str(input("Se desejas aumentar ou diminuir o volume pressiona - --> Diminuir | + --> aumentar"))  
    
    if questao_2 == '+':
        new_volume = int(input(f"Nivel de Volume atual {tv1.volume}\nVolume --> "))
        while new_volume not in volumeTV or new_volume > 25 or new_volume < tv1.volume:
            new_volume = int(input(f"O volume nãop pode ser ajustado para o que desejas colaca um entre {tv1.volume} - 25 \n Nivel de Volume --> "))
        tv1.aumentar_volume(new_volume)
        print(f"Volume ajustado para {tv1.volume}")
    else:
        print("Volume inalterado") 
    
else:
    print("TV TURN OFF") 


    
    
    
    
    
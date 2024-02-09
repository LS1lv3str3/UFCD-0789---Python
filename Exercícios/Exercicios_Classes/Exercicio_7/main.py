from modelos import * 
import random

t1 = Tamagotshi("Lu")

print(t1.fome)

nivel_fome = ["0 -> Sem fome", "1 -> Pouca Fome", "2-> Tenho fome", "3-> Esfomeado"]

t1.fome_level(nivel_fome[3])

if t1.fome_level == nivel_fome[3]:
    print("Estou a morrer de fome")
    
nivel_saude = ["Saudavél", "Doente"]

estado_saude = random.choice(nivel_saude)

t1.level_saude(estado_saude)

print(t1.saude)


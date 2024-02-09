from modelos import *

tv1 = TV(4)
print(tv1.canal)
print(tv1.volume)

canal = str(input("Introduzz o canal quue desejas ver.\nCanal --> "))
tv1.new_canal(canal)

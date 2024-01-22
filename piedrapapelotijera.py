import random

print("Piedra, papel o tijera, V0.3")
def bucle():
    print("1 = piedra")
    print("2 = papel")
    print("3 = tijera")
    tirada = int(input("Escoge tu tirada: "))

    tiradaordenador = random.randint(1, 3)


    if tiradaordenador == 1:
        print("El ordenador ha sacado piedra")
    elif tiradaordenador == 2:
        print("El ordenador ha sacado papel")
    elif tiradaordenador == 3:
        print("El ordenador ha sacado tijera")
        

    if tirada == 1 and tiradaordenador == 1:
        print ("Empate")
    elif tirada == 1 and tiradaordenador == 2:
        print ("Gana la maquina")
    elif tirada == 1 and tiradaordenador == 3:
        print ("El jugador gana")

    elif tirada == 2 and tiradaordenador == 1:
        print ("El jugador gana")
    elif tirada == 2 and tiradaordenador == 2:
        print ("Empate")
    elif tirada == 2 and tiradaordenador == 3:
        print ("Gana la maquina")

    elif tirada == 3 and tiradaordenador == 1:
        print ("Gana la maquina")
    elif tirada == 3 and tiradaordenador == 2:
        print ("El jugador gana")
    elif tirada == 3 and tiradaordenador == 3:
        print ("Empate")
    bucle()

bucle()

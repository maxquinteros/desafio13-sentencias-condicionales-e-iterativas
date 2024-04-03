import random

eleccion_jugador = (input("Escriba piedra o papel o tijera: ")).lower()

if eleccion_jugador != "piedra" and eleccion_jugador != "papel" and eleccion_jugador != "tijera":
    print("Argumento inválido: Debe ser piedra, papel o tijera.")

else:
    print(f"Tu jugaste {eleccion_jugador}")

    eleccion_computador = random.choice(("piedra", "papel", "tijera"))
    print(f"Computador jugó {eleccion_computador}")
    
    if eleccion_jugador == "piedra" and eleccion_computador == "piedra":
        print("Empate!!")
    elif eleccion_jugador == "piedra" and eleccion_computador == "papel":
        print("Perdiste!!")
    elif eleccion_jugador == "piedra" and eleccion_computador == "tijera":
        print("Ganaste!!")
        
    if eleccion_jugador == "papel" and eleccion_computador == "piedra":
        print("Ganaste!!")
    elif eleccion_jugador == "papel" and eleccion_computador == "papel":
        print("Empate!!")
    elif eleccion_jugador == "papel" and eleccion_computador == "tijera":
        print("Perdiste!!")
        
    if eleccion_jugador == "tijera" and eleccion_computador == "piedra":
        print("Perdiste!!")
    elif eleccion_jugador == "tijera" and eleccion_computador == "papel":
        print("Ganaste!!")
    elif eleccion_jugador == "tijera" and eleccion_computador == "tijera":
        print("Empate!!")
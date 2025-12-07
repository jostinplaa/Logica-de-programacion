import random

def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijera")

    opciones = {1: "piedra", 2: "papel", 3: "tijera"}
    opcion_valida = False
    
    while not opcion_valida:
         
        print("\n--- Menú ---") 
        print("(1) Piedra")
        print("(2) Papel")
        print("(3) Tijera")

        try:
            opcion_usuario = int(input("Elige una opcion: "))

            
            if opcion_usuario in opciones:
                opcion_valida = True
                print("Has elegido: ", opciones[opcion_usuario])
            else:
                print("Opcion no valida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingresa un numero valido")

    opcion_computador = random.randint(1, 3)
    print("La computadora ha elegido: ", opciones[opcion_computador])
    # Verifica quien gano la partida comparando las variables donde se guardo la jugada del usuario y la de la computadora dentro de la variables
    # opciones donde se guardo el diccionario con las opciones de juego
    
    if opcion_usuario == opcion_computador:
        print("Empate")
    elif (opcion_usuario == 1 and opcion_computador == 3) or \
         (opcion_usuario == 2 and opcion_computador == 1) or \
         (opcion_usuario == 3 and opcion_computador == 2):
        print("Ganaste")
    else:
        print("Perdiste")
    # Este código representa el avance del 70%, demostrando la lógica selectiva y la validación.
    # Para la entrega final del proyecto (100%), realizare las siguientes implementaciones:
    # 1. Implementare la ESTRUCTURA REPETITIVA PRINCIPAL (el while grande) para el rombo "¿Jugar de nuevo?".
    # 2. Añadire comentarios (#) detallados dentro del codigo para asegurar el entendimiento del código.

jugar()


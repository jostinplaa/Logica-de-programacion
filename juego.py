import random

def jugar():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    
    # ----------------------------------------------------
    # PASO 1: INICIO DEL CICLO PRINCIPAL
    repetir_juego = True # Variable de control para el rombo "¿Jugar de nuevo?"
    
    # Este WHILE GRANDE ejecuta todo el juego
    while repetir_juego: 
    # ----------------------------------------------------

        opciones = {1: "piedra", 2: "papel", 3: "tijera"}
        opcion_valida = False
        
        # ESTRUCTURA REPETITIVA 1: Validar Entrada
        while not opcion_valida:
            # ... (Toda la lógica de Menú y Try/Except va aquí) ...

            print("\n--- Menú ---") 
            print("(1) Piedra")
            print("(2) Papel")
            print("(3) Tijera")

            try:
                opcion_usuario = int(input("Elige una opcion: "))

                if opcion_usuario in opciones:
                    opcion_valida = True
                    # Aquí se usa opcion_usuario como el número para la lógica
                    print("Has elegido: ", opciones[opcion_usuario])
                else:
                    print("Opcion no valida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingresa un numero valido")

        # ESTRUCTURA SECUENCIAL: Generar el turno de la computadora
        opcion_computador = random.randint(1, 3) 
        print("La computadora ha elegido: ", opciones[opcion_computador])

        # ESTRUCTURA SELECTIVA: Lógica de Comparación
        
        if opcion_usuario == opcion_computador:
            print("Empate")
        elif (opcion_usuario == 1 and opcion_computador == 3) or \
             (opcion_usuario == 2 and opcion_computador == 1) or \
             (opcion_usuario == 3 and opcion_computador == 2):
            print("Ganaste")
        else:
            print("Perdiste")
            
        # ----------------------------------------------------
        # PASO 2: CONTROL DEL CICLO PRINCIPAL (Rombo "¿Jugar de nuevo?")
        
        # Bucle para validar que la respuesta sea solo 's' o 'n'
        respuesta_valida = False
        while not respuesta_valida:
            # Pedimos input al usuario y lo convertimos a minúscula
            respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ")
            
            if respuesta == 'n':
                repetir_juego = False # Cambia la variable a False, el while grande terminará
                respuesta_valida = True
                print("¡Gracias por jugar! Fin del programa.")
            elif respuesta == 's':
                respuesta_valida = True # La variable 'repetir_juego' sigue en True, el while se repite
            else:
                print("Respuesta no válida. Por favor, usa 's' o 'n'.")
                
    # ----------------------------------------------------
    # FIN: El programa sale del while y la función termina aquí.

jugar()

import random

def jugar():
    print("🎮 ¡Bienvenido al juego de Piedra, Papel o Tijera! 🎮")
    print("=" * 45)
    
    # DATOS INICIALES: Diccionarios para la interfaz y la lógica del juego.
    opciones = {1: "piedra", 2: "papel", 3: "tijera"}
    emojis = {1: "🪨", 2: "📄", 3: "✂️ "}
    
    # ----------------------------------------------------
    # ESTRUCTURA REPETITIVA PRINCIPAL (WHILE GRANDE)
    # Controla el rombo "¿Jugar de nuevo?" y permite que el juego se repita continuamente.
    repetir_juego = True 
    while repetir_juego: 
    # ----------------------------------------------------

        opcion_valida = False
        
        # ESTRUCTURA REPETITIVA INTERNA: Validar Entrada
        # Este bucle se repite hasta que el usuario ingrese una opción válida (1, 2 o 3).
        while not opcion_valida:

            print("\n🎯 --- Menú --- 🎯") 
            print("(1) Piedra  🪨")
            print("(2) Papel   📄")
            print("(3) Tijera  ✂️")

            try:
                opcion_usuario = int(input("\n👉 Elige una opcion: "))

                if opcion_usuario in opciones:
                    opcion_valida = True
                    # La variable opcion_usuario guarda el NÚMERO entero para la lógica.
                    print(f"\n🙋 Has elegido: {emojis[opcion_usuario]} {opciones[opcion_usuario]}")
                else:
                    print("❌ Opcion no valida. Intente de nuevo.")
            except ValueError:
                # MANEJO DE EXCEPCIONES: Captura errores si el usuario ingresa texto (Robustez).
                print("⚠️  Por favor, ingresa un numero valido")

        # ESTRUCTURA SECUENCIAL: Generar el turno de la computadora
        opcion_computador = random.randint(1, 3) 
        print(f"🤖 La computadora ha elegido: {emojis[opcion_computador]} {opciones[opcion_computador]}")
        
        print("\n" + "=" * 30)
        print("⚔️  ¡RESULTADO! ⚔️")
        print("=" * 30)

        # ESTRUCTURA SELECTIVA: Determinar el ganador
        # Compara la elección del usuario vs la computadora usando decisiones anidadas.
        
        if opcion_usuario == opcion_computador:
            print("🤝 ¡EMPATE! 🤝")
            
        # LÓGICA DE VICTORIA: Piedra(1) vence Tijera(3), Papel(2) vence Piedra(1), Tijera(3) vence Papel(2)
        elif (opcion_usuario == 1 and opcion_computador == 3) or \
             (opcion_usuario == 2 and opcion_computador == 1) or \
             (opcion_usuario == 3 and opcion_computador == 2):
            print("🏆🎉 ¡GANASTE! 🎉🏆")
            
        else:
            # Si no es empate ni gane, el resultado es pérdida.
            print("😢💔 ¡PERDISTE! 💔😢")
            
        # ----------------------------------------------------
        # CONTROL DEL CICLO PRINCIPAL: Pregunta si desea jugar de nuevo
        
        respuesta_valida = False
        # Bucle para validar que la respuesta sea solo 's' o 'n' (Estructura repetitiva interna)
        while not respuesta_valida:
            respuesta = input("\n🔄 ¿Quieres jugar de nuevo? (s/n): ")
            
            if respuesta == 'n':
                # Detiene el bucle grande (repetir_juego = False)
                repetir_juego = False 
                respuesta_valida = True
                print("\n" + "=" * 45)
                print("👋 ¡Gracias por jugar! Hasta pronto 🌟")
                print("=" * 45)
            elif respuesta == 's':
                # Permite que el bucle grande se repita
                respuesta_valida = True 
                print("\n🔥 ¡Vamos de nuevo! 🔥")
            else:
                print("❌ Respuesta no válida. Por favor, usa 's' o 'n'.")
                
    # ----------------------------------------------------
    # FIN DEL PROGRAMA: Sale del bucle while cuando el usuario elige 'n'.
jugar()

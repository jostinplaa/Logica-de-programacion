import random

def jugar():
    print("👋 ¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("-" * 40)
    
    # Diccionario para convertir números a texto
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    
    # Variable de control para el Bucle Principal (Estructura Repetitiva)
    jugar_de_nuevo = True
    
    while jugar_de_nuevo:
        
        print("\n--- Menú ---")
        print("(1) Piedra")
        print("(2) Papel")
        print("(3) Tijera")
        
        # --- Validación de Entrada (Manejo de Errores e Innovación) ---
        opcion_valida = False
        while not opcion_valida:
            try:
                opcion_usuario_num = int(input("Elige tu opción (1, 2 o 3): "))
                if opcion_usuario_num in opciones:
                    opcion_valida = True
                    opcion_usuario = opciones[opcion_usuario_num]
                else:
                    print("⚠️ Opción inválida. Elige 1, 2 o 3.")
            except ValueError:
                # Si el usuario escribe texto, el programa no falla (Try-Except)
                print("⚠️ Error: Debes ingresar un NÚMERO.")

        # Generar opción del computador
        opcion_computador_num = random.randint(1, 3)
        opcion_computador = opciones[opcion_computador_num]

        print(f"\n✨ Tú: {opcion_usuario} vs 🤖 PC: {opcion_computador}")

        # --- Lógica de Decisión (Estructuras Selectivas) ---
        
        # 1. ¿Es Empate?
        if opcion_usuario == opcion_computador:
            print("🤝 ¡Es un EMPATE!")
        else:
            # 2. Decisión Anidada: ¿Usuario Gana?
            if (opcion_usuario == "Piedra" and opcion_computador == "Tijera") or \
               (opcion_usuario == "Papel" and opcion_computador == "Piedra") or \
               (opcion_usuario == "Tijera" and opcion_computador == "Papel"):
                print("🥳 ¡GANASTE!")
            else:
                print("😢 PERDISTE.")
        
        # --- Pregunta de Reinicio (Validación Estricta) ---
        respuesta_valida = False
        while not respuesta_valida:
            resp = input("\n¿Jugar de nuevo? (s/n): ").lower()
            if resp == 's' or resp == 'n':
                respuesta_valida = True
                if resp == 'n':
                    jugar_de_nuevo = False
                    print("¡Gracias por jugar! Fin del programa.")
            else:
                print("❌ Por favor, responde solo 's' o 'n'.")

# Punto de entrada del programa
if __name__ == "__main__":
    jugar()
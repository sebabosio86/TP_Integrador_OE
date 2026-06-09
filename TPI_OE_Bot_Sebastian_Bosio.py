import csv

def ejecutar_bot():
    
    # Carga de datos desde el archivo CSV a una lista de diccionarios
    filas = []

    # Lectura del CSV
    with open("base_datos.csv", mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        # Almacena cada fila como un diccionario en la lista
        for fila in lector:
            filas.append(fila)
    
    # Mensaje de bienvenida
    print("="*50)
    print("    ¡Hola! Bienvenido al Gestor de Vacaciones.")
    print("="*50)
    
    # Inicialización de la máquina de estados
    '''
    El bot sigue una estructura de máquina de estados. Cada estado representa una etapa del proceso de solicitud de vacaciones.
    El flujo es el siguiente:
    1. VALIDAR_DNI: El bot solicita al usuario que ingrese su DNI y verifica si existe en la base de datos.
    2. VERIFICAR_SALDO: El bot solicita al usuario que ingrese la cantidad de días que desea solicitar.
    3. PROCESAR_SOLICITUD: El bot procesa la solicitud restando los días solicitados del saldo disponible del empleado
    y actualiza el archivo CSV con el nuevo saldo.
    4. FIN_PROCESO: El proceso finalizó, el bot muestra un mensaje de despedida y termina la ejecución.
    '''
    estado = "VALIDAR_DNI"  # Estado inicial
    
    # Variables de almacenamiento temporal de datos
    dni_usuario = ""
    empleado_encontrado = None
    dias_disponibles = 0
    dias_solicitados = 0

    # Bucle de ejecución de la máquina de estados
    while estado != "FIN_PROCESO":
        
        # Validar DNI del usuario
        if estado == "VALIDAR_DNI":
            # Validación del DNI, asegurar que el usuario ingrese un número válido
            while True:
                try:
                    # Solicitud de entrada al usuario (Camino Feliz)
                    dni_usuario = int(input("\nUsuario: Ingrese su número de DNI (sin puntos): "))
                    break # Sale del bucle si la entrada es válida

                except ValueError:
                    print("Bot: Entrada no válida. Por favor, ingrese un número de DNI sin puntos.\n")
                    continue  # Repite el ciclo para solicitar nuevamente el DNI 
                
            
            dni_usuario = str(dni_usuario)  # Convertir a string para comparación con CSV

            # Verificar si el DNI existe en la base de datos
            for empleado in filas:
                if empleado["dni"] == dni_usuario:
                    empleado_encontrado = empleado
                    break
            
            # Si encontró el empleado, muestra su nombre y días disponibles, sino muestra error
            if empleado_encontrado:
                nombre_empleado = empleado_encontrado["nombre"]
                dias_disponibles = int(empleado_encontrado["dias_disponibles"])
                
                print(f"\nBot: DNI Verificado. Empleado/a: {nombre_empleado}")
                print(f"Bot: Tiene {dias_disponibles} días de vacaciones disponibles.\n")
                
                # Verificar si el saldo de vacaciones es 0
                if dias_disponibles == 0:
                    print("Bot: ERROR. No tiene días de vacaciones disponibles. No puedes iniciar solicitudes.")
                    estado = "FIN_PROCESO"

                else:
                    estado = "VERIFICAR_SALDO" # Avanza al siguiente paso

            else:
                # Camino Infeliz: DNI no encontrado
                print("Bot: ERROR. El DNI ingresado no pertenece a un empleado de la empresa. Intente de nuevo.\n")
                # Se mantiene en el estado actual


        # verificar saldo de días solicitados con los disponibles
        elif estado == "VERIFICAR_SALDO":
            while True:
                try:
                    # Solicitud de cantidad de días a solicitar
                    dias_solicitados = int(input("Usuario: Ingrese la cantidad de días que desea tomarse: "))
                    break  # Sale del bucle si la entrada es válida

                except ValueError:
                    print("Bot: ERROR. Entrada no válida. Por favor, ingrese un número entero.\n")
                    continue  # Repite el ciclo para solicitar nuevamente la cantidad de días
            
            if dias_solicitados <= 0:
                print("Bot: ERROR. La cantidad de días debe ser mayor a 0.\n")
                continue
                
            # Validación de negocio: Comparar pedido contra saldo del CSV
            if dias_solicitados <= dias_disponibles:
                # Cambio de estado: Solicitud válida, se procesa la solicitud
                estado = "PROCESAR_SOLICITUD"

            else:
                # Camino Infeliz: Pide más de lo que tiene
                print(f"Bot: ERROR. No puedes solicitar {dias_solicitados} días. Tu saldo actual es de {dias_disponibles} días. Intenta una cantidad menor.\n")
                # Se mantiene en VERIFICAR_SALDO

        # Procesar la solicitud y actualizar el CSV
        elif estado == "PROCESAR_SOLICITUD":
            # Se resta la cantidad de días solicitados al saldo del empleado
            nuevo_saldo = dias_disponibles - dias_solicitados

            # Actualización del saldo en la lista. EL tip[o de dato cambia de entero a sting (para guardarlo en el CSV) 
            empleado_encontrado["dias_disponibles"] = str(nuevo_saldo)
            
            # Guardar los cambios en el archivo CSV (sobrescribe el archivo con los nuevos datos)
            campos = ["dni", "nombre", "dias_disponibles"]
            with open("base_datos.csv", mode="w", encoding="utf-8", newline="") as archivo:

                # Se escribe el encabezado
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                # Se escriben las filas actualizadas
                escritor.writerows(filas)
                    
            print("\n--------------------------------------------------")
            print(f"Bot: ¡Solicitud procesada con éxito!")
            print(f"Bot: Se han descontado {dias_solicitados} días de su saldo.")
            print(f"Bot: Tu nuevo saldo disponible es de {nuevo_saldo} días.")
            print("--------------------------------------------------")
            
            # Cambio de estado: Fin de la ejecución
            estado = "FIN_PROCESO"

    print("\nBot: Proceso finalizado correctamente. ¡Gracias por usar el Gestor de Vacaciones!")

# Llamada a la función principal para iniciar el bot
ejecutar_bot()
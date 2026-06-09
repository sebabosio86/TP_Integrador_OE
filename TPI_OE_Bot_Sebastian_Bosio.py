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

    estado = "VALIDAR_DNI"

    while estado != "FIN_PROCESO":
        if estado == "VALIDAR_DNI":
            # Acá se pide el DNI y comprueba si existe

            estado = "VERIFICAR_SALDO"  # Cambia de estado
            
            
        elif estado == "VERIFICAR_SALDO":
            # Comprueba saldo, si es 0 termina el proceso, sino pide los días a solicitar
            estado = "PROCESAR_SOLICITUD"
            
        elif estado == "PROCESAR_SOLICITUD":
            # Procesa la solicitud, actualiza el CSV y muestra mensaje de éxito
            estado = "FIN_PROCESO"
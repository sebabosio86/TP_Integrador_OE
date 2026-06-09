
# Esqueleto del Bot de Vacaciones 

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
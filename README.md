# TP_Integrador_OE
Trabajo Práctico Integrador - Organización Empresarial 2026

Alumno: Sebastián Ezequiel Bosio
Comisión 17

# Gestor de Vacaciones

Bot desarrollado en Python que permite a los empleados consultar y solicitar días de vacaciones mediante una máquina de estados. La información de los empleados y sus días disponibles se almacena en un archivo CSV.

### Funcionalidades:

• Verificación de identidad mediante DNI.
• Consulta automática del saldo de días disponibles.
• Solicitud de días de vacaciones.
• Validación de disponibilidad de saldo.
• Actualización automática de la base de datos.
• Gestión de errores y validación de entradas.

### Flujo de uso:

1. Ingreso de DNI:
El bot solicita al usuario su número de DNI y verifica que exista en la base de datos.
2. Consulta de saldo:
Si el DNI es válido, el bot informa el nombre del empleado y la cantidad de días de vacaciones disponibles.
3. Solicitud de vacaciones:
El usuario ingresa la cantidad de días que desea solicitar.
4. Validación:
El sistema verifica que la cantidad ingresada sea válida y que no supere el saldo disponible.
5. Procesamiento:
Si la solicitud es aprobada, el sistema actualiza el saldo de vacaciones y guarda los cambios en la base de datos.

### El bot contempla los siguientes casos de error (camino infeliz):

• DNI inexistente.
• DNI ingresado con formato incorrecto.
• Empleado sin días de vacaciones disponibles.
• Cantidad de días menor o igual a cero.
• Solicitud superior al saldo disponible.
• Ingreso de texto cuando se espera un valor numérico.




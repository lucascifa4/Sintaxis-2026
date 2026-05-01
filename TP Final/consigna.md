# Consigna: Diseñar e implementar una aplicación que permita a una Agencia de Turismo gestionar la información relacionada con la venta de excursiones y servicios, utilizando los Tipos Abstractos de Datos (TADs) adecuados. Cada venta debe registrar: Código de Excursión, Nombre del Servicio, Tipo de Actividad (ej: Aventura, Cultural, Relax), Operador Turístico, Plan de Pago, Importe, Fecha y Hora de la venta. El sistema deberá contar con un menú interactivo para realizar las siguientes operaciones:

Puntos a resolver

a
1. Registro de Nuevas Ventas:
Implementar la opción para ingresar nuevas ventas de servicios, cargando todos los datos requeridos para cada registro.

b
2. Gestión de Registros Específicos:
• Modificación: Permitir la modificación de una venta existente, identificada por el Nombre del Servicio.
• Cancelación: Permitir la eliminación de una venta a partir del Código de Excursión.

c
3. Visualización Completa de Ventas:
Mostrar un listado detallado de todas las ventas registradas, incluyendo todos los datos asociados a cada servicio vendido.

d
4. Informes Financieros y Actualizaciones:
• Total por Operador: Generar un informe con el total recaudado por cada Operador Turístico, basándose en las ventas realizadas.
• Bonificación Masiva: Aplicar un descuento del 20% en el importe de las ventas correspondientes a un Plan de Pago específico (ej: "Previaje", "Efectivo"), ingresado por el usuario.

e
5. Depuración por Actividad y Fecha Reciente:
Eliminar todas las ventas del último mes que correspondan a servicios cuya Tipo de Actividad coincida con la especificada por el usuario (útil para limpiar registros de actividades de temporada que ya cerraron).

f
6. Filtrado de Operador y Resumen de Caja Diario:
• Cola de Operador: Generar una Cola con el Nombre del Servicio, Tipo de Actividad y Fecha de Venta de los servicios vendidos por un Operador Turístico determinado, y mostrarla en pantalla.
• Corte de Caja Parcial: Dada una hora específica, listar la cantidad de servicios vendidos y el monto total recaudado en el día actual hasta dicha hora.

g
Agregar validaciones
Deben agregar las validaciones necesarias para que el programa no rompa en tiempo de ejecución y al ingresar valores en los imputs.
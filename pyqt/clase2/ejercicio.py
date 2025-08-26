# -----------------------------------------------------------------------------
# Ejercicio extra: Agregar un campo de fecha de nacimiento y validación avanzada
# -----------------------------------------------------------------------------
# Teoría:
# - QDateEdit permite seleccionar una fecha desde un calendario.
# - Puedes obtener la fecha seleccionada con .date().toString() o .date().year(), etc.
#
# Consigna:
# - Agrega un QLabel "Fecha de nacimiento:" y un QDateEdit al lado, usando el grid.
# - Al hacer clic en "Registrarse", valida que la fecha no sea posterior a hoy y que el usuario tenga al menos 13 años.
# - Si la validación falla, muestra un mensaje de error; si es correcta, muestra un mensaje de éxito.
#
# Pista: Usa QDate.currentDate() para comparar fechas.

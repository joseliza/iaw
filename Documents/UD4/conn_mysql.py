import pymysql

# Conexión a la base de datos
conexion = pymysql.connect(
    host="10.3.29.20",
    port=33060,
    user="root",
    password="usuario",
    database="agenda_db"
)

try:
    # Crear el cursor manualmente
    mi_cursor = conexion.cursor()
    
    # Ejecutar la consulta
    mi_cursor.execute("SELECT * FROM agenda_db.contactos")
    resultados = mi_cursor.fetchall()
    
    # Mostrar resultados
    print(type(resultados))  # Verificar el tipo de resultados
    print(resultados)        # Verificar el contenido
finally:
    # Asegurar el cierre de recursos
    mi_cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión


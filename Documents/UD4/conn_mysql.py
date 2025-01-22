import pymysql

# Conexión a la base de datos
conexion = pymysql.connect(
    host="IP remota",
    port=33060,
    user="admin",
    password="usuario",
    database="agenda_db"
)

try:
    # Crear el cursor manualmente
    cursor = conexion.cursor()
    
    # Ejecutar la consulta
    cursor.execute("SELECT * FROM agenda_db.contactos")
    resultados = cursor.fetchall()
    
    # Mostrar resultados
    print(type(resultados))  # Verificar el tipo de resultados
    print(resultados)        # Verificar el contenido
finally:
    # Asegurar el cierre de recursos
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión


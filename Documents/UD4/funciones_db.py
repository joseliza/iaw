# Importación de módulos
import os
import pymysql

# Parámetros de conexión a la base de datos
HOST = ""
PORT = 
USER = ""
PASSWORD = ""
DATABASE = "agenda_db"

# Mostrar contactos
def mostrar_agenda(conn):
    borra_pantalla()
    mi_cursor = conn.cursor()
    mi_cursor.execute("SELECT * FROM contactos")
    resultados = mi_cursor.fetchall()
    for fila in resultados:
        print(f"Nombre: {fila[1]}, Teléfono: {fila[2]}")
    input("Pulsa una tecla para continuar...")


def agregar_contacto(conn):
    pass


def buscar_contacto(conn):
    pass


def eliminar_contacto(conn):
    pass

    
def borra_pantalla():
    if os.name == 'posix':
        os.system('clear')  # Limpiar la pantalla en sistemas Unix
    elif os.name == 'nt':
        os.system('cls')  # Limpiar la pantalla en sistemas Windows

# Menú de opciones
def menu():
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, database=DATABASE)
    while True:
        borra_pantalla()
        print("\n=== MENÚ ===")
        print("1. Mostrar contactos")
        print("2. Agregar contacto")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        print("=============")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_agenda(conn)
        elif opcion == "2":
            agregar_contacto(conn)
        elif opcion == "3":
            buscar_contacto(conn)
        elif opcion == "4":
            eliminar_contacto(conn)
        elif opcion == "5":
            print("Saliendo de la agenda...")
            conn.close()
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
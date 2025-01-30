# Importación de módulos
import os
import pymysql

# Parámetros de conexión a la base de datos (Ésta es la del servidor ProxMox. 
# Cambia los valores para conectarte a tu base de datos local)
HOST = "10.3.29.20"
PORT = 33060 
USER = "user_app_employees"
PASSWORD = "usuario"
DATABASE = "employees"

# Mostrar contactos
def mostrar_empleado(conn):
    borra_pantalla()
    mi_cursor = conn.cursor()
    mi_cursor.execute("SELECT * FROM employees")
    resultados = mi_cursor.fetchall()
    for fila in resultados:
        print(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}, {fila[5]}")
    input("Pulsa una tecla para continuar...")


def agregar_empleado(conn):
    pass


def buscar_empleado(conn):
    borra_pantalla()
    cod = input("Introduce el código del empleado: ")
    mi_cursor = conn.cursor()
    mi_cursor.execute("SELECT * FROM employees where emp_no = %s", (cod))
    resultados = mi_cursor.fetchall()
    for fila in resultados:
        print(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}, {fila[4]}, {fila[5]}")
    input("Pulsa una tecla para continuar...")


def eliminar_empleado(conn):
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
        print("\n=== MENÚ APP EMPLOYEES ===")
        print("1. Mostrar empleados")
        print("2. Agregar empleado") # Sólo funcional en tu base de datos local
        print("3. Buscar empleado")
        print("4. Eliminar empleado") # Sólo funcional en tu base de datos local
        print("5. Salir")
        print("============================")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_empleado(conn)
        elif opcion == "2":
            agregar_empleado(conn)
        elif opcion == "3":
            buscar_empleado(conn)
        elif opcion == "4":
            eliminar_empleado(conn)
        elif opcion == "5":
            print("Saliendo de la aplicación...")
            conn.close()
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
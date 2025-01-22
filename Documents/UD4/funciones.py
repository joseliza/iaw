import os

# Crear una agenda con 20 contactos
agenda = {
    "Ana": "612",
    "Luis": "622",
    "Pedro": "632",
    "Marta": "642",
    "Juan": "652",
    "Lucía": "662",
    "Carlos": "672",
    "Sofía": "682",
    "Elena": "692",
    "Miguel": "602",
    "Laura": "612",
    "Javier": "622",
    "Paula": "632",
    "Diego": "642",
    "Clara": "652",
    "Alberto": "662",
    "María": "672",
    "Raúl": "682",
    "Carmen": "692",
    "Tomás": "602"
}

def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def mostrar_contactos():
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono
    print(f"\n{nombre} ha sido agregado a la agenda.")

def buscar_contacto():
    nombre = input("Nombre: ")
    if nombre in agenda:
        print(f"\n{nombre}: {agenda[nombre]}")
    else:
        print(f"\n{nombre} no está en la agenda.")

def eliminar_contacto():
    nombre = input("Nombre: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"\n{nombre} ha sido eliminado de la agenda.")
    else:
        print(f"\n{nombre} no está en la agenda.")

def menu():
    while True:
        borrar_pantalla()
        print("\n=== AGENDA ===")
        print("1. Mostrar contactos")
        print("2. Agregar contacto")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            borrar_pantalla()
            print("\n=== CONTACTOS ===")
            mostrar_contactos()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "2":
            borrar_pantalla()
            print("\n=== AGREGAR CONTACTO ===")
            agregar_contacto()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "3":
            borrar_pantalla()
            print("\n=== BUSCAR CONTACTO ===")
            buscar_contacto()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "4":
            borrar_pantalla()
            print("\n=== ELIMINAR CONTACTO ===")
            eliminar_contacto()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "5":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
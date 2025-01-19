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

while True:
    print("\n=== AGENDA ===")
    print("1. Mostrar contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Mostrar contactos")
    elif opcion == "2":
        print("Agregar contacto")
    elif opcion == "3":
        print("Buscar contacto")
    elif opcion == "4":
        print("Eliminar contacto")
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
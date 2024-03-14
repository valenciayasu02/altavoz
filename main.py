bandas = []

opcion = 0
while opcion != 5:
    print("***Festival Altavoz***")
    print("**********************")
    print("1. Agregar banda.")
    print("2. Ver el cartel del festival")
    print("3. Buscar banda")
    print("4. Modificar banda")
    print("5. Finalizar")

    opcion = int(input("Digite una opción: "))

    if opcion == 1:
        banda = {}  # Definir una nueva banda como un diccionario vacío
        banda["id"] = int(input("Digite el id: "))
        banda["nombre"] = input("Nombre: ")
        banda["genero"] = input("Género: ")
        banda["costo"] = int(input("Costo: "))
        print(banda)
        bandas.append(banda)  # Agregar el diccionario de la banda a la lista de bandas

    elif opcion == 2:
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar['id']} -- {bandaAuxiliar['nombre']}")

    elif opcion == 3:
        bandaBuscada = input("Digite el nombre de la banda que desea buscar: ")
        encontrada = False
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"] == bandaBuscada:
                print("¡La encontraste!")
                encontrada = True
                break  # Salir del bucle una vez que se encuentra la banda
        if not encontrada:
            print("No la encontraste")

    elif opcion == 4:
        pass  # Aquí se debe implementar la lógica para modificar una banda

    elif opcion == 5:
        pass  # Aquí se puede agregar lógica de finalización si es necesario

    else:
        print("Opción inválida")

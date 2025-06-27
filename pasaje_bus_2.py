asientos_disponibles = [1, 2, 3, 4, 5]
registro_pasajes = {}
def mostrar_menu():
    print("\n***** SISTEMA DE PASAJES PASAJEBUS *****")
    print("1.- Ver asientos disponibles")
    print("2.- Comprar pasaje")
    print("3.- Ver pasajeros registrados")
    print("4.- Salir")
while True:
    mostrar_menu()
     opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(f"Asientos disponibles: {asientos_disponibles}")
    elif opcion == "2":
        if len(asientos_disponibles) == 0:
            print("No hay asientos disponibles.")
            continue
        rut = input("Ingrese su RUT: ")
        if rut in registro_pasajes:
            print("Este RUT ya tiene un pasaje registrado.")
        
        try:
            asiento = int(input("Ingrese número de asiento a comprar: "))
            if asiento in asientos_disponibles:
                registro_pasajes[rut] = asiento
                asientos_disponibles.remove(asiento)
                print(f"Asiento {asiento} comprado con éxito.")
            else:
                print("Asiento no disponible.")
        except ValueError:
            print("Debe ingresar un número válido.")

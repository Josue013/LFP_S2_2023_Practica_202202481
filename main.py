import os
import producto
from cargar import cargarArchivoInv, cargarArchivoMov
from inventario import InventoryManager

def main():
    inventory_manager = InventoryManager()
    print("=====================================================")
    print("        Bienvenido al sistema de inventario.         ")
    print("=====================================================")
    print("")
    while True:
        print("\nMenú Principal:")
        print("1. Cargar Inventario Inicial")
        print("2. Cargar Instrucciones de Movimientos")
        print("3. Crear Informe de Inventario")
        print("4. Salir")
        print("=====================================================")
        print("")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listaDatos = [] 
            cargarArchivoInv(listaDatos)
            
            # Recorrer cada linea del archivo
            for linea in listaDatos:
                partes = linea.strip().split(' ')  
                accion = partes[0] 
                if accion == "crear_producto": 
                    _, data = linea.split(' ', 1) 
                    name, quantity, price, location = data.split(';') 
                    inventory_manager.crear_producto(name, int(quantity), float(price), location)
            print("Se cargó exitosamente el inventario inicial.")

        elif opcion == "2":
            listaDatos = []
            cargarArchivoMov(listaDatos)
            
            # Recorrer cada linea del archivo
            for linea in listaDatos: 
                partes = linea.strip().split()  # Dividir por partes o espacios
                accion = partes[0] 

                # Si la acción es crear_producto
                if accion == "agregar_stock":
                    accion_partes = linea.split(' ', 1)[1].split(';') #dividir por espacio y luego por ;
                    name = accion_partes[0]
                    quantity = int(accion_partes[1])
                    location = accion_partes[2]
                    inventory_manager.agregar_stock(name, quantity, location)

                # Si la acción es vender_producto    
                elif accion == "vender_producto":
                    accion_partes = linea.split(' ', 1)[1].split(';')  #dividir por espacio y luego por ;
                    name = accion_partes[0]
                    quantity = int(accion_partes[1])
                    location = accion_partes[2]
                    inventory_manager.vender_producto(name, quantity, location)

            print("Cargadas exitosamente las instrucciones de movimientos.")
            

        elif opcion == "3":
            inventory_manager.generar_inventario("informe_inventario.txt")
            print("")
            print("Generado exitosamente el informe de inventario.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, Seleccione una opción válida.")

if __name__ == "__main__":
    main()
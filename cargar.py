import os
from producto import Producto

# Función para cargar el archivo .inv
def cargarArchivoInv(listaDatos):
    print("\nHa seleccionado cargar archivo .inv\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".inv":
            print("\nArchivo válido\n")
            break
        else:
            print("\nArchivo inválido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            listaDatos.append(linea.strip())

# Función para cargar el archivo .mov
def cargarArchivoMov(listaDatos):
    print("\nHa seleccionado cargar archivo .mov\n")
    ruta = input("Ingrese la ruta del archivo: ")

    while True:
        nombre, extension = os.path.splitext(ruta)
        if extension == ".mov":
            print("\nArchivo válido\n")
            break
        else:
            print("\nArchivo inválido\n")
            ruta = input("\nIngrese la ruta del archivo: ")

    with open(ruta, "r") as archivo:
        for linea in archivo:
            listaDatos.append(linea.strip())
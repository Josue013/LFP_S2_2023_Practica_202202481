from producto import Producto

class InventoryManager:
    def __init__(self):
        self.inventario = [] #lista de productos
    
    # Función para encontrar un producto en el inventario
    def Encontrar_producto(self, name, location):
        for product in self.inventario:
            if product.name == name and product.location == location:
                return product
        return None

    # Función para crear un producto
    def crear_producto(self, name, quantity, price, location):
        producto_existente = self.Encontrar_producto(name, location)
        if producto_existente:
            print(f"El producto '{name}' ya existe en la ubicación :'{location}'.")
            return

        product = Producto(name, quantity, price, location)
        self.inventario.append(product)

    # Función para agregar stock
    def agregar_stock(self, name, quantity, location):
        product = self.Encontrar_producto(name, location)
        if not product:
            print(f"El producto '{name}' no existe en la ubicación :'{location}'.")
            return

        product.quantity += quantity #se suma la cantidad de productos

    # Función para vender un producto
    def vender_producto(self, name, quantity, location):
        product = self.Encontrar_producto(name, location)
        if not product:
            print(f"El producto '{name}' no existe en la ubicación :'{location}'.")
            return

        if product.quantity >= quantity:
            product.quantity -= quantity #se resta la cantidad de productos
        else:
            print(f"No hay suficiente cantidad de '{name}' en la ubicación :'{location}'.")

    # Función para generar el informe de inventario
    def generar_inventario(self, filename):
        with open(filename, "w") as file:
            file.write("Informe de Inventario:\n")
            file.write("{:<15} {:<10} {:<20} {:<15} {}\n".format("Producto", "Cantidad", "Precio Unitario", "Valor Total", "Ubicacion"))

            for product in self.inventario:
                total_value = product.quantity * product.price
                file.write("{:<15} {:<10} ${:<19} ${:<14} {}\n".format(product.name, product.quantity, product.price, round(total_value,2), product.location))


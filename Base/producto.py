class Producto:
    def __init__(self, producto_animal, nombre, cantidad, precio):
        self._producto_animal = producto_animal
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    @property
    def producto_animal(self):
        return self._producto_animal

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    # Setters
    @producto_animal.setter
    def producto_animal(self, producto_animal):
        self._producto_animal = producto_animal

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Método para mostrar detalles
    def mostrar_detalles(self):
        print("Información del producto:")
        print(f"Producto animal: {self._producto_animal.especie}")
        print(f"Nombre: {self._nombre}")
        print(f"Cantidad: {self._cantidad}")
        print(f"Precio en pesos: {self._precio}")
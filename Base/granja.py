class Granja:
    def __init__(self, propietario="No hay dueño", ubicacion="No hay ubicacion", nombre="", tamaño=230, produccion=""):
        self._propietario = propietario
        self._ubicacion = ubicacion
        self._nombre = nombre
        self._tamaño = tamaño
        self._produccion = produccion

    # Getters
    @property
    def propietario(self):
        return self._propietario

    @property
    def ubicacion(self):
        return self._ubicacion

    @property
    def nombre(self):
        return self._nombre

    @property
    def tamaño(self):
        return self._tamaño

    @property
    def produccion(self):
        return self._produccion

    # Setters
    @propietario.setter
    def propietario(self, propietario):
        self._propietario = propietario

    @ubicacion.setter
    def ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    @produccion.setter
    def produccion(self, produccion):
        self._produccion = produccion

    # Método para mostrar detalles
    def mostrar_detalles(self):
        print(f"Propietario: {self._propietario}")
        print(f"Ubicación: {self._ubicacion}")
        print(f"Nombre: {self._nombre}")
        print(f"Tamaño: {self._tamaño}")
        print(f"Producción: {self._produccion}")
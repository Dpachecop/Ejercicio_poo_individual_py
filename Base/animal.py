class Animal:
    def __init__(self, id, especie, cantidad, edad, peso_kg):
        self._id = id
        self._especie = especie
        self._cantidad = cantidad
        self._edad = edad
        self._peso_kg = peso_kg

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def especie(self):
        return self._especie

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def edad(self):
        return self._edad

    @property
    def peso_kg(self):
        return self._peso_kg

    # Setters
    @id.setter
    def id(self, id):
        self._id = id

    @especie.setter
    def especie(self, especie):
        self._especie = especie

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @peso_kg.setter
    def peso_kg(self, peso_kg):
        self._peso_kg = peso_kg

    
    def mostrar_detalles(self):
        print("Información del animal:")
        print(f"ID del animal: {self._id}")
        print(f"Especie: {self._especie}")
        print(f"Cantidad: {self._cantidad}")
        print(f"Edad: {self._edad}")
        print(f"Peso en kg: {self._peso_kg}")
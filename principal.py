
from Base.granja import Granja
from Base.animal import Animal
from Base.producto import Producto

def main():

   
    granja = Granja("Señora Maria", "Zona rosa", "Granja La Esperanza", 314, "Carnívora")
    animal = Animal(342, "Porcina", 50, 2, 50)
    producto = Producto(animal, "Carne de cerdo", 50, 8000)

    print("       Código: 750241006")
    print("  Estudiante: Daniel Pacheco Perez")
    print("**************************************")
    print("Información de la granja:")
    
    granja.mostrar_detalles()
    print("\nInformación del animal:")
    animal.mostrar_detalles()

    print("\nInformación del producto:")
    producto.mostrar_detalles()

if __name__ == "__main__":
    main()
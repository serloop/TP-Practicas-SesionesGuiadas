from app.tdas.persona import Persona
from app.tdas.libros.libro import Libro
from app.tdas.libros.libroCientifico import LibroCientifico
from app.tdas.libros.libroInfantil import LibroInfantil
import copy

if __name__ == "__main__":
    # Crear instancias de Persona
    persona1 = Persona("Paco", 9)
    persona2 = Persona("Sergio", 25)  # Persona adulta

    # Crear un libro base y probar su funcionalidad
    libro1 = Libro("El Hobbit", "J.R.R. Tolkien", 300)
    persona2.leer_libro(libro1)
    print("Libro1: ", libro1)

    # Crear un libro infantil y probar su funcionalidad
    libro_infantil = LibroInfantil("El Principito", "Antoine de Saint-Exupéry", 96, 10, True, True)
    print("Libro infantil: ", libro_infantil)

    # Agregar lector al libro infantil
    libro_infantil.agregar_lector(persona1)  # Edad inadecuada (9 años)
    libro_infantil.agregar_lector(persona2)  # Edad adecuada (25 años)

    # Crear libros científicos y probar su funcionalidad
    libro_cientifico1 = LibroCientifico("Física Cuántica", "Einstein", 500, "Física", "Avanzado")
    libro_cientifico2 = LibroCientifico("Relatividad General", "Einstein", 300, "Física", "Avanzado")
    print("Libro científico 1: ", libro_cientifico1)
    print("Libro científico 2: ", libro_cientifico2)

    # Probar la compra de los libros científicos según la experiencia de la persona
    persona2.leer_libro(libro_cientifico1)  # Sergio lee un libro científico
    resultado_compra1 = libro_cientifico1.comprar_libro(persona2)  # No tiene suficiente experiencia
    print(f"Resultado de la compra del libro científico 1: {resultado_compra1}")  # False

    persona2.leer_libro(libro_cientifico2)  # Sergio lee otro libro científico
    resultado_compra2 = libro_cientifico1.comprar_libro(persona2)  # Ahora puede comprar el libro
    print(f"Resultado de la compra del libro científico 1 después de leer más: {resultado_compra2}")  # True

    # Ejemplo de agregar una referencia solo en el libro científico
    libro_cientifico1.agregar_referencia(libro_cientifico2)

    listado_referencias = libro_cientifico1.get_referencias()

    print(f"Referencias en el libro científico 1: ")
    for referencia in libro_cientifico1.get_referencias():
        print("> ", referencia)

    # Usar type() para comparar tipos exactos
    print("libro_infantil es de tipo LibroInfantil? ", type(libro_infantil) is LibroInfantil)  # True
    print("libro_cientifico1 es de tipo LibroCientifico? ", type(libro_cientifico1) is LibroCientifico)  # True
    print("libro_cientifico1 es de tipo Libro? ", type(libro_cientifico1) is Libro)  # False, no es exactamente de tipo Libro

    # Usar isinstance() para verificar si un objeto es de una clase o una subclase
    print("libro_infantil es instancia de LibroInfantil? ", isinstance(libro_infantil, Libro))  # True, porque LibroInfantil hereda de Libro
    print("libro_cientifico1 es instancia de Libro? ", isinstance(libro_cientifico1, Libro))  # True
    print("libro_cientifico1 es instancia de LibroInfantil? ", isinstance(libro_cientifico1, LibroInfantil))  # False, no es una instancia de LibroInfantil

    # Usar issubclass() para verificar si una clase es una subclase de otra
    print("LibroCientifico es subclase de Libro? ", issubclass(LibroCientifico, Libro))  # True, LibroCientifico hereda de Libro
    print("LibroInfantil es subclase de Libro? ", issubclass(LibroInfantil, Libro))  # True, LibroInfantil hereda de Libro
    print("LibroInfantil es subclase de LibroCientifico? ", issubclass(LibroInfantil, LibroCientifico))  # False, no hay relación directa entre ellas

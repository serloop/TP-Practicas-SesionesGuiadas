from tdas.persona import Persona
from tdas.libro import Libro
import copy

if __name__ == "__main__":
    # Sergio agrega los libros manualmente y tiene libros en propiedad
    persona1 = Persona("Sergio", 50)
    libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1178)
    libro2 = Libro("1984", "George Orwell", 328)
    libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Sergio tiene libros en propiedad
    persona1.comprar_libro(libro1)
    persona1.comprar_libro(libro2)

    # Sergio ha leído algunos libros
    persona1.leer_libro(libro1)  # Libro que es de su propiedad
    persona1.leer_libro(libro3)  # Libro que no es de su propiedad

    # Listar los libros que Sergio tiene en propiedad
    persona1.listar_libros_propiedad()

    # Listar los libros que Sergio ha leído
    persona1.listar_libros_leidos()

    # Sergio utiliza un libro (relación de uso)
    persona1.hojear_libro(libro1)

    # Crear una copia superficial de Sergio
    persona_copia = copy.copy(persona1)

    # Modificar el objeto original (lista de libros en propiedad)
    print("\nModificando la lista de libros en propiedad de persona1...")
    libro_nuevo = Libro("El hobbit", "J.R.R. Tolkien", 310)
    persona1.comprar_libro(libro_nuevo)

    # Mostrar los datos del original y de la copia después de la modificación
    print("\nDatos de persona1 tras la modificación:")
    persona1.listar_libros_propiedad()

    print("\nDatos de persona_copia tras la modificación en persona1 (copia superficial):")
    persona_copia.listar_libros_propiedad()

    persona_deep = copy.deepcopy(persona1)
    persona_deep.comprar_libro(libro3)

    print("-----")
    persona1.listar_libros_propiedad()
    persona_deep.listar_libros_propiedad()
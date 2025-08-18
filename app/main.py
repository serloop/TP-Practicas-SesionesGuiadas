from tdas.persona import Persona
from tdas.libro import Libro
import copy

if __name__ == "__main__":
    # Crear una persona
    persona1: 'Persona' = Persona("Sergio", 50, altura=1.75, activo=True)
    libro1: 'Libro' = Libro("El señor de los anillos", "J.R.R. Tolkien", 1178)
    libro2: 'Libro' = Libro("1984", "George Orwell", 328)
    libro3: 'Libro' = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Agregar hobbies
    persona1.agregar_hobby("Leer")
    persona1.agregar_hobby("Viajar")

    # Sergio compra libros (agregación)
    persona1.comprar_libro(libro1)
    persona1.comprar_libro(libro2)

    # Sergio lee libros (asociación)
    persona1.leer_libro(libro1)  # De su propiedad
    persona1.leer_libro(libro3)  # No es de su propiedad

    # Sergio hojea un libro (uso)
    persona1.hojear_libro(libro2)

    # Mostrar datos generales (método mágico __str__ implícito)
    print("\n--- Información de persona1 ---")
    print(persona1)

    # Mostrar listas de libros
    print("\n--- Libros en propiedad ---")
    persona1.listar_libros_propiedad()

    print("\n--- Libros leídos ---")
    persona1.listar_libros_leidos()

    # Mostrar diario (composición)
    print(f"\nEl diario de {persona1.get_nombre()} es: {persona1.get_diario()}")

    # Mostrar si es mayor de edad
    print(f"\n¿{persona1.get_nombre()} es mayor de edad? {Persona.es_mayor_edad(persona1.get_edad())}")

    # Copia superficial
    persona_copia: 'Persona' = copy.copy(persona1)
    print("\n--- Copia superficial creada ---")
    print(persona_copia)

    # Modificar la copia original
    libro_nuevo: 'Libro' = Libro("El hobbit", "J.R.R. Tolkien", 310)
    persona1.comprar_libro(libro_nuevo)

    print("\n--- Después de modificar los libros de persona1 ---")
    print("persona1:")
    persona1.listar_libros_propiedad()

    print("persona_copia:")
    persona_copia.listar_libros_propiedad()  # Verás que también cambia, porque es copia superficial

    # Copia profunda
    persona_deep: 'Persona' = copy.deepcopy(persona1)
    persona_deep.comprar_libro(libro3)

    print("\n--- Después de copiar profundamente y modificar persona_deep ---")
    print("persona1:")
    persona1.listar_libros_propiedad()

    print("persona_deep:")
    persona_deep.listar_libros_propiedad()  # Ahora tienen libros distintos

    # Comparar edades entre dos personas
    persona2: 'Persona' = Persona("Lucía", 30)
    print(f"\n¿{persona1.get_nombre()} es mayor que {persona2.get_nombre()}? {persona1 > persona2}")

    # Cambiar algunos atributos
    persona2.set_altura(1.68)
    persona2.set_activo(True)
    persona2.agregar_hobby("Cocinar")
    persona2.cumplir_años()

    print("\n--- Información de persona2 actualizada ---")
    print(persona2)

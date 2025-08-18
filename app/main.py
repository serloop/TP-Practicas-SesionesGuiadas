from tdas.Persona import Persona

if __name__ == "__main__":
    # Crear dos instancias de Persona
    persona1: Persona = Persona("Ana", 25, 1.68, True, ['leer', 'escribir'])
    persona2: Persona = Persona("Juan", 30, 1.75, True, ['deporte', 'viajar'])

    # Usar __str__ para mostrar la información de las personas
    print(persona1)  # Salida: Persona(nombre=Ana, edad=25, altura=1.68, activo=True)
    print(persona2)  # Salida: Persona(nombre=Juan, edad=30, altura=1.75, activo=True)

    print("Datos de persona 1: ")
    # Mostrar atributos de persona1 individualmente
    print("- Especie: ", Persona.get_especie())  # Salida: Humano
    print("- Nombre: ", persona1.get_nombre())  # Salida: Ana
    print("- Edad: ", persona1.get_edad())  # Salida: 25
    print("- Altura: ", persona1.get_altura())  # Salida: 1.68
    print("- Activo: ", persona1.get_activo())  # Salida: True
    print("- Hobbies: ", persona1.get_hobbies())  # Salida: ['leer', 'escribir']

    # Usar es_mayor_edad (método estático)
    print("Con 25 años es mayor de edad? ", Persona.es_mayor_edad(25))  # Salida: True (porque 25 >= 18)
    print("Con 17 años es mayor de edad? ", Persona.es_mayor_edad(17))  # Salida: False (porque 17 < 18)

    # Aumentar la edad
    persona1.cumplir_años()

    # Consultar edad tras incrementarla
    print("Edad: ", persona1.get_edad())  # Salida: 26

    # Intento de cambio de altura con valor inválido
    print("Cambio de altura: ", persona1.set_altura(-1))  # Salida: False

    # Usar __gt__ para comparar las edades de persona1 y persona2
    if persona1 > persona2:
        print(f"{persona1.get_nombre()} es mayor que {persona2.get_nombre()}")
    else:
        print(f"{persona2.get_nombre()} es mayor que {persona1.get_nombre()}")  # Salida: Juan es mayor que Ana
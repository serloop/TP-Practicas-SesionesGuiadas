class Persona:
    # Definir los atributos de instancia permitidos mediante __slots__
    __slots__ = ['_nombre', '_edad', '_altura', '_activo', '_hobbies']
    
    especie: str = "Humano"            # Atributo de clase de tipo string

    def __init__(self, nombre: str, edad: int, altura: float, activo: bool, hobbies: list):
        self._nombre: str = nombre     # Atributo de instancia de tipo string
        self._edad: int = edad         # Atributo de instancia de tipo entero
        self._altura: float = altura   # Atributo de instancia de tipo real
        self._activo: bool = activo    # Atributo de instancia de tipo booleano
        self._hobbies: list = hobbies  # Atributo de instancia de tipo lista (compuesto)
    
    # Método de instancia
    def obtener_info(self) -> str:
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Altura: {self._altura}, Activo: {self._activo}"

    # Método de clase
    @classmethod
    def obtener_especie(cls) -> str:
        return f"La especie es {cls.especie}"

    # Método estático
    @staticmethod
    def es_mayor_edad(edad: int) -> bool:
        return edad >= 18

    # Método mágico __str__
    def __str__(self) -> str:
        return f"Persona(nombre={self._nombre}, edad={self._edad}, altura={self._altura}, activo={self._activo})"

    # Método mágico __gt__ para comparar la edad de dos personas
    def __gt__(self, otra_persona: 'Persona') -> bool:
        return self._edad > otra_persona._edad

if __name__ == "__main__":
    # Crear dos instancias de Persona
    persona1: Persona = Persona("Ana", 25, 1.68, True, ['leer', 'escribir'])
    persona2: Persona = Persona("Juan", 30, 1.75, True, ['deporte', 'viajar'])

    # Usar obtener_info (método de instancia)
    print(persona1.obtener_info())  # Salida: Nombre: Ana, Edad: 25, Altura: 1.68, Activo: True
    print(persona2.obtener_info())  # Salida: Nombre: Juan, Edad: 30, Altura: 1.75, Activo: True
    
    # Usar __str__ para mostrar la información de las personas
    print(persona1)  # Salida: Persona(nombre=Ana, edad=25, altura=1.68, activo=True)
    print(persona2)  # Salida: Persona(nombre=Juan, edad=30, altura=1.75, activo=True)

    # Usar obtener_especie (método de clase)
    print(Persona.obtener_especie())  # Salida: La especie es Humano

    # Usar es_mayor_edad (método estático)
    print(Persona.es_mayor_edad(25))  # Salida: True (porque 25 >= 18)
    print(Persona.es_mayor_edad(17))  # Salida: False (porque 17 < 18)

    # Usar __gt__ para comparar las edades de persona1 y persona2
    if persona1 > persona2:
        print(f"{persona1._nombre} es mayor que {persona2._nombre}")
    else:
        print(f"{persona2._nombre} es mayor que {persona1._nombre}")  # Salida: Juan es mayor que Ana
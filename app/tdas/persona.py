class Persona:
    # Definir los atributos de instancia permitidos mediante __slots__
    __slots__ = ['_nombre', '_edad', '_altura', '_activo', '_hobbies']
    
    especie: str = "Humano"            # Atributo de clase de tipo string

    def __init__(self, nombre: str, edad: int, altura: float = None, activo: bool = None, hobbies: list = None):
        self._nombre: str = nombre     # Atributo de instancia de tipo string
        self._edad: int = edad         # Atributo de instancia de tipo entero
        self._altura: float = altura   # Atributo de instancia de tipo real
        self._activo: bool = activo    # Atributo de instancia de tipo booleano
        
        # Manejo de hobbies
        if hobbies is None:
            self._hobbies: list = []  # Si no se pasan hobbies, asigna una lista vacía
        else:
            self._hobbies: list = hobbies  # Si se pasan hobbies, asigna la lista recibida
    
    # Getter para el atributo de clase "especie"
    @classmethod
    def get_especie(cls) -> str:
        return cls.especie

    # Setter para el atributo de clase "especie"
    @classmethod
    def set_especie(cls, nueva_especie: str) -> None:
        cls.especie = nueva_especie

    # Getter para el nombre
    def get_nombre(self) -> str:
        return self._nombre

    # Setter para el nombre
    def set_nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    # Getter para la edad
    def get_edad(self) -> int:
        return self._edad

    # Setter protegido para la edad con validación de valor positivo
    def _set_edad(self, nueva_edad: int) -> bool:
        if nueva_edad >= 0:
            self._edad = nueva_edad
            return True
        return False  # Edad negativa

    # Método público para cumplir años
    def cumplir_años(self) -> bool:
        return self._set_edad(self.get_edad() + 1)

    # Getter para la altura
    def get_altura(self) -> float:
        return self._altura

    # Setter para la altura con validación
    def set_altura(self, nueva_altura: float) -> bool:
        if nueva_altura > 0:
            self._altura = nueva_altura
            return True
        return False  # Altura inválida

    # Getter para el estado de actividad
    def get_activo(self) -> bool:
        return self._activo

    # Setter para el estado de actividad
    def set_activo(self, estado: bool) -> None:
        self._activo = estado

    # Getter para los hobbies
    def get_hobbies(self) -> list:
        return self._hobbies

    # Método para agregar un hobby
    def agregar_hobby(self, hobby: str) -> None:
        self._hobbies.append(hobby)

    # Método para eliminar un hobby
    def eliminar_hobby(self, hobby: str) -> bool:
        if hobby in self._hobbies:
            self._hobbies.remove(hobby)
            return True
        return False  # Hobby no encontrado

    # Método estático
    @staticmethod
    def es_mayor_edad(edad: int) -> bool:
        return edad >= 18

    # Método mágico __str__
    def __str__(self) -> str:
        if self._hobbies:
            hobbies_str = ", ".join(self._hobbies)  # Une los hobbies con coma y espacio
        else:
            hobbies_str = "No tiene hobbies"  # Mensaje si no hay hobbies

        return (f"Persona(nombre={self._nombre}, edad={self._edad}, altura={self._altura}, "
                f"activo={self._activo}, hobbies=[{hobbies_str}])")

    # Método mágico __gt__ para comparar la edad de dos personas
    def __gt__(self, otra_persona: 'Persona') -> bool:
        return self._edad > otra_persona._edad

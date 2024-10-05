from app.tdas.libro import Libro
import copy

class Persona:
    # Definir los atributos de instancia permitidos mediante __slots__
    __slots__ = ['_nombre', '_edad', '_altura', '_activo', '_hobbies', '_libros_leidos', '_libros_propiedad', '_diario']
    
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

        self._libros_leidos: list['Libro'] = [] # Relación de asociación
        self._libros_propiedad: list['Libro'] = []  # Relación de agregación
        self._diario: Libro = Libro(titulo="Diario", autor=self._nombre, paginas=0, propietario=self) # Relación de composición

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
    
    # Método estático
    @staticmethod
    def es_mayor_edad(edad: int) -> bool:
        return edad >= 18

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
    
    # Método para hojear un libro (relación de uso)
    def hojear_libro(self, libro: 'Libro') -> None:
        print(f"{self.get_nombre()} está ojeando {libro}")

    # Método getter para la lista de libros leídos
    def get_libros_leidos(self) -> list:
        return self._libros_leidos

    # Método para agregar un libro a la lista de libros leídos
    def leer_libro(self, libro: 'Libro') -> None:
        libro.agregar_lector(self)  # Asociar la persona con este libro
        self.get_libros_leidos().append(libro)

    # Método para listar los libros leídos por la persona
    def listar_libros_leidos(self) -> None:
        print(f"Libros leídos por {self.get_nombre()}:")
        for libro in self.get_libros_leidos():
            print("> ", libro)

    # Métodos getter/setter para la lista de libros en propiedad
    def get_libros_propiedad(self) -> list:
        return self._libros_propiedad

    # Método para comprar un libro (lo agrego a mi listado de libros en propiedad)
    def comprar_libro(self, libro: 'Libro') -> None:
        # Asociar el libro con esta persona como propietario: (delegación de métodos)
        libro.comprar_libro(self)
        self._libros_propiedad.append(libro)

    # Método para listar los libros en propiedad de la persona
    def listar_libros_propiedad(self) -> None:
        print(f"Libros en propiedad de {self.get_nombre()}:")
        for libro in self.get_libros_propiedad():
            print("> ", libro)
    
    # Método mágico __str__
    def __str__(self) -> str:
        if self._hobbies:
            hobbies_str = ", ".join(self._hobbies)
        else:
            hobbies_str = "No tiene hobbies"

        if self._libros_leidos:
            libros_leidos_str = ", ".join(libro.titulo for libro in self._libros_leidos)
        else:
            libros_leidos_str = "No ha leído libros"

        if self._libros_propiedad:
            libros_propiedad_str = ", ".join(libro.titulo for libro in self._libros_propiedad)
        else:
            libros_propiedad_str = "No tiene libros en propiedad"
        
        return (f"Persona(nombre={self._nombre}, edad={self._edad}, altura={self._altura}, "
                f"activo={self._activo}, hobbies=[{hobbies_str}], "
                f"libros_leidos=[{libros_leidos_str}], libros_propiedad=[{libros_propiedad_str}], "
                f"diario={self._diario.titulo})")

    # Método mágico __gt__ para comparar la edad de dos personas
    def __gt__(self, otra_persona: 'Persona') -> bool:
        return self._edad > otra_persona._edad
    
    # Método mágico __copy__ para la copia superficial
    def __copy__(self):
        # Crear una nueva instancia de Persona con la referencia a las mismas listas
        nueva_persona = Persona(
            self._nombre,
            self._edad,
            self._altura,
            self._activo,
            self._hobbies  # Aquí no se crea una copia nueva de la lista, se usa la misma referencia
        )

        nueva_persona._diario = copy.copy(self._diario)  # Invocación a copy por ser un objeto
        nueva_persona._libros_leidos = self._libros_leidos  # Se copia la referencia
        nueva_persona._libros_propiedad = self._libros_propiedad

        return nueva_persona

    def __deepcopy__(self, memo):
        nueva_persona = Persona(
            self._nombre,  # El nombre es inmutable (string), por lo que puede copiarse superficialmente
            self._edad,  # La edad es un entero (inmutable), también puede copiarse superficialmente
            self._altura,  # Altura es un float (inmutable)
            self._activo,  # Activo es un booleano (inmutable)
            copy.deepcopy(self._hobbies, memo),  # Se hace una copia profunda de la lista de hobbies
        )

        nueva_persona._diario = copy.deepcopy(self._diario, memo)
        nueva_persona._libros_leidos = copy.deepcopy(self._libros_leidos, memo)
        nueva_persona._libros_propiedad = copy.deepcopy(self._libros_propiedad, memo)

        return nueva_persona

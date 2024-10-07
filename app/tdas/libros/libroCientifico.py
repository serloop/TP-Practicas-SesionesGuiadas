from app.tdas.libros.libro import Libro

class LibroCientifico(Libro):
    def __init__(self, titulo: str, autor: str, paginas: int, campo_estudio: str, nivel_dificultad: str, propietario: 'Persona' = None):
        super().__init__(titulo, autor, paginas, propietario)
        
        # Nuevos atributos de la clase hija
        self._campo_estudio: str = campo_estudio
        self._nivel_dificultad: str = nivel_dificultad
        self._referencias: list[Libro] = []

    def get_campo_estudio(self) -> str: 
        return self._campo_estudio
    
    def get_nivel_dificultad(self) -> str:
        return self._nivel_dificultad   
    
    def get_referencias(self) -> list[Libro]:
        return self._referencias

    # Ejemplo de nueva funcionalidad añadida en la clase hija     
    def agregar_referencia(self, referencia: str) -> None:
        self._referencias.append(referencia)

    # Ejemplo de extensión de funcionalidad heredada
    def __str__(self) -> str:
        descripcion_basica = super().__str__()  # Llamada al método __str__ de la clase padre

        # Construcción de los detalles específicos del libro científico
        detalles_cientificos = (f"Campo de estudio: {self._campo_estudio}, "
                                f"Nivel de dificultad: {self._nivel_dificultad}")

        # Añadir las referencias si existen
        if self._referencias:
            referencias_str = ", ".join([referencia.get_titulo() for referencia in self._referencias])
            detalles_cientificos += f", Referencias: {referencias_str}"
        else:
            detalles_cientificos += ", No hay referencias"

        return f"{descripcion_basica} | {detalles_cientificos}"
    
    '''
    Sobrescritura completa del método:
        - Se añade funcionalidad para verificar si el propietario tiene experiencia previa con libros científicos
        - Se cambia el tipo de retorno, de None a bool
    '''
    def comprar_libro(self, propietario: 'Persona') -> bool:
        # Verificar si la persona ha leído libros científicos con anterioridad. 
        # Uso de isinstance() para verificar el tipo de libro
        libros_cientificos_leidos = []
        for libro in propietario.get_libros_leidos():
            if isinstance(libro, LibroCientifico):
                libros_cientificos_leidos.append(libro)
        
        if len(libros_cientificos_leidos) >> 2: # Tiene experiencia previa leyendo libros científicos
            self._set_propietario(propietario)
            return True
        else:
            return False

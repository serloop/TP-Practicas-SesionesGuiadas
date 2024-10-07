from app.tdas.libros.libro import Libro

class LibroInfantil(Libro):

    def __init__(self, titulo: str, autor: str, paginas: int, edad_recomendada: int, ilustraciones: bool, 
                 interactividad: bool, propietario: 'Persona' = None):
        super().__init__(titulo, autor, paginas, propietario) # Llamada al constructor de la clase padre
        
        # Nuevos atributos de la clase hija
        self._edad_recomendada = edad_recomendada # Edad recomendada de lectura
        self._ilustraciones = ilustraciones # El libro tiene ilustraciones
        self._interactividad = interactividad # El libro es interactivo
    
    def get_edad_recomendada(self) -> int:
        return self._edad_recomendada
    
    def get_ilustrado(self) -> bool:
        return self._ilustraciones
    
    def get_interactivo(self) -> bool:
        return self._interactividad

    # Ejemplo de extensión de funcionalidad heredada
    def __str__(self) -> str:
        # Obtiene la descripción básica del libro (superclase)
        descripcion_basica = super().__str__() 
        
        # Detalles extra por ser libro infantil
        detalles_infantiles = (f"Edad recomendada: {self._edad_recomendada}, "
                               f"Ilustraciones: {'Sí' if self._ilustraciones else 'No'}, "
                               f"Interactividad: {'Sí' if self._interactividad else 'No'}") 
        return f"{descripcion_basica} | {detalles_infantiles}"
    
    '''
    Ejemplo de extensión de funcionalidad: 
        - Se añade funcionalidad al método de la clase hija: comprobación de la edad
        - Se hace uso de super().agregar_lector() para llamar al método de la clase padre
    '''
    def agregar_lector(self, persona: 'Persona') -> None:
        # get_edad() viene heredado de la superclase
        if persona.get_edad() < self._edad_recomendada:
            print(f"{persona.get_nombre()} es demasiado joven para leer este libro infantil.")
        else:
            # Si la edad es adecuada, llamamos al método de la clase padre
            super().agregar_lector(persona)
            print(f"{persona.get_nombre()} ha sido añadido como lector del libro '{self._titulo}'.")

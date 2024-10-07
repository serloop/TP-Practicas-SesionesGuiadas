class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int, propietario: 'Persona' = None):
        self._titulo: str = titulo
        self._autor: str = autor
        self._paginas: int = paginas
        self._listado_lectores: list['Persona'] = []  # Lista de personas que han leído el libro
        self._propietario: 'Persona' = propietario  # Relación de agregación: un libro tiene un propietario

    # Método getter para el título del libro
    def get_titulo(self) -> str:
        return self._titulo

    # Método getter para el autor del libro
    def get_autor(self) -> str:
        return self._autor

    # Método getter/setter para el número de páginas del libro
    def get_paginas(self) -> int:
        return self._paginas

    # Método setter para el número de páginas del libro (caso del diario)
    def set_paginas(self, nuevas_paginas: int) -> bool:
        if nuevas_paginas > 0:
            self._paginas = nuevas_paginas
            return True
        return False

    # Método getter/setter para los lectores del libro
    def get_listado_lectores(self) -> list['Persona']:
        return self._listado_lectores

    def agregar_lector(self, persona: 'Persona') -> None:
        self.get_listado_lectores().append(persona)

    # Métodos getter y setter para el propietario del libro
    def get_propietario(self) -> 'Persona':
        return self._propietario

    def _set_propietario(self, propietario: 'Persona'):
        self._propietario = propietario

    def comprar_libro(self, propietario: 'Persona'):
        self._set_propietario(propietario)

    # Método mágico __str__ para obtener la información del libro
    def __str__(self) -> str:
        if len(self.get_listado_lectores()) > 0:
            lectores = ", ".join([persona.get_nombre() for persona in self.get_listado_lectores()])
        else:
            lectores = "Nadie lo ha leído"

        if self.get_propietario():
            propietario = self.get_propietario().get_nombre()
        else:
            propietario = "Sin propietario"

        return (f"'{self.get_titulo()}' de {self.get_autor()}, {self.get_paginas()} páginas. "
                f"Leído por: {lectores}")
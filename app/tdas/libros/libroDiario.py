from datetime import datetime
from app.tdas.libros.libro import Libro

class LibroDiario(Libro):
    def __init__(self, titulo: str, autor: str, paginas: int, propietario: 'Persona' = None):
        super().__init__(titulo, autor, paginas, propietario)
        self.fecha_creacion: datetime = datetime.now()
        self.completado: bool = False
        self.numero_entradas: int = 0

    def get_fecha_creacion(self) -> datetime:
        return self.fecha_creacion

    def get_completado(self) -> bool:
        return self.completado

    def get_numero_entradas(self) -> int:
        return self.numero_entradas

    def agregar_entrada(self, entrada: str) -> None:
        self.numero_entradas += 1

    def completar_diario(self) -> None:
        self.completado = True

    def __str__(self) -> str:
        descripcion_basica = super().__str__()
        detalles_diario = (f"Fecha de creación: {self.fecha_creacion}, "
                           f"Completado: {'Sí' if self.completado else 'No'}, "
                           f"Número de entradas: {self.numero_entradas}")
        return f"{descripcion_basica} | {detalles_diario}"

    # Implementación del método abstracto
    def comprar_libro(self, propietario: 'Persona') -> bool:
        self._set_propietario(propietario)
        return True

    # Implementación del método abstracto
    def recomendar_libro(self, persona: 'Persona') -> bool:
        return True
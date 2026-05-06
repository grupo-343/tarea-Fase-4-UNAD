from abc import ABC, abstractmethod
from excepciones import SoftwareFJError, ValidationError
from logger import Logger

class Servicio(ABC):
    """Clase abstracta para servicios."""
    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base
        try:
            self.validar()
            Logger.registrar_info(f"Servicio {nombre} creado")
        except ValidationError as e:
            Logger.registrar_error(f"Error servicio {nombre}: {str(e)}")
            raise

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    def calcular_costo_con_impuesto(self, duracion, impuesto=0.19, descuento=0.0):
        """Método sobrecargado con parámetros opcionales."""
        try:
            costo_base = self.calcular_costo(duracion)
            costo = costo_base * (1 + impuesto) * (1 - descuento)
            Logger.registrar_info(f"Costo calculado para {self._nombre}: {costo}")
            return round(costo, 2)
        except Exception as e:
            Logger.registrar_error(f"Error cálculo {self._nombre}: {str(e)}")
            raise SoftwareFJError("Cálculo de costo fallido")

    def validar(self):
        if not isinstance(self._precio_base, (int, float)) or self._precio_base <= 0:
            raise ValidationError("Precio base debe ser positivo")
        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ValidationError("Nombre de servicio inválido")

    @property
    def nombre(self):
        return self._nombre

class ReservaSala(Servicio):
    def calcular_costo(self, duracion):
        return self._precio_base * duracion

    def descripcion(self):
        return "Reserva de sala por horas"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion):
        return self._precio_base * (duracion * 1.2)  # Recargo por equipo

    def descripcion(self):
        return "Alquiler de equipo técnico"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion):
        return self._precio_base + (duracion * 50)  # Tarifa fija + hora

    def descripcion(self):
        return "Asesoría personalizada"
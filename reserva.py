from datetime import datetime
from excepciones import SoftwareFJError, ValidationError
from logger import Logger

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = None
        self._estado = "pendiente"
        self._fecha = datetime.now()
        try:
            self.duracion = duracion
            # CORREGIDO: Usar _cliente directamente (encapsulación interna)
            self._cliente.agregar_reserva(self)
            Logger.registrar_info(f"Reserva creada para {self._cliente.nombre}")
        except ValidationError as e:
            Logger.registrar_error(f"Error reserva: {str(e)}")
            raise
        except AttributeError as e:
            Logger.registrar_error(f"Error cliente en reserva: {str(e)}")
            raise SoftwareFJError("Cliente inválido para reserva")

    @property
    def cliente(self):
        """Getter para cliente (encapsulación)."""
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValidationError("Duración debe ser entero positivo")
        self._duracion = valor

    @property
    def estado(self):
        return self._estado

    def confirmar(self):
        try:
            self._estado = "confirmada"
            costo = self._servicio.calcular_costo_con_impuesto(self._duracion)
            Logger.registrar_info(f"Reserva confirmada. Costo: {costo}")
            return costo
        except Exception as e:
            Logger.registrar_error(f"Error confirmación: {str(e)}")
            raise SoftwareFJError("No se pudo confirmar reserva")

    def cancelar(self):
        self._estado = "cancelada"
        Logger.registrar_info(f"Reserva cancelada para {self._cliente.nombre}")
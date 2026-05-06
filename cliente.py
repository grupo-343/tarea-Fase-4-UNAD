from abc import ABC, abstractmethod
from excepciones import SoftwareFJError, ValidationError
from logger import Logger

class Entidad(ABC):
    """Clase abstracta base para entidades del sistema."""
    @abstractmethod
    def validar(self):
        pass

class Cliente(Entidad):
    def __init__(self, id_cliente, nombre, email):
        self._id_cliente = id_cliente
        self._nombre = None
        self._email = None
        self._reservas = []
        try:
            self.nombre = nombre
            self.email = email
            Logger.registrar_info(f"Cliente {id_cliente} creado exitosamente")
        except ValidationError as e:
            Logger.registrar_error(f"Error al crear cliente {id_cliente}: {str(e)}")
            raise

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValidationError("Nombre debe ser string con al menos 2 caracteres")
        self._nombre = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or '@' not in valor:
            raise ValidationError("Email inválido")
        self._email = valor

    def agregar_reserva(self, reserva):
        self._reservas.append(reserva)

    def validar(self):
        return bool(self._nombre and self._email)
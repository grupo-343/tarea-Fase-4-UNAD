class SoftwareFJError(Exception):
    """Excepción base para el sistema Software FJ."""
    pass

class ValidationError(SoftwareFJError):
    """Error de validación de datos."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Servicio no disponible."""
    pass
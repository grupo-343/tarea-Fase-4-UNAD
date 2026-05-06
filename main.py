from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from logger import Logger
from excepciones import SoftwareFJError

def simular_operaciones():
    operaciones = [
        # 1-3: Clientes válidos
        {"tipo": "cliente", "id": "C001", "nombre": "Ana López", "email": "ana@ej.com"},
        {"tipo": "cliente", "id": "C002", "nombre": "Juan Pérez", "email": "juan@ej.com"},
        {"tipo": "cliente", "id": "C003", "nombre": "María García", "email": "maria@ej.com"},
        # 4: Cliente inválido (nombre corto)
        {"tipo": "cliente", "id": "C004", "nombre": "A", "email": "inv@ej.com"},
        # 5-7: Servicios válidos
        {"tipo": "servicio", "clase": ReservaSala, "nombre": "Sala A", "precio": 100.0},
        {"tipo": "servicio", "clase": AlquilerEquipo, "nombre": "Proyector", "precio": 50.0},
        {"tipo": "servicio", "clase": AsesoriaEspecializada, "nombre": "Consultoría", "precio": 200.0},
        # 8: Servicio inválido (precio negativo)
        {"tipo": "servicio", "clase": ReservaSala, "nombre": "Sala X", "precio": -10.0},
        # 9: Reserva válida
        {"tipo": "reserva", "cliente_id": "C001", "servicio_nombre": "Sala A", "duracion": 2},
        # 10: Reserva inválida (duración negativa)
        {"tipo": "reserva", "cliente_id": "C002", "servicio_nombre": "Proyector", "duracion": -1}
    ]

    clientes = {}
    servicios = {}

    for i, op in enumerate(operaciones, 1):
        try:
            if op["tipo"] == "cliente":
                cliente = Cliente(op["id"], op["nombre"], op["email"])
                clientes[op["id"]] = cliente
            elif op["tipo"] == "servicio":
                servicio = op["clase"](op["nombre"], op["precio"])
                servicios[op["nombre"]] = servicio
            elif op["tipo"] == "reserva":
                cliente = clientes.get(op["cliente_id"])
                servicio = servicios.get(op["servicio_nombre"])
                if cliente and servicio:
                    reserva = Reserva(cliente, servicio, op["duracion"])
                    reserva.confirmar()
            print(f"Operación {i} exitosa")
        except SoftwareFJError as e:
            print(f"Operación {i} fallida (maneajada): {str(e)}")
        else:
            print(f"Operación {i} completada sin errores")
        finally:
            Logger.registrar_info(f"Operación {i} procesada")

if __name__ == "__main__":
    print("Iniciando simulación Software FJ...")
    simular_operaciones()
    print("Simulación completada. Revisa logs.txt para detalles.")
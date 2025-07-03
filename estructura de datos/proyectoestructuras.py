import random
import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "normal"  # normal, alerta, crítico

    def recibir_mensaje(self, mensaje):
        print(f"[{self.nombre}] Mensaje recibido: {mensaje}")

    def detectar_emergencia(self):
        if random.random() < 0.1:
            self.estado = "alerta"
            print(f"[{self.nombre}] ¡EMERGENCIA DETECTADA!")
            return True
        return False

class RedLAN:
    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def simular_evento(self):
        for nodo in self.nodos:
            if nodo.detectar_emergencia():
                self.alertar_red(nodo)

    def alertar_red(self, nodo_emisor):
        for nodo in self.nodos:
            if nodo != nodo_emisor:
                nodo.recibir_mensaje(f"Alerta desde {nodo_emisor.nombre} - Estado: {nodo_emisor.estado}")

# Crear red y nodos
red = RedLAN()
for nombre in ["Nodo1", "Nodo2", "Nodo3", "Nodo4"]:
    red.agregar_nodo(Nodo(nombre))

# Simulación en tiempo real
for paso in range(10):
    print(f"\n--- Simulación paso {paso+1} ---")
    red.simular_evento()
    time.sleep(1)

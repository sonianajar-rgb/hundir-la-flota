# utilizamos 4 metodos __init__() colocar_barcos() recibir_disparo() y mostrar()
import numpy as np

from variables import TAMANO_TABLERO, AGUA, BARCO, JUGADOR

class Tablero:

    def __init__(self, jugador):
        self.jugador = jugador
        self.tablero = np.full((TAMANO_TABLERO, TAMANO_TABLERO), AGUA)
        self.disparos = np.full((TAMANO_TABLERO, TAMANO_TABLERO), AGUA)

    def mostrar(self, ocultar_barcos=False):
        matriz = self.disparos if ocultar_barcos else self.tablero
        for fila in matriz:
            print(" ".join(fila))

    def colocar_barcos(self):
        self.tablero[2, 4:7] = BARCO        

if __name__ == "__main__":
    mi_tablero = Tablero(JUGADOR)
    mi_tablero.colocar_barcos()
    mi_tablero.mostrar()
    print()
    mi_tablero.mostrar(ocultar_barcos=True)
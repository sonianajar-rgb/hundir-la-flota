# utilizamos 4 metodos __init__() colocar_barcos() recibir_disparo() y mostrar()
import numpy as np

from variables import TAMANO_TABLERO, AGUA, BARCO, JUGADOR, TOCADO, DISPARO_AGUA

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
        posiciones = [ (0, 0, 4),
                       (2, 0, 3), (2, 5, 3),
                         (4, 0, 2), (4, 3, 2), (4, 6, 2),
                           (6, 0, 1), (6, 2, 1), (6, 4, 1), (6, 6, 1),
                           ]
        for fila, col, longitud in posiciones:
            self.tablero[fila, col:col + longitud] = BARCO  

    def recibir_disparo(self, fila, columna):
        if self.disparos[fila, columna] != AGUA:
            return "repetido"

        if self.tablero[fila, columna] == BARCO:
            self.tablero[fila, columna] = TOCADO
            self.disparos[fila, columna] = TOCADO
            return "tocado"

        self.tablero[fila, columna] = DISPARO_AGUA
        self.disparos[fila, columna] = DISPARO_AGUA
        return "agua"

    def quedan_barcos(self):
        return np.count_nonzero(self.tablero == BARCO) > 0

    
       
        
if __name__ == "__main__":
    mi_tablero = Tablero(JUGADOR)
    mi_tablero.colocar_barcos()
    print(np.count_nonzero(mi_tablero.tablero == BARCO))
    print(mi_tablero.quedan_barcos())
    print(mi_tablero.recibir_disparo(0, 0))
    print(mi_tablero.recibir_disparo(0, 0))
    print(mi_tablero.recibir_disparo(9, 9))
    mi_tablero.mostrar()
    print()
    mi_tablero.mostrar(ocultar_barcos=True)
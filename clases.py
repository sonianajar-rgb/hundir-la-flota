# utilizamos 4 metodos __init__() colocar_barcos() recibir_disparo() y mostrar()

import random
import numpy as np

from variables import TAMANO_TABLERO, AGUA, BARCO, JUGADOR, TOCADO, DISPARO_AGUA, BARCOS

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
        for longitud, cantidad in BARCOS.items():
            for _ in range(cantidad):
                colocado = False
                while not colocado:
                    if random.choice(["H", "V"]) == "H":
                        fila = random.randint(0, TAMANO_TABLERO - 1)
                        col = random.randint(0, TAMANO_TABLERO - longitud)
                        zona = self.tablero[fila, col:col + longitud]
                    else:
                        fila = random.randint(0, TAMANO_TABLERO - longitud)
                        col = random.randint(0, TAMANO_TABLERO - 1)
                        zona = self.tablero[fila:fila + longitud, col]
                    if np.all(zona == AGUA):
                        zona[:] = BARCO
                        colocado = True    

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
    for _ in range(20):
        t = Tablero(JUGADOR)
        t.colocar_barcos()
        print(np.count_nonzero(t.tablero == BARCO))
    t.mostrar()    

    
       
        
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
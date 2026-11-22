import random                      # para sacar números al azar
import numpy as np                 # para crear y manejar el tablero como una tabla

# Traemos las constantes (los datos fijos del juego) desde variables.py
from variables import TAMANO_TABLERO, AGUA, BARCO, JUGADOR, TOCADO, DISPARO_AGUA, BARCOS


class Tablero:
    #Tablero de un jugador: guarda sus barcos y los disparos recibidos

    def __init__(self, jugador):
        # Se ejecuta solo, al crear un tablero nuevo: Tablero(JUGADOR)
        self.jugador = jugador     # de quién es el tablero (Jugador o Máquina)
        # Tabla de 10x10 llena de agua. Aquí se guardan los barcos y los disparos
        self.tablero = np.full((TAMANO_TABLERO, TAMANO_TABLERO), AGUA)
        # Otra tabla igual, pero solo con los disparos (sin barcos). Es lo que ve el rival
        self.disparos = np.full((TAMANO_TABLERO, TAMANO_TABLERO), AGUA)

    def mostrar(self, ocultar_barcos=False):
        # Dibuja el tablero en pantalla
        # Si ocultar_barcos es True, enseña la tabla de disparos (sin barcos)
        matriz = self.disparos if ocultar_barcos else self.tablero
        for fila in matriz:                # recorre el tablero fila por fila
            print(" ".join(fila))         # pega las casillas de la fila con un espacio

    def colocar_barcos(self):
        # Coloca todos los barcos al azar, sin salirse y sin pisarse
        for longitud, cantidad in BARCOS.items():   # por ejemplo: longitud 2, cantidad 3
            for _ in range(cantidad):               # repite una vez por cada barco de ese tipo
                colocado = False                    # de momento este barco no está puesto
                while not colocado:                 # prueba posiciones hasta que encuentre una libre
                    if random.choice(["H", "V"]) == "H":    # elige horizontal o vertical
                        # Horizontal: cualquier fila, y una columna que deje espacio al barco
                        fila = random.randint(0, TAMANO_TABLERO - 1)
                        col = random.randint(0, TAMANO_TABLERO - longitud)
                        zona = self.tablero[fila, col:col + longitud]    # casillas que ocuparía
                    else:
                        # Vertical: una fila que deje espacio al barco, y cualquier columna
                        fila = random.randint(0, TAMANO_TABLERO - longitud)
                        col = random.randint(0, TAMANO_TABLERO - 1)
                        zona = self.tablero[fila:fila + longitud, col]   # casillas que ocuparía
                    if np.all(zona == AGUA):        # si todas esas casillas están libres...
                        zona[:] = BARCO             # ...pone el barco
                        colocado = True             # y pasa al siguiente barco

    def recibir_disparo(self, fila, columna):
        # Recibe un disparo y devuelve "repetido", "tocado" o "agua"
        if self.disparos[fila, columna] != AGUA:    # si ya se había disparado ahí
            return "repetido"

        if self.tablero[fila, columna] == BARCO:    # si hay un barco en esa casilla
            self.tablero[fila, columna] = TOCADO    # lo marca como tocado en el tablero
            self.disparos[fila, columna] = TOCADO   # y también en la tabla de disparos
            return "tocado"

        # Si no era repetido ni barco, es agua
        self.tablero[fila, columna] = DISPARO_AGUA
        self.disparos[fila, columna] = DISPARO_AGUA
        return "agua"

    def quedan_barcos(self):
        # Cuenta las casillas que siguen siendo barco (sin tocar)
        # Devuelve True si queda alguna y False si no queda ninguna
        return np.count_nonzero(self.tablero == BARCO) > 0

# es editar
# Esta parte solo se ejecuta si lanzas clases.py directamente (es una prueba)
# Si otro archivo importa Tablero, esta parte NO se ejecuta
if __name__ == "__main__":
    t = Tablero(JUGADOR)                            # crea un tablero
    t.colocar_barcos()                              # pone los barcos al azar
    t.mostrar()                                     # lo dibuja

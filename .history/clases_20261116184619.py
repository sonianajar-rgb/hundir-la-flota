# utilizamos 4 metodos __init__() colocar_barcos() recibir_disparo() y mostrar()
import numpy as np

import numpy as np

def crear_tablero(lado=10, agua="~"):
    tablero = np.full((lado, lado), agua)
    return tablero


tablero = crear_tablero()

print(tablero)
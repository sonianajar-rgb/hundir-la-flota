# utilizamos 4 metodos __init__() colocar_barcos() recibir_disparo() y mostrar()
from variables import TAMANO_TABLERO, AGUA 
import numpy as np
tablero = np.full((10,10), " ")
print(tablero)

def crear_tablero(lado = 10, agua = " "):
    tablero = np.full((lado, lado), agua)
    return tablero
tablero = crear_tablero()
print(tablero)
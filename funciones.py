from variables import AGUA, BARCO, DISPARO_AGUA, MENSAJE_AGUA, MENSAJE_TOCADO, TOCADO


def validar_celda(tablero: list[list[str]], fila: int, columna: int) -> bool:
    #Indica si la posición existe y todavía se puede disparar en ella.#
    if not isinstance(tablero, list) or not tablero:
        return False
    if type(fila) is not int or type(columna) is not int:
        return False
    if fila < 0 or fila >= len(tablero):
        return False

    if any(not isinstance(f, list) for f in tablero):
        return False
    ancho = len(tablero[0])
    if ancho == 0 or any(len(f) != ancho for f in tablero):
        return False
    if columna < 0 or columna >= ancho:
        return False

    return tablero[fila][columna] in (AGUA, BARCO)


def disparar(tablero: list[list[str]], fila: int, columna: int) -> str:
    #Dispara en una celda válida, actualiza el tablero y devuelve el mensaje#
    if not validar_celda(tablero, fila, columna):
        raise ValueError("La celda no existe o ya recibió un disparo.")

    if tablero[fila][columna] == BARCO:
        tablero[fila][columna] = TOCADO
        return MENSAJE_TOCADO

    tablero[fila][columna] = DISPARO_AGUA
    return MENSAJE_AGUA

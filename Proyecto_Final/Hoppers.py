# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

import numpy as np

class Juego():
    def validar(self, fila, columna):
        if (fila <= 0 or fila > 9 or columna <= 0  or columna > 9):
            return False
        else:
            return True

    def getTablero(self):
        tablero = [[0] * 10 for _ in range(10)]
        for fila in range(10):
            for columna in range(10):
                pos = (fila, columna)
                if fila + columna < 5:
                    ficha_ = 2    
                elif fila + columna > 13:
                    ficha_ = 1
                else:
                    ficha_ = 0
                tablero[fila][columna] = type('Ficha', (object,),{'pos': pos, 'ficha_': ficha_})()
        return tablero

    def mostrar_tablero(self, tablero):
        for i in range(0, 10):
            for j in range(0, 10):
                p = tablero[i][j].ficha_
                if (p ==1 or p ==2):
                    print('{},'.format('☺' if (tablero[i][j].ficha_ == 1) else '♥'), end=" ")
                else: 
                    print('{},'.format(' '), end=" ")
            print()

    def getFicha(self, fila, columna, tablero):
        return tablero[fila][columna]

    def getfichasJugador(self, tablero):
        return [element for fila in tablero
                    for element in fila if element.ficha_ == 2]

    def getfichasMarta(self, tablero):
        return [element for fila in tablero
                    for element in fila if element.ficha_ == 1]

    def ganador(self, tablero):
        fichas_marta = self.getfichasJugador(tablero)
        fichas_jugador = self.getfichasMarta(tablero)
        if all(gana.ficha_ == 1 for gana in fichas_marta):
            return 1
        elif all(gana.ficha_ == 2 for gana in fichas_jugador):
            return 2
        else:
            return None
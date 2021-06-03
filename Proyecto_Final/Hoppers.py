# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

import numpy as np

class Juego():

    def __init__(self):
        pass


    def get_board(self):
        tablero = [[None] * 10 for _ in range(10)]
        for row in range(10):
            for col in range(10):
                pos = (row, col)
                if row + col < 5:
                    ficha_ = 2    
                elif row + col > 13:
                    ficha_ = 1
                else:
                    ficha_ = 0
                
                tablero[row][col] = type('Piece', (object,),{'pos': pos, 'ficha_': ficha_})()#Piece(row, col)  # la pieza puede ser blanca, negra, o ninguna
                
        return tablero


    def getfichasJugador(self, tablero):
        # retorna las posiciones en el tablero en donde se inician las piezas negras
        return [element for row in tablero
                    for element in row if element.ficha_ == 2]


    def getfichasMarta(self, tablero):
        # retorna las posiciones en el tablero en donde se inician las piezas blancas
        return [element for row in tablero
                    for element in row if element.ficha_ == 1]


    def getFicha(self, row, col, tablero):
        # retorna una pieza del tablero.
        return tablero[row][col]


    def mostrar_tablero(self, tablero):
        # dibuja el tablero en consola
        for i in range(0, 10):
            for j in range(0, 10):
                p = tablero[i][j].ficha_
                if (p ==1 or p ==2):
                    print('{},'.format('☺' if (tablero[i][j].ficha_ == 1) else '♥'), end=" ")
                else: 
                    print('{},'.format(' '), end=" ")
            print()
        print()


    def ganador(self, tablero):
        # obtiene las posiciones iniciales de las piezas blancas que sirven para comprobar si ya las ocupo el equipo contrario
        black_home = self.getfichasJugador(tablero)
        withe_home = self.getfichasMarta(tablero)
        # valida que no haya ganador
        if all(win.ficha_ == 1 for win in black_home):
            return 1
        elif all(win.ficha_ == 2 for win in withe_home):
            return 2
        else:
            return None


    def valid_board_position(self, row, col):
        # retorna si la posición row,col estan dentro de la matriz del tablero
        return (False) if (row <= 0 or row > 9 or col <= 0  or col > 9) else True
# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

import time
import math

class Marta():
    def __init__(self, tablero):
        #se inicializa el tablero del juego
        self.tablero = tablero
    
    def funcion_evaluadora(self, ficha_, tablero):
        resultado = 0
        humano_jugador = self.tablero.getfichasMarta(tablero)
        humano_marta = self.tablero.getfichasJugador(tablero)
        for columna in range(10):
            for fila in range(10):
                if tablero[fila][columna].ficha_ == 2:
                    valor_jugada = [math.factorial((math.fabs(f.pos[0] - fila) + (f.pos[1] - columna)**2)) for f in humano_jugador if f.ficha_ != 2]
                    if len(valor_jugada):
                        resultado += min(valor_jugada)
                    else:
                        resultado += -1000
                if tablero[fila][columna].ficha_ == 1:
                    valor_jugada = [math.factorial((math.fabs(f.pos[0] - fila)**2 + (f.pos[1] - columna)**2)) for f in humano_marta if f.ficha_ != 1]
                    if len(valor_jugada):
                        resultado -= max(valor_jugada)
                    else:
                        resultado -= -1000 
        if ficha_ == 2:
            resultado *= -1000
        return resultado

    def getJugadas(self, jugador, tablero) :
        jugadas_ = [] 
        for columna in range(10):
            for fila in range(10):
                if tablero[fila][columna].ficha_ == jugador:
                    jugadas_.append([tablero[fila][columna], self.jugadas(fila,columna, tablero)])
        return jugadas_

    #MINIMAX
    def minimax(self, profundida, limite, tablero, alpha=float("-inf"), beta=float("inf"), maximizando=True):
        nodo = None
        if profundida == 0 or time.time() > limite or self.tablero.ganador(tablero):
            return self.funcion_evaluadora(2, tablero), None
        if maximizando:
            nodo_v = float("-inf")
            jugadas = self.getJugadas(2, tablero)
        else:
            nodo_v = float("inf")
            jugadas = self.getJugadas(1, tablero)
        for movimiento in jugadas:
            for to in movimiento[1]:
                if time.time() > limite:
                    return nodo_v, nodo
                ficha_ = movimiento[0].ficha_
                movimiento[0].ficha_ = 0
                to.ficha_ = ficha_
                valor, m = self.minimax(profundida - 1, limite, tablero, alpha, beta, maximizando=False)
                to.ficha_ = 0    
                movimiento[0].ficha_ = ficha_
                if maximizando and valor > nodo_v:
                    nodo_v = valor
                    nodo = (movimiento[0].pos, to.pos)
                    alpha = max(alpha, valor)
                if not maximizando and valor < nodo_v:
                    nodo_v = valor
                    nodo = (movimiento[0].pos, to.pos)
                    beta = min(beta, valor)
                if beta <= alpha:
                    return nodo_v, nodo
        return nodo_v, nodo

    def jugadas(self, fila, columna, tablero, jugada_nueva=None, salto=True):
        if jugada_nueva is None:
            jugada_nueva = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if ((fila + j) != fila and (columna + i) != columna):
                    fila_n = fila + j
                    columna_n = columna + i
                    if (self.tablero.validar(fila_n, columna_n) == True):
                        if tablero[fila_n][columna_n].ficha_ == 0: 
                            if (salto == True):
                                jugada_nueva.append(tablero[fila_n][columna_n])
                        else:                        
                            if (self.tablero.validar(fila_n + j, columna_n + i) == True):
                                if not (tablero[fila_n + j][columna_n + i] in jugada_nueva):
                                    if tablero[fila_n + j][columna_n + i].ficha_ == 0:
                                        jugada_nueva.insert(0, tablero[fila_n + j][columna_n + i])  
                                        self.jugadas(tablero[fila_n + j][columna_n + i].pos[0], tablero[fila_n + j][columna_n + i].pos[1], tablero, jugada_nueva, False)
        return jugada_nueva

    
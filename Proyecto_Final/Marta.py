# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

import time
import math
#from ficha_ import Piece

class Marta():

    def __init__(self, tablero):
        self.tablero = tablero
        pass 
    
    def minimax(self, depth, time_limit, tablero, alpha=float("-inf"), beta=float("inf"), maximizing=True):
        node_option = None
        
        # valida que no haya llegado al ultimo nivel de profundidad, que se haya cumplido el tiempo o que haya un ganador.
        if depth == 0 or time.time() > time_limit or self.tablero.ganador(tablero):
            return self.eval_fun(2, tablero), None

        # obtiene los posibles movimientos según se este maximizando o minimizando
        if maximizing:

            # como maximiza se setea el valor del nodo a menos infinito, mientras no se ha evaluado el nodo.
            node_value = float("-inf")
            # obtiene los posibles movimientos del jugador (maximiza para las negras)
            possible_moves = self.get_possible_moves(2, tablero)
        else:

            # como miminiza se setea el valor del nodo con infinito, mientras no se ha evaluado el nodo.
            node_value = float("inf")
            # obtiene los posibles movimientos del jugador (minimiza para las blancas)
            possible_moves = self.get_possible_moves(1, tablero)

        # Se recorren los posibles movimientos para calcular las jugadas.
        for move in possible_moves:
            for to in move[1]:

                # retorna el valor si ya se cumplió el tiempo
                if time.time() > time_limit:
                    return node_value, node_option

                # simula el movimiento
                ficha_ = move[0].ficha_
                move[0].ficha_ = 0
                to.ficha_ = ficha_

                # llamada recursiva de la función MINMAX para minimizar la jugada del oponente. 
                val, mov = self.minimax(depth - 1, time_limit, tablero, alpha, beta, not maximizing)

                # regresa el movimiento luego de haber sido evaluado
                to.ficha_ = 0    
                move[0].ficha_ = ficha_

                # evalua el valor del modo, si el valor es mayor que el valor actual para tomar la mejor jugada
                if maximizing and val > node_value:
                    node_value = val
                    node_option = (move[0].pos, to.pos)
                    alpha = max(alpha, val)

                    # evalua el valor del modo, si el valor es menor que el valor actual para tomar la mejor jugada
                if not maximizing and val < node_value:
                    node_value = val
                    node_option = (move[0].pos, to.pos)
                    beta = min(beta, val)

                # alpha beta pruning para descartar nodos descartados porque ya hay un mejor valor.
                if beta <= alpha:
                    return node_value, node_option

        #retorna la mejor jugada que fue evaluada, y el valor que obtuvo el nodo
        return node_value, node_option
      


    def eval_fun(self, ficha_, tablero):

        resultado = 0
        # se obtienen los lugares finales para las piezas blancas y negras
        humano_marta = self.tablero.getfichasJugador(tablero)
        humano_jugador = self.tablero.getfichasMarta(tablero)

        # se recorre todo el tablero buscando piezas para evaluar la distancia que hay entre la pieza y la meta y obtener un valor max o min
        for columna in range(10):
            for fila in range(10):
                
                # si las piezas son blancas se maximiza la distancia para obtener el mejor resultado
                if tablero[fila][columna].ficha_ == 1:
                    d = [math.sqrt((end.pos[0] - fila)**2 + (end.pos[1] - columna)**2) for end in humano_marta if end.ficha_ != 1]
                    if len(d):
                        resultado -= max(d)
                    else:
                        resultado -= -100    
                
                # si las piezas son negras se minimiza la distancia para obtener el mejor resultado
                if tablero[fila][columna].ficha_ == 2:
                    d = [math.sqrt((end.pos[0] - fila)**2 + (end.pos[1] - columna)**2) for end in humano_jugador if end.ficha_ != 2]
                    if len(d):
                        resultado += min(d)
                    else:
                        resultado += -100    
                    
        if ficha_ == 2:
            resultado *= -1

        return resultado

    
    def get_possible_moves(self, player, tablero) :
        moves = [] 
        # se recorre todo el tablero para ubicar todas las piezas del jugador
        for columna in range(10):
            for fila in range(10):
                # si en la posicion del tablero encuentra una pieza del jugador determina todas los posibles saltos que puede dar
                if tablero[fila][columna].ficha_ == player:
                    moves.append([tablero[fila][columna], self.possible_moves(fila,columna, tablero)])

        return moves


    def possible_moves(self, fila, columna, tablero, new_mov=None, first_salt=True):
        
        if new_mov is None:
            new_mov = []

        # para una pieza especifica se calculan los saltos que esta puede dar
        for i in range(-1, 2):
            for j in range(-1, 2):
                
                # se determina si la casilla a donde se quiera saltar no sea la casilla desde donde se quiere saltar
                if ((fila + j) != fila and (columna + i) != columna):
                    new_row = fila + j
                    new_col = columna + i

                    # se valida que la posicion hasta donde quiera llegar esta dentro del tablero de 10x10
                    if (self.tablero.validar(new_row, new_col) == True):
                        # si la casilla esta libre salta
                        if tablero[new_row][new_col].ficha_ == 0:  
                            # solo se permite mover a una casilla en blanco con un primer salto
                            if (first_salt == True):
                                new_mov.append(tablero[new_row][new_col])
                        
                        else: 
                            # si la casilla no está libre entonces evalua la casilla posterior para saltar la pieza                               
                            if (self.tablero.validar(new_row + j, new_col + i) == True):
                                # comprueba que no haya sido ingresado el destino para no duplicar posibles lugares a ocupar
                                if not (tablero[new_row + j][new_col + i] in new_mov):
                                    # si la siguiente casilla a una ocupada esta libre hace un salto
                                    if tablero[new_row + j][new_col + i].ficha_ == 0:
                                        new_mov.insert(0, tablero[new_row + j][new_col + i])  

                                        # se evalúa recursivamente si puede saltar otra pieza
                                        self.possible_moves(tablero[new_row + j][new_col + i].pos[0], tablero[new_row + j][new_col + i].pos[1], tablero, new_mov, False)
        return new_mov

    
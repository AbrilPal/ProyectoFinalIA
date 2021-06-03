# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

from Marta import Marta
from Hoppers import Juego
import time

class Hoopers():

    def __init__(self):
        #tiempo
        self.time_limit = 40
        #profundidad
        self.depth = 4
        #inicia el tablero
        self.b = Juego()
        #inicia Marta
        self.ia = Marta(self.b)
        self.tablero = self.b.get_board()
        self.humano_jugador = 1 
        #posiciones de las fichas en el tablero
        self.fichas_jugador = self.b.getfichasJugador(self.tablero)
        self.fichas_marta = self.b.getfichasMarta(self.tablero)
        print("")
        print("Holi, inicias tu con las fichas ☺ (las de abajo) y Marta(inteligencia) con las fichas ♥ (las de arriba)")
        print("El tablero comienza en (1,1) que es la esquina superior izquierda y llega a la esquina inferior derecha (10,10).")
        print("solo debes ingresar la pisicion inicial y la posicion final, NO TODA LA CADENA")
        print("Espero esto sea suficiente para ganar la clase‼")
        print("")
        print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ Disfruta del juego :) ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
        print("")
        
    def jugar(self):
        comenzar = True
        while comenzar:
            self.b.mostrar_tablero(self.tablero)
            self.resultado = self.b.ganador(self.tablero)
            if (self.b.ganador(self.tablero) == 1):
                print("\n ♪♫♪♫♪♫♪♫♪♫ GANASTE ♪♫♪♫♪♫♪♫♪♫")
                quit()
            if (self.b.ganador(self.tablero) == 2):
                print("\n :( PERDISTE :(")
                quit()
            if self.humano_jugador == 1:
                    turno = True
                    while (turno):
                        
                        mi = input ("Mover desde (fila, columna): \n")
                        if (mi == 't'):
                            comenzar = False
                            break   
                        mf = input ("Mover hasta (fila, columna): \n")
                        if (mf == 't'):
                            comenzar = False
                            break   
                        
                        mix, miy = mi.split(',')
                        mfx, mfy = mf.split(',')

                        pi = (int(mix)-1, int(miy)-1)
                        pf = (int(mfx)-1, int(mfy)-1)
                                                
                        # se mueve la pieza
                        if (self.manual_move(pi,pf) == True):
                            turno = False
                        
                        # se establece el turno para el oponente
                        self.humano_jugador = 2
                        print()

            else:

                # si el turno es de las negras entonces el agente de IA hace el movimiento
                print('Turno de la compu, espere...')
                self.agent_move()
                # se establece el turno para el oponente
                self.humano_jugador = 1


    def manual_move(self, A, B):
        
        # obtiene las posiciones que seran intercambiadas
        curr_pos = self.b.get_piece(A[0], A[1], self.tablero)
        final_pos = self.b.get_piece(B[0], B[1], self.tablero)    
        
        # valida que se seleccione una ficha y que la casilla final este libre
        if curr_pos.piece == 0 or final_pos.piece != 0:
            print("\nMovimiento incorrecto\n")
            return False

        # mueve la ficha
        final_pos.piece = curr_pos.piece
        curr_pos.piece = 0
        return True

    
    def agent_move(self):

        # se obtiene el tiempo limite
        time_to_move = time.time() + self.time_limit

        # se obtiene el mejor movimiento evaluando con MINIMAX
        val , best_move = self.ia.minimax(self.depth, time_to_move, self.tablero)

        print("Movimiento calculado")
        
        # se obtiene el mejor movimiento
        mi = (best_move[0][0],best_move[0][1])
        mf = (best_move[1][0],best_move[1][1])

        # se mueve la pieza
        self.manual_move(mi, mf)
        print("Movimiento de la computadora (fila, columna) desde " 
                +  str((mi[0] + 1, mi[1] + 1)) + ' hasta ' 
                +  str((mf[0] + 1, mf[1] + 1)))
        print()    


if __name__ == "__main__":
    game = Hoopers()
    game.jugar() # inicia el juego
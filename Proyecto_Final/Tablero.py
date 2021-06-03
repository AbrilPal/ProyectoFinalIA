# Andrea aAbril Palencia Gutierrez, 18198
# Inteligencia Artificial - Proyecto Final
# 01/06/2021

from Marta import Marta
from Hoppers import Juego
import time

class Hoopers():

    def __init__(self):
        #tiempo
        self.limite = 40
        #profundidad
        self.depth = 4
        #inicia el tablero
        self.b = Juego()
        #inicia Marta
        self.ia = Marta(self.b)
        self.tablero = self.b.getTablero()
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

    def marta_juega(self):
        #limite
        tiempo = time.time() + self.limite
        #lo que marta retorna
        val, jugada_marta_mejor = self.ia.minimax(self.depth, tiempo, self.tablero)
        pos_i_marta = (jugada_marta_mejor[0][0],jugada_marta_mejor[0][1])
        pos_f_marta = (jugada_marta_mejor[1][0],jugada_marta_mejor[1][1])
        self.movimiento_cambio(pos_i_marta, pos_f_marta)
        print()

    def movimiento_cambio(self, A, B):
        pos_inicial = self.b.getFicha(A[0], A[1], self.tablero)
        pos_final = self.b.getFicha(B[0], B[1], self.tablero)    
        #comprobar si es valido el movimiento
        if pos_inicial.ficha_ == 0 or pos_final.ficha_ != 0:
            print("")
            print("Este movimiento es incorrecto")
            print()
            return False
        pos_final.ficha_ = pos_inicial.ficha_
        pos_inicial.ficha_ = 0
        return True
 
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
                        print("posicion de la ficha que quieres mover")
                        pos_i_marta = input ("fila,columna: ")
                        if (pos_i_marta == 't'):
                            comenzar = False
                            break   
                        print("posicion final de la ficha seleccionada")
                        pos_f_marta = input ("fila,columna: ")
                        if (pos_f_marta == 't'):
                            comenzar = False
                            break   
                        #separar cordenadas x y y para poder mover en tablero
                        pos_i_x, pos_i_y = pos_i_marta.split(',')
                        pos_f_x, pos_f_y = pos_f_marta.split(',')
                        p_i = (int(pos_i_x)-1, int(pos_i_y)-1)
                        p_f = (int(pos_f_x)-1, int(pos_f_y)-1)
                        if (self.movimiento_cambio(p_i,p_f) == True):
                            turno = False
                        #cambio de turno
                        self.humano_jugador = 2
            else:
                print()
                print('Marta esta pensando su jugada')
                self.marta_juega()
                #cambio de turno
                self.humano_jugador = 1
if __name__ == "__main__":
    juego_comienza = Hoopers()
    juego_comienza.jugar() 

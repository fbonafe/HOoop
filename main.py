import radar
import medio
import blanco
import generador
import datetime
import detector
import matplotlib.pyplot as plt

# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales
    gen = generador.Generador(amplitud, fase, frecuencia)

    #TODO construir un detector
    detec = detector.Detector()

    #TODO construir un nuevo radar
    rad = radar.Radar(gen, detec)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 1.
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    
    #TODO contruir un nuevo blanco
    mi_blanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco, \
                            tiempo_inicial_del_blanco, tiempo_final_del_blanco)
    mis_blancos = [mi_blanco]
    #TODO contruir un medio
    mi_medio = medio.Medio(mis_blancos)

    #TODO construir un radar
    senal_emitida = gen.generar(tiempo_inicial, tiempo_final)
    senal_salida = rad.detectar(mi_medio, tiempo_inicial, tiempo_final)
    plt.plot(senal_emitida)
    plt.plot(senal_salida)
    
if __name__ == "__main__":
    main()

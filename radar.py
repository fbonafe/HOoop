"""
Define el similador del Radar
"""
import matplotlib.pyplot as plt

class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector

    def plotear_senal(self, senal_emitida, senal_salida):
        plt.plot(senal_emitida, label='emitida')
        plt.plot(senal_salida, label='detectada')
        plt.legend()
        plt.savefig('radar.png')
        
    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final)
        
        self.plotear_senal(una_senal, una_senal_reflejada)
        
        return self.detector.detectar(una_senal_reflejada, una_senal)
        

class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        #TODO: completar con la inicializacion de los parametros del objeto
        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        senal_salida = [0.] * len(senal)
        dt = (tiempo_final - tiempo_inicial).seconds/len(senal)
        times = [tiempo_inicial.second + i*dt for i in range(len(senal))]
        
        for i,time in enumerate(times):
            if time > self.tiempo_inicial.second and \
            time < self.tiempo_final.second:
                senal_salida[i] = self.amplitud
        
        return senal_salida
                
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        

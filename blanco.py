class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        senal_salida = [0.] * len(senal)
        dt = (tiempo_final - tiempo_inicial).seconds / len(senal)
        si = (self.tiempo_inicial - tiempo_inicial).seconds
        sf = (self.tiempo_final - tiempo_inicial).seconds

        if (self.tiempo_inicial >= tiempo_inicial):
            ni = int(si/dt)
            if (self.tiempo_final <= tiempo_final):
                nf = int(sf/dt)
            else: #(self.tiempo_final > tiempo_final):
                nf = len(senal)
        else: #(self.tiempo_inicial < tiempo_inicial)
            ni = 0
            if (self.tiempo_final >= tiempo_inicial):
                if (self.tiempo_final <= tiempo_final):
                    nf = int(sf/dt)
                else: #(self.tiempo_final > tiempo_final):
                    nf = len(senal)
            else:
                nf = 0
        
        for i in range(ni, nf):
            senal_salida[i] = senal[i]*self.amplitud
            
        return senal_salida
                
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        

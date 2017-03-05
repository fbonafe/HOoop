class Detector(object):

    def __init__(self):
        pass
    def detectar(self, senal, senal_generada):
        if max(senal) > max(senal_generada):
            print('Se detecto uno o mas blancos!')
        else:
            print('No se detecto nada')
        return senal
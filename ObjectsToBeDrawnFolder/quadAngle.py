class qAngle:
    def __init__(self, x0, y0, xf, yf, color):
        self.vertices= [
         x0,    y0, 0.0,  *color, # izq arriba
         x0,    yf, 0.0,  *color, # izq abajo
         xf,    yf, 0.0,  *color, # der abajo
         xf,    y0, 0.0,  *color, # der arriba
        ]

        self.indices= [0, 1, 2, 2, 3, 0]

        self.IPList= [min(x0, xf), min(y0, yf)]

        self.FPList= [max(x0, xf), max(y0, yf)]

    def getVer(self):
        return self.vertices

    def getIn(self):
        return self.indices

    def getIPList(self):
        return self.IPList

    def getFPList(self):
        return self.FPList
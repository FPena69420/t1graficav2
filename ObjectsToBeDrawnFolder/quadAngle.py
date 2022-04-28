class qAngle:
    def __init__(self, x0, y0, xf, yf, color, message=""):
        self.vertices= [
         x0,    y0, 0.0,  *color, # izq arriba
         x0,    yf, 0.0,  *color, # izq abajo
         xf,    yf, 0.0,  *color, # der abajo
         xf,    y0, 0.0,  *color, # der arriba
        ]

        self.indices= [0, 1, 2, 2, 3, 0]

        self.message= message

        self.yrange= [min(y0, yf), max(y0, yf)]
        self.xrange= [min(x0, xf), max(x0, xf)]

    def getVer(self):
        return self.vertices

    def getIn(self):
        return self.indices

    def getIPList(self):
        return self.IPList

    def getFPList(self):
        return self.FPList

    def hoveringOn(self, plist):
        assert(len(plist)==2)
        xMouse = plist[0]
        yMouse = plist[1]
        if (self.yrange[0]<= yMouse<= self.yrange[1] and self.xrange[0]<= xMouse<= self.xrange[1]):
            #print(self.message)
            return True

    def clicked(self):
        print(f'{self.message} was clicked!')
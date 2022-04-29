import ObjectsToBeDrawnFolder.myWindow as NW
import ObjectsToBeDrawnFolder.objectsToBeDrawn as doodle
import glfw

class qAngle:
    def __init__(self, x0, y0, xf, yf, color, message="", function= "None", myWindow= None):
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

        self.function= function
        self.myWindow= myWindow

    def getVer(self):
        return self.vertices

    def getIn(self):
        return self.indices

    def hoveringOn(self, plist):
        assert(len(plist)==2)
        xMouse= plist[0]
        yMouse= plist[1]
        if self.yrange[0]<= yMouse<= self.yrange[1] and self.xrange[0]<= xMouse<= self.xrange[1]:
            #print(self.message)
            return True

    def clicked(self):
        print(f'{self.message} was clicked!')
        if self.function== "windowCarrier":
            self.myWindow= NW.myNewWindow(-0.7, 0.9, 0.7, -0.3, [1.0, 1.0, 1.0], "window", self)

        if self.function== "closeWindow":
            self.myWindow.closed()

        if self.function== "fullscreen":
            self.myWindow.goFull()

    def windowWasClosed(self):
        self.myWindow= None

    def getMyWindow(self):
        return self.myWindow
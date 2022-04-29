import ObjectsToBeDrawnFolder.quadAngle as QA
import ObjectsToBeDrawnFolder.objectsToBeDrawn as doodle


class myNewWindow:
    def __init__(self, x0, y0, xf, yf, color, message="", assQuad= None):
        self.vertices= [
         x0,    y0, 0.0,  *color, # izq arriba
         x0,    yf, 0.0,  *color, # izq abajo
         xf,    yf, 0.0,  *color, # der abajo
         xf,    y0, 0.0,  *color, # der arriba
        ]

        self.fullsVer= [
         -1,    -1, 0.0,  *color, # izq arriba
         -1,    1, 0.0,  *color, # izq abajo
         1,    1, 0.0,  *color, # der abajo
         1,    -1, 0.0,  *color, # der arriba
        ]

        self.indices= [0, 1, 2, 2, 3, 0]
        self.color= color

        self.message= message
        self.assQuad= assQuad

        self.yrange= [min(y0, yf), max(y0, yf)]
        self.xrange= [min(x0, xf), max(x0, xf)]

        self.closebutton= QA.qAngle(xf-0.1, y0-0.1, xf, y0, [0, 0, 1], "close", "closeWindow", self)
        self.fullscreenbutton= QA.qAngle(xf-0.2, y0-0.1, xf-0.1, y0, [0, 1, 0], "fullscreen", "fullscreen", self)

        self.fullsClosebutton = QA.qAngle(0.9, 0.9, 1, 1, [0, 0, 1], "close", "closeWindow", self)
        self.fullsFullsbutton = QA.qAngle(0.8, 0.9, 0.9, 1, [0, 1, 0], "fullscreen", "fullscreen", self)

        self.fullscreen= False

    def getVer(self):
        return self.vertices

    def getIn(self):
        return self.indices

    def hoveringOn(self, plist):
        assert(len(plist)==2)
        xMouse = plist[0]
        yMouse = plist[1]
        if (self.yrange[0]<= yMouse<= self.yrange[1] and self.xrange[0]<= xMouse<= self.xrange[1]):
            #print(self.message)
            return True

    def clicked(self):
        print(f'{self.message} was clicked!')

    def closed(self):
        self.assQuad.windowWasClosed()

    def getCloseButton(self):
        return self.closebutton

    def getFullsButton(self):
        return self.fullscreenbutton

    def goFull(self):
        aux= self.vertices
        self.vertices=self.fullsVer
        self.fullsVer= aux

        closeButAux= self.closebutton
        self.closebutton = self.fullsClosebutton
        self.fullsClosebutton= closeButAux

        fullsButAux = self.fullscreenbutton
        self.fullscreenbutton = self.fullsFullsbutton
        self.fullsFullsbutton = fullsButAux
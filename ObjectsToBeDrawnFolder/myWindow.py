import ObjectsToBeDrawnFolder.quadAngle as QA
import ObjectsToBeDrawnFolder.objectsToBeDrawn as doodle


class myNewWindow:
    def __init__(self, x0, y0, xf, yf, color, message="", assQuad= None):
        self.x0= x0
        self.y0= y0
        self.xf= xf
        self.yf= yf

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

        self.header= [x0, y0-0.1, xf-0.2, y0]
        self.fullsHeader= [-1, 0.9, 0.8, 1]
        self.headeryrange= [min(self.header[1], self.header[3]), max(self.header[1], self.header[3])]
        self.headerxrange= [min(self.header[0], self.header[2]), max(self.header[0], self.header[2])]

        self.armer= [xf-0.1, yf-0.1, xf, y0]
        self.fullsArmer= [0.9, -0.9, 1, 1]
        self.armeryrange = [min(self.armer[1], self.armer[3]), max(self.armer[1], self.armer[3])]
        self.armerxrange = [min(self.armer[0], self.armer[2]), max(self.armer[0], self.armer[2])]

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

    def hoveringOnHeader(self, plist):
        assert (len(plist) == 2)
        xMouse = plist[0]
        yMouse = plist[1]
        if (self.headeryrange[0] <= yMouse <= self.headeryrange[1] and self.headerxrange[0] <= xMouse <= self.headerxrange[1]):
            #print("window header")
            return True

    def hoveringOnArmer(self, plist):
        assert (len(plist) == 2)
        xMouse = plist[0]
        yMouse = plist[1]
        if (self.armeryrange[0] <= yMouse <= self.armeryrange[1] and self.armerxrange[0] <= xMouse <= self.armerxrange[1]):
            #print("window armer")
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

        headerAux = self.header
        self.header = self.fullsHeader
        self.fullsHeader = headerAux

        armerAux= self.armer
        self.armer= self.fullsArmer
        self.fullsArmer= armerAux

        self.headeryrange = [min(self.header[1], self.header[3]), max(self.header[1], self.header[3])]
        self.headerxrange = [min(self.header[0], self.header[2]), max(self.header[0], self.header[2])]

        self.armeryrange = [min(self.armer[1], self.armer[3]), max(self.armer[1], self.armer[3])]
        self.armerxrange = [min(self.armer[0], self.armer[2]), max(self.armer[0], self.armer[2])]

    def gety0(self):
        return self.vertices[1]

    def getx0(self):
        return self.vertices[0]

    def getyf(self):
        return self.vertices

    def printCoor(self):
        print(f'window at x0={self.x0}, xf={self.xf}, y0= {self.y0}, yf={self.yf}')
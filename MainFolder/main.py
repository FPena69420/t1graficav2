import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
from grafica.gpu_shape import GPUShape
import ShadersFolder.SimpleShaderCopypasta as SPC
import ObjectsToBeDrawnFolder.objectsToBeDrawn as doodle
import ObjectsToBeDrawnFolder.quadAngle as QA

#Controls----------------------------------------------------------------------------

class Controller:
    def __init__(self):
        self.leftClickOn = False
        self.rightClickOn= False
        self.normalMousePos= (0.0, 0.0)

        self.hoveringOnQuad= None
        self.wShouldOpen= False

controller= Controller()

def on_key(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

# Dimensiones de la ventana de la aplicacion
width = 900
wHalf= width/2
height = 700
hHalf= height/2

def cursor_pos_callback(window, x, y):
    global controller
    controller.normalMousePos = ((x-wHalf)/wHalf, -(y-hHalf)/hHalf)

def mouse_button_callback(window, button, action, mods):
    global controller

    overQuad = controller.hoveringOnQuad

    """
    glfw.MOUSE_BUTTON_1: left click
    glfw.MOUSE_BUTTON_2: right click
    glfw.MOUSE_BUTTON_3: scroll click
    """

    if (action == glfw.PRESS or action == glfw.REPEAT):
        if (button == glfw.MOUSE_BUTTON_1):
            controller.leftClickOn = True
            print("Mouse click - button 1")

        if (button == glfw.MOUSE_BUTTON_2):
            controller.rightClickOn = True
            print(f'Mouse click - button 2')

            if overQuad!= None:
                overQuad.clicked()

    elif (action == glfw.RELEASE):
        if (button == glfw.MOUSE_BUTTON_1):
            controller.leftClickOn = False

        if (button == glfw.MOUSE_BUTTON_2):
            controller.rightClickOn = False

#fin controls------------------------------------------------------------------------

if __name__ == '__main__':
    window = None

    # Initialize glfw
    if not glfw.init():
        glfw.set_window_should_close(window, True)
        raise Exception("glfw cannot be initialized.")

    # Se crea la ventana con el titulo asignadog
    window = glfw.create_window(width, height, "DEEZNU OS - Versión de prueba 2.01", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)
        raise Exception("glfw window cannot be created.")

    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)

    #Mouse---------------------------------------------------------------------------

    glfw.set_cursor_pos_callback(window, cursor_pos_callback)
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    #fin de mouse--------------------------------------------------------------------

    #Pipeline------------------------------------------------------------------------

    pipeline= SPC.SimpleShaderProgram()
    glUseProgram(pipeline.shaderProgram)

    #fin pipeline--------------------------------------------------------------------

    #Crear figuras-------------------------------------------------------------------

    quad2 = QA.qAngle(-0.9, 0.9, -0.6, 0.6, [1.0, 1.0, 0.0], "yellow", "windowCarrier")
    chasis2 = doodle.OTBD(pipeline, quad2.getVer(), quad2.getIn()).getGPUThingy()


    quad1 = QA.qAngle(-0.4, 0.9, -0.1, 0.6, [1.0, 0.0, 0.0], "red", "windowCarrier")
    chasis = doodle.OTBD(pipeline, quad1.getVer(), quad1.getIn()).getGPUThingy()

    myWindow= None
    wgpu= None
    closeButton= None
    fullsButton= None

    #Fin crear figuras---------------------------------------------------------------

    #Color de fondo------------------------------------------------------------------

    glClearColor(0.25, 0.25, 0.25, 1.0)

    #fin de color de fondo-----------------------------------------------------------


    while not glfw.window_should_close(window):
        glfw.poll_events()

        #Code------------------------------------------------------------------------

        glClear(GL_COLOR_BUFFER_BIT)

        #Draw: careful with order----------------------------------------------------
        pipeline.drawCall(chasis)
        pipeline.drawCall(chasis2)
        #fin de draw-----------------------------------------------------------------

        myWindow = quad1.getMyWindow() or quad2.getMyWindow()

        if myWindow== None:

            #pipeline.drawCall(chasis)
            #pipeline.drawCall(chasis2)

            if (quad1.hoveringOn(controller.normalMousePos)):
                controller.hoveringOnQuad= quad1
            elif (quad2.hoveringOn(controller.normalMousePos)):
                controller.hoveringOnQuad= quad2
            else:
                controller.hoveringOnQuad= None

        if myWindow!= None:
            controller.hoveringOnQuad = None

            wgpu= doodle.OTBD(pipeline, myWindow.getVer(), myWindow.getIn()).getGPUThingy()
            pipeline.drawCall(wgpu)

            closeButton = myWindow.getCloseButton()
            fullsButton = myWindow.getFullsButton()

            closegpu = doodle.OTBD(pipeline, closeButton.getVer(), closeButton.getIn()).getGPUThingy()
            pipeline.drawCall(closegpu)
            fullsgpu = doodle.OTBD(pipeline, fullsButton.getVer(), fullsButton.getIn()).getGPUThingy()
            pipeline.drawCall(fullsgpu)

            if (closeButton.hoveringOn(controller.normalMousePos)):
                controller.hoveringOnQuad= closeButton
            elif (fullsButton.hoveringOn(controller.normalMousePos)):
                controller.hoveringOnQuad= fullsButton
            else:
                controller.hoveringOnQuad= None

            myWindow = quad1.getMyWindow()


        #end code--------------------------------------------------------------------

        glfw.swap_buffers(window)

    chasis.clear()
    chasis2.clear()
    glfw.terminate()

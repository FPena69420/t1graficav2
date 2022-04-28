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
        self.mousePos = (0.0, 0.0)

controller= Controller()

def on_key(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

def cursor_pos_callback(window, x, y):
    global controller
    controller.mousePos = (x, y)

def mouse_button_callback(window, button, action, mods):
    global controller

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
            print("Mouse click - button 2")

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

    # Dimensiones de la ventana de la aplicacion
    width = 800
    height = 720

    # Se crea la ventana con el titulo asignado
    window = glfw.create_window(width, height, "DEEZNU", None, None)

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

    quad2 = QA.qAngle(-0.9, 0.9, -0.6, 0.6, [1.0, 1.0, 0.0])
    chasis2 = doodle.OTBD(pipeline, quad2.getVer(), quad2.getIn()).getGPUThingy()


    quad1 = QA.qAngle(-0.4, 0.9, -0.1, 0.6, [1.0, 0.0, 0.0])
    chasis = doodle.OTBD(pipeline, quad1.getVer(), quad1.getIn()).getGPUThingy()

    #Fin crear figuras---------------------------------------------------------------

    #Color de fondo------------------------------------------------------------------

    glClearColor(0.4, 0.4, 1.0, 1.0)

    #fin de color de fondo-----------------------------------------------------------


    while not glfw.window_should_close(window):
        glfw.poll_events()

        #Code------------------------------------------------------------------------

        glClear(GL_COLOR_BUFFER_BIT)

        #Draw: careful with order----------------------------------------------------
        pipeline.drawCall(chasis)
        pipeline.drawCall(chasis2)
        #fin de draw-----------------------------------------------------------------



        #end code--------------------------------------------------------------------

        glfw.swap_buffers(window)

    chasis.clear()
    chasis2.clear()
    glfw.terminate()

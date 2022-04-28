from OpenGL.GL import *
from grafica.gpu_shape import GPUShape

class SimpleShaderProgram:
    """
    Clase para guardar los shaders compilados.
    Shader: Programa que define cómo se tratan vértices y píxeles.
    """

    def __init__(self):
        """
        Los shaders se entregan como un string hecho en GLSL
        (Graphic Library Shading Language) muy similar a C
        """

        # Vertex shader con una pequeña modificacion de ejemplo que divide cada coordenada por el numero deseado
        vertex_shader = """
            #version 130

            in vec3 position;
            in vec3 color;

            out vec3 newColor;
            void main()
            {   
                // Nuevo vector para modificar los valores de las coordenadas de la posición
                vec3 newPos = vec3(position[0]/1.0, position[1]/1.0, position[2]/1.0);

                // Se le asigna la posición modificada
                gl_Position = vec4(newPos, 1.0f);

                newColor = color;
            }
            """
        # Fragment shader con una pequeña modificacion de ejemplo para modificar cada componente del color rgb
        fragment_shader = """
            #version 130
            in vec3 newColor;

            out vec4 outColor;
            void main()
            {   
                vec3 finalColor = vec3(newColor.r*1.0, newColor.g*1.0, newColor.b*1.0);

                // Se le asigna el color modificado
                outColor = vec4(finalColor, 1.0f);
            }
            """
        # Se compila el shader (Se transforma el código GLSL a código de chip
        self.shaderProgram = OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))


    def setupVAO(self, gpuShape):
        """
        Se le "dice" al shader cómo leer los bits de la gpuShape asignada
        """

        glBindVertexArray(gpuShape.vao)

        glBindBuffer(GL_ARRAY_BUFFER, gpuShape.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gpuShape.ebo)

        # 3d vertices = 3 * 4 bytes = 12 bytes
        position = glGetAttribLocation(self.shaderProgram, "position")
        glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)
        # 3 colors RGB = 3 * 4 bytes = 12 bytes
        color = glGetAttribLocation(self.shaderProgram, "color")
        glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(color)

        # Unbinding current vao
        glBindVertexArray(0)


    def drawCall(self, gpuShape, mode=GL_TRIANGLES):
        """
        Se dibuja la gpuShape.
        """
        assert isinstance(gpuShape, GPUShape)

        # Binding the VAO and executing the draw call
        glBindVertexArray(gpuShape.vao)
        glDrawElements(mode, gpuShape.size, GL_UNSIGNED_INT, None)

        # Unbind the current VAO
        glBindVertexArray(0)
from grafica.gpu_shape import GPUShape
import ShadersFolder.SimpleShaderCopypasta as SPC
from OpenGL.GL import *

class OTBD:
    def __init__(self, pipeline: SPC.SimpleShaderProgram, vertices, indices):
        self.vertices= vertices
        self.indices= indices
        self.gpuThingy= GPUShape().initBuffers()

        pipeline.setupVAO(self.gpuThingy)

        self.gpuThingy.fillBuffers(self.vertices, self.indices, GL_STATIC_DRAW)


    def getGPUThingy(self):
        return self.gpuThingy
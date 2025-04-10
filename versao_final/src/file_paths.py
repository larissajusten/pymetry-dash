import os
from src.singleton import Singleton
from pygame.locals import *


class FilePaths(Singleton):

    def __init__(self):
        super().__init__()
        current_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
        self.musicas = os.path.join(current_directory, 'musicas')
        self.imagens = os.path.join(current_directory, 'imagens')
        self.mapas = os.path.join(current_directory, 'mapas')


file_paths = FilePaths()

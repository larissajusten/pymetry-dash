import os
from src.singleton import Singleton
from pygame.locals import *

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")

class FilePaths(Singleton):

    def __init__(self):
        super().__init__()
        self.musicas = os.path.join(ASSETS_DIR, 'music')
        self.imagens = os.path.join(ASSETS_DIR, 'imgs')
        self.mapas = os.path.join(ASSETS_DIR, 'maps')


file_paths = FilePaths()

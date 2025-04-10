import os
import sys
from src.singleton import Singleton
from pygame.locals import *

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")


class FilePaths(Singleton):

    def __init__(self):
        super().__init__()

        if hasattr(sys, "_MEIPASS") or sys.platform == "emscripten":
            # Rodando em navegador ou bundle tipo PyInstaller
            self.musicas =  os.fspath(os.path.join(ASSETS_DIR, "sfx/prod"))
            self.imagens = os.fspath(os.path.join(ASSETS_DIR, "img"))
            self.mapas = os.fspath(os.path.join(ASSETS_DIR, "maps"))
        else:
            # Rodando localmente
            self.musicas = os.path.join(ASSETS_DIR, 'sfx')
            self.imagens = os.path.join(ASSETS_DIR, 'img')
            self.mapas = os.path.join(ASSETS_DIR, 'maps')


file_paths = FilePaths()

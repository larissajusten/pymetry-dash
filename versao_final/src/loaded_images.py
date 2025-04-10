from src.singleton import Singleton
import pygame
import os
from pygame.locals import *
from src.file_paths import file_paths


class LoadedImages(Singleton):

    def __init__(self):
        super().__init__()
        self.tela = pygame.display.set_mode((800, 480))

        self.imagens_obtaculos = {'Spike': pygame.image.load(os.fspath(os.path.join(file_paths.imagens, "fake_spike_01.png"))).convert_alpha(),
                                  'Win': pygame.image.load(os.path.join(file_paths.imagens, "win.png")).convert_alpha(),
                                  'Orb': pygame.image.load(os.path.join(file_paths.imagens, "orb_yellow.png")).convert_alpha(),
                                  'Block': pygame.image.load(os.path.join(file_paths.imagens, "block_2.png")).convert_alpha(),
                                  'Portal': pygame.image.load(os.path.join(file_paths.imagens, "portal.png")).convert_alpha(),
                                  'PortalSaida': pygame.image.load(os.path.join(file_paths.imagens, "portal_saida.png")).convert_alpha()
                                  }

        self.imagens_telas = {
            'Menu_skin': self.__add_imagem(
                os.path.join("menu_view", "fundo_menu_skins.png"), 800, 480),
            'Menu_principal': self.__add_imagem(
                os.path.join("menu_view", "fundo_menu.png"), 800, 480),
            'Menu_fases': self.__add_imagem(
                os.path.join("menu_view", "tela_fases.png"), 800, 500),
            'Menu_instrucoes': self.__add_imagem(
                os.path.join("menu_view", "fundo_instrucoes.png"), 800, 480)}

        self.imagens_botoes = {
            'Ret_select_rosa': self.__add_imagem(
                os.path.join("menu_view", "ret_menu.png"), 100, 30),
            'Ret_select_rosa_120': self.__add_imagem(
                os.path.join("menu_view", "ret_menu.png"), 120, 30), }

        self.skin_nave = pygame.image.load(
            os.path.join(file_paths.imagens, "nave_teste.png")).convert_alpha()

        self.imagens_skins = {'Padrão': pygame.image.load(os.path.join(file_paths.imagens, "geo.png")).convert_alpha(),
                              'Azul': pygame.image.load(os.path.join(file_paths.imagens, "geo_blue.jpg")).convert_alpha(),
                              'Glitch': pygame.image.load(os.path.join(file_paths.imagens, "glitch.jpg")).convert_alpha(),
                              'Mine': pygame.image.load(os.path.join(file_paths.imagens, "mine_block.png")).convert_alpha(),
                              'Cubo Mágico': pygame.image.load(os.path.join(file_paths.imagens, "cubo_magico.jpg")).convert_alpha(),
                              'Pride': pygame.image.load(os.path.join(file_paths.imagens, "pride_skin.png")).convert_alpha()}

        self.miniatura_fases = {
            'Blue': self.__add_imagem('fase_01_miniatura.png', 100, 60),
            'Purple': self.__add_imagem('fase_02_miniatura.png', 100, 60),
            'Green': self.__add_imagem('fase_03_miniatura.png', 100, 60),
            'Orange': self.__add_imagem('orange_miniatura.png', 100, 60)
        }

        self.bg_fase = {
            'Blue': pygame.image.load(os.path.join(file_paths.imagens, "bg_blue.png")).convert_alpha(),
            'Purple': pygame.image.load(os.path.join(file_paths.imagens, "bg_purple.jpg")).convert_alpha(),
            'Green': pygame.image.load(os.path.join(file_paths.imagens, "bg_green.png")).convert_alpha(),
            'Orange': pygame.image.load(os.path.join(file_paths.imagens, "bg_orange.png")).convert_alpha(),

        }

        self.floor_fase = {
            'Blue': pygame.image.load(os.path.join(file_paths.imagens, "floor_blue.png")).convert_alpha(),
            'Purple': pygame.image.load(os.path.join(file_paths.imagens, "floor_purple.png")).convert_alpha(),
            'Green': pygame.image.load(os.path.join(file_paths.imagens, "floor_green.png")).convert_alpha(),
            'Orange': pygame.image.load(os.path.join(file_paths.imagens, "floor_orange.png")).convert_alpha(),
        }

    def __add_imagem(self, file_name, size_x, size_y):
        image = pygame.image.load(
            os.path.join(os.fspath(file_paths.imagens), file_name)).convert_alpha()
        return pygame.transform.smoothscale(
            image.convert(), (size_x, size_y))


loaded_images = LoadedImages()

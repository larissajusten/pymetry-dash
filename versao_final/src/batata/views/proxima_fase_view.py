import pygame
from pygame.locals import *
from batata.objects.botao_menu import Botao
from batata.views.abstract_view import AbstractView


class ProximaFaseView(AbstractView):

    def __init__(self) -> None:
        super().__init__(None, None)

        tela = pygame.Surface((500, 200), SRCALPHA)
        pygame.draw.rect(tela, self.COR_BASE_BACKGROUND, tela.get_rect(), 99)
        self.tela = tela

        texto_mensagem = 'Você ganhou!'
        self.tela_texto_mensagem = self.fonte_titulo.render(
            texto_mensagem, 1, (0, 0, 0))

        self.lista_botoes = [
            Botao(imagem=self.fundo_botao_grande, x_pos=240, y_pos=280,
                  mensagem='Proxima fase', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO,
                  cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=360, y_pos=280,
                  mensagem='Reiniciar', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO,
                  cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=470, y_pos=280,
                  mensagem='Menu', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO,
                  cor_mouse=self.COR_MOUSE),
            Botao(imagem=self.fundo_botao, x_pos=580, y_pos=280,
                  mensagem='Sair', fonte=self.fonte_botao,
                  cor_base_texto=self.COR_BASE_TEXTO,
                  cor_mouse=self.COR_MOUSE)
        ]

    def desenha_mensagem(self, tela):
        tela.blit(self.tela_texto_mensagem, (320, 200))

    def desenha(self, tela):
        for botao in self.lista_botoes:
            botao.update(tela)
            botao.muda_cor()

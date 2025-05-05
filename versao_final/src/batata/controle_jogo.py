import pygame
import asyncio
from pygame.locals import *
from batata.views.fim_de_fase_view import FimDeFaseView
from batata.objects.jogador import Jogador
from batata.objects.partida import Partida
from batata.views.menu_view import MenuView
from batata.updater import Updater
from batata.views.escolha_fases_view import EscolhaFasesView
from batata.views.pause_view import PauseView
from batata.views.menu_skin_view import MenuSkinView
from batata.loaded_images import loaded_images
from batata.containers.container_skins import ContainerSkins
from batata.views.instrucoes_view import InstrucoesView
from batata.containers.container_fases import ContainerFases
from batata.views.proxima_fase_view import ProximaFaseView
from batata.views.fim_de_jogo_view import FimDeJogoView

import logging

class ControleJogo():
    def __init__(self):
        self.tela = loaded_images.tela
        self.container_skin = ContainerSkins()
        self.container_fase = ContainerFases()
        self.jogador = Jogador(self.container_skin)
        self.menu_view = MenuView(self.tela)
        self.escolha_fase_view = EscolhaFasesView(
            self.tela, self.container_fase.fases)
        self.pause_view = PauseView()
        self.partida = Partida(self.jogador, self.tela)
        self.updater = Updater(self.jogador, self.partida)
        self.intrucoes_view = InstrucoesView(self.tela)
        self.menu_skin = MenuSkinView(
            self.tela, self.container_skin.skins_quadrado)
        self.fim_de_fase = FimDeFaseView()
        self.proxima_fase = ProximaFaseView()
        self.fim_de_jogo = FimDeJogoView()

        self.flag_transparencia = False
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

async def inicio_jogo():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting Pymetry Dash game...")
    pygame.display.set_caption('Pymetry Dash Menu')
    controle_jogo = ControleJogo()

    while controle_jogo.running:
        await asyncio.sleep(0)
        controle_jogo.menu_view.desenha()
        for event in pygame.event.get():
            if event.type == QUIT:
                controle_jogo.running = False
            if event.type == MOUSEBUTTONDOWN:
                botao_selecionado = next(
                    (botao.mensagem for botao in controle_jogo.menu_view.lista_botoes if botao.is_clicked()), False)

                if botao_selecionado == 'Jogar':
                    return await escolha_fase(controle_jogo)
                elif botao_selecionado == 'Skins':
                    return await selecao_skin(controle_jogo)
                elif botao_selecionado == 'Instruções':
                    return await mostra_intrucoes(controle_jogo)
                elif botao_selecionado == 'Sair':
                    controle_jogo.running = False

        controle_jogo.clock.tick(controle_jogo.FPS)

    pygame.display.quit()
    pygame.quit()

async def mostra_intrucoes(controle_jogo):
    pygame.display.set_caption('Menu Instruções')

    while True:
        await asyncio.sleep(0)
        controle_jogo.intrucoes_view.desenha()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if controle_jogo.intrucoes_view.botao_voltar.is_clicked():
                    return await inicio_jogo()
        controle_jogo.clock.tick(controle_jogo.FPS)

async def selecao_skin(controle_jogo):
    pygame.display.set_caption('Menu Seleção de Skin')

    while True:
        await asyncio.sleep(0)
        controle_jogo.menu_skin.desenha()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                for botao_tup in controle_jogo.menu_skin.lista_botoes:
                    if botao_tup[0].is_clicked(
                    ) and botao_tup[0].mensagem == 'Voltar':
                        return await inicio_jogo()
                    elif botao_tup[0].is_clicked():
                        # clicou em um botão e não é o de voltar
                        skin = controle_jogo.container_skin.skins_quadrado[botao_tup[1]]
                        controle_jogo.jogador.muda_skin(skin)
                        controle_jogo.menu_skin.seleciona_skin(skin.arquivo)
        controle_jogo.clock.tick(controle_jogo.FPS)

async def escolha_fase(controle_jogo):
    pygame.display.set_caption('Menu Escolha de Fase')

    while True:
        await asyncio.sleep(0)
        controle_jogo.escolha_fase_view.desenha()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for botao_tup in controle_jogo.escolha_fase_view.lista_botoes:
                    if botao_tup[0].is_clicked(
                    ) and botao_tup[0].mensagem == 'Voltar':
                        return await inicio_jogo()
                    elif botao_tup[0].is_clicked():
                        # clicou em um botão e não é o de voltar
                        controle_jogo.partida.fase = controle_jogo.container_fase.fases[botao_tup[1]]
                        return await iniciar_partida(controle_jogo)
        controle_jogo.clock.tick(controle_jogo.FPS)

async def iniciar_partida(controle_jogo):
    pygame.display.set_caption('Pymetry Dash')

    controle_jogo.jogador.muda_skin(controle_jogo.jogador.skin_atual)
    controle_jogo.partida.inicia()
    jogador_group = pygame.sprite.Group()
    jogador_group.add(controle_jogo.jogador)
    flag_pausar_jogo = False
    jogando = True

    while True:
        await asyncio.sleep(0)
        pygame.display.update()
        if not flag_pausar_jogo and not controle_jogo.jogador.morte and not controle_jogo.jogador.vitoria:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if not controle_jogo.jogador.morte and not controle_jogo.jogador.vitoria and not flag_pausar_jogo:
                            controle_jogo.partida.tela.blit(
                                controle_jogo.pause_view.tela, (150, 140))
                            flag_pausar_jogo = True
                            jogando = False
        keys_pressed = pygame.key.get_pressed()

        if flag_pausar_jogo:
            jogando = False
            sair_do_jogo_pausado = await pausar_jogo(controle_jogo)
            if sair_do_jogo_pausado:
                flag_pausar_jogo = False
                jogando = True

        if controle_jogo.jogador.morte:
            jogando = False
            controle_jogo.tela.blit(controle_jogo.fim_de_fase.tela, (150, 140)
                            ) if not controle_jogo.flag_transparencia else None
            controle_jogo.flag_transparencia = True
            await perdeu_a_fase(controle_jogo)

        index_fase_atual = controle_jogo.container_fase.fases.index(
            controle_jogo.partida.fase)
        if controle_jogo.jogador.vitoria and index_fase_atual+1 == len(controle_jogo.container_fase.fases):
            jogando = False
            controle_jogo.tela.blit(controle_jogo.fim_de_jogo.tela, (150, 140)
                            ) if not controle_jogo.flag_transparencia else None
            controle_jogo.flag_transparencia = True
            await terminou_o_jogo(controle_jogo)

        if controle_jogo.jogador.vitoria and not index_fase_atual+1 == len(controle_jogo.container_fase.fases):
            jogando = False
            controle_jogo.tela.blit(controle_jogo.proxima_fase.tela, (150, 140)
                            ) if not controle_jogo.flag_transparencia else None
            controle_jogo.flag_transparencia = True
            await passou_de_fase(controle_jogo)

        if jogando:
            controle_jogo.flag_transparencia = False
            if keys_pressed[K_SPACE]:
                if controle_jogo.jogador.voo:
                    controle_jogo.jogador.velocidade.y = 0
                    controle_jogo.jogador.pular()
                else:
                    if controle_jogo.jogador.nochao:
                        controle_jogo.jogador.pular()

            controle_jogo.partida.draw_bg()
            controle_jogo.partida.desenhar_elementos()
            controle_jogo.updater.update_partida(controle_jogo.jogador.velocidade.x)
            jogador_group.draw(controle_jogo.partida.tela)
            controle_jogo.updater.update_jogador(keys_pressed)

        controle_jogo.clock.tick(controle_jogo.FPS)

async def perdeu_a_fase(controle_jogo):
    controle_jogo.partida.para_musica()
    controle_jogo.fim_de_fase.desenha_mensagem(controle_jogo.tela)
    controle_jogo.fim_de_fase.desenha(controle_jogo.tela)
    botao_selecionado = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                botao_selecionado = next(
                    (botao.mensagem for botao in controle_jogo.fim_de_fase.lista_botoes if botao.is_clicked()), False)

    if botao_selecionado:
        if botao_selecionado == 'Menu':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await inicio_jogo()
        elif botao_selecionado == 'Reiniciar':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await iniciar_partida(controle_jogo)
        elif botao_selecionado == 'Sair':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            pygame.display.quit()
            pygame.quit()
            exit()

async def passou_de_fase(controle_jogo):
    controle_jogo.partida.para_musica()
    controle_jogo.proxima_fase.desenha_mensagem(controle_jogo.tela)
    controle_jogo.proxima_fase.desenha(controle_jogo.tela)
    botao_selecionado = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                botao_selecionado = next(
                    (botao.mensagem for botao in controle_jogo.proxima_fase.lista_botoes if botao.is_clicked()), False)

    if botao_selecionado:
        if botao_selecionado == 'Proxima fase':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            index_fase_atual = controle_jogo.container_fase.fases.index(
                controle_jogo.partida.fase)
            controle_jogo.partida.fase = controle_jogo.container_fase.fases[index_fase_atual+1]
            await iniciar_partida(controle_jogo)
        if botao_selecionado == 'Menu':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await inicio_jogo()
        elif botao_selecionado == 'Reiniciar':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await iniciar_partida(controle_jogo)
        elif botao_selecionado == 'Sair':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            pygame.display.quit()
            pygame.quit()
            exit()

async def terminou_o_jogo(controle_jogo):
    controle_jogo.partida.para_musica()
    controle_jogo.fim_de_jogo.desenha_mensagem(controle_jogo.tela)
    controle_jogo.fim_de_jogo.desenha(controle_jogo.tela)
    botao_selecionado = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                botao_selecionado = next(
                    (botao.mensagem for botao in controle_jogo.fim_de_jogo.lista_botoes if botao.is_clicked()), False)

    if botao_selecionado:
        if botao_selecionado == 'Reiniciar':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await iniciar_partida(controle_jogo)
        elif botao_selecionado == 'Menu':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await inicio_jogo()
        elif botao_selecionado == 'Sair':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            pygame.display.quit()
            pygame.quit()
            exit()

async def pausar_jogo(controle_jogo):
    controle_jogo.partida.pausa_musica()
    controle_jogo.jogador.parar_jogador()
    controle_jogo.pause_view.desenha_mensagem(controle_jogo.partida.tela)
    controle_jogo.pause_view.desenha(controle_jogo.partida.tela)
    botao_selecionado = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                botao_selecionado = next(
                    (botao.mensagem for botao in controle_jogo.pause_view.lista_botoes if botao.is_clicked()), False)

    if botao_selecionado:
        if botao_selecionado == 'Continuar':
            controle_jogo.jogador.continuar_jogador()
            controle_jogo.partida.despausa_musica()
            return True
        elif botao_selecionado == 'Menu':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await inicio_jogo()
        elif botao_selecionado == 'Reiniciar':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            await iniciar_partida(controle_jogo)
        elif botao_selecionado == 'Sair':
            controle_jogo.jogador.resetar()
            controle_jogo.partida.para_musica()
            pygame.display.quit()
            pygame.quit()
            exit()

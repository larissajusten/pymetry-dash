"""Root `__init__` of the views module setting the `__all__` of views modules."""


from batata.views.abstract_view import AbstractView
from batata.views.escolha_fases_view import EscolhaFasesView
from batata.views.fim_de_fase_view import FimDeFaseView
from batata.views.fim_de_jogo_view import FimDeJogoView
from batata.views.instrucoes_view import InstrucoesView
from batata.views.menu_skin_view import MenuSkinView
from batata.views.menu_view import MenuView
from batata.views.pause_view import PauseView
from batata.views.proxima_fase_view import ProximaFaseView


__all__ = [
    # views
    "AbstractView",
    "EscolhaFasesView",
    "FimDeFaseView",
    "FimDeJogoView",
    "InstrucoesView",
    "MenuSkinView",
    "MenuView",
    "register",
    "PauseView",
    "ProximaFaseView",
]
"""Root `__init__` of the objects module setting the `__all__` of objects modules."""


from batata.objects.botao_menu import Botao
from batata.objects.colisao import Colisao
from batata.objects.fase import Fase
from batata.objects.jogador import Jogador
from batata.objects.obstaculos import Obstaculo
from batata.objects.partida import Partida
from batata.objects.skin import Skin


__all__ = [
    # objects
    "Botao",
    "Colisao",
    "Fase",
    "Jogador",
    "Obstaculo",
    "Partida",
    "Skin",
]
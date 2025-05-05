"""Root `__init__` of the batata module setting the `__all__` of batata modules."""

from batata import containers, objects, views
from batata.controle_jogo import ControleJogo, inicio_jogo
from batata.file_paths import FilePaths
from batata.loaded_images import loaded_images
from batata.singleton import Singleton
from batata.updater import Updater
from batata.objects import Skin, Partida, Obstaculo, Jogador, Fase, Colisao, Botao


__all__ = [
    "inicio_jogo",
    # objects
    "Skin",
    "Partida",
    "Obstaculo",
    "Jogador",
    "Fase",
    "Colisao",
    "Botao",
    # core classes
    "ControleJogo",
    "FilePaths",
    "loaded_images",
    "Singleton",
    "RewardWrapper",
    "Updater",
    # module folders
    "containers",
    "objects",
    "views",
]

# Grupo 6 - Pymetry Dash

Disponivel em https://ambitious-flower-0faa8c510.6.azurestaticapps.net.

Este jogo tem como modelo o estilo de jogo de Geometry Dash, tendo jogabilidade similiar. O jogador precisa atravessar uma série de obstáculos, sem colisão e assim conseguir chegar ao final da fase.

## Instruções de jogo

> **Pular:** Para pular você deve apertar a tecla `ESPAÇO` do teclado. <br>
> **Pausar o jogo:** Para pausa o jogo você deve apertar a tecla `ESC` do teclado. <br>

## Instalação
Para a instalação você precisa utilizar o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/).

```bash
py -3.11 -m pip install -r requirements.txt
```

## Uso
Para abrir o jogo você deve abrir o terminal de comando no seu computador e digitar o seguindo comando dentro da pasta do jogo (lugar onde se encontra esse arquivo).

```python
python main.py
```

## Uso de [pygbag](https://pypi.org/project/pygbag/)
_Pygbag compila jogos Pygame para WebAssembly usando Emscripten_

Para rodar o arquivo .py no navegador utilize o seguite comando dentro da pasta do jogo (lugar onde se encontra esse arquivo).

```python
pygbag main.py
```

Logo após acesse em: http://localhost:8000
Acesso com debug: http://localhost:8000?-i


## Contribuições
Pull requests são bem-vindos. Para grandes mudanças, por favor, abra um issue primeiro para discutir o que você gostaria de mudar.

## License
[MIT](https://choosealicense.com/licenses/mit/)

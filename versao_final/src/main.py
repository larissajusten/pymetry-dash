import asyncio
import pygame
from batata import inicio_jogo

async def main():
    pygame.init()
    await inicio_jogo()


if __name__ == "__main__":
    asyncio.run(main())

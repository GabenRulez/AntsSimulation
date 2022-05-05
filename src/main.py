import pygame
from WorldMap import WorldMap
import WorldMap
from Position import Position

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")

gameData = {
    "fps_limit": 60,
    "running": False,
    "clock": pygame.time.Clock(),
    "worldMap": WorldMap.WorldMap(0, 0),
}


def main():
    gameData["clock"] = pygame.time.Clock()
    setup()

    while gameData["running"]:
        loop()

    pygame.quit()


def setup():
    gameData["running"] = True
    gameData["worldMap"] = WorldMap.WorldMap(200, 100)


def loop():
    gameData["clock"].tick(gameData["fps_limit"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameData["running"] = False

    WIN.fill((63, 142, 252))

    pygame.display.update()


if __name__ == "__main__":
    main()

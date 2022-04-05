import pygame

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")

gameData = {
    "running": False,
    "window": WIN
}

def main():
    setup()

    while gameData["running"]:
        loop()

    pygame.quit()


def setup():
    gameData["running"] = True


def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameData["running"] = False

    WIN.fill((127,127,127))
    pygame.display.update()

def setup_pygame():


if __name__ == "__main__":
    main()
import pygame
import WorldMap
import Nest
from Position import Position
from Ant import Ant
import numpy as np

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")

gameData = {
    "fps_limit": 60,
    "running": False,
    "clock": pygame.time.Clock(),
    "worldMap": WorldMap.WorldMap(0, 0),
    "screenWidth": 1920,
    "screenHeight": 1080,
    "window": None,
    "antsNest": Nest.Nest(Position(100, 50))
}


def main():
    gameData["clock"] = pygame.time.Clock()
    setup()

    while gameData["running"]:
        loop()

    pygame.quit()


def setup():
    gameData["running"] = True
    worldMap = WorldMap.WorldMap(200, 200)
    gameData["worldMap"] = worldMap
    worldMap.addAnt(Ant(Position(150, 50), worldMap))
    worldMap.addAnt(Ant(Position(50, 50), worldMap))
    worldMap.addAnt(Ant(Position(150, 150), worldMap))
    worldMap.addAnt(Ant(Position(50, 150), worldMap))


    gameData["window"] = pygame.display.set_mode((gameData["screenWidth"], gameData["screenHeight"]), flags=pygame.RESIZABLE)
    updateScreenInfo()


def loop():
    gameData["clock"].tick(gameData["fps_limit"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameData["running"] = False

    drawBackground()
    drawNest()
    drawFood()
    drawAnts()

    pygame.display.update()


def drawBackground():
    BACKGROUND_COLOR = (0,0,0)
    MAP_COLOR = (207, 136, 70)

    WIN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(gameData["window"], MAP_COLOR, (0, 0, gameData["worldMap"].width, gameData["worldMap"].height))

def drawNest():
    NEST_COLOR = (255,0,0)
    pygame.draw.circle(gameData["window"], NEST_COLOR, (gameData["antsNest"].position.x, gameData["antsNest"].position.y), 10)

def drawFood():
    FOOD_COLOR = (0,255,0)
    for food in gameData["worldMap"].foods:
        pygame.draw.circle(gameData["window"], FOOD_COLOR, (food.position.x, food.position.y), 1)

def drawAnts():
    ANT_COLOR = (255,255,255)

    def DrawArrow(x, y, angle=0):
        def rotate(pos, angle):
            cen = (5 + x, 0 + y)
            angle *= -(np.pi / 180)
            cos_theta = np.cos(angle)
            sin_theta = np.sin(angle)
            ret = ((cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1])) + cen[0],
                   (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1])) + cen[1])
            return ret

        p0 = rotate((0 + x, -4 + y), angle + 90)
        p1 = rotate((0 + x, 4 + y), angle + 90)
        p2 = rotate((10 + x, 0 + y), angle + 90)

        pygame.draw.polygon(gameData["window"], ANT_COLOR, [p0, p1, p2])

    for ant in gameData["worldMap"].ants:
        DrawArrow(ant.pos.x, ant.pos.y, ant.direction)



def updateScreenInfo():
    screenInfo = pygame.display.Info()
    gameData["screenWidth"] = screenInfo.current_w
    gameData["screenHeight"] = screenInfo.current_h


if __name__ == "__main__":
    main()

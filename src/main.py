import pygame
import WorldMap
import Nest
from Position import Position
from Ant import Ant
import numpy as np
from PheromoneType import PheromoneType

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")

gameData = {
    "fps_limit": 60,
    "running": False,
    "clock": pygame.time.Clock(),
    "worldMap": WorldMap.WorldMap(0, 0),
    "screenWidth": 1280,
    "screenHeight": 720,
    "window": None,
}


def main():
    gameData["clock"] = pygame.time.Clock()
    setup()

    while gameData["running"]:
        loop()

    pygame.quit()


def setup():
    gameData["running"] = True
    worldMap = WorldMap.WorldMap(gameData["screenWidth"], gameData["screenHeight"])
    gameData["worldMap"] = worldMap
    gameData["antsNest"] = Nest.Nest(Position(100, 100), 50, worldMap)

    for _ in range(10):
        antSpawnPosition = Position(np.random.uniform(low=0, high=gameData["screenWidth"]),  np.random.uniform(low=0, high=gameData["screenHeight"]))
        worldMap.addAnt(Ant(antSpawnPosition, worldMap))

    worldMap.spawnFoodClump(Position(700, 300), 100)

    gameData["window"] = pygame.display.set_mode(
        (gameData["screenWidth"], gameData["screenHeight"]), flags=pygame.RESIZABLE
    )
    updateScreenInfo()


def loop():
    gameData["clock"].tick(gameData["fps_limit"])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameData["running"] = False

    updateAllAnts()
    gameData["antsNest"].update()
    gameData["worldMap"].updatePheromones()

    drawBackground()
    drawNest()
    drawFood()
    drawPheromones()
    drawAnts()

    pygame.display.update()


def drawBackground():
    BACKGROUND_COLOR = (0, 0, 0)
    MAP_COLOR = (207, 136, 70)

    WIN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(
        gameData["window"],
        MAP_COLOR,
        (0, 0, gameData["worldMap"].width, gameData["worldMap"].height),
    )


def drawNest():
    NEST_COLOR = (255, 0, 0)
    pygame.draw.circle(
        gameData["window"],
        NEST_COLOR,
        (gameData["antsNest"].position.x, gameData["antsNest"].position.y),
        gameData["antsNest"].radius,
    )


def drawFood():
    FOOD_COLOR = (0, 255, 0)
    for food in gameData["worldMap"].foods:
        pygame.draw.circle(
            gameData["window"], FOOD_COLOR, (food.position.x, food.position.y), 1
        )


def drawPheromones():
    for pheromone in gameData["worldMap"].pheromones:
        pheromoneStrength = min(pheromone.strength, 255)
        pheromoneColor = (pheromoneStrength, pheromoneStrength, pheromoneStrength)
        x = pheromone.position.x
        y = pheromone.position.y
        pygame.draw.circle(gameData["window"], pheromoneColor, (x, y), 1)


def drawAnts():
    ANT_COLOR = (255, 255, 255)

    def DrawArrow(x, y, angle=0):
        def rotate(pos, angle):
            cen = (5 + x, 0 + y)
            angle *= -(np.pi / 180)
            cos_theta = np.cos(angle)
            sin_theta = np.sin(angle)
            ret = (
                (cos_theta * (pos[0] - cen[0]) - sin_theta * (pos[1] - cen[1]))
                + cen[0],
                (sin_theta * (pos[0] - cen[0]) + cos_theta * (pos[1] - cen[1]))
                + cen[1],
            )
            return ret

        p0 = rotate((0 + x, -4 + y), angle + 90)
        p1 = rotate((0 + x, 4 + y), angle + 90)
        p2 = rotate((10 + x, 0 + y), angle + 90)

        pygame.draw.polygon(gameData["window"], ANT_COLOR, [p0, p1, p2])

    for ant in gameData["worldMap"].ants:
        DrawArrow(ant.position.x, ant.position.y, ant.direction)


def updateScreenInfo():
    screenInfo = pygame.display.Info()
    gameData["screenWidth"] = screenInfo.current_w
    gameData["screenHeight"] = screenInfo.current_h


def updateAllAnts():
    for ant in gameData["worldMap"].ants:
        ant.update()


if __name__ == "__main__":
    main()

import random
import pygame, emoji
import WorldMap
import Nest
from Position import Position
from Ant import Ant
import numpy as np
from PheromoneType import PheromoneType
from enum import Enum
import pygame.freetype  # Import the freetype module.


mapColors = {
    "map": (102, 255, 179),
    "nest_a": (0, 128, 64),
    "nest_b": (40, 168, 104),
    "food": (127, 176, 105),
    "ant": (0, 0, 0),
    "trail_pheromone": (255, 153, 0),
    "food_pheromone": (0, 0, 255),
}

WIDTH, HEIGHT = 1920, 1080
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")
# GAME_FONT = pygame.freetype.Font(24)
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.
GAME_FONT = pygame.font.SysFont("arialunicode", 30)

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
        antSpawnPosition = Position(
            np.random.uniform(low=0, high=gameData["screenWidth"]),
            np.random.uniform(low=0, high=gameData["screenHeight"]),
        )
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

    WIN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(
        gameData["window"],
        mapColors["map"],
        (0, 0, gameData["worldMap"].width, gameData["worldMap"].height),
    )


def drawNest():
    ringWidth = 5
    for i in range(gameData["antsNest"].radius // ringWidth):
        if i % 2 == 0:
            color = mapColors["nest_a"]
        else:

            color = mapColors["nest_b"]

        pygame.draw.circle(
            gameData["window"],
            color,
            (gameData["antsNest"].position.x, gameData["antsNest"].position.y),
            gameData["antsNest"].radius - i * ringWidth,
        )


def drawFood():
    for food in gameData["worldMap"].foods:

        # img1 = GAME_FONT.render("★", True, (r,g,b))
        # WIN.blit(img1, (food.position.x, food.position.y))

        pygame.draw.circle(
            gameData["window"], mapColors["food"], (food.position.x, food.position.y), 2
        )


def drawPheromones():
    foodPheromonesColor = (63, 94, 49)
    foodPheromonesColor = (255, 255, 0)
    trailPheromonesColor = (29, 26, 5)

    for pheromone in gameData["worldMap"].pheromones:
        pheromoneStrength = min(pheromone.strength, 255)
        maxPheromoneStrength = 255

        if pheromone.type == PheromoneType.TRAIL:
            initialPheromoneColor = mapColors["trail_pheromone"]

        else:
            initialPheromoneColor = mapColors["food_pheromone"]

        r, g, b = (
            initialPheromoneColor[0],
            initialPheromoneColor[1],
            initialPheromoneColor[2],
        )
        r_0, g_0, b_0 = mapColors["map"][0], mapColors["map"][1], mapColors["map"][2]

        pheromoneColor = (
            int(
                float(
                    (
                        r * pheromoneStrength
                        + r_0 * (maxPheromoneStrength - pheromoneStrength)
                    )
                    / maxPheromoneStrength
                )
            ),
            int(
                float(
                    (
                        g * pheromoneStrength
                        + g_0 * (maxPheromoneStrength - pheromoneStrength)
                    )
                    / maxPheromoneStrength
                )
            ),
            int(
                float(
                    (
                        b * pheromoneStrength
                        + b_0 * (maxPheromoneStrength - pheromoneStrength)
                    )
                    / maxPheromoneStrength
                )
            ),
        )

        x = pheromone.position.x
        y = pheromone.position.y

        pygame.draw.circle(gameData["window"], pheromoneColor, (x, y), 3)


def drawAnts():
    antRad = 5

    for ant in gameData["worldMap"].ants:
        antPosition = ant.position
        pygame.draw.circle(
            gameData["window"], mapColors["ant"], (antPosition.x, antPosition.y), antRad
        )

        headPosition = antPosition.pointAtAngle(ant.direction, antRad * (2 / 3))
        pygame.draw.circle(
            gameData["window"],
            mapColors["ant"],
            (headPosition.x, headPosition.y),
            antRad,
        )

        backPosition = antPosition.pointAtAngle(ant.direction, -antRad * (2 / 3))
        pygame.draw.circle(
            gameData["window"],
            mapColors["ant"],
            (backPosition.x, backPosition.y),
            antRad,
        )


def updateScreenInfo():
    screenInfo = pygame.display.Info()
    gameData["screenWidth"] = screenInfo.current_w
    gameData["screenHeight"] = screenInfo.current_h


def updateAllAnts():
    for ant in gameData["worldMap"].ants:
        ant.update()


if __name__ == "__main__":
    main()

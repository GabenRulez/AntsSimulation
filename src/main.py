from typing import Union

import pygame

# import pygame_textinput
import WorldMap
import Nest
from Position import Position
from Ant import Ant
import numpy as np
from PheromoneType import PheromoneType


mapColors = {
    "extra": (229, 208, 204),
    "background": (23, 33, 33),
    "map": (127, 123, 130),
    "nest": (68, 69, 84),
    "trail_pheromone": (191, 172, 181),
    "food_pheromone": (182, 198, 73),
    "food": (218, 255, 125),
    "ant": (23, 33, 33),
}

WIDTH, HEIGHT = 1920, 1080
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ants Simulation")

# SIDE MENU
pygame.font.init()
GAME_FONT_LARGE = pygame.font.SysFont("arialunicode", 60)
GAME_FONT = pygame.font.SysFont("arialunicode", 30)
# amountOfAntsInput = pygame_textinput.TextInputVisualizer()

gameData = {
    "fps_limit": 60,
    "running": False,
    "clock": pygame.time.Clock(),
    "worldMap": WorldMap.WorldMap.emptyObject(),
    "mapWidth": 1920,
    "sideMenuWidth": 0,
    "mapHeight": 1080,
    "window": Union[pygame.Surface, pygame.SurfaceType],
    "startingAntsAmount": 100,
    "antsNest": Nest.Nest.emptyObject(),
}


def main():
    gameData["clock"] = pygame.time.Clock()

    setup()

    while gameData["running"]:
        loop()

    pygame.quit()


def setup():
    gameData["running"] = True
    worldMap = WorldMap.WorldMap(gameData["mapWidth"], gameData["mapHeight"])
    gameData["worldMap"] = worldMap

    nestPosition = Position(
        float(gameData["mapWidth"]) / 10 * 3, float(gameData["mapHeight"]) / 10 * 3
    )
    gameData["antsNest"] = Nest.Nest(
        position=nestPosition,
        radius=75,
        worldMap=worldMap,
        antsToSpawn=gameData["startingAntsAmount"],
    )

    worldMap.spawnFoodClump(
        position=Position(
            gameData["mapWidth"] / 10 * 7, gameData["mapHeight"] / 10 * 7
        ),
        amount=gameData["startingAntsAmount"] * 5,
        recoil=gameData["mapHeight"] / 20,
    )

    gameData["window"] = pygame.display.set_mode(
        (gameData["mapWidth"] + gameData["sideMenuWidth"], gameData["mapHeight"]),
        flags=pygame.RESIZABLE,
    )
    updateScreenInfo()


def loop():
    gameData["clock"].tick(gameData["fps_limit"])
    events = pygame.event.get()
    for event in events:
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
    # drawSideMenu(events)

    pygame.display.update()


def drawSideMenu(events):
    x_start = gameData["mapWidth"]
    y_start = 0
    pygame.draw.rect(
        gameData["window"],
        mapColors["menu"],
        (
            x_start,
            y_start,
            x_start + gameData["sideMenuWidth"],
            y_start + gameData["worldMap"].height,
        ),
    )

    MenuLabel = GAME_FONT_LARGE.render("MENU", True, (0, 255, 0))
    WIN.blit(MenuLabel, (x_start + 10, 10))

    amountOfAntsLabel = GAME_FONT.render("Number of ants:", True, (0, 255, 0))
    WIN.blit(amountOfAntsLabel, (x_start + 10, 140))

    # amountOfAntsInput.update(events)
    # WIN.blit(amountOfAntsInput.surface, (x_start + 10, 200))


def drawBackground():
    BACKGROUND_COLOR = (0, 0, 0)

    WIN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(
        gameData["window"],
        mapColors["map"],
        (0, 0, gameData["worldMap"].width, gameData["worldMap"].height),
    )


def drawNest():
    nest = gameData["antsNest"]
    pygame.draw.circle(
        gameData["window"], mapColors["nest"], nest.position.get(), nest.radius
    )


def drawFood():
    queriedFood = []
    gameData["worldMap"].foods.query(
        gameData["worldMap"].boundary, found_objects=queriedFood
    )
    for food in queriedFood:
        pygame.draw.circle(
            gameData["window"], mapColors["food"], food.position.get(), 2
        )


def drawPheromones():
    for pheromone in gameData["worldMap"].pheromones.query(
        gameData["worldMap"].boundary, found_objects=[]
    ):
        if pheromone.type == PheromoneType.HOME:
            colorA = pygame.Color(mapColors["trail_pheromone"])

        else:
            colorA = pygame.Color(mapColors["food_pheromone"])

        finalColor = colorA.lerp(
            pygame.Color(mapColors["map"]),
            1.0 - pheromone.strength / pheromone.startingStrength,
        )

        pygame.draw.circle(gameData["window"], finalColor, pheromone.position.get(), 3)


def drawAnts():
    antRad = 5
    for ant in gameData["worldMap"].ants:
        # pygame.draw.circle(gameData["window"], mapColors["menu"], (antPosition.x, antPosition.y), ant.seeing_radius)
        pygame.draw.circle(
            gameData["window"], mapColors["ant"], ant.position.get(), antRad
        )


def updateScreenInfo():
    screenInfo = pygame.display.Info()
    # gameData["mapWidth"] = screenInfo.current_w
    # gameData["mapHeight"] = screenInfo.current_h


def updateAllAnts():
    for ant in gameData["worldMap"].ants:
        ant.update()


if __name__ == "__main__":
    main()

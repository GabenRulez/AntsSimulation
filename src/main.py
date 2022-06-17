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
    "ant": (23, 33, 33)
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
    "worldMap": WorldMap.WorldMap(0, 0),
    "mapWidth": 1920,  # 876,
    "sideMenuWidth": 0,  # 256,
    "mapHeight": 1080,  # 720,
    "window": None,
    "startingAntsAmount": 25,
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
    gameData["antsNest"] = Nest.Nest(nestPosition, 50, worldMap)

    for _ in range(gameData["startingAntsAmount"]):
        worldMap.addAnt(Ant(nestPosition, worldMap))

    worldMap.spawnFoodClump(
        Position(gameData["mapWidth"] / 10 * 7, gameData["mapHeight"] / 10 * 7),
        gameData["startingAntsAmount"] * 5,
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
    queriedFood = []
    gameData["worldMap"].foods.query(
        gameData["worldMap"].boundary, found_objects=queriedFood
    )
    for food in queriedFood:
        pygame.draw.circle(
            gameData["window"], mapColors["food"], (food.position.x, food.position.y), 2
        )


def drawPheromones():
    for pheromone in gameData["worldMap"].pheromones.query(
        gameData["worldMap"].boundary, found_objects=[]
    ):
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

        """
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
        """
        pheromoneColor = (0, 0, 0)

        x = pheromone.position.x
        y = pheromone.position.y

        pygame.draw.circle(gameData["window"], pheromoneColor, (x, y), 3)


def drawAnts():
    antRad = 5

    for ant in gameData["worldMap"].ants:

        antPosition = ant.position

        # pygame.draw.circle(gameData["window"], mapColors["menu"], (antPosition.x, antPosition.y), ant.seeing_radius)

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
    # gameData["mapWidth"] = screenInfo.current_w
    # gameData["mapHeight"] = screenInfo.current_h


def updateAllAnts():
    for ant in gameData["worldMap"].ants:
        ant.update()


if __name__ == "__main__":
    main()

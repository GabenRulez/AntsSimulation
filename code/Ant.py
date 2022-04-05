class Ant:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.sense_angle = 60
        self.walking_speed = 100
        # self.age = 0
        self.holding_food = False

    def decide(self):
        # Detect pheromones in cone shape in front of the ant.
        # Take the angle from ant's `self.sense_angle`.

        # Roll a dice and depending on the result:
        # Go right
        # Go left
        # Go towards the center of trail pheromones (towards food)
        # - this option should have the biggest chance of happening
        # If you have food go towards the center of "return to base pheromones"

        # Return the angle of "desired movement"
        pass

    def move(self):
        # Make a decision on the direction of your movement.
        direction = self.decide()

        # (Possible in the future) Check for obstacles on your path.

        # Create a "move" vector depending on the "direction" and "walking_speed" constant.
        # The "walking_speed" depends on whether the ant holds food.
        # (Possible in the future) The "walking_speed" depends on the ant's age.
        # (Possible in the future) The "walking_speed" depends on the angle of the terrain.
        # (Possible in the future) The "walking_speed" depends on the wind.

        # Spawn a "ReturnPheromone" or "FoodPheromone" depending on the current state of "holding_food".
        pass

    def mark_food_trail(self):
        # Invoke when you have found food.
        # It will be used in order for other ants to find the food more optimally.

        # Spawn a "FoodPheromone" object.
        # This object will have lifespan that will gradually go down until it disappears.

        pass

    def mark_return_trail(self):
        # Invoke when you are looking for food.
        # It will be used in order to find optimal return path to the nest.

        # Spawn a "ReturnPheromone" object.
        # This object will have lifespan that will gradually go down until it disappears.
        pass

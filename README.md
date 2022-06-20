# AntsSimulation
## <i>Simulation of natural creation of tracks with pheromone-based communication.<i>


## Project description
Project for "System Modelling and Simulation" ("Modelowanie i Symulacja Systemów") course of Computer Science Master's major in AGH Academy of Science and Technology.

### Main world concepts:
 - The world is rectangular and two dimensional 🌍
 - Each ant thinks for itself and acts on it's own depending on: the random factor, the strength and type of pheromones in it's viscinity in front of them. 🧠
 - The ants target is to find food and get it back to their nest. 🍕
 - The ants leave traces of pheromones wherever they go ("return to base" pheromone). 🧭
 - When an ant finds food source, it leaves traces of a different pheromone ("food source" pheromone). 🐜

 ### Algorithm of decision making
 ```mermaid
graph LR;
    A(Choose your direction) --> B{Are you holding <br/> food right now?};
    B --->|YES| C(Track<br/><br/>HOME<br/><br/>pheromone)
    B --->|NO| D(Track<br/><br/>FOOD<br/><br/>pheromone)
    C --->E(Divide your field of view into<br/>three circular sectors)
    D ---> E
    E ---> F(Perform ranom move<br/>toward sector with the<br/>strongest pheromone track)
 
 classDef orange fill:#fb8,stroke:#d74,stroke-width:2px;
     class sq,e green
     class B orange
```
 
 ### Example Results

 |Active tracks| Dying tracks|
 |---|---|
 |![image](https://user-images.githubusercontent.com/56199675/174561626-3a195fe7-6d99-488e-b0a7-02091aa6a3eb.png)|![image](https://user-images.githubusercontent.com/56199675/174570572-d1d48752-c38b-483e-9786-7b5e51cb5adc.png)|

### Possible world concepts:
 - The world is 3D. It has depth and depending on this depth the ants go slower/faster.
 - The world has obstacles that ants can't get through.
 - The pheromones change their position based on the wind.
 - The pheromones diffuse faster or slower depending on the temperature.
 - There are multiple nests (factions) of ants that don't cooperate with each other and prefer to stay separate.
 - Ants die when they're not in their nest for too long. They also change their choices depending on their own health.

### Environment
 - Language: ![Python](https://www.python.org/) `3.10.3`
 - Game engine: ![Pygame](https://www.pygame.org/wiki/about)

# AntsSimulation
## <i>Simulation of natural creation of tracks with pheromone-based communication.<i>


## Project description
Project for "System Modelling and Simulation" ("Modelowanie i Symulacja Systemów") course of Computer Science Master's major in AGH Academy of Science and Technology.
 
## Introduction
Ant colonies use the sense of smell to coordinate tasks such as foraging for food, defense or brood care. 
> Trail pheromone signals are particularly important in the context of foraging. When a forager has located a profitable food source and then returns to her nest, she deposits trail pheromones that guide nest mates to the same resource. <a href="" onclick="document.getElementById('citation1').scrollIntoView()">[1]</a>

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
 <details> <summary>Examle simulation explained</summary>

 |![image](https://user-images.githubusercontent.com/56199675/174571534-e3425d10-a7f0-46f9-b77e-417337c8ae38.png)| ![image](https://user-images.githubusercontent.com/56199675/174571600-eb477d41-0599-4304-82b7-535e2f32a994.png)|
  |---|---|
 |1. Initial chaos|2. First track forming|
 |![image](https://user-images.githubusercontent.com/56199675/174571861-0b074579-7adf-447a-a720-07bdc6b53c9c.png)|![image](https://user-images.githubusercontent.com/56199675/174572175-d86e8a03-31c0-4570-8422-545448f00ec7.png)|
 |3. First track is self-optimizing to get shorter. <br> More paths are forming but they are not leading to the nest yet|4. All the paths got connetced to the nest|
 |![image](https://user-images.githubusercontent.com/56199675/174572865-579437b9-6cd8-4fb6-9d1c-5b1cbf9a8fbb.png)|![image](https://user-images.githubusercontent.com/56199675/174573657-7ee17bbd-1197-495d-9962-021d86d83c33.png)|
 |5. Paths keep getting straigher and shorter|6. Paths are almost ready but since some ants are still walking free their location is not stable yet.
|![image](https://user-images.githubusercontent.com/56199675/174574295-902bf23c-8f9d-420b-92e6-7806e752854c.png)|![image](https://user-images.githubusercontent.com/56199675/174574849-553ab8e0-ce12-4589-94f4-11312fe45fb5.png)|
 |7. Pheromne map significantly more stable and durable. |8. Loop o rightgot slower to optimize distance|
|![image](https://user-images.githubusercontent.com/56199675/174575705-c41b38dc-5b90-449b-a773-51829bf24931.png)|![image](https://user-images.githubusercontent.com/56199675/174576115-671c1bdf-bed1-49c2-849f-0e616558f651.png)|
 |9. The loop on righis at the point of the collapse|10.The whole food is collected|
 </details>
 
 <details>
 <summary>Post-simulation ants behaviour</summary>
  <h4> The behaviour of ants after collecting all the food </h4>
  
 Once all the food is collected the path are becoming forgotten starting with the longest one. If we keep the simmulation running we may even observe forming of so called "ant mill" [(wikipeda)](https://en.wikipedia.org/wiki/Ant_mill) which is apperaing close to the place of the picked loot - so in an area filled densly with pheromonses.
 
 <img src="https://user-images.githubusercontent.com/56199675/174591378-3253670d-8a90-4122-84f5-242ba2ab2b3c.png" width=800/>
 
In this case the distance travelled by ants is self-optimizing too, so the circle is collapsing towards ts center and then disapperaing 
 
  <img src="https://user-images.githubusercontent.com/56199675/174592530-4878ac4e-df73-4d99-895d-f3afd37038cb.png" width=800/>
</details>
 

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


 
#### Citations
 - <div id="citation1">Morgan E.D. Trail pheromone of ants. Physiol. Entomol. 2009;34:1–17. doi: 10.1111/j.1365-3032.2008.00658.x.</div>

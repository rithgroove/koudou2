# Koudou Mk2
Mk2 of Koudou with different environment type 

# Forewords
## Why did I remake this one? 
The main reason why I remake this one is to refactor environment into three different type of environment:

- OSMEnv (Open Street Map Environment)

This is the environment we used for the previous studies. This one was based on graph 

- FlatEnv (Flat Environment)

A flat environment with obstacles such as circles, squares, poligons, etc. (usefull to simulate indoors environment)

- GridEnv (Grid Environment)

A Grid environment to simulate other things (Chess for example) 

# Dependencies

- Pickle (4.0) : For saving and loading experiments

- Numpy (1.22.4): Required by many libraries

- Shapely (1.8.2) : Currently used for FlatEnv for object representation and collision. 




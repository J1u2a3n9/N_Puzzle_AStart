# THIRD PRACTICE IS

## NAMES
Balderrama Mauricio

Canedo Juan Luis

La Fuente Mercedes

## IMPORTANT!

--> How to use
* After cloning the repository enter the folder, open a git bash and put the following command: git checkout master, with this command you will be able to see all the files 
* For the correct functioning of the code you first need to install "numpy" from the console with the following command: pip install numpy  

### PROBLEM SOLVER AGENT

### Objective Formulation:
    The first square of the puzzle must start with the number zero and the other squares with the following consecutive numbers 

### Problem Formulation:

### Initial State:
      Puzzle with random values in the squares 
      
![NpuzzleStart](https://user-images.githubusercontent.com/74753713/133524075-1d7cff6a-6272-4ac3-8301-6cac0420cc00.png)

### Objective State:
     Puzzle with values equal to that of the target state
 
![NpuzzleStart](https://user-images.githubusercontent.com/74753713/133523852-fb118808-ca64-429f-b5d1-0a100ef72fa3.png)

### Test of Objective:
     Is the initial puzzle the same as the target puzzle?
 
### Actions:
      Moven Up
      Move Down
      Move Right
      Move Left



### Cost:
     Cost dependent on the heuristic functions to be applied
  
## DESCRIPTION OF THE PROBLEM
Solve the N Puzzle with the A START algorithm with the following heuristics:

## SOLUTION DESCRIPTION 
A computer program was designed to solve the n puzzle with the a start algorithm using the respective heuristics seen in the lectures. 

## EXPERIMENTS
1. h1(n) Number of parts out of place with respect to the target condition

--> Experiments and results: For 8-puzzle


  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  
  [6 8 7 1 0 2 3 4 5] | 3770 | 0.07059230 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
    
    
--> Experiments and results: For 15-puzzle

  
  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  
2. h2(n) Sum of the Manhattan distance

--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
    
--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:


3. h3(n) Sum of inverse permutations
    
--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  
--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  
    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
  :---: | :---: | :---: | :---: | :---:
  



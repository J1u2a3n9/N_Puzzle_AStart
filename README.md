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
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 3770 | 0.07059230 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 11964 | 0.22098280 | ['LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP']

    
--> Experiments and results: For 15-puzzle

  
  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 6419 | 0.15697680 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 10 | 0.00039170 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']

    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00012590 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 1220849 | 51.66905610 | ['LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']


2. h2(n) Sum of the Manhattan distance

--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 2829 | 0.46352890 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 6318 | 0.93772820 | ['LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP']



--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 39041 | 5.70482880 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 58 | 0.010006930 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']

  
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00050680 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 507896 | 420.04782418 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  



3. h3(n) Sum of inverse permutations
    
--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
  
--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 1706 | 0.11785460 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 155 | 0.0.1324760 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT'] 

  
    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.000048140 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 94783 | 15.82658280 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  


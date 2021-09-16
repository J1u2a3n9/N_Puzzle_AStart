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
[6 4 1 0 2 3 8 5 7] | 5435 | 0.11722230 |  ['UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 11472 | 0.21567120 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] | 3158 | 0.05536390 | ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 12797 | 0.25152650 | ['UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']

    
--> Experiments and results: For 15-puzzle

  
  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 6419 | 0.15697680 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 10 | 0.00039170 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
|||
|||
|||
    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00012590 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 1220849 | 51.66905610 | ['LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']
|||
|||
|||

2. h2(n) Sum of the Manhattan distance

--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 2829 | 0.46352890 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 6318 | 0.93772820 | ['LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP']
[6 4 1 0 2 3 8 5 7] | 3506 | 0.52976960 | ['UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 5903 | 0.87684250 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] |2212 | 0.32229310 |  ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 8506 | 1.32256760 | ['UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']


--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 39041 | 5.70482880 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 58 | 0.010006930 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
|||
|||
|||
  
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00050680 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 507896 | 420.04782418 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  
|||
|||
|||


3. h3(n) Sum of inverse permutations
    
--> Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 1010 | 0.03482590 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 2078 | 0.06877550 | ['LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP', 
'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP']
[6 4 1 0 2 3 8 5 7] | 3992 | 0.13357460 | ['UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 2499 | 0.08234000 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] | 3605 | 0.11708110 | ['LEFT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 2128 | 0.06980460 | ['UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']

  
--> Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 1706 | 0.11785460 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 155 | 0.0.1324760 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT'] 
|||
|||
|||
  
    
--> Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.000048140 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 94783 | 15.82658280 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  
|||
|||
|||

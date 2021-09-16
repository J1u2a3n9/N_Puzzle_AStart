# THIRD PRACTICE INTELLIGENT SYSTEMS 🚀

## NAMES 📋
* Balderrama Mauricio
* Canedo Juan Luis
* La Fuente Mercedes

## IMPORTANT! HOW TO USE 🔧
* After cloning the repository enter the folder, open a git bash and put the following command: git checkout master, with           this command you will be able to see all the files 
* For the correct functioning of the code you first need to install "numpy" from the console with the following command:                   
             -pip install numpy  
* Insert the command 'python n_puzzle.py' to start the program.
* The program allows to read at most and at least two rows of text in which is first the initial state and the target.
* Each time the execution of the A start algorithm is performed, the global values are initialized to the default values, so it    will be necessary to read the data again.


## PROBLEM SOLVER AGENT ⚙️

### Objective Formulation:
The first square of the puzzle must start with the number zero and the other squares with the following consecutive numbers 

### Problem Formulation:

### Initial State:
Puzzle with random values in the squares 
  
![NpuzzleEnd](https://user-images.githubusercontent.com/74753713/133536453-acac7e4a-96cd-4e1f-b2dd-2576661726f3.png)

### Objective State:
Puzzle with values equal to that of the target state
 
![NpuzzleStart](https://user-images.githubusercontent.com/74753713/133524075-1d7cff6a-6272-4ac3-8301-6cac0420cc00.png)


### Test of Objective:
Is the initial puzzle the same as the target puzzle?
 
### Actions:
* Up
* Down
* Right
* Left



### Cost:
Cost dependent on the heuristic functions to be applied
  
## DESCRIPTION OF THE PROBLEM
Solve the N Puzzle with the A START algorithm with the following heuristics:

## SOLUTION DESCRIPTION 
A computer program was designed to solve the n puzzle with the a start algorithm using the respective heuristics seen in the lectures. 

## EXPERIMENTS  📢
#### 1. H1(n) Number of parts out of place with respect to the target condition

#### :arrow_down: Experiments and results: For 8-puzzle

  
  
  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 3770 | 0.07059230 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 11964 | 0.22098280 | ['LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP']
[6 4 1 0 2 3 8 5 7] | 5435 | 0.11722230 |  ['UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 11472 | 0.21567120 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] | 3158 | 0.05536390 | ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 12797 | 0.25152650 | ['UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']

    
#### :arrow_down: Experiments and results: For 15-puzzle

  
  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 6419 | 0.15697680 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 10 | 0.00039170 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 92 | 0.00227410 | ['LEFT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] | 8 | 0.00039290 | ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 92 | 0.00222060 | ['LEFT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] | 8 | 0.00028970 | ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']


#### :arrow_down: Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00012590 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 1220849 | 51.66905610 | ['LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']


#### 2. H2(n) Sum of the Manhattan distance

#### :arrow_down: Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 2829 | 0.46352890 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 6318 | 0.93772820 | ['LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP']
[6 4 1 0 2 3 8 5 7] | 3506 | 0.52976960 | ['UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 5903 | 0.87684250 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] |2212 | 0.32229310 |  ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 8506 | 1.32256760 | ['UP', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']


#### :arrow_down: Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 39041 | 5.70482880 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'UP']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 58 | 0.010006930 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 1012 | 0.16894770 | ['LEFT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] |43 | 0.00759850 | ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 1012 | 0.16332710 | ['LEFT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] | 43 | 0.00735990 |  ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
  
#### :arrow_down: Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.00050680 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 507896 | 420.04782418 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  



#### 3. H3(n) Sum of inverse permutations
    
#### :arrow_down: Experiments and results: For 8-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[6 8 7 1 0 2 3 4 5] | 1010 | 0.03482590 | ['UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP']
[6 5 8 7 1 4 2 0 3] | 2078 | 0.06877550 | ['LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP','RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP']
[6 4 1 0 2 3 8 5 7] | 3992 | 0.13357460 | ['UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 6 4 1 5 8 2 0 3] | 2499 | 0.08234000 | ['RIGHT', 'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'UP', 'LEFT']
[4 2 0 8 3 5 7 6 1] | 3605 | 0.11708110 | ['LEFT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'UP']
[7 4 1 8 5 2 6 0 3] | 2128 | 0.06980460 | ['UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT']

  
#### :arrow_down: Experiments and results: For 15-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[3 1 2 0 4 5 6 7 8 9 10 11 12 13 14 15] | 1706 | 0.11785460 | ['DOWN', 'LEFT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'LEFT']
[1 5 2 3 0 6 10 7 4 8 14 11 12 9 13 15] | 155 | 0.0.1324760 | ['DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT'] 
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 876 | 0.06581840 | ['LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'LEFT']
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] | 127 | 0.00922920 | ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']
[1 2 10 3 6 5 7 0 4 8 14 11 12 9 13 15] | 876 | 0.06350390 | ['LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'LEFT'] 
[1 5 2 3 4 6 10 7 0 8 14 11 12 9 13 15] | 127 | 0.01086230 | ['RIGHT', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'UP', 'LEFT']

    
#### :arrow_down: Experiments and results: For 24-puzzle

  Initial State | Number of states | Time | Steps 
:---: | :---: | :---: | :---:
[1 2 0 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 2 | 0.000048140 | ['LEFT', 'LEFT']
[1 2 3 4 5 6 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24] | 94783 | 15.82658280 | ['RIGHT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT']  

#### :arrow_down: Comparisons

## 8-PUZZLE

With 8-puzzle the maximum number of expanded states (11964 states) was obtained with heuristic 1 and the minimum number of expanded states (1010 states) was obtained with heuristic 3. 

The heuristic that finds the solution the fastest is h3 because the minimum execution time is 0.0348482590 seconds.
And the maximum execution time is h2 with 1.3225256760 seconds.

![8time](https://user-images.githubusercontent.com/65575674/133536231-8bdd0364-dd2b-486a-95a6-e2c855dfd748.png)

## 15-puzzle

With 15-puzzle the maximum number of expanded states (39041 states) was obtained with heuristic 2 and the minimum number of expanded states (8 states) was obtained with heuristic 1.

The heuristic that finds the solution the fastest is h1 because the minimum execution time is 0.0002870 seconds
And the maximum execution time is performed by h2 with 5.7048482880 seconds.

![133536270-580b18ea-dc57-4149-a81d-89708cd3d8a0](https://user-images.githubusercontent.com/74753713/133538555-f220664b-c890-42ca-928f-879841ca0985.png)


## 24-puzzle

With 24-puzzle the maximum number of expanded states (507896 states) was obtained with heuristic 2 and the minimum number of expanded states (94783 states) was obtained with heuristic 3.

The heuristic that finds the fastest solution is h3 because the minimum execution time is 0.000048140 seconds.
And the maximum execution time is performed by h2 with 420.04782418 seconds.

![n=24](https://user-images.githubusercontent.com/65575674/133536297-70485073-e67b-4239-8edc-4bc71cdab7a9.png)


## CONCLUSION

The memory occupied in the execution of the program with A* depends on the expanded states that vary according to the heuristic selected and also the size of the puzzle.
Therefore, the heuristic that uses the largest memory is h2: sum of the Manhattan distance from the piece in the initial state to the same piece in the target state because the process has to be performed for all pieces. 

The time complexity with A* in terms of the worst execution time is the heuristic h2 because its Big-Oh is exponential and the heuristic function that finds the fastest solution is h3 because of the times calculated in the tables. 

Comparing the results of the heuristic functions h1,h2 and h3 we can discard all of them because they have a weakness either in time or in space and this makes A-star not optimal. 


## BIBLIOGRAPHY
Class slides, Code reference: https://github.com/speix/8-puzzle-solver



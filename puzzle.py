import timeit
import time
import numpy as np
from math import factorial, sqrt
from collections import deque
from state import State
from random import randint
from heapq import heappush, heappop


empty_state=[0,0,0,0]
initial_state = list()
objective_state = list()
objective_node = State
comparative_node=State(empty_state,None,None,0,0,0)
movements = list()
lenght = 0
side = 0
expanded_nodes = 0

visited_state=0
cost=set()


def reset_values():
    global empty_state,initial_state,objective_state,objective_node,comparative_node,movements,lenght,side,expanded_nodes
    empty_state=[0,0,0,0]
    initial_state = list()
    objective_state = list()
    objective_node = State
    comparative_node=State(empty_state,None,None,0,0,0)
    movements = list()
    lenght = 0
    side = 0
    expanded_nodes = 0

def move(state, position):
    new_state = state[:]
    indexx = new_state.index(0)
    if position == 1:  # UP
        if indexx not in range(0, side):
            auxiliary = new_state[indexx - side]
            new_state[indexx - side] = new_state[indexx]
            new_state[indexx] = auxiliary
            return new_state
        else:
            return None
    if position == 2:  # DOWN
        if indexx not in range(lenght - side, lenght):
            auxiliary = new_state[indexx + side]
            new_state[indexx + side] = new_state[indexx]
            new_state[indexx] = auxiliary
            return new_state
        else:
            return None
    if position == 3:  # LEFT
        if indexx not in range(0, lenght, side):
            auxiliary = new_state[indexx - 1]
            new_state[indexx - 1] = new_state[indexx]
            new_state[indexx] = auxiliary
            return new_state
        else:
            return None
    if position == 4:  # RIGHT
        if indexx not in range(side - 1, lenght, side):
            auxiliary = new_state[indexx + 1]
            new_state[indexx + 1] = new_state[indexx]
            new_state[indexx] = auxiliary
            return new_state
        else:
            return None


def expand(node):
    global expanded_nodes
    expanded_nodes += 1
    neighbors = list()
    neighbors.append(State(move(node.state, 1), node, 1,node.depth+1,node.cost+1,0))
    neighbors.append(State(move(node.state, 2), node, 2,node.depth+1,node.cost+1,0))
    neighbors.append(State(move(node.state, 3), node, 3,node.depth+1,node.cost+1,0))
    neighbors.append(State(move(node.state, 4), node, 4,node.depth+1,node.cost+1,0))
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes

def get_initial_states(initial_state):
    size_aux=len(initial_state)
    return factorial(size_aux)

def modify_initial_state(initial_state):
    state=State(initial_state,None,None,0,0,0)
    i=1
    while i<=4:
        state_aux=move(state.state,i)
        if state_aux!=None:
            i=5
        else:
            i+=1
    return state_aux

def modify_official_state(initial_state):
    initial_state += [initial_state.pop(0)]
    initial_state += [initial_state.pop(1)]
    return initial_state

def state_space(initial_state):
    global objective_node,expanded_nodes
    explored = set()
    queuee = deque([State(initial_state, None, None,0,0,0)])
    limit=get_initial_states(initial_state)
    while queuee and expanded_nodes<limit:
        node = queuee.pop()
        explored.add(node.map)
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)
    disturbed_state=modify_official_state(initial_state)
    queuee = deque([State(disturbed_state, None, None,0,0,0)])
    while queuee and expanded_nodes<limit:
        node = queuee.pop()
        explored.add(node.map)
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)


 #*********************************************************************************************************
def heuristica1(state):
        count=0
        for i in range(0,len(state)):
               if(state[i]!=objective_state[i]):
                    count+=1
        return count


def heuristica2(state):
    tam=int(sqrt(len(state)))
    state_Matriz=np.array(state).reshape(tam,tam)
    stateObj_Matriz=np.array(objective_state).reshape(tam,tam)
    sum=0
    for i in range(0,3):
        for j in range(0,3):
            if(state_Matriz[i][j]!=stateObj_Matriz[i][j]):
                posState=np.where(state_Matriz==state_Matriz[i][j])
                posObjState=np.where(stateObj_Matriz==state_Matriz[i][j])
                sum+=abs(int(posState[0])-int(posObjState[0]))+abs(int(posState[1])-int(posObjState[1]))
    return sum/2


def heuristica3(state):
    counter=0
    total_amount=0
    while state!=[]:
        cont1=counter
        while cont1 < len(state):
            if counter==cont1:
                if cont1+1<len(state) and state[counter]>state[cont1+1]:
                    total_amount+=1
                    cont1+=2
                else:
                    cont1+=1
            else:
                if state[counter]>state[cont1]:
                    total_amount+=1
                    cont1+=1
                else:
                    cont1+=1
        if counter == len(state):
            state=[]
        else:
            counter+=1
    return total_amount

 #*********************************************************************************************************


def a_start(initial_state,objective_state,num_h):
    global visited_state,objective_node
    explored=set()
    priority_queuee=list()
    heuristic=num_h(initial_state)
    root_node=State(initial_state,None,None,0,0,heuristic)
    start=(heuristic,0,root_node)
    heappush(priority_queuee,start) #inserta en el monticulo
    while priority_queuee:
        node = heappop(priority_queuee) #Extrae y devuelve el element más pequeño del montón
        explored.add(node[2].map) #agrega a explorados el state actual sin el peso
        if node[2].state == objective_state:
            objective_node = node[2]
            return priority_queuee

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.heuristic = neighbor.cost + num_h(neighbor.state)

            start = (neighbor.heuristic, neighbor.movement, neighbor) #tupla

            if neighbor.map not in explored:

                heappush(priority_queuee, start) #inserta en el monticulo

                explored.add(neighbor.map) 

                if neighbor.depth > visited_state:
                    visited_state += 1

           









def path():
    current_node = objective_node
    while initial_state != current_node.state:
        if current_node.movement == 1:
            movement = 'UP'
        elif current_node.movement == 2:
            movement = 'DOWN'
        elif current_node.movement == 3:
            movement = 'LEFT'
        else:
            movement = 'RIGHT'
        movements.insert(0, movement)
        current_node = current_node.father
    return movements


    



def show_results(time):
    global movements
    if objective_node != comparative_node:
        movements = path()
        print("---------------------------------------------------------------------------------------------------------------------------")
        print()
        print("RESULTS")
        print("Steps: "+str(movements))
        print("Number of steps: "+str(len(movements)))
        print("Number of expanded nodes: "+str(expanded_nodes))
        print("Number of visited states: "+str(objective_node.depth))
        print("Time of ejecution: " + format(time, '.8f'))
        print()
        print("---------------------------------------------------------------------------------------------------------------------------")
    else :
        print("Doesn't exists solution")


    

def read_random_state(initial):
    global lenght, side
    initial_state.clear()
    objective_state.clear()
    for element in initial:
        initial_state.append(int(element))
    lenght = len(initial_state)
    side = int(lenght**0.5)
    counter = 0
    while counter < lenght:
        objective_state.append(int(counter))
        counter += 1


def read_states(initial, end):
    global lenght, side
    initial_state.clear()
    objective_state.clear()
    for element in initial:
        initial_state.append(int(element))
    lenght = len(initial_state)
    side = int(lenght**0.5)
    for elementII in end:
        objective_state.append(int(elementII))


def map_list(lists):
    return list(map(int, lists))


def read_file_txt(name, limit):
    data = []
    aux = 1
    with open(str(name)+'.txt') as fname:
        for lineas in fname:
            if limit == aux:
                data.extend(lineas.split())
            aux += 1
    return data


def read_of_file(name):
    initial_state = []
    objective_state = []
    i = 0
    while i < 2:
        if i == 0:
            initial_state = read_file_txt(name, 1)
        if i == 1:
            objective_state = read_file_txt(name, 2)
        i += 1
    initial_state = map_list(initial_state)
    objective_state = map_list(objective_state)
    read_states(initial_state, objective_state)


def generate_random_puzzle(size_aux):
    aux_initial_state = []
    counter = 0
    while counter <= (size_aux*size_aux-1):
        random_num = randint(0, (size_aux*size_aux)-1)
        if random_num in aux_initial_state:
            pass
        else:
            aux_initial_state.append(random_num)
            counter += 1
    return aux_initial_state


def sub_main(size_aux):
    option = 0
    random = generate_random_puzzle(size_aux)
    read_random_state(random)
    print("Puzzle to resolve")
    print(initial_state)
    print("Target State if a search function is chosen")
    print(objective_state)
    generate_random_puzzle(size_aux)
    print("Choose an option")
    print("1)Get total number of states")
    print("2)Solve for A*")
    print("Please enter an option: ")
    option = int(input())
    if option==1:
        start = timeit.default_timer()
        state_space(initial_state)
        end = timeit.default_timer()
        print("The number of states is: "+str(expanded_nodes))
        print("time of ejecution: " + format(end-start, '.8f'))
    if option == 2:
        print("HEURISTICS")
        print("1)Number of pieces out of place")
        print("2)Manhattan")
        print("3)Add inverse permutations")
        print("Enter the number of heuristics to use")
        opcionII='heuristica'+(str(input()))
        start=timeit.default_timer()
        a_start(initial_state,objective_state,function[opcionII])
        end=timeit.default_timer()
        show_results(end-start)



def main():
    
    option = 1
    while option >= 1 and option <= 6:
        
        print("Welcome to N puzzle")
        print("1)Read for file the state initial and objective")
        print("2)Test Random")
        print("3)Solve for A STAR*")
        print("Please enter an option: ")
        option = int(input())
        if option == 1:
            print("-------------Do not forget that you must read a text file with two rows, one that has the initial state and the other the objective -------------")
            print("Enter the file name")
            name = input()
            read_of_file(name)
            print("Welcome to N puzzle")
            print("3)Solve for A STAR*")
            print("4)Retroceder")
            print("Please enter an option: ")
            option = int(input())
            if option==4:
                main()
        if option == 2:
            print("Enter the size of puzzle: ")
            size_aux = int(input())
            sub_main(size_aux)
        if option == 3:
            print("HEURISTICS")
            if (initial_state==[] or objective_state==[]):
                print("-------------Do not forget to fill your puzzle, since the puzzle restarts in empty every time the a start is executed :C-------------")
                time.sleep(2)
                main()
            else:
                print("1)Number of pieces out of place")
                print("2)Manhattan")
                print("3)Add inverse permutations")
                print("Enter the number of heuristics to use")
                opcionII='heuristica'+(str(input()))
                start=timeit.default_timer()
                a_start(initial_state,objective_state,function[opcionII])
                end=timeit.default_timer()
                show_results(end-start)
                reset_values()
               


function = {
    'heuristica1':heuristica1,
    'heuristica2':heuristica2,
    'heuristica3':heuristica3
}


if __name__ == '__main__':
    main()


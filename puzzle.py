import timeit
# import numpy as np
from math import factorial
from collections import deque
from state import State
from random import randint
from heapq import heappush, heappop,heapify
import itertools

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
    



def bfs(initial_state, objective_state):
    global objective_node
    explored = set()
    queuee = deque([State(initial_state, None, None,0,0,0)])
    while queuee:
        node = queuee.popleft()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return queuee
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)


def dfs(initial_state, objective_state):
    global objective_node
    explored = set()
    stack = list([State(initial_state, None, None,0,0,0)])
    while stack:
        node = stack.pop()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return stack
        neighbors = reversed(expand(node))
        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)


def dls_not_recursive(initial_state, objective_state, limit):
    global objective_node
    explored = set()
    stack = list([State(initial_state, None, None,0,0,0)])
    counter = 0
    while stack:
        node = stack.pop()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return stack 
        if counter < limit:
            neighbors = reversed(expand(node))
            for neighbor in neighbors:
                if neighbor.map not in explored:
                    stack.append(neighbor)
                    explored.add(neighbor.map)
        counter += 1
        if counter == limit:
            stack = []
            return "CUTOFF"


def id(initial_state, objective_state):
    global objective_node
    i = 1000000000
    while i < 100000000000:
        result = dls_not_recursive(initial_state, objective_state, i)
        if result == 'CUTOFF':
            i += 1
        else:
            i = 100000000000
    return result









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


# def mostrar_puzzle(puzzle):
    if lenght == 16:
        puzzle_nuevo = np.array(puzzle).reshape(4, 4)
    if lenght == 9:
        puzzle_nuevo = np.array(puzzle).reshape(3, 3)
    if lenght == 4:
        puzzle_nuevo = np.array(puzzle).reshape(2, 2)
    if lenght == 0:
        puzzle_nuevo = []
    print(puzzle_nuevo)


def sub_main(size_aux):
    option = 0
    random = generate_random_puzzle(size_aux)
    read_random_state(random)
    print("Puzzle to resolve")
    print(initial_state)
    # mostrar_puzzle(initial_state)
    print("Target State if a search function is chosen")
    print(objective_state)
    # mostrar_puzzle(objective_state)
    generate_random_puzzle(size_aux)
    print("Choose an option")
    print("1)Solve for BFS")
    print("2)Solve for DLS")
    print("3)Solve for dfs")
    print("4)Solve for Iterative Deepening")
    print("5)Get total number of states")
    print("6)Solve for A*")
    print("Please enter an option: ")
    option = int(input())
    if option == 1:
        start = timeit.default_timer()
        bfs(initial_state, objective_state)
        end = timeit.default_timer()
        show_results(end-start)
    if option == 2:
        start = timeit.default_timer()
        respuesta = dls_not_recursive(initial_state, objective_state, 181440)
        if respuesta == "CUTOFF":
            print("No solution was found in the limit")
        else:
            end = timeit.default_timer()
            show_results(end-start)
    if option == 3:
        start = timeit.default_timer()
        dfs(initial_state, objective_state)
        end = timeit.default_timer()
        show_results(end-start)
    if option == 4:
        start = timeit.default_timer()
        respuesta = id(initial_state, objective_state)
        if respuesta == "CUTOFF":
            print("No solution was found in the limit")
        else:
            end = timeit.default_timer()
            show_results(end-start)
    if option==5:
        start = timeit.default_timer()
        state_space(initial_state)
        end = timeit.default_timer()
        print("The number of states is: "+str(expanded_nodes))
        print("time of ejecution: " + format(end-start, '.8f'))
    if option == 6:
        print("HEURISTICS")
        print("1)Number of pieces out of place")
        print("2)Manhattan")
        print("3)Add inverse permutations")
        print("Enter the number of heuristics to use")
        opcionII='h'+(str(input()))
        start=timeit.default_timer()
        #a_start(initial_state,objective_state,function[opcionII])
        end=timeit.default_timer()
        show_results(end-start)
#*********************************************************************************************************
def num_of_parts_out_place(state,stateObj):
        count=0
        for i in range(0,len(state[0] )):
            for j in range(0,len(state[0] )):
                if(state[i][j]!=stateObj[i][j]):
                    count+=1
        return count

def manhattan_distance(x,y,x1,y1):
    return abs(x-x1)+abs(y-y1)

def main():
    
    option = 1
    while option >= 1 and option <= 6:
        
        print("Welcome to N puzzle")
        print("1)Read for file the state initial and objective")
        print("2)Solve for BFS")
        print("3)Solve for DLS")
        print("4)Solve for dfs")
        print("5)Solve for Iterative Deepening")
        print("6)Test Random")
        print("7)Solve for A STAR*")
        print("Please enter an option: ")
        option = int(input())
        if option == 1:
            print("Enter the file name")
            name = input()
            read_of_file(name)
        if option == 2:
            start = timeit.default_timer()
            bfs(initial_state, objective_state)
            end = timeit.default_timer()
            show_results(end-start)
        if option == 3:
            start = timeit.default_timer()
            respuesta = dls_not_recursive(
                initial_state, objective_state, 181440)
            if respuesta == "CUTOFF":
                print("No solution was found in the limit")
            else:
                end = timeit.default_timer()
                show_results(end-start)
        if option == 4:
            start = timeit.default_timer()
            dfs(initial_state, objective_state)
            end = timeit.default_timer()
            show_results(end-start)
        if option == 5:
            start = timeit.default_timer()
            respuesta = id(initial_state, objective_state)
            if respuesta == "CUTOFF":
                print("No solution was found in the limit")
            else:
                end = timeit.default_timer()
                show_results(end-start)
        if option == 6:
            print("Enter the size of puzzle: ")
            size_aux = int(input())
            sub_main(size_aux)
        if option == 7:
            print("HEURISTICS")
            print("1)Number of pieces out of place")
            print("2)Manhattan")
            print("3)Add inverse permutations")
            print("Enter the number of heuristics to use")
            opcionII='h'+(str(input()))
            start=timeit.default_timer()
            state=[[1,2,3],[4,5,6],[7,8,9]] 
            ob=[[1,2,3],[4,5,6],[7,8,9]]
            print(num_of_parts_out_place(state,ob))
            
            #a_start(initial_state,objective_state,function[opcionII])
            end=timeit.default_timer()
            #show_results(end-start)



if __name__ == '__main__':
    main()


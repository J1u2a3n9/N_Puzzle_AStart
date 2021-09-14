class State:
    def __init__(self,state,father,movement,depth,cost,heuristic):
        self.state=state
        self.father=father
        self.movement=movement
        self.depth=depth
        self.cost=cost
        self.heuristic=heuristic
        if self.state:
            self.map=''.join(str(state) for state in self.state)
    
    


    def __eq__(self,objective_state):
        return self.map == objective_state.map
    
    def __lt__(self,objective_state):
        return self.map<objective_state.map

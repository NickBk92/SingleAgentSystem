from abc import ABCMeta, abstractmethod


class Heuristic(metaclass=ABCMeta):
    def __init__(self, initial_state: 'State'):
        # Here's a chance to pre-process the static parts of the level.
        pass
    
    def h(self, state: 'State') -> 'int':
        box_loc=[]
        goal_loc=[]
        for row in range(len(state.boxes)):
            for col in range(len(state.boxes[row])):
                if state.boxes[row][col]:
                    box_loc.append((state.boxes[row][col],row,col))
                if state.goals[row][col]:
                    goal_loc.append((state.goals[row][col],row,col))
        h=0
        for box in box_loc:
            for goal in goal_loc:
                if box[0].lower()==goal[0]:
                    fromAgentToBox = abs(state.agent_row - box[1]) + abs(state.agent_col - box[2])
                    h+= abs(box[1]-goal[1]) + abs(box[2]-goal[2])
                    h+=fromAgentToBox
 
        return h
    
    @abstractmethod
    def f(self, state: 'State') -> 'int': pass
    
    @abstractmethod
    def __repr__(self): raise NotImplementedError


class AStar(Heuristic):
    def __init__(self, initial_state: 'State'):
        super().__init__(initial_state)
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.h(state)
    
    def __repr__(self):
        return 'A* evaluation'


class WAStar(Heuristic):
    def __init__(self, initial_state: 'State', w: 'int'):
        super().__init__(initial_state)
        self.w = w
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.w * self.h(state)
    
    def __repr__(self):
        return 'WA* ({}) evaluation'.format(self.w)


class Greedy(Heuristic):
    def __init__(self, initial_state: 'State'):
        super().__init__(initial_state)
    
    def f(self, state: 'State') -> 'int':
        return self.h(state)
    
    def __repr__(self):
        return 'Greedy evaluation'


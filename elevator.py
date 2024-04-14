import numpy as np

class Elevator:
    parent = None
    state = None
    operator = None
    depth = 0
    cost = 0

    def __init__(self, state, parent=None, operator=None, depth=0):
        self.parent = parent
        self.state = np.array(state)
        self.operator = operator
        self.depth = depth
        self.cost = self.depth + self.heuristic_six()

    def __lt__(self, other):
        if self.cost != other.cost:
            return self.cost < other.cost
        else:
            op_pr = {'12+': 0, '13+': 1, '14+': 2, '15+': 3, '23+': 4, '24+': 5, '25+': 6, '34+': 7, '35+': 8, '45+': 9, '12-': 10, '13-': 11, '14-': 12, '15-': 13, '23-': 14, '24-': 15, '25-': 16, '34-': 17, '35-': 18, '45-': 19}
            return op_pr[self.operator] < op_pr[other.operator]

    def __str__(self):
        return str(self.state[:]) + ' ' + str(self.depth) + ' ' + str(self.operator) + '\n'

    def goal_test(self):
        for i in range(self.state.size):
            if not (self.state[i] >= 21 and self.state[i] <= 25):
                return False
        return True

    def not_heuristic(self):
        return 0
    
    def heuristic_one(self):
        # minimizar soma do erro de cada elevador até a média do intervalo do objetivo [21-25]
        err = 0
        for i in range(self.state.size):
            err = err + abs(self.state[i]-23)
        return err
    
    def heuristic_two(self):
        # minimizar soma do erro de cada elevador até o objetivo [21-25]
        err = 0
        for i in range(self.state.size):
            if self.state[i] > 25:
                err = err + abs(self.state[i]-25)
            elif self.state[i] < 21:
                err = err + abs(self.state[i]-21)
        return err
    
    def heuristic_three(self):
        # minimizar soma do erro de cada elevador até o objetivo [21-25] e diferença entre os elevadores
        err = 0
        for i in range(self.state.size):
            if self.state[i] > 25:
                err = err + abs(self.state[i]-25)
            elif self.state[i] < 21:
                err = err + abs(self.state[i]-21)
            err = err + abs(self.state[i]- self.state.mean())
        return err
    
    def heuristic_four(self):
        # minimizar diferença entre os elevadores
        err = 0
        for i in range(self.state.size):
            err = err + abs(self.state[i]- self.state.mean())
        return err
    
    def heuristic_five(self):
        # minimizar desvio padrão
        return self.state.std()
    
    def heuristic_six(self):
        # minimizar soma do erro de cada elevador até o objetivo [21-25] e desvio padrão
        err = 0
        for i in range(self.state.size):
            if self.state[i] > 25:
                err = err + abs(self.state[i]-25)
            elif self.state[i] < 21:
                err = err + abs(self.state[i]-21)
        return err + self.state.std()
    
    def up(self,idx1,idx2):
        if (self.state[idx1] + 8 <= 49) and (self.state[idx2] + 8 <= 49):
            new_state = self.state.copy()
            new_state[idx1] = new_state[idx1] + 8
            new_state[idx2] = new_state[idx2] + 8
            return Elevator(new_state, self, str(idx1+1) + str(idx2+1) + '+', self.depth + 1)
        else:
            return None

    def down(self,idx1,idx2):
        if (self.state[idx1] - 13 >= 0) and (self.state[idx2] - 13 >= 0):
            new_state = self.state.copy()
            new_state[idx1] = new_state[idx1] - 13
            new_state[idx2] = new_state[idx2] - 13
            return Elevator(new_state, self, str(idx1+1) + str(idx2+1) + '-', self.depth + 1)
        else:
            return None

    def neighbors(self):
        neighbors = [self.up(0,1), self.up(0,2), self.up(0,3), self.up(0,4), self.up(1,2), self.up(1,3), self.up(1,4), self.up(2,3), self.up(2,4), self.up(3,4), \
                      self.down(0,1), self.down(0,2), self.down(0,3), self.down(0,4), self.down(1,2), self.down(1,3), self.down(1,4), self.down(2,3), self.down(2,4), self.down(3,4)]
        return list(filter(None, neighbors))

    __repr__ = __str__

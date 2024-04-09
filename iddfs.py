import itertools

from solver import Solver


class IDDFS(Solver):
    def __init__(self, initial_state):
        super(IDDFS, self).__init__(initial_state)
        self.frontier = []

    def dls(self, limit):
        self.frontier.append(self.initial_state)
        while self.frontier:
            elevator = self.frontier.pop()
            self.explored_nodes.add(tuple(elevator.state))
            if elevator.goal_test():
                self.set_solution(elevator)
                return self.solution
            if elevator.depth < limit:
                for neighbor in elevator.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.frontier.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
                        self.max_depth = max(self.max_depth, neighbor.depth)
        return None

    def solve(self):
        for i in itertools.count():
            self.frontier = []
            self.explored_nodes = set()
            self.max_depth = 0
            self.frontier.append(self.initial_state)
            sol = self.dls(i)
            if sol is not None:
                break
        return

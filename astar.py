import heapq

from solver import Solver


class AStar(Solver):
    def __init__(self, initial_state):
        super(AStar, self).__init__(initial_state)
        self.frontier = []

    def solve(self):
        heapq.heappush(self.frontier, self.initial_state)
        while self.frontier:
            elevator = heapq.heappop(self.frontier)
            self.explored_nodes.add(tuple(elevator.state))
            if elevator.goal_test():
                self.set_solution(elevator)
                break
            for neighbor in elevator.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    heapq.heappush(self.frontier, neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return

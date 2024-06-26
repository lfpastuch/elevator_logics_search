from solver import Solver


class DFS(Solver):
    def __init__(self, initial_state):
        super(DFS, self).__init__(initial_state)
        self.frontier = []

    def solve(self):
        self.frontier.append(self.initial_state)
        while self.frontier:
            elevator = self.frontier.pop()
            self.explored_nodes.add(tuple(elevator.state))
            if elevator.goal_test():
                self.set_solution(elevator)
                break
            for neighbor in elevator.neighbors()[::-1]:
                if tuple(neighbor.state) not in self.explored_nodes:
                    self.frontier.append(neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return

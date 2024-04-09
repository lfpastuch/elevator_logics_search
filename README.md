# Elevator Logic
Elevator logics (https://archive.org/details/elevators-logic#) solver using BFS, DFS, IDDFS and A-star algorithm
     
#### Usage
You can run `main.py` with the name of algorithm - which is `ast` for A*, `bfs`, or `dfs`, or `ids` for iterative deepening dfs - as the first argument and initial state as the second one:

```
$ python main.py bfs 17,26,20,19,31
$ python main.py dfs 17,26,20,19,31
$ python main.py ids 17,26,20,19,31
$ python main.py ast 17,26,20,19,31
```

Solution and details will be saved to ```{alg-name}_elevator_output.txt```.

Based on 8-puzzle implementation from https://github.com/abpaudel/8-puzzle.

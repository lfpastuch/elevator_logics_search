# Elevator Logic
Elevator logics (https://archive.org/details/elevators-logic#) solver using PDDL.
     
#### Usage
You can use the following sequence of commands to run the solver in a docker container.

```
docker pull aiplanning/planutils
docker run -it --privileged --rm -v $(pwd):/mnt -w /mnt aiplanning/planutils:latest bash
planutils install lpg-td
planutils activate
lpg-td domain.pddl problem.pddl -out plan.txt
```

Solution and details will be saved to ```plan.txt```.

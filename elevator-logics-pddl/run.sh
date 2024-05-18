docker pull aiplanning/planutils
docker run -it --privileged --rm -v $(pwd):/mnt -w /mnt aiplanning/planutils:latest bash
planutils install lpg-td
planutils install lama
planutils activate
lpg-td domain.pddl problem.pddl -out plan.txt


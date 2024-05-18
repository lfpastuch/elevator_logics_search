#!/bin/bash

# Puxe a imagem docker
docker pull aiplanning/planutils

# Instale o solver lpg-td sem interação manual e execute-o
docker run --rm -v $(pwd):/mnt -w /mnt aiplanning/planutils:latest /bin/bash -c "echo 'Y' | planutils install lpg-td; planutils activate; lpg-td -o domain.pddl -f problem.pddl -out plan.txt"

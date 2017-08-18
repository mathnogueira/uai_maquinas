#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uai.file_parser import *
from uai.solver import solve_problem
from uai.output_formater import *

import sys

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print "Error: you must specify the input file for the problem"
        exit()
    
    input_file = sys.argv[1]
    (problem_constants, problem_input) = parse_input_file(input_file)
    (valor_otimo, ordem_impressao, cores_maquina) = solve_problem(problem_constants, problem_input)

    # Imprime o resultado do modelo:

    print_solution(valor_otimo, ordem_impressao, cores_maquina, problem_constants[2])
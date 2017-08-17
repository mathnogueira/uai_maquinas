#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uai.file_parser import *
from uai.solver import solve_problem
import sys

if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print "Error: you must specify the input file for the problem"
		exit()
	
	input_file = sys.argv[1]
	(problem_constants, problem_input) = parse_input_file(input_file)
	(valor_otimo, ordem_impressao, cores_maquina) = solve_problem(problem_constants, problem_input)

	# Imprime o resultado do modelo:
	print "Menor número de lavagens: {0}".format(valor_otimo)
	print "Ordem de impressão: {0}".format(ordem_impressao)
	for momento, cores_momento in enumerate(cores_maquina):
		print "Cores presentes na máquina do momento {0}: {1}".format(momento+1, cores_momento)

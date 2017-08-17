from uai.file_parser import *
from uai.solver import solve_problem
import sys

arquivo_entrada = sys.argv

if __name__ == "__main__":
	
	if len(sys.argv) < 2:
		print "Error: you must specify the input file for the problem"
		exit()
	
	input_file = sys.argv[1]
	(problem_constants, problem_input) = parse_input_file(input_file)
	solve_problem(problem_constants, problem_input)

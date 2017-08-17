def read_file_content(file_name):
    with open(file_name) as f:
        content = f.readlines()

    return [x.strip() for x in content]

def transpose_matrix(matrix):
    return [list(l) for l in zip(*matrix)]

def parse_input_file(input_file):
    lines = read_file_content(input_file)
    problem_constants = [int(v) for v in lines[0].split()]
    problem_values = []
    for array in lines[1:]:
        problem_values.append([int(v) for v in array.split()])

    # Retorna as contantes e a matriz transposta do problema
    # para que o 
    return (problem_constants, transpose_matrix(problem_values))
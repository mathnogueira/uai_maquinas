#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Lê e retorna o conteúdo de um arquivo, colocando cada linha em uma posição
### de uma lista. Essa função também remove todos os characteres desnecessários
### do arquivo antes de retornar seu conteúdo.
### @param file_name nome do arquivo que será lido
### @return lista contendo em cada posição uma linha do arquivo
def read_file_content(file_name):
    with open(file_name) as f:
        content = f.readlines()

    return [x.strip() for x in content]

### Transforma uma matriz em sua transposta
### @param matriz matriz a ser transformada
### @return matriz transporta
def transpose_matrix(matrix):
    return [list(l) for l in zip(*matrix)]

### Lê o conteúdo do arquivo de entrada e extraí todas as informações
### relevantes para a execução do problema utilizando o Gurobi
### @param input_file nome do arquivo a ter informações extraídas
### @return tupla contendo em sua primeira posição todas as constantes do problema, e 
### na segunda posição a matriz de cores/embalagens.
def parse_input_file(input_file):
    lines = read_file_content(input_file)
    problem_constants = [int(v) for v in lines[0].split()]
    problem_values = []
    for array in lines[1:]:
        problem_values.append([int(v) for v in array.split()])

    # Retorna as contantes e a matriz transposta do problema
    # para que o 
    return (problem_constants, transpose_matrix(problem_values))
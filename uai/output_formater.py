#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy

### Insere uma cor no slot na posição na primeira posição
### que ainda não está preenchida.
### @param slots lista de slots da máquina
### @param cor cor que será inserida no slot
def inserir_cor_slot(slots, cor):
    for i, cor_slot in enumerate(slots):
        if cor_slot == '-':
            slots[i] = cor
            return

### Define a ordem das cores nos slots a cada iteração de pintura
### @param matriz_cores matriz de cores que foram usadas na solução do problema
### @param numero_slots número de slots da máquina
### @return matriz de slots com a sequencia correta
def definir_sequencia_cores_slot(matriz_cores, numero_slots):
    slot = ['-'] * numero_slots
    nova_matriz = []
    for momento, cores in enumerate(matriz_cores, numero_slots):
        for i in range(numero_slots):
            if slot[i] != '-' and slot[i] not in cores:
                slot[i] = '-'
        
        for cor in cores:
            if cor not in slot:
                inserir_cor_slot(slot, cor)
        nova_matriz.append(copy(slot))

    return nova_matriz

def print_solution(valor_otimo, ordem_impressao, cores_maquina, numero_slots):
    print "Menor número de slots lavados: {0}".format(valor_otimo)
    print "Sequência de embalagens pintadas: {0}".format(ordem_impressao)
    cores_processadas = []
    for momento, cores_momento in enumerate(cores_maquina):
        indice_cores = [indice + 1 for indice, cor in enumerate(cores_momento) if cor > 0]
        cores_processadas.append(indice_cores)
        #print "Cores presentes na máquina do momento {0}: {1}".format(momento+1, indice_cores)

    cores_slots = definir_sequencia_cores_slot(cores_processadas, numero_slots)
    for momento, cores in enumerate(cores_slots):
        print "Cores presentes na máquina do momento {0}: {1}".format(momento+1, cores)

### Imprime na saída padrão a solução do problema no formato de latex
def print_as_latex(valor_otimo, ordem_impressao, cores_maquina, numero_slots):
    print "Menor número de \\textit{slots} lavados: %d\\\\" % (valor_otimo)
    print "Sequência de embalagens pintadas: {0}\\\\".format(ordem_impressao).replace("[", "\\{").replace("]", "\\}")
    cores_processadas = []
    for momento, cores_momento in enumerate(cores_maquina):
        indice_cores = [indice + 1 for indice, cor in enumerate(cores_momento) if cor > 0]
        cores_processadas.append(indice_cores)
        #print "Cores presentes na máquina do momento {0}: {1}".format(momento+1, indice_cores)

    cores_slots = definir_sequencia_cores_slot(cores_processadas, numero_slots)
    tabular = '|'
    num_slots = numero_slots
    for i in range(num_slots):
        tabular += 'c | '
    tabular += 'c|'
    print '\\begin{table}[!htbp]'
    print '\\begin{center}'
    print ' \\begin{tabular}{' + tabular + '}'
    print ' \\hline'
    print '\\backslashbox{\\textbf{Momento}}{\\textbf{\\textit{Slot}}} &'
    for i in range(num_slots):
            if i != num_slots -1:
                print '\\textbf{' + str(i+1) + '} &'
            else:
                print '\\textbf{' + str(i+1) + '}\\\\'	
    print ' \\hline'
    for ind, sequencia_cor_slot in enumerate(cores_slots):
        line = str(ind+1) + ' & ' 
        for cor in sequencia_cor_slot:
            line += str(cor) + ' & '
        line = line[:-3]
        line += '\\\\'
        print line
        print ' \\hline'

    print '\\end{tabular}'
    print '\\caption{Resultados}'
    print '\\label{table:tb_2}'
    print '\\end{center}'
    print '\\end{table}'
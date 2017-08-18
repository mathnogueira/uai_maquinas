#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gurobipy import *


def solve_problem(constants, data_input):
    # numero_embalagens <-- número de embalagens a serem impressas na máquina.
    # numero_cores <-- número total de cores que serão utilizadas para imprimir as embalagens.
    # numero_slots <-- quantidade de slots de tinta disponíveis na máquina.
    # I(j,k) <-- Indica que a impressão da embalagem j será feita no momento k.
    # C(i,k) <-- Indica se a cor i está presente na máquina no momento k.
    # T(i,j) <-- Indica se a cor i é necessária para imprimir a embalagem j.
    [numero_embalagens, numero_cores, numero_slots] = constants
    T = data_input

    print "matriz {0}x{1}".format(len(T), len(T[0]))
    for t in T:
        print t

    model = Model("UaiMaquinas")
    # define o tempo limite de execução em uma hora
    model.Params.timeLimit = 3600
    S = model.addVars(numero_embalagens, numero_cores, vtype=GRB.BINARY, name="S")
    I = model.addVars(numero_embalagens, numero_embalagens, vtype=GRB.BINARY, name="I")
    C = model.addVars(numero_embalagens, numero_cores, vtype=GRB.BINARY, name="C")

    # Somente uma embalagem pode ser impressa no momento K
    for k in range(numero_embalagens):
        model.addConstr(I.sum(k, '*'), GRB.EQUAL, 1, "r0")

    # Uma embalagem j deve ser impressa somente em um momento.
    for j in range(numero_embalagens):
        model.addConstr(I.sum('*', j), GRB.EQUAL, 1, "r1")

    # O número de cores na máquina não pode extrapolar o número de slots da máquina no momento k
    for k in range(numero_embalagens):
        model.addConstr(C.sum(k, '*'), GRB.LESS_EQUAL, numero_slots, "r2")

    # Todas as cores i necessárias para imprimir a embalagem j devem estar na máquina
    # no momento j, caso a embalagem j seja impressa no momento k.
    for i in range(numero_cores):
        for j in range(numero_embalagens):
            for k in range(numero_embalagens):
                C_ki = C.select(k,i)[0]   # C(k,i)
                I_kj = I.select(k,j)[0]   # I(k,j)
                T_ji = T[j][i]             # T(j,i)
                model.addConstr(C_ki, GRB.GREATER_EQUAL, T_ji * I_kj, "r3")


    for i in range(numero_cores):
        # S(0,i) = C(0,i)
        model.addConstr(S.select(0, i)[0], GRB.EQUAL, C.select(0, i)[0], "r4")

    for i in range(numero_cores):
        for k in range(1, numero_embalagens):
            C_atual = C.select(k,i)[0]          # C(k,i)
            C_anterior = C.select(k-1,i)[0]     # C(k-1, i)

            # S(k,i) >= C(k,i) - C(k-1,i)
            model.addConstr(S.select(k,i)[0], GRB.GREATER_EQUAL, (C_atual - C_anterior), "r5")
            # S(k,i) <= 1 - C(k-1,i)
            model.addConstr(S.select(k,i)[0], GRB.LESS_EQUAL, 1 - C_anterior, "r6")
            # S(k,i) <= C(k,i)
            model.addConstr(S.select(k,i)[0], GRB.LESS_EQUAL, C_atual, "r7")

    # Objetivo: somatório de S - numero_slots
    model.setObjective(S.sum('*', '*') - numero_slots, GRB.MINIMIZE)

    # Otimiza o modelo
    model.optimize()

    # Obtém os dados para exibir os relatórios
    ordem_impressao = []
    for i in range(numero_embalagens):
        for j in range(numero_embalagens):
            printed_on_i = I.select(i,j)[0].X
            if printed_on_i > 0:
                ordem_impressao.append(j + 1)

    cores_maquina = []
    for momento in range(numero_embalagens):
        conjunto_cores = C.select(momento, '*')
        cores_maquina.append([int(cor.X) for cor in conjunto_cores])

    # Retorna os resultados do modelo
    return (model.objVal, ordem_impressao, cores_maquina)

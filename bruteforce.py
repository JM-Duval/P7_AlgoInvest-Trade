#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script is an algorithme in order to find the optimal combination of
# action to get maximum gain

import time


def bruteforce(data, max_invest):
    # 1 - put all binary combinaison posible for 2^20 in data so 1 048 576
    # possibility
    nb_element_data = len(data)
    array_whole_nb = [i for i in range(2 ** nb_element_data)]
    array_binary_nb = [bin(i)[2:] for i in array_whole_nb]
    array_combi = ['0' * (nb_element_data - len(k)) + k for k in
                   array_binary_nb]  # add 0 to get the right lenght

    # 2 - combinaison possible
    valid_combinaisons = []
    for combi in array_combi:
        cout_combi = 0
        benefice_combi = 0
        for i in range(nb_element_data):
            if combi[i] == '1':
                cout_combi = cout_combi + data[i]['cout']
                benefice_combi = benefice_combi + (
                    data[i]['cout'] * data[i]['benefice'])
        # 3 - get combinaisons lower max_invest
        if cout_combi <= max_invest:
            valid_combinaisons.append((combi, cout_combi, benefice_combi))

    # 4 - get combinaison most profitable
    optimal_choice = array_combi[0][0]
    benefice_max = int(array_combi[0][2])
    for combi in valid_combinaisons:
        if combi[2] > benefice_max:
            benefice_max = combi[2]
            optimal_choice = combi[0]

    # 5 - get action name with max benefice
    liste_optimale = []
    solution_optimale = optimal_choice
    for i in range(len(solution_optimale)):
        if solution_optimale[i] == '1':
            liste_optimale.append(data[i]['nom'])

    for action in liste_optimale:
        return action

# print(f"Liste des actions a favoriser pour un gain maximal de
# {benefice_max} €:")

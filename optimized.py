#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script is an algorithme in order to find the optimal combination of action to get maximum gain 

import time

data = [
{'nom':'action-1', 'cout':20, 'benefice':0.05},
{'nom':'action-2', 'cout':30, 'benefice':0.10},
{'nom':'action-3', 'cout':50, 'benefice':0.15},
{'nom':'action-4', 'cout':70, 'benefice':0.20},
{'nom':'action-5', 'cout':60, 'benefice':0.17},

{'nom':'action-6', 'cout':80, 'benefice':0.25},
{'nom':'action-7', 'cout':22, 'benefice':0.07},
{'nom':'action-8', 'cout':26, 'benefice':0.11},
{'nom':'action-9', 'cout':48, 'benefice':0.13},
{'nom':'action-10', 'cout':34, 'benefice':0.27},

{'nom':'action-11', 'cout':42, 'benefice':0.17},
{'nom':'action-12', 'cout':110, 'benefice':0.09},
{'nom':'action-13', 'cout':38, 'benefice':0.23},
{'nom':'action-14', 'cout':14, 'benefice':0.01},
{'nom':'action-15', 'cout':18, 'benefice':0.03},

{'nom':'action-16', 'cout':8, 'benefice':0.08},
{'nom':'action-17', 'cout':4, 'benefice':0.12},
{'nom':'action-18', 'cout':10, 'benefice':0.14},
{'nom':'action-19', 'cout':24, 'benefice':0.21},
{'nom':'action-20', 'cout':114, 'benefice':0.18},
]

start = time.time() # calculate the working time of the program 

file_algoInvestTrade = 'data_AlgoInvest&Trade.csv'
file_dataset1 = 'dataset1_Python+P7.csv'
file_dataset2 = 'dataset2_Python+P7.csv'



max_invest = 500

def algo_dynamique(max_invest, data):

	def benefice (data):
		return data['cout'] * data['benefice']

	matrice = [[0 for x in range(max_invest + 1)] for x in range(len(data) + 1)]
	for i in range(1, len(data) + 1):
		for w in range(1, max_invest + 1):
			if data[i-1]['cout'] <= w:	
				matrice[i][w] = max(benefice(data[i-1]) + matrice[i-1][w - data[i-1]['cout']], matrice[i-1][w])
			else:
				matrice[i][w] = matrice[i-1][w]

	# find action with result
	nb_data = len(data)
	action_selected = []

	while max_invest >= 0 and nb_data >= 0:
		element = data[nb_data-1]
		print(element)
		print(matrice[nb_data][max_invest])
		print(matrice[nb_data - 1][max_invest - element['cout']])
		print(benefice(element))
		if matrice[nb_data][max_invest] == matrice[nb_data - 1][max_invest - element['cout']] + benefice(element):
			action_selected.append(element)
			max_invest-= element['cout']

		nb_data -= 1

	return matrice[-1][-1], action_selected


print(algo_dynamique(max_invest, data))


end = time.time()
elapsed = end - start
print(f"Temps d'execution du programme :{elapsed} s.")


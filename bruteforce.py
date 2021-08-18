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

# 1 - put all binary combinaison posible for 2^20 in data so 1 048 576 possibility
nb_element_data = len(data)
array_whole_nb = [i for i in range(2**nb_element_data)]
array_binary_nb = [bin(i)[2:] for i in array_whole_nb]
array_combi = ['0'*(nb_element_data-len(k)) + k for k in array_binary_nb] # add 0 to get the right lenght

# 2 - combinaison possible 
max_invest = 500
valid_combinaisons = []
for combi in array_combi:
	cout_combi = 0
	benefice_combi = 0
	for i in range (nb_element_data):
		if combi[i] == '1':
			cout_combi = cout_combi + data[i]['cout']
			benefice_combi = benefice_combi + (data[i]['cout']*data[i]['benefice'])
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
for i in range (len(solution_optimale)):
	if solution_optimale[i] == '1':
		liste_optimale.append(data[i]['nom'])

end = time.time()
elapsed = end - start


print(f"Liste des actions a favoriser pour un gain maximal de {benefice_max} €:")
for action in liste_optimale:
	print(action)
	
print(f"Temps d'execution du programme :{elapsed} s.")


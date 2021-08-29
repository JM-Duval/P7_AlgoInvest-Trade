#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script is an algorithme in order to find the optimal combination of action to get maximum gain 

import time
import csv
import pandas as pd
import numpy as np


class AlgoDynamique:

	def __init__(self, row_data, capacity):
		self.row_data = row_data
		self.capacity = capacity * 100
		
	def check_data(self, row_data):
		data = row_data[~(row_data[:,1]<=0)] # delete line with number 0
		return data * 100   # to run the script without float number
		
	def profit(self, index):
		return int (index[1] * index[2] )	
		
	def results(self, matrice):
		
		data = self.check_data(self.row_data)
		w = self.capacity
		n = len(data)
		action_selected = []
		
		while w >= 0 and n >= 0: # tant que la capacité est >= à 0 et que nous n'avons pas parcourus tout les éléments 
			element = data[n-1]
			if matrice[n][int(w)] == matrice[int(n-1)][int(w-element[1])] + self.profit(element):
				action_selected.append(element)
				w -= element[1]	
			n-=1
		
		total_cost = 0
		total_profit = 0
		nb_letter_name = len(row_data[0][0])  # we do this because we have multiplied all data per 100 
		name_actions = []
		for i in action_selected:
			total_cost += i[1] / 100
			total_profit += (i[1] / 100 * i[2] / 100 / 100)
			name_actions.append(i[0][:nb_letter_name])

		
		#print(name_actions)
		for action in name_actions:
			print('  ',action)
		print('total cost', round(total_cost,2))
		print('total profit', round(total_profit,2))
		#answer = str(round(answer, 2))

	def algo(self):

		data = self.check_data(self.row_data)
		
		matrice = [[0 for x in range (int((self.capacity + 1) ))] for x in range(len(data) + 1)]
		colomns = len(matrice[0]) 
		lines = len(matrice)
		
		for i in range(1, lines): # ligne
			for x in range(1, colomns): # colonne
				if data[i-1][1] <= x: # si le prix de l'élément courant est inférieur à la capacité
					matrice[i][x] = max( matrice[i-1][x] , # valeur de la ligne précédante
						matrice[i-1][int(x - data[i-1][1])] + # matrice[i-1][capacité - poids de l'élément courant => place qui reste dispo]
						self.profit(data[i-1]))# valeur de mon element courant
				else:
					matrice[i][x] = matrice[i-1][x] # on garde la valeur de i-1 
		
		return matrice

	def run(self):
		start = time.time() # calculate the working time of the program 
		self.results(self.algo())
		end = time.time()
		elapsed = end - start
		print(f"Temps d'execution :{round(elapsed,2)} s.")


file_dataset1 = 'dataset1_Python+P7.csv'
file_dataset2 = 'dataset2_Python+P7.csv'
dt = pd.read_csv(file_dataset2)
df = pd.DataFrame(dt)
row_data = df.to_numpy()

budget = 500
algo_dataset = AlgoDynamique(row_data, budget)
algo_dataset.run()


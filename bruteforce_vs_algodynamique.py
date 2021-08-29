#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This script give a comparison between a bruteforce script.py and optimized.py
# script



import time
import matplotlib.pyplot as plt
import numpy as np
from bruteforce import bruteforce
from optimized import algo_dynamique


data_base = [
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

{'nom':'action-21', 'cout':8, 'benefice':0.08},
{'nom':'action-22', 'cout':4, 'benefice':0.12},
{'nom':'action-23', 'cout':10, 'benefice':0.14},
{'nom':'action-24', 'cout':24, 'benefice':0.21},
{'nom':'action-25', 'cout':114, 'benefice':0.18},

{'nom':'action-26', 'cout':8, 'benefice':0.08},
{'nom':'action-27', 'cout':4, 'benefice':0.12},
{'nom':'action-28', 'cout':10, 'benefice':0.14},
{'nom':'action-29', 'cout':24, 'benefice':0.21},
{'nom':'action-30', 'cout':114, 'benefice':0.18},
]

max_invest = 500
nb_element = 16
e = 5

y_time_bf = []
x_elements_bf = []
y_time_op = []
x_elements_op = []
while e < nb_element:
	data = []
	for i in range(e):
		data.append(data_base[i])

	x_elements_bf.append(e)
	start_bf = time.time() # calculate the working time of the program 
	bruteforce(data, max_invest)
	end_bf = time.time()
	elapsed_bf = end_bf - start_bf
	y_time_bf.append(elapsed_bf)

	x_elements_op.append(e)
	start_op = time.time() # calculate the working time of the program 
	algo_dynamique(data, max_invest)
	end_op = time.time()
	elapsed_op = end_op - start_op
	y_time_op.append(elapsed_op)

	e+=1



x_bf = np.array(x_elements_bf)
y_bf = np.array(y_time_bf)

x_op = np.array(x_elements_op)
y_op = np.array(y_time_op)

plt.plot(x_bf, y_bf)
plt.plot(x_op, y_op)

plt.xlabel("element(n)")
plt.ylabel("time(s)")

plt.show()



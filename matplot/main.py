import csv
from math import sqrt, pi, sin, cos, atan2
import matplotlib.pyplot as plt 
import numpy as np 

branchs_X = [41.049792,41.069940,41.049997]
branchs_Y = [29.003031,29.019250,29.026108]
orders = []
orders_X = []
orders_Y = []
with open('orders.csv') as order_file:
    csv_reader = csv.reader(order_file, delimiter=',')

    for row in csv_reader:
        
        orders.append([float(x) for x in row])

for o in orders:
    orders_X.append(o[0])
    orders_Y.append(o[1])

plt.scatter(branchs_X,branchs_Y)
plt.scatter(orders_X, orders_Y,marker='X', c="g")
plt.show()
# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    check.py                                         .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: gaennuye <gaennuye@student.le-101.fr>      +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2020/01/20 16:24:53 by gaennuye     #+#   ##    ##    #+#        #
#    Updated: 2020/02/12 16:58:44 by gaennuye    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #


# Linear regression using direct formulas to use as basis when checking the
# results against ML generated data

import pandas as pd
from tools import *


def statLinearRegression():

	data = pd.read_csv("./data.csv")
	
	km_l = data["km"].tolist()  # List of the mileages
	price_l = data["price"].tolist()  # List of the prices
	
	# x will be the mileage
	# y will be the price
	
	avg_x = average(km_l)  # avg_x is the average mileage
	avg_y = average(price_l)  # avg_y is the average price
	
	print(avg_x)
	print(avg_y)
	
	sxx = 0
	sxy = 0

	
	i = 0
	while i < len(data["km"]):
		sxx += (data["km"][i] - avg_x) ** 2
		sxy += (data["km"][i] - avg_x) * (data["price"][i] - avg_y)
		i += 1
	
	print(sxx)
	print(sxy)
	
	# The plot's formula is aX + b + err
	a = sxy / sxx
	
	print("\na =", a)
	
	b = avg_y - a * avg_x
	
	print("b =", b)
	
	
	new_km = int(input("What's the mileage of the car ? "))
	
	new_price = round(a * new_km + b)
	
	print(new_price)
	
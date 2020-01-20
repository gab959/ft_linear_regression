# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    main.py                                          .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: gaennuye <gaennuye@student.le-101.fr>      +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2020/01/20 11:05:31 by gaennuye     #+#   ##    ##    #+#        #
#    Updated: 2020/01/20 14:19:57 by gaennuye    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #


import pandas as pd
from tools import *

data = pd.read_csv("./data.csv")

km_l = data["km"].tolist() # List of the mileages
price_l = data["price"].tolist() # List of the prices

# x will be the mileage
# y will be the price

avg_x = average(km_l) # avg_x is the average mileage
avg_y = average(price_l) # avg_y is the average price

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



# [240000; 139800; 150500; 185530; 176000; 114800; 166800; 89000; 144500; 84000; 82029; 63060; 74000; 97500; 67000; 76025; 48235; 93000; 60949; 65674; 54000; 68500; 22899; 61789]
# [3650; 3800; 4400; 4450; 5250; 5350; 5800; 5990; 5999; 6200; 6390; 6390; 6600; 6800; 6800; 6900; 6900; 6990; 7490; 7555; 7990; 7990; 7990; 8290]
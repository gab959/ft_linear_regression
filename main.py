# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    main.py                                          .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: gaennuye <gaennuye@student.le-101.fr>      +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2020/01/20 11:05:31 by gaennuye     #+#   ##    ##    #+#        #
#    Updated: 2020/02/21 18:23:14 by gaennuye    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as preprocessing

# theta0 = 0
# theta1 = 0

learning_rate = 1
num_iterations = 10

data = pd.read_csv("./resources/data.csv")
# data = preprocessing.scale(data)
points = preprocessing.scale(np.array(data))
# print(points)
kms = preprocessing.scale(points[:,0])
prices = preprocessing.scale(points[:,1])

print(kms)
print(prices)

def estimatePrice(theta0, theta1,km):
    res = theta1 * km + theta0
    return res


def gradientStep(learning_rate, theta0, theta1, points):
    error = [0, 0]
    tmp_theta0 = 0
    tmp_theta1 = 0
    for km, price in points:
        diff = estimatePrice(theta0, theta1, km) - price
        error[0] += diff
        error[1] += diff * km
    # print(error)
    tmp_theta0 = learning_rate * error[0] / len(points)
    tmp_theta1 = learning_rate * error[1] / len(points)
    print("end gradient tmp :", tmp_theta0, tmp_theta1, "\n\n")
    return theta0 - tmp_theta0, theta1 - tmp_theta1


def trainProgram(num_iterations):
    newtheta0 = 0
    newtheta1 = 0
    for i in range(num_iterations):
        print("in train new :", newtheta0, newtheta1)
        newTheta = gradientStep(learning_rate, newtheta0, newtheta1, points)
        newtheta0 = newTheta[0]
        newtheta1 = newTheta[1]
    return
    

axes = plt.gca()
axes.set_xlim([0, max(kms) * 1.1])
axes.set_ylim([0,max(prices) * 1.1])

plt.scatter(kms, prices)
plt.xlabel('km', color='#1C2833')
plt.ylabel('Price', color='#1C2833')
plt.grid()

# gradientStep(learning_rate, theta0, theta1, points)
trainProgram(num_iterations)
# plt.show()
    
# [240000; 139800; 150500; 185530; 176000; 114800; 166800; 89000; 144500; 84000; 82029; 63060; 74000; 97500; 67000; 76025; 48235; 93000; 60949; 65674; 54000; 68500; 22899; 61789]
# [3650; 3800; 4400; 4450; 5250; 5350; 5800; 5990; 5999; 6200; 6390; 6390; 6600; 6800; 6800; 6900; 6900; 6990; 7490; 7555; 7990; 7990; 7990; 8290]
    
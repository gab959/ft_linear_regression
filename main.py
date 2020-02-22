# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    main.py                                          .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: gaennuye <gaennuye@student.le-101.fr>      +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2020/01/20 11:05:31 by gaennuye     #+#   ##    ##    #+#        #
#    Updated: 2020/02/22 17:54:47 by gaennuye    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as sk

theta0 = 0
theta1 = 0

learning_rate = 1.2
num_iterations = 1000

data = pd.read_csv("./resources/data.csv")
# data = pd.read_csv("../GradientDescentExample/data.csv")

scaler = sk.MinMaxScaler()
points = scaler.fit_transform(np.array(data))

print(scaler.scale_)
sys.exit()

kms = points[:,0]
prices = points[:,1]

# print("points : \n", points, '\n')

stock_points = np.array(data)
stock_kms = stock_points[:,0]
stock_prices = stock_points[:,1]


def estimatePrice(theta0, theta1, km):
    res = theta1 * km + theta0
    return res


def gradientStep(learning_rate, theta0, theta1, points):
    print("GS : ", theta0, theta1)
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
    theta0 = 0
    theta1 = 0
    plt.ion()
    for i in range(num_iterations):
        print("TP | i = ", i, " | Coefs :", theta0, theta1)
        print(theta0 / scaler.scale_[0])
        print(theta1 * scaler.scale_[1])
        # print(scaler.inverse_transform(theta0))
        # print(scaler.inverse_transform(theta1))
        newTheta = gradientStep(learning_rate, theta0, theta1, points)
        theta0 = newTheta[0]
        theta1 = newTheta[1]
        plt.scatter(stock_kms, stock_prices)

        plt.plot(stock_kms, estimatePrice(theta0, theta1, kms) * 2 / scaler.scale_[1], '-r', label='estimatePrice(km)')
    
        plt.xlabel('Km', color='#1C2833')
        plt.ylabel('Price', color='#1C2833')
        plt.legend(loc='upper right')
    
        plt.grid()
        plt.pause(0.01)
        plt.clf()
    return
    
trainProgram(num_iterations)
#TODO add prompt for user input
    
# [240000; 139800; 150500; 185530; 176000; 114800; 166800; 89000; 144500; 84000; 82029; 63060; 74000; 97500; 67000; 76025; 48235; 93000; 60949; 65674; 54000; 68500; 22899; 61789]
# [3650; 3800; 4400; 4450; 5250; 5350; 5800; 5990; 5999; 6200; 6390; 6390; 6600; 6800; 6800; 6900; 6900; 6990; 7490; 7555; 7990; 7990; 7990; 8290]
    
#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as sk

theta0 = 0
theta1 = 0

learning_rate = 1
num_iterations = 1000

data = pd.read_csv("./resources/data.csv")

scaler = sk.MinMaxScaler()
points = scaler.fit_transform(np.array(data))

print(scaler.scale_)

kms = points[:,0]
prices = points[:,1]
print(kms)
print(prices)


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

        if i < 81:
            axes = plt.gca()
            axes.set_xlim([0, max(stock_kms) * 1.1])
            axes.set_ylim([0, max(stock_prices) * 1.1])
            
            plt.plot(stock_kms, estimatePrice(theta0, theta1, kms) / scaler.scale_[1] + min(stock_prices), '-r', label='estimatePrice(km)')
            plt.scatter(stock_kms, stock_prices)
        
            # plt.plot(kms, estimatePrice(theta0, theta1, kms), '-r', label='estimatePrice(km)')
            # plt.scatter(kms, prices)
    
            plt.xlabel('Km', color='#1C2833')
            plt.ylabel('Price', color='#1C2833')
            plt.legend(loc='upper right')
        
            plt.grid()
            if i < 80:
                plt.pause(0.01)
                plt.clf()
            else:
                plt.draw()

    print("TP END : ", theta0, theta1)
    return theta0, theta1

thetas = trainProgram(num_iterations)


print(theta0, theta1)

while 1:
    print("Please type the mileage of the car :")
    km_in = float(input())
    scaled_km_in = scaler.scale_[0] * km_in - min(stock_kms) * scaler.scale_[0]
    price = estimatePrice(thetas[0], thetas[1], scaled_km_in) / scaler.scale_[1] + min(stock_prices)
    print("The price of your car is ", price, "€")
    plt.scatter(km_in, price)

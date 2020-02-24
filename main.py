#! /usr/bin/env python3




#TODO Add plotting of the thetas
#TODO Add arguments to either run or train the program
#TODO Learn what overfitting is
#TODO CLEAN THE CODE




import time
import progressbar
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as sk

learning_rate = 1
num_iterations = 1000

# for i in progressbar.progressbar(range(100)):
    # time.sleep(0.02)


data = pd.read_csv("./resources/data.csv")

scaler = sk.MinMaxScaler()
points = scaler.fit_transform(np.array(data))

kms = points[:,0]
prices = points[:,1]

stock_points = np.array(data)
stock_kms = stock_points[:,0]
stock_prices = stock_points[:,1]


def estimatePrice(theta, km):
    res = theta[1] * km + theta[0]
    return res


def computeDiff(theta, points):
    error = [0, 0]
    for km, price in points:
        diff = estimatePrice(theta, km) - price
        error[0] += diff
        error[1] += diff * km
    return error


def gradientStep(learning_rate, theta, points):
    # error = [0, 0]
    tmp_theta = [0, 0]

    # for km, price in points:
        # diff = estimatePrice(theta, km) - price
        # error[0] += diff
        # error[1] += diff * km
    error = computeDiff(theta, points)

    tmp_theta[0] = learning_rate * error[0] / len(points)
    tmp_theta[1] = learning_rate * error[1] / len(points)
   
    # print("GS | tmp_theta : ", tmp_theta[0], tmp_theta[1])

    return theta[0] - tmp_theta[0], theta[1] - tmp_theta[1]


def trainProgram(num_iterations):
    theta = [0,0]
    plt.ion()
    for i in progressbar.progressbar(range(num_iterations)):
        theta = gradientStep(learning_rate, theta, points)
        # print("TP | i = ", i," newTheta :", theta)

        if i < 81:
            axes = plt.gca()
            axes.set_xlim([0, max(stock_kms) * 1.1])
            axes.set_ylim([0, max(stock_prices) * 1.1])
            # 
            plt.plot(stock_kms, estimatePrice(theta, kms) / scaler.scale_[1] + min(stock_prices), '-r', label='estimatePrice(km)')
            plt.scatter(stock_kms, stock_prices)

            # plt.plot(kms, estimatePrice(theta, kms), '-r', label='estimatePrice(km)')
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

    print("\nThe training of the program is done. \nFinal parameters : ", theta)

    diff = []
    for i, val in enumerate(points):
        # print(val[0], val[1], i)
        ep = abs(estimatePrice(theta, val[0]) / scaler.scale_[1] + min(stock_prices))
        # print(ep, stock_prices[i], ep/stock_prices[i])
        prop = ep / stock_prices[i] - 1
        diff.append(abs(prop))

    print("Average error : ", round(sum(diff)/len(diff), 4) * 100, "%") 


    print("\n------------------------------------------------------------------\n\n")
    return theta

thetas = trainProgram(num_iterations)


# print(theta)
sys.exit(0)
while 1:
    print("What is the mileage of the car ?")
    km_in = input()
    try:
        km_in = float(km_in)
    except ValueError:
        print("Please type a valid mileage.")
        continue
    if km_in < 0:
        print("Are you dumb ?")
        continue
    scaled_km_in = scaler.scale_[0] * km_in - min(stock_kms) * scaler.scale_[0]
    price = estimatePrice(thetas, scaled_km_in) / scaler.scale_[1] + min(stock_prices)
    print("The price of your car is ", round(price,2), "€")
    plt.scatter(km_in, price)

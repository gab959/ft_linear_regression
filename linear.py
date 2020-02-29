# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 14:29:06 by gaennuye          #+#    #+#              #
#    Updated: 2020/02/29 18:56:24 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import header as h
import plot as p
import matplotlib.pyplot as plt
import numpy as np
import progressbar


h.init()


def estimatePrice(km):
    res = h.g_theta[1] * km + h.g_theta[0]
    return res


# For each point, calculating the difference between the 
# computed price and the "real" price with the current thetas

def computeDiff(points):
    error = [0, 0]
    for km, price in points:
        diff = estimatePrice(km) - price
        error[0] += diff
        error[1] += diff * km
    return error


# Returns the difference between current thetas and the processed
# tmp_thetas 

def gradientStep(learning_rate, points):
    tmp_theta = [0, 0]

    error = computeDiff(points)

    tmp_theta[0] = learning_rate * error[0] / len(points)
    tmp_theta[1] = learning_rate * error[1] / len(points)
   
    # print("GS | tmp_theta : ", tmp_theta[0], tmp_theta[1])

    return h.g_theta[0] - tmp_theta[0], h.g_theta[1] - tmp_theta[1]


# Calculating the error ratio of the program

def calcError(points, stock_prices):
    diff = []
    for i, val in enumerate(points):
        ep = abs(estimatePrice(val[0]) / h.scaler.scale_[1] + min(stock_prices))
        # calculating the ratio between the "real" price and the computed price
        proportion = ep / stock_prices[i] - 1
        diff.append(abs(proportion))
    return diff


# Main function used to train the program

def trainProgram(points, stock_points):

    args = h.parser.parse_args()
    
    kms = points[:,0]

    stock_kms = stock_points[:,0]
    stock_prices = stock_points[:,1]


    h.g_theta = [0,0]
    learning_rate = 1
    num_iterations = 1000
    plot_refreshes = 0

    if args.plot:
        plot_refreshes = 80
        plt.ion()
        evo_thetas_x = []
        evo_thetas_y = []
    
    print("Training the program...")
    for i in progressbar.progressbar(range(num_iterations)):

        h.g_theta = gradientStep(learning_rate, points)
       
        if i < plot_refreshes:
            
            evo_thetas_x.append(h.g_theta[0])
            evo_thetas_y.append(h.g_theta[1])

            p.plotThetas(evo_thetas_x, evo_thetas_y)
            p.plotAll(stock_kms, stock_prices, kms) 
            plt.grid()

            # Refreshing the graph 
            if i < plot_refreshes - 1:
                plt.pause(0.01)
                plt.clf()
            else:
                plt.draw()
 

    print("\nThe training of the program is done.\n")
    print("The final parameters are :\ntheta0 = ", h.g_theta[0], "\ntheta1 = ", h.g_theta[1], "\n")

    diff = calcError(points, stock_prices)

    print("Average error : ", round(sum(diff)/len(diff), 4) * 100, "%") 

    print("\n------------------------------------------------------------------\n\n")
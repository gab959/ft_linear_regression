# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 18:38:27 by gaennuye          #+#    #+#              #
#    Updated: 2020/03/01 12:47:56 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import _global as g
import linear as l
import matplotlib.pyplot as plt


g.init()


# Plotting the evolution of the theta for each step of the gradient descent

def plotThetas(evo_thetas_x, evo_thetas_y):
    plt.figure(58)
    fig = plt.gcf()
    fig.canvas.set_window_title('ft_linear_regression')
    plt.title("Evolution of the parameters, based on the scaled datasets")
    
    plt.plot(evo_thetas_x, evo_thetas_y) # Plotting the evolution of the thetas
    # Plotting as a point the current thetas
    plt.scatter(g.theta[0], g.theta[1], label='Current (theta0, theta1)')
    
    plt.xlabel('theta0', color='#1C2833')
    plt.ylabel('theta1', color='#1C2833')
    plt.legend(loc='upper right')
 

# Plots the current regression line and all the points of the dataset

def plotAll(stock_kms, stock_prices, scaled_kms):
    plt.figure(59) #initializing the plot figure
    fig = plt.gcf()
    fig.canvas.set_window_title('ft_linear_regression')
    plt.title("Linear regression")
    
    # Setting the axes depending on the dataset
    axes = plt.gca()
    axes.set_xlim([0, max(stock_kms) * 1.1])
    axes.set_ylim([0, max(stock_prices) * 1.1])
    
    # Plots the data and the line with the de-scaled values
    estP = l.estimatePrice(scaled_kms) / g.scaler.scale_[1] + min(stock_prices)
    plt.plot(stock_kms, estP, '-r', label='estimatePrice(km)')
    plt.scatter(stock_kms, stock_prices)
    
    plt.xlabel('Km', color='#1C2833')
    plt.ylabel('Price', color='#1C2833')
    plt.legend(loc='upper right')
#! /usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 17:48:35 by gaennuye          #+#    #+#              #
#    Updated: 2020/02/29 17:48:38 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import os
import sys
import _global as g
import linear
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


g.init()


# Reading the arguments

g.parser.add_argument("-t", "--path", type=str,
                    help="Trains the program with the selected dataset")
g.parser.add_argument("--plot",
                    help="Enables the visualization of the data",
                    action="store_true")
args = g.parser.parse_args()

if args.plot and args.path is None:
    g.parser.error("Training of the program is required to plot the data.")


# Runs the training of the program only if the -t argument is specified

if args.path is not None:
    
    if os.path.exists(args.path):
        data = pd.read_csv(args.path)
        points = g.scaler.fit_transform(np.array(data))

        stock_points = np.array(data)
        stock_kms = stock_points[:,0]
        stock_prices = stock_points[:,1]

        linear.trainProgram(points, stock_kms, stock_prices)
    else:
        print("File doesn't exist !")
        sys.exit(1)


# Prompt user for mileage

while 1:
    print("What is the mileage of the car?")
    km_in = input("> ")
    
    try:
        km_in = float(km_in)
    except ValueError:
        print("Please type a valid mileage.\n")
        continue

    if km_in < 0:
        print("Are you drunk?\n")
        continue

    #If the program is trained, data must be "de-scaled"
    if args.path is not None:
        scaled_km_in = g.scaler.scale_[0] * km_in - min(stock_kms) * g.scaler.scale_[0]
        price = linear.estimatePrice(scaled_km_in) / g.scaler.scale_[1] + min(stock_prices)
    else:
        price = linear.estimatePrice(km_in)
    
    if price < 0:
        print("I'll bring your car to the junkyard if you give me", abs(round(price,2)), "€\n")
    else:
        print("The price of your car is " + str(round(price,2)) + "€\n")
    if plt.fignum_exists(59):
        plt.scatter(km_in, price)

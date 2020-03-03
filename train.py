#! /usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 17:48:35 by gaennuye          #+#    #+#              #
#    Updated: 2020/03/02 16:58:16 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import os
import sys
import json
import _global as g
import linear
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from predict import predict


g.init()


# Updates the values in the config.json after the training
# or resets them when the --reset flag is present

def updateConfig(is_trained, min_price, min_km):
    to_json = {}
    to_json['is_trained'] = is_trained
    to_json['theta'] = g.theta
    to_json['min'] = {'price' : min_price, 'km' : min_km}
    try:
        to_json['scale'] = g.scaler.scale_.tolist()
    except:
        to_json['scale'] = [0,0]
    
    with open('config.json', 'w') as outfile:
        json.dump(to_json, outfile, indent=4)


# Reading the arguments

g.parser.add_argument("path", nargs='?', type=str,
                    help="Trains the program with the selected dataset")
g.parser.add_argument("--plot",
                    help="Enables the visualization of the data",
                    action="store_true")
g.parser.add_argument("--reset",
                    help="Resets the values in the config.json file",
                    action="store_true")

args = g.parser.parse_args()

if args.reset and (args.path or args.plot):
    g.parser.error("You can't use additional flag when using --reset")

if args.plot and args.path is None:
    g.parser.error("Please specify a file to train the program to plot the data.")

if args.reset:
    updateConfig(False, 0,0)
    print("The program was successfully reset.")
    sys.exit(0)


# Runs the training of the program only if the -t argument is specified

if args.path is not None:
    
    if os.path.exists(args.path):
        try:
            data = pd.read_csv(args.path)
        except:
            print("Are you sure that the specified path is correct?")
            sys.exit(1)

        points = g.scaler.fit_transform(np.array(data))

        stock_points = np.array(data)
        stock_kms = stock_points[:,0]
        stock_prices = stock_points[:,1]

        linear.trainProgram(points, stock_kms, stock_prices)

        updateConfig(True, int(min(stock_prices)), int(min(stock_kms))) 

    else:
        print("File doesn't exist!")
        sys.exit(1)

else:
    print("Please specify the path of the dataset used to train the program.")
    sys.exit(1)

answer = input("Do you want to run the prediction program? [Y/n] : ")

if answer in {"Y", "y", "yes", "yeah"}:
    print("\n")
    predict()

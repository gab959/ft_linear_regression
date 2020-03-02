#! /usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/02 11:49:37 by gaennuye          #+#    #+#              #
#    Updated: 2020/03/02 16:58:33 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import json
import os
import sys


# Initializing the prediction program with the config file

def initPredict():
    global g
    if os.path.exists('config.json') is not True:
        print("There was an error reading the config.json file. Have you trained the program?")
        sys.exit(1)

    with open('config.json', 'r') as f:
        g = json.load(f)


# Estimating the price depending on the mileage

def estimatePrice(km):
    res = g['theta'][1] * km + g['theta'][0]
    return res


# Main function of the prediction, prompting the user for a mileage
# and calling the estimatePrice function

def predict():

    initPredict()

    while 1:
        print("What is the mileage of the car?")
        km_in = input("> ")

        if km_in in {"quit", "exit"}:
            sys.exit(1)

        # Checking that the input is valid
        try:
            km_in = float(km_in)
        except ValueError:
            print("Please type a valid mileage.\n")
            continue
        if km_in < 0:
            print("Are you drunk?\n")
            continue

        #If the program is trained, data must be "de-scaled"
        if g["is_trained"] is True:
            scaled_km_in = g['scale'][0] * (km_in - g['min']['km'])
            price = estimatePrice(scaled_km_in) / g['scale'][1] + g['min']['price']
        else:
            price = estimatePrice(km_in)
    
        if price < 0:
            print("I'll bring your car to the junkyard if you give me", abs(round(price,2)), "€\n")
        else:
            print("The price of your car is " + str(round(price,2)) + "€\n")


def main():
    predict()


if __name__== "__main__":
  main()
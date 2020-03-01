# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    _global.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gaennuye <gaennuye@student.le-101.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/29 15:12:49 by gaennuye          #+#    #+#              #
#    Updated: 2020/03/01 12:48:27 by gaennuye         ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sklearn.preprocessing as sk
import argparse


def init():
    global scaler
    global parser
    global theta

    scaler = sk.MinMaxScaler()
    parser = argparse.ArgumentParser()
    theta = [0,0]
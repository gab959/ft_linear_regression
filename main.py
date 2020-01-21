# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    main.py                                          .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: gaennuye <gaennuye@student.le-101.fr>      +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2020/01/20 11:05:31 by gaennuye     #+#   ##    ##    #+#        #
#    Updated: 2020/01/20 17:03:34 by gaennuye    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

import pandas as pd

tet0 = 0
tet1 = 0


def estimatePrice(mileage):
    #estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)

    return tet0 + (tet1 * mileage)

    
def trainProgram(tet0, tet1):
    print("Training")

    data = pd.read_csv("./data.csv")
    print(data)

    i = 0
    for i < len(data["km"]):
        

    return tet0, tet1



print(estimatePrice(8255))
trainProgram()
    
    
# [240000; 139800; 150500; 185530; 176000; 114800; 166800; 89000; 144500; 84000; 82029; 63060; 74000; 97500; 67000; 76025; 48235; 93000; 60949; 65674; 54000; 68500; 22899; 61789]
# [3650; 3800; 4400; 4450; 5250; 5350; 5800; 5990; 5999; 6200; 6390; 6390; 6600; 6800; 6800; 6900; 6900; 6990; 7490; 7555; 7990; 7990; 7990; 8290]
    

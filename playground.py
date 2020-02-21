import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./data.csv")

def hypothesis(x, i):
    theta0 = i*50
    # theta1 = i/100
    theta1 = 1
    return theta1 * x / 100 + theta0
    # return i/100 * x


# for index, row in data.iterrows():
    # km = row['km']
    # price = row['price']
    # print(km)
    # print(price)
    # print('hyp : ', hypothesis(km));
    # print('\n')




# # #PLOT

kms = data['km'].to_numpy()
prices = data['price'].to_numpy()

plt.ion()
# plt.scatter(kms, prices)

# y = 0.04*kms+1
# plt.plot(kms, y, '-r', label='y=0.04km+1')
# plt.xlabel('km', color='#1C2833')
# plt.ylabel('estPrice', color='#1C2833')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

x = np.linspace(0,max(kms))

for i in range(1000):
    print(i)
    plt.scatter(kms, prices)
    y = hypothesis(x, i)
    
    axes = plt.gca()
    axes.set_xlim([0, max(kms) * 1.1])
    axes.set_ylim([0,max(prices) * 1.1])

    plt.plot(x, y, '-r', label='estPrice(km)')
    
    plt.xlabel('km', color='#1C2833')
    plt.ylabel('estPrice', color='#1C2833')
    plt.legend(loc='upper right')
    
    plt.grid()
    plt.pause(1)
    plt.clf()
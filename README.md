# ft_linear_regression


This project is the first data project of the 42 school's cursus.
The goal is to implement a program to predict the price of a used car depending on its mileage.
The values of the program are initialized to 0, and we have to train the program using a linear regression to predict the price of the car. In order to calculate the coefficients, we have to use a gradient descent algorithm. This repo contains two different programs : the first one processes the training and the second one estimates the price.


## Requirements

- `matplotlib.pyplot`
- `numpy`
- `pandas`
- `argparse`
- `progressbar2`

## Usage

You can run the training program with `python3 train.py ./path_to_the_file`. \
To plot the data, the line and the evolution of the coefficients during the training, use `--plot`.\
The coefficients will be stored in the `config.json` file which will be used by the prediction program.\
To reset the program, you can use the flag `--reset` without specifying any other option.

Once the training is done, you can then run the prediction program with `python3 predict.py`.\
It will ask you for the mileage of your car, and return its estimated value. To quit the program, just type `quit` or `exit` in the prompt.

Please note that the plotting option only works if you specify a path for the training.
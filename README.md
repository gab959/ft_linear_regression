# ft_linear_regression


This project is the first data project of the 42 school's cursus.
The goal is to implement a program to predict the price of a used car depending on its mileage.
The values of the program are initialized to 0, and we have to train the program using a linear regression to predict the price of the car. In order to calculate the coefficients, we have to use a gradient descent algorithm.


## Requirements

- `matplotlib.pyplot`
- `numpy`
- `pandas`
- `argparse`
- `progressbar2`

## Usage

You can run the program with `python3 main.py`. If no argument is specified, it will display a prompt for the mileage of the car without any previous training, the result will always be 0.

To train the program, use the following option : `-t ./path_to_your_file`\
To plot the data, the line and the evolution of the coefficients during the training, use `--plot`.

Once the training is done, the program will then ask you for the mileage of your car, and return its estimated value.

Please note that the `-t` option is mandatory to use the plotting flag.
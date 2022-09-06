"""
    loss calculation function for regression
    input: real, computed:2 lists of floats representing real and simulated data
    output:  cost: error from the dataset
"""


def loss_squared_error(real, computed):
    suma = 0
    for i in range(len(real)):
        suma += (computed[i] - real[i]) ** 2
    cost = suma / len(real)
    return cost


def testLoss():
    real = [1,5,4,3,2,3,2]
    computed = [1,3,4,2,5,2,1]
    assert loss_squared_error(real, computed) == 2.2857142857142856
    real = [0,1, 2, 3, 4, 5, 6, 7, 8]
    computed = [0,1,2,3,4,5,6,7,8]
    assert loss_squared_error(real, computed) == 0



import numpy as np
import numpy.random as rand
from sklearn import linear_model

from ZNormalisation import normalize_uni
from loss import loss_squared_error

"""
    input: inputs: lista de numere reale, outputs: lista de numere reale, epochs: numar intreg
    output: eroare de predictie in cazul regresie cu gradient descrescător bazat pe batch-uri (cu tool)
    + se calculeaza si modelul liniar al regresie: f(x) = w0 + w1 * x

   Mini-batch GD
         Setul de date se împarte în mai multe părți (mini-batch-uri)
         Eroarea se calculează pentru fiecare exemplu de antrenament dintr-un mini-batch
         Modelul se updatează pentru fiecare exemplu de antrenament dintr-un mini-batch
"""


def univariateTool(inputs, outputs, epochs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs = [inputs[i] for i in testSample]
    validationOutputs = [outputs[i] for i in testSample]

    trainInputs, trainOutputs, validationInputs, validationOutputs = normalize_uni(
        trainInputs, trainOutputs, validationInputs, validationOutputs)
    # pasul de antrenament
    X = [[trainInputs[i]] for i in range(len(trainInputs))]
    regressor = linear_model.SGDRegressor(learning_rate='constant', eta0=0.01, shuffle=True)

    # vom forma batch-uri de elemente folosind doi indecsi random din intervalul [0, len(X)]
    for i in range(epochs):
        x_aux, y_aux = generateBatch(X, trainOutputs)
        regressor.partial_fit(x_aux, y_aux)
    w0, w1 = regressor.intercept_[0], regressor.coef_[0]
    print("Modelul invatat este: f(x)= " + str(w1) + " * feat1 + " + str(w0))

    # pasul de validare
    computedValidationOutputs = []
    for i in range(len(validationInputs)):
        value = w0 + w1 * validationInputs[i]
        computedValidationOutputs.append(value)

    # calculam eroarea in predictie
    manual_err = loss_squared_error(computedValidationOutputs, validationOutputs)

    return manual_err


"""
    input: X-lista de liste formate dintr-un numar real si Y-lista de numere reale
    output: aux_x submultime a listei X si aux_Y submultime a listei Y
"""


def generateBatch(X, Y):
    i = np.random.randint(len(X))
    j = np.random.randint(len(X))
    if i > j:
        i, j = j, i
    aux_x = []
    aux_y = []
    for k in range(i, j):
        aux_x.append(X[k])
        aux_y.append(Y[k])
    return aux_x, aux_y


"""
    input: inputs: lista de numere reale, outputs: lista de numere reale, epochs: numar intreg 
    output: eroare de predictie in cazul regresie cu gradient descrescător bazat pe batch-uri
    + se calculeaza si modelul liniar al regresie: f(x) = w0 + w1 * x
"""


def univariateManual(inputs, outputs, epochs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs = [inputs[i] for i in testSample]
    validationOutputs = [outputs[i] for i in testSample]

    trainInputs, trainOutputs, validationInputs, validationOutputs = normalize_uni(
        trainInputs, trainOutputs, validationInputs, validationOutputs)
    # pasul de antrenament
    eta = 0.01
    w = []
    w.append([rand.random(), rand.random()])
    for j in range(epochs):
        x_aux, y_aux = generateBatch(trainInputs, trainOutputs)
        w_aux = [[w[j][0], w[j][1]]]
        for i in range(1, len(x_aux)):
            err = sum([(w_aux[i - 1][0] + w_aux[i - 1][1] * x_aux[j] - y_aux[j]) for j in range(i)]) / i
            w1 = w_aux[i - 1][1] - eta * err * x_aux[i - 1]
            w0 = w_aux[i - 1][0] - eta * err
            w_aux.append([w0, w1])
        w.append([w_aux[-1][0], w_aux[-1][1]])

    w0, w1 = w[-1][0], w[-1][1]
    print("Modelul invatat este: f(x)= " + str(w1) + " * feat1 + " + str(w0))

    # pasul de validare
    computedValidationOutputs = []
    for i in range(len(validationInputs)):
        value = w0 + w1 * validationInputs[i]
        computedValidationOutputs.append(value)

    # calculam eroarea in predictie
    manual_err = loss_squared_error(computedValidationOutputs, validationOutputs)

    return manual_err

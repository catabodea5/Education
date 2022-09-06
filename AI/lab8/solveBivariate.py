import numpy as np
import numpy.random as rand
from sklearn import linear_model
from loss import loss_squared_error
from ZNormalisation import normalize

""""
    input: inputs1: lista de numere reale, inputs2: lista de numere reale,
                            outputs: lista de numere reale, epochs: numar intreg
    output: impartirea datelor in date de antrenament (80% din total) si restul pentru validare
                        folosind indici random
"""
def createData(inputs1, inputs2, outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs1))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs1)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs1 = [inputs1[i] for i in trainSample]
    trainInputs2 = [inputs2[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    validationInputs1 = [inputs1[i] for i in testSample]
    validationInputs2 = [inputs2[i] for i in testSample]
    validationOutputs = [outputs[i] for i in testSample]

    return trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs

"""
    input: inputs1: lista de numere reale, inputs2: lista de numere reale,
                            outputs: lista de numere reale, epochs: numar intreg
    output: eroare de predictie in cazul regresie cu gradient descrescător bazat pe batch-uri (cu tool)
    + se calculeaza si modelul liniar al regresie: f(x) = w0 + w1 * x1 + w2 * x2

   Mini-batch GD
         Setul de date se împarte în mai multe părți (mini-batch-uri)
         Eroarea se calculează pentru fiecare exemplu de antrenament dintr-un mini-batch
         Modelul se updatează pentru fiecare exemplu de antrenament dintr-un mini-batch
"""


def bivariateTool(inputs1, inputs2, outputs, epochs):
    trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs = createData(
        inputs1, inputs2, outputs)
    trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs = normalize(
        trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs)

    # pasul de antrenament
    X = [[trainInputs1[i], trainInputs2[i]] for i in range(len(trainInputs1))]
    regressor = linear_model.SGDRegressor(learning_rate='constant', eta0=0.01, shuffle=True)

    # vom forma batch-uri de elemente folosind doi indecsi random din intervalul [0, len(X)]
    for i in range(epochs):
        x_aux, y_aux = generateBatch(X, trainOutputs)
        regressor.partial_fit(x_aux, y_aux)
    w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
    print("Modelul invatat este: f(x)= " + str(w0) + " + " + str(w1) + " * feat1 + " +  str(w2) + " * feat2")

    # pasul de validare
    computedValidationOutputs = []
    for i in range(len(validationInputs1)):
        value = w0 + w1 * validationInputs1[i] + w2 * validationInputs2[i]
        computedValidationOutputs.append(value)

    # calculam eroarea in predictie
    manual_err =loss_squared_error(computedValidationOutputs, validationOutputs)

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
    input: inputs1: lista de numere reale, inputs2: lista de numere reale, outputs: lista de numere reale, epochs: numar intreg 
    output: eroare de predictie in cazul regresie cu gradient descrescător bazat pe batch-uri
    + se calculeaza si modelul liniar al regresie: f(x) = w0 + w1 * x1 + w2 * x2
"""


def bivariateManual(inputs1, inputs2, outputs, epochs):
    trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs = createData(
        inputs1, inputs2, outputs)
    trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs = normalize(
        trainInputs1, trainInputs2, trainOutputs, validationInputs1, validationInputs2, validationOutputs)

    #pasul de antrenament
    X = [[trainInputs1[i], trainInputs2[i]] for i in range(len(trainInputs1))]
    eta = 0.01
    w = []
    w.append([rand.random(), rand.random(), rand.random()])
    for j in range(epochs):
        x_aux, y_aux = generateBatch(X, trainOutputs)
        w_aux = [[w[j][0], w[j][1], w[j][2]]]
        for i in range(1, len(x_aux)):
            err = sum([(w_aux[i-1][0] + w_aux[i-1][1] * x_aux[j][0] + w_aux[i-1][2] * x_aux[j][1] - y_aux[j])
                        for j in range(i)]) / i
            w0 = w_aux[i-1][0] - eta * err
            w1 = w_aux[i-1][1] - eta * err * x_aux[i-1][0]
            w2 = w_aux[i-1][2] - eta * err * x_aux[i-1][1]
            w_aux.append([w0,w1, w2])
        w.append([w_aux[-1][0], w_aux[-1][1], w_aux[-1][2]])

    w0, w1, w2 = w[-1][0], w[-1][1], w[-1][2]
    print("Modelul invatat este: f(x)= "  + str(w0) + " + "+ str(w1) + " * feat1 + " + str(w2) + " * feat2")

    # pasul de validare
    computedValidationOutputs = []
    for i in range(len(validationInputs1)):
        value = w0 + w1 * validationInputs1[i] + w2 * validationInputs2[i]
        computedValidationOutputs.append(value)

    # calculam eroarea in predictie
    manual_err = loss_squared_error(computedValidationOutputs, validationOutputs)

    return manual_err


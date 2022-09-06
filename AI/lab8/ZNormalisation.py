import math

""""
    inputs: lista de numere reale ce reprezinta features + lista de numere reale
                ce reprezinta valorile de output in calcularea regresiei
    output: media si deviatia standard pentru fiecare set de date
"""
def createParams(trainInputs1, trainInputs2, trainOutputs):
    med1 = sum(trainInputs1) / len(trainInputs1)
    med2 = sum(trainInputs2) / len(trainInputs2)
    med3 = sum(trainOutputs) / len(trainOutputs)

    s1, s2, s3 = 0,0,0
    for i in range(len(trainInputs1)):
        s1 += (trainInputs1[i] - med1) ** 2
        s2 += (trainInputs2[i] - med2) ** 2
        s3 += (trainOutputs[i] - med3) ** 2
    standar_dev1 = math.sqrt(s1 / len(trainInputs1))
    standard_dev2 = math.sqrt(s2 / len(trainInputs2))
    standard_dev3 = math.sqrt(s3 / len(trainOutputs))

    return med1, med2, med3, standar_dev1, standard_dev2, standard_dev3

def createParams_uni(trainInputs1, trainOutputs):
    med1 = sum(trainInputs1) / len(trainInputs1)
    med2 = sum(trainOutputs) / len(trainOutputs)
    s1, s2 = 0,0
    for i in range(len(trainInputs1)):
        s1 += (trainInputs1[i] - med1) ** 2
        s2 += (trainOutputs[i] - med2) ** 2
    standard_dev1 = math.sqrt(s1 / len(trainInputs1))
    standard_dev2 = math.sqrt(s2 / len(trainOutputs))
    return med1,  med2, standard_dev1, standard_dev2

""""
    inputs: liste de numere reale ce reprezinta seturi de date ce trebuie normalizate folosind formula:
        new_x = (old_x - mean) / std_dev
    outputs: liste de numere reale cu valorile actualizate dupa formula data
"""
def normalize(trainInputs1, trainInputs2, trainOutputs, validInputs1, validInputs2, validOutputs):
    med1, med2, med3, standard_dev1, standard_dev2, standard_dev3 = createParams(trainInputs1, trainInputs2, trainOutputs)
    for i in range(len(trainInputs1)):
        trainInputs1[i] = (trainInputs1[i] - med1) / standard_dev1
        trainInputs2[i] = (trainInputs2[i] - med2) / standard_dev2
        trainOutputs[i] = (trainOutputs[i] - med3) / standard_dev3
    for i in range(len(validInputs1)):
        validInputs1[i] = (validInputs1[i] - med1) / standard_dev1
        validInputs2[i] = (validInputs2[i] - med2) / standard_dev2
        validOutputs[i] = (validOutputs[i] - med3) / standard_dev3
    return trainInputs1, trainInputs2, trainOutputs, validInputs1, validInputs2, validOutputs


def normalize_uni(trainInputs1, trainOutputs, validInputs, validOutput):
    med1, med2, standard_dev1, standard_dev2 = createParams_uni(trainInputs1,  trainOutputs)
    for i in range(len(trainInputs1)):
        trainInputs1[i] = (trainInputs1[i] - med1) / standard_dev1

        trainOutputs[i] = (trainOutputs[i] - med2) / standard_dev2
    for i in range(len(validInputs)):
        validInputs[i] = (validInputs[i] - med1) / standard_dev1

        validOutput[i] = (validOutput[i] - med2) / standard_dev2
    return trainInputs1, trainOutputs, validInputs, validOutput

def testNormalize():
    traiInputs1 = [1, 2, 3, 12, 12, 3, 10, 5, 8, 19]
    trainInputs2 = [5,3,2,6,8,7,9,12,15,10]
    trainOutputs = [1,3,6,5,4,12,4,18,11,5]
    mean1, mean2, mean3, standard_dev1, standard_dev2, standard_dev3 = createParams(traiInputs1, trainInputs2, trainOutputs)
    assert mean1 == 7.5 and mean2 == 7.7 and mean3 == 6.9
    assert round(standard_dev1) == 5 and round(standard_dev2) == 4 and round(standard_dev3) == 5
    test1, test2, test3, a,b,c = normalize(traiInputs1,trainInputs2,trainOutputs,traiInputs1,trainInputs2,trainOutputs)
    assert test1 == [-1.5904979946044624, -1.5569971570835244, -1.5234963195625864, -1.2219887818741442, -1.2219887818741442, -1.5234963195625864, -1.2889904569160202, -1.4564946445207103, -1.3559921319578965, -0.987482919227578]
    assert test2 == [-2.2157938556556247, -2.3545863608603437, -2.423982613462703, -2.1463976030532654, -2.0076050978485465, -2.0770013504509057, -1.9382088452461868, -1.7300200874391085, -1.5218313296320298, -1.8688125926438273]
    assert test3 ==[-1.6507380526936553, -1.567716051863435, -1.443183050618105, -1.4846940510332152, -1.526205051448325, -1.194117048127445, -1.526205051448325, -0.9450510456367851, -1.2356280485425553, -1.4846940510332152]


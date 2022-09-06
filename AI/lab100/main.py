import glob

from sklearn import neural_network


def loadDigitData():
    from sklearn.datasets import load_digits

    data = load_digits()
    inputs = data.images
    outputs = data['target']
    outputNames = data['target_names']

    # shuffle the original data
    noData = len(inputs)
    permutation = np.random.permutation(noData)
    inputs = inputs[permutation]
    outputs = outputs[permutation]

    return inputs, outputs, outputNames


from sklearn.preprocessing import StandardScaler


def normalisation(trainData, testData):
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        # encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]

        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

        # decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
    return normalisedTrainData, normalisedTestData


def training(classifier, trainInputs, trainOutputs):
    # step4: training the classifier
    # identify (by training) the classification model
    classifier.fit(trainInputs, trainOutputs)

def classification(classifier, testInputs):
    # step5: testing (predict the labels for new inputs)
    # makes predictions for test data
    computedTestOutputs = classifier.predict(testInputs)

    return computedTestOutputs



def plotConfusionMatrix(cm, classNames, title):
    import itertools

    classes = classNames
    plt.figure()
    plt.imshow(cm, interpolation = 'nearest', cmap = 'Blues')
    plt.title('Confusion Matrix ' + title)
    plt.colorbar()
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)

    text_format = 'd'
    thresh = cm.max() / 2.
    for row, column in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(column, row, format(cm[row, column], text_format),
                horizontalalignment = 'center',
                color = 'white' if cm[row, column] > thresh else 'black')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

    plt.show()


def splitData(inputs, outputs):
    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    return trainInputs, trainOutputs, testInputs, testOutputs

def evalMultiClass(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix

    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])
    return acc, precision, recall, confMatrix
def flatten(mat):
    x = []
    for line in mat:
        for el in line:
            x.append(el)
    return x

import matplotlib.pyplot as plt
# main flow

import numpy as np
from PIL import Image

import cv2
from skimage.io import imread
from skimage.transform import resize
def load_images():
    import numpy as np
    inputs=[]
    outputs=[]
    width=50;
    height=50;
    for f in glob.glob("D:/Facultate/An2/Sem2/AI/lab100/databasesepia/training_set/normal/*.jpg"):
        image = imread(f)
        new_img = image.reshape((image.shape[0]*image.shape[1]), image.shape[2])
        new_img = new_img.transpose()
        image=new_img
        if image is not None:
            image=resize(image, (width, height))
            image=flatten(image)
            inputs.append(image)
            outputs.append(0)
    for f in glob.glob("D:/Facultate/An2/Sem2/AI/lab100/databasesepia/training_set/sepia/*.jpg"):
        image = cv2.imread(f)
        new_img = image.reshape((image.shape[0] * image.shape[1]), image.shape[2])
        new_img = new_img.transpose()
        image = new_img
        if image is not None:
            image=cv2.resize(image, (width, height))
            image=flatten(image)
            inputs.append(image)
            outputs.append(1)



    output_names = ["normal","sepia"]
    return inputs,outputs,output_names

inputs,outputs,outputNames=load_images()
#print(inputs,outputs)
trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)
#print('train')
#print(trainInputs)



#trainInputsFlatten = [flatten(el) for el in trainInputs]
#testInputsFlatten = [flatten(el) for el in testInputs]
#trainInputsNormalised, testInputsNormalised = normalisation(trainInputs, testInputs)

# try to play by MLP parameters (e.g. change the HL size from 10 to 20 and see how this modification impacts the accuracy)
classifier = neural_network.MLPClassifier(hidden_layer_sizes=(10,), activation='relu', max_iter=100, solver='sgd',random_state=1, learning_rate_init=.1)

training(classifier, trainInputs, trainOutputs)
predictedLabels = classification(classifier, testInputs)
acc, prec, recall, cm = evalMultiClass(np.array(testOutputs), predictedLabels, outputNames)

print('acc: ', acc)
print('precision: ', prec)
print('recall: ', recall)




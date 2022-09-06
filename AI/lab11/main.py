# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import os

from Regression import MyLogisticRegression
from myKMeans import MyKMeans


def read_data():
    crtDir = os.getcwd()
    fileName = os.path.join(crtDir, 'data/review.csv')

    data = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1

    inputs = [data[i][0] for i in range(len(data))]
    outputs = [data[i][1] for i in range(len(data))]
    labelNames = list(set(outputs))

    print(inputs[:2])
    print(labelNames[:2])
    return inputs,outputs,labelNames

def split_data(inputs, outputs):
    import numpy as np

    np.random.seed(5)
    # noSamples = inputs.shape[0]
    noSamples = len(inputs)
    indexes = [i for i in range(noSamples)]
    trainSample = np.random.choice(indexes, int(0.8 * noSamples), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    print(trainInputs[:3])
    print(trainOutputs)
    return trainInputs, testInputs, trainOutputs, testOutputs


def extract_bag_of_words(trainInputs, testInputs):
    # extract some features from the raw text

    # # representation 1: Bag of Words
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()

    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)

    # vocabbulary from the train data
    print('vocab: ', vectorizer.get_feature_names()[:10])
    # extracted features
    print('features: ', trainFeatures.toarray()[:3][:10])
    return trainFeatures.toarray(),testFeatures.toarray()

def extract_tf_idf(trainInputs, testInputs):
    # representation 2: tf-idf features - word granularity
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(max_features=50)

    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)

    # vocabbulary from the train data
    print('vocab: ', vectorizer.get_feature_names()[:10])
    # extracted features
    print('features: ', trainFeatures.toarray()[:3])
    return trainFeatures.toarray(), testFeatures.toarray()

def extract_embeded():
    # representation 3: embedded features extracted by a pre-train model (in fact, word2vec pretrained model)

    import gensim

    # Load Google's pre-trained Word2Vec
    crtDir = os.getcwd()
    modelPath = os.path.join(crtDir, 'models', 'GoogleNews-vectors-negative300.bin')

    word2vecModel300 = gensim.models.KeyedVectors.load_word2vec_format(modelPath, binary=True)
    print(word2vecModel300.most_similar('support'))
    print("vec for house: ", word2vecModel300["house"])
import numpy as np

def featureComputation(model, data):
    features = []
    phrases = [ phrase.split() for phrase in data]
    for phrase in phrases:
        # compute the embeddings of all the words from a phrase (words of more than 2 characters) known by the model
        vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.vocab.keys())]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features
def mykmeans(n_clusters):
    pass

def classification():
    # unsupervised classification ( = clustering) of data
    inputs,outputs,labelNames=read_data()
    #print(labelNames)
    trainInputs, testInputs, trainOutputs, testOutputs=split_data(inputs,outputs)
    #trainOutputs=[0 if i=="negative" else 1 for i in trainOutputs]
    #clas = MyKMeans(2,10)
    #clas.fit(trainFeatures)
    #print(clas.predict(testFeatures))
    #trainFeatures, testFeatures = extract_tf_idf(trainInputs, testInputs)
    trainFeatures, testFeatures = extract_bag_of_words(trainInputs, testInputs)
    from sklearn.cluster import KMeans
    print(trainFeatures)
    unsupervisedClassifier = KMeans(n_clusters=2, random_state=0)
    #unsupervisedClassifier = MyLogisticRegression()
    unsupervisedClassifier.fit(trainFeatures,trainOutputs)
    computedTrainOutputs=unsupervisedClassifier.predict(trainFeatures)
    computedTrainLabels=[labelNames[value] for value in computedTrainOutputs]
    computedTestIndexes = unsupervisedClassifier.predict(testFeatures)
    computedTestOutputs = [labelNames[value] for value in computedTestIndexes]

    from sklearn.metrics import accuracy_score
    print("acc test: ", accuracy_score(testOutputs, computedTestOutputs))
    print("acc train: ",accuracy_score(trainOutputs, computedTrainLabels))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    classification()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

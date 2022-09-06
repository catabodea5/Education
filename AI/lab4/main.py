from math import sqrt

from GA import GA
import random
import NetworkChromosome as nc

def readFromFile3(fileName):
    f = open(fileName, "r")
    net = {}
    n = f.readline()
    while not n[0].isnumeric():
        n = f.readline()
    line = n.split(" ")
    coordinatesList = [[float(line[1]), float(line[2])]]
    n = f.readline()
    while n[0].isnumeric():
        line = n.split(" ")
        coordinatesList.append([float(line[1]), float(line[2])])
        n = f.readline()
    net['noNodes'] = len(coordinatesList)
    mat = []
    for i in range(net['noNodes']):
        line = [0 for _ in range(net['noNodes'])]
        for j in range(net['noNodes']):
            if i != j:
                distance = lengthBetweenNodes(coordinatesList[i], coordinatesList[j])
                line[j] = distance
        mat.append(line)
    net['mat'] = mat
    return net
def lengthBetweenNodes(node1, node2):
    return sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
def readFromFile():
    net={}
    fin = open("fricker26.txt", "r")
    lines = fin.readlines()
    n = int(lines[0])
    aux = []
    for i in range(1, n + 1):
        aux.append(lines[i])
    graf=[[int(num) for num in line.split(',')] for line in aux]
    net['mat'] = graf
    net['noNodes'] = n
    fin.close()
    return net
def readFromFile2():
    net={}
    fin = open("medium.txt", "r")
    lines = fin.readlines()
    n = int(lines[0])
    aux = []
    for i in range(1, n + 1):
        aux.append(lines[i])
    graf=[[int(num) for num in line.split(',')] for line in aux]
    net['mat'] = graf
    net['noNodes'] = n
    fin.close()
    return net
def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']

    Q = 0.0
    for i in range(len(communities)-1):
        Q+=mat[communities[i]][communities[i+1]]
    Q+=mat[communities[0]][communities[i+1]]
    return Q

def main():
    network = readFromFile()
    #network = readFromFile3("eli51.txt")
    n = network['noNodes']
    mat=network['mat']
    # initialise de GA parameters
    parametrii_ga = {'popSize': 1000, 'noGen': 500}
    # problem parameters
    parametrii_prob = {'function': modularity, 'noNodes':n, 'mat':mat, 'network':network}
    ga = GA(parametrii_ga, parametrii_prob)
    ga.initialisation()
    ga.evaluation()
    generatii=[]

    for generatie in range(parametrii_ga['noGen']):
        generatii.append(generatie)
        ga.oneGenerationElitism()
        best = ga.worstChromosome()
        print(best)


if __name__ == '__main__':
    main()


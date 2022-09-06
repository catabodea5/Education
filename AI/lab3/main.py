import networkx as nx
from GA import GA
import random
import NetworkChromosome as nc
import numpy as np

def readFromFile():
    #G = nx.read_gml('dolphins.gml')
    #G = nx.read_gml('football.gml')
    #G = nx.read_gml('karate.gml', label='id')
    #G = nx.read_gml('krebs.gml')
    #G = nx.read_gml('lesmis.gml')
    G = nx.read_gml('word.gml')

    net = {}
    n = G.number_of_nodes()
    net['noNodes'] = n
    aux = nx.adjacency_matrix(G)
    mat = []
    mat_adiacenta = []
    for i in range(n):
        valori = []
        line = str(aux[i])
        val = line.split(', ')
        for j in range(1, len(val)):
            number = val[j].split(')')[0]
            valori.append(int(number))
        mat.append(valori)
    for i in range(n):
        lin = []
        for j in range(n):
            if j in mat[i]:
                lin.append(1)
            else:
                lin.append(0)
        mat_adiacenta.append(lin)
    net['mat'] = mat_adiacenta
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat_adiacenta[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat_adiacenta[i][j]
        degrees.append(d)
    net['noEdges'] = noEdges
    net['degrees'] = degrees
    return net

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
               Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M


def main():
    network = readFromFile()
    n = network['noNodes']
    max_nr_comunities = 14

    # initialise de GA parameters
    parametrii_ga = {'popSize': 100, 'noGen': 500}
    # problem parameters
    parametrii_prob = {'function': modularity, 'nr_com':max_nr_comunities, 'network':network}

    ga = GA(parametrii_ga, parametrii_prob)
    ga.initialisation()
    ga.evaluation()
    generatii=[]

    for generatie in range(parametrii_ga['noGen']):
        generatii.append(generatie)
        ga.oneGeneration()
        best = ga.bestChromosome()
        print(best)
        print("nr comunitati", len(set(best.repres)))


if __name__ == '__main__':
    main()


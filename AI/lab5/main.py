from math import sqrt
from random import choices

def readFromFile2(fileName):
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

def tsp(mat, pheromones):
    fitness=0
    visited=[]
    visited.append(0)
    next = choose_path(0,mat,pheromones)
    visited.append(next)
    fitness += mat[0][next]
    pheromones[0][next] += 1
    next1=next
    while len(visited) != len(mat):
        next = visited[-1]
        while next1 in visited:
            next1 = choose_path(next, mat, pheromones)
        visited.append(next1)
        fitness += mat[next1][next]
        pheromones[next][next1] += 1
    fitness += mat[0][visited[-1]]
    pheromones[visited[-1]][visited[0]] += 1
    return fitness



#chooses a road from node "nod"  based on the probabilities of each node getting chosen
#nod - int
#mat, pheromones - int[][]
def choose_path(nod, mat, pheromones):
    probabilities = probability_for_a_road(nod, mat, pheromones)
    nodes=[]
    for i in range(len(mat)):
        nodes.append(i)
    return choices(nodes, probabilities)[0]

#calculates probability for each road between the node "nod" and every other one. also takes into account the weight
#nod - int
#mat, pheromones - int[][]
def probability_for_a_road(nod, mat, pheromones):
    probabilities=[]
    sum = 0
    for j in range(len(mat)):
        if mat[nod][j]==0:
            probabilities.append(0)
        else:
            probPhero=calculate_probability_on_pheromones(nod, mat, pheromones)
            for i in range(len(probPhero)):
                sum += probPhero[i]
            probabilities.append((pheromones[nod][j] * 1/mat[nod][j]) / sum)
        sum = 0
    return probabilities


#return a list of all the probabilites of choosing a road based on pheromones and the weight for each road starting from node "nod"
#nod - int
#mat, pheromones, int[][]
def calculate_probability_on_pheromones(nod, mat, pheromones):
    probabilities=[]
    for j in range(len(mat)):
        if mat[nod][j] == 0:
            probabilities.append(0)
        else:
            probabilities.append(pheromones[nod][j]/mat[nod][j])
    return probabilities



def main():
    #network= readFromFile2("eli51.txt")
    network=readFromFile()
    n= network['noNodes']
    pheromones=[]
    line=[]
    for i in range(n):
        for j in range(n):
            line.append(1)
        pheromones.append(line)
        line=[]
    print(network['mat'])
    mat=network['mat']
    print(choose_path(0,network['mat'],pheromones))
    for i in range(0,1000):
        print(tsp(network['mat'], pheromones))
        print(pheromones)

    max=0
    maxj=0
    sum=0;
    for i in range(n):
        for j in range(n):
            if pheromones[i][j]>max:
                max=pheromones[i][j]
                maxj=j
        sum+=mat[i][maxj]
   # print ("valoarea medie bazata pe feromoni este: ",sum)


if __name__ == '__main__':
    main()



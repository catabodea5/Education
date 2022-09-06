from math import sqrt
from random import random

import numpy as np
class MyKMeans:
    def __init__(self, n_centroids, n_iterations):
        self.n_centroids=n_centroids
        self.n_iterations=n_iterations

    def fit(self, inputs):
        centroids=[]
        indexes = [i for i in range(len(inputs))]

        #initializare centroizi
        for c in range(0,self.n_centroids):
            centroids.append(inputs[np.random.choice(indexes)])



        for iteration in range(self.n_iterations):
            list_min_centroizi = []
            min_centroid=[]
            #calculare lista de centroizi minimi
            for i in range(len(inputs)):
                min=10000
                for j in range(len(centroids)):
                    if(self.dist(inputs[i],centroids[j])<min):
                        min=self.dist(inputs[i],centroids[j])
                        min_centroid=centroids[j]
                list_min_centroizi.append(min_centroid)

            #recalculare centroizi
            new_centroids=[]
            for centroid in centroids:
                new_centroid = [0 for i in range(len(min_centroid))]
                for input in centroid:
                    for i in range(len(input)):
                        new_centroid[i]+=input[i]
                for i in range(len(new_centroid)):
                    new_centroid[i]=new_centroid[i]/len(new_centroid)
                new_centroids.append(new_centroid)


            #conditia de stop: daca centroizii raman neschimbati atunci am gasit cei mai buni centroizi si ajuns la final
            ok=1
            for i in range(len(new_centroids)):
                if new_centroids[i]!=centroids[i]:
                    ok=0
            if ok==0:
                break
            else:
                centroids=new_centroids
        self.centroids=centroids

    def predict(self, inputs):
        centroid = []
        for i in range(len(inputs)):
            min=10000
            for j in range(len(self.centroids)):
                if (self.dist(inputs[i], self.centroids[j]) < min):
                    min = self.dist(inputs[i], self.centroids[j])
                    min_centroid = self.centroids[j]
            centroid.append(min_centroid)
        return centroid

    def dist(self,input1,input2):
        dist=0
        for i in range(len(input1)):
            dist+= (input1[i]-input2[i])**2
        dist=sqrt(dist)
        return dist

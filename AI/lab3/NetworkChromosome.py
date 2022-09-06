import numpy as np


class Chromosome:
    def __init__(self, problem_param):
        network = problem_param['network']
        self.__problem_param = problem_param
        k = problem_param['nr_com']
        # generam un vector de dimensiune n cu elemente random din intervalul [1,k]
        self.__repres = np.random.randint(1, k + 1, size=network['noNodes'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l):
        self.__repres = l

    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    #incrucisare uniforma
    #avem o masca de biti , ex:[1,0,0,1,1]
    #unde bitul e 1 luam din a doilea parinte, iar daca e 0 luam din primul
    def crossover(self, chromosome):
        n = len(chromosome.repres)
        masca = np.random.randint(2, size=n)
        succesor = []
        for i in range(n):
            if masca[i] == 1:
                succesor.append(chromosome.repres[i])
            else:
                succesor.append(self.__repres[i])
        c = Chromosome(self.__problem_param)
        c.repres = []
        for i in range(len(succesor)):
            c.repres.append(succesor[i])
        return c

    #schimbam un nod random cu alt nod random
    def mutation(self):
        network = self.__problem_param['network']
        n = len(self.__repres)
        poz = np.random.randint(n)
        nod1 = np.random.randint(1, self.__problem_param['nr_com'] + 1)
        self.__repres[poz] = nod1


    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

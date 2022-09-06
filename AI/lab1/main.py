import  math


#Bodea Catalin grupa 221
#lab1 AI


# Problema1
# Gaseste ultimul cuvant lexicografic care apare intr-un text
# propozitie: un string
# ultim: ultimul cuvant din punct de vedere lexicografic
# cuvinte: lista de cuvinte obtinuta din propozitie

def problema1(propozitie):
    cuvinte=propozitie.split(' ')
    ultim=''
    for cuv in cuvinte:
        if ultim.lower() < cuv.lower():
            ultim=cuv
    return ultim


def test1():
    assert problema1("") == ""
    assert problema1("blabla") == "blabla"
    assert problema1("Ana are mere") == "mere"
    assert problema1("x y z") == "z"
    assert problema1("1 x 2 3 xy 4 abc") == "xy"


# Problema 2
# distanta euclidiana dintre 2 puncte in plan
# a, b: coordonate de tipul (i,j)
# Returneaza un float reprezentand distanta euclidiana
def problema2(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def test2():
    assert problema2((1, 5), (4, 1)) == 5
    assert problema2( (0,0), (0,0)) ==0;



# Problema 3

# Determina produsul scalar a 2 vectori rari de numere reale
# a, b: liste de numere reale
# produs = un nr real care reprezinta produsul scalar al celor 2 vectori

def prob_3(a, b):
    assert len(a) == len(b)
    produs = 0
    for i in range(len(a)):
        produs += a[i] * b[i]
    return produs


def test3():
    assert prob_3([], []) == 0
    assert prob_3([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    assert prob_3([12, 0], [0, 3]) == 0



#Problema 4
# Sa se afiseze toate cuvintele care apar o sg data
# propozitie = string
# cuvinte = un dictionar de tipul (string, int) unde cheia e cuvantul si valoare e numarul de aparitii in propozitie
# rezultat = string rezultat

def problema4(propozite):
    cuvinte ={}
    rezultat=[]
    lista=propozite.split(' ')
    for i in lista:
        if i in cuvinte:
            cuvinte[i] += 1
        else:
            cuvinte[i] = 1
    for i in lista:
        if cuvinte[i] == 1:
            rezultat.append(i)
    return rezultat

def test4():

    assert problema4("ana ana") == []
    assert problema4("ana") == ['ana']
    assert problema4("ana are mere") == ['ana', 'are', 'mere']
    assert problema4("ana are mere mere") == ['ana', 'are']


#Problema5
# Sa se determine numarul care apare 2 2 ori din sirul de n numere din intervalul [1, n-1]
# numberOfApparitions = sir de aparitii

def problema5(lista):
    numberOfApparitions=[]
    for i in range(len(lista)):
        numberOfApparitions.append(0)
    for i in lista:
        numberOfApparitions[i] += 1
        if numberOfApparitions[i]==2:
            return i
    return 0

def test5():
    assert problema5([]) == 0
    assert problema5([1, 1]) == 1
    assert problema5([1, 2, 3, 4, 5, 3]) == 3



# Problema 6

# elementul majoritar dintr-un sir de numere (trebuie sa apara de mai mult de n / 2 ori)
# lista: obiect reprezentand o lista de numere intregi
# number = numarul majoritar de returnat

def problema6(lista):
    dict = { }
    for number in lista:
        if number in dict:
            dict[number] += 1
        else:
            dict[number]=1
    for number in lista:
        if dict[number] > len(lista)/2:
            return number
    return 0


def test6():
    assert problema6([]) == 0
    assert problema6([1, 1, 1, 8, 0]) == 1
    assert problema6([1,2,3,4,5,6,7]) == 0






# Problema 7
# Determina al k-lea cel mai mare element al unui sir cu n numere
# max = numarul maxim
# numerele = lista de numere
# k = al catelea cel mai mare numar
def problema7(numerele, k):
    max = 0
    for i in range(k):
        max = float('-inf')
        n = len(numerele)
        for j in range(n):
            if numerele[j] > max:
                max = numerele[j]
        while max in numerele:
            numerele.remove(max)

    return max

def test7():
    assert problema7([-7, -2, 1], 3) == -7
    assert problema7([1, 2, 3], 1) == 3
    assert problema7([10 ,11, 22, 1], 2) == 11
    assert problema7([1,2,3,4,5,6,6,6,6,7], 3) == 5


# Problema 8
# numerele de la 1 la n in binar
# lista = lista de numere in binar
# binarul = un string care reprezinta reprezentarea in binar a unui nr
def problema8(n):
    lista=[]
    binarul=''
    for i in range (1,n+1):
        while (i != 0):
            binarul = str(i % 2) + binarul
            i = int(i / 2)

        lista.append(binarul)
        binarul=''
    return lista

def test8():
    assert problema8(1) == ['1']
    assert problema8(2) == ['1', '10']
    assert problema8(3) == ['1', '10', '11']

# Problema9
# suma elementelor din submatricele determinate de o lista de coordonate [[(p, q) , (r, s)], ...]
# sume = lista sumelor in fct de coordonate
# a,b= coordonate de tipul (p ,q) din lista de coordonate
# coordonate = set  de coordonate de tipul [(p,q), (r,s)]

def problema9(matrice, lista):
    sume = []
    for coordonate in lista:
        suma = 0
        a = coordonate[0]
        b = coordonate[1]
        for i in range(a[0], b[0] + 1):
            for j in range(a[1], b[1] + 1):
                suma += matrice[i][j]
        sume.append(suma)
    return sume

def test9():
    matx = [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]
    assert problema9(matx, [[(1, 1), (3, 3)], [(2, 2), (4, 4)]]) == [38, 44]


# Problema 10

# Determina indexul liniei unei matrici ce contine cele mai multe cifre de 1
# matx: matrice de numere intregi
# Returneaza un numar natural, reprezentand indexul liniei cu cei mai multi 1

def problema10(matrice):
    global j
    linia, max = -1, -1
    contor=0
    for i in range(len(matrice)):
        contor=0
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                contor+=1
        if contor > max:
            max , linia= contor, i

    return linia

def test10():
    assert problema10([[1, 2, 1, 3, 1], [0, 1, 4, 4, 1], [0, 0, 0, 0, 0]]) == 0
    assert problema10([[1, 2, 0, 3, 0], [0, 1, 4, 4, 1], [0, 0, 0, 0, 0]]) == 1

def teste():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
if __name__ == '__main__':
    teste()





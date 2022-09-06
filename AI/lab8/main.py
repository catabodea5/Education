import os
import csv
from loss import testLoss
from solveUnivariate import univariateTool, univariateManual
from solveBivariate import bivariateTool, bivariateManual
from ZNormalisation import testNormalize

def loadData(fileName, inputFeat1, inputFeat2, outputVariabName):
    datas = []
    names_f_data = []
    with open(fileName) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                names_f_data = row
            else:
                datas.append(row)
            line_count += 1

    inputs1 = [float(datas[i][names_f_data.index(inputFeat1)]) for i in range(len(datas))]
    inputs2 = [float(datas[i][names_f_data.index(inputFeat2)]) for i in range(len(datas))]
    outputs = [float(datas[i][names_f_data.index(outputVariabName)]) for i in range(len(datas))]
    return inputs1, inputs2, outputs

def main():
    crtDir = os.getcwd()
    path = os.path.join(crtDir, 'data', '2017.csv')
    inputs1, inputs2, outputs = loadData(path, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')

    error = univariateTool(inputs1, outputs, 100)

    print("Regresie univariata tool: Eroarea de predictie este: " + error.__str__() + "\n")

    error = univariateManual(inputs1, outputs, 100)

    print("Regresie univariata manuala: Eroarea de predictie este: " + error.__str__() + "\n")

    error = bivariateTool(inputs1, inputs2, outputs, 100)

    print("Regresie bivariata cu tool: Eroarea de predictie este: " + error.__str__() + "\n")

    error = bivariateManual(inputs1, inputs2, outputs, 100)

    print("Rezultat regresie bivariata manuala: Eroarea de predictie este: " + error.__str__() + "\n")


if __name__ == '__main__':
    main()
    testLoss()
    testNormalize()
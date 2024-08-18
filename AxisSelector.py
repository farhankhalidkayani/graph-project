import csv


def getXAxis():
    with open("iris.csv", "r") as file:
        reader = csv.reader(file)
        xAxis = []
        for row in list(reader)[1:]:
            xAxis.append(row[4])
        return xAxis


def getSepalLength():
    with open("iris.csv", "r") as file:
        reader = csv.reader(file)
        yAxis = []
        for row in list(reader)[1:]:
            yAxis.append(row[0])
    return yAxis


def getSepalWidth():
    with open("iris.csv", "r") as file:
        reader = csv.reader(file)
        yAxis = []
        for row in list(reader)[1:]:
            yAxis.append(row[1])
    return yAxis


def getPetalLength():
    with open("iris.csv", "r") as file:
        reader = csv.reader(file)
        yAxis = []
        for row in list(reader)[1:]:
            yAxis.append(row[2])
    return yAxis


def getPetalWidth():
    with open("iris.csv", "r") as file:
        reader = csv.reader(file)
        yAxis = []
        for row in list(reader)[1:]:
            yAxis.append(row[3])
    return yAxis

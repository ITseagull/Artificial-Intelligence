import math
import operator
import sys
from collections import defaultdict
from matplotlib import pyplot as plt
from ast import literal_eval
from operator import itemgetter, attrgetter

#read file with items
path = 'TestData'
with open(path, "r") as f: 
    fileTest = f.read().splitlines()

#read file with items
path = '\\TrainingSet'
with open(path, "r") as f:  
    fileTrain = f.read().splitlines()


class Element :
    def __init__(self, coordinates, name):
        self.coordinates = coordinates
        self.name = name

#separate coordinates and name of class
def get_el (line): 
    coord = []
    temp = line.split(",")
    for i in range(len(line.split(","))-1):
        coord.append(float(temp[i]))
    return Element(coord, line.split(",")[-1])

# method which will take two elements and calculate distance between x and given point
def get_distance(coordin, x):
    dist = 0
    for i in range(len(coordin)):
        dist += ((coordin[i]) - x[i]) ** 2
    dist = math.sqrt(dist)
    return dist

#method which will return list of all distances
def get_distances(allEl, x, k):

    distances = {i:0 for i in allEl}

    for i in allEl:
        distances[i] = get_distance(i.coordinates, x.coordinates)
    distances =  sorted(distances.items(), key= lambda t : t[1])

    distances = [distances[i][0] for i in range(k)]

    return(distances)

def test_data(list_testData,all_ell,k):
    positive = 0
    negative = 0
    acc = 0
    for i in list_testData:
        if i.name == get_class(get_distances(allEl=all_ell, x=i, k=k_value),element=i):
            positive +=1
        else:
            negative +=1
    acc = 100*(positive/len(list_testData))
    return positive, negative, acc

def get_class(list_distances, element):
    dict_class = {i.name:0 for i in list_distances}
    for key, value in dict_class.items():
        if  element.name == key:
            dict_class[key]+=1
    return(max(dict_class))

#main
if __name__ == "__main__":
    
    string_input = input("Coordinates for flower: ")
    custom_coordinates = [float(i) for i in string_input.split(',')]
    elCheck = Element(custom_coordinates, name='check')
    k_value = int(input("Give value for k: "))

    #separate given line
    get_el(fileTrain[0])  
    get_el(fileTest[0])

    #list of all lines with coordinates
    listEl = []  
    for x in fileTrain:
        listEl.append(get_el(x))

    #training list of elements
    listElTest = []  
    for y in fileTest:
        listElTest.append(get_el(y))

    test_data(listElTest, listEl, k_value)
    print('Total number of correct answers: ' + str(test_data(listElTest, listEl, k_value)[0]))
    print('Total number of false answers: ' + str(test_data(listElTest, listEl, k_value)[1]))
    print('Accuracy: ' + str(test_data(listElTest, listEl, k_value)[2]))
    print('Class: ', get_class(get_distances(listEl, elCheck, k_value), elCheck))


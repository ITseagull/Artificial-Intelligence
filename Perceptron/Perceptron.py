import random

path = '\\TrainingSet'
with open(path, "r") as f:
   fileTrain= f.read().splitlines()

path_test = '\\TestData'
with open(path_test, "r") as f:
    fileTest = f.read().splitlines()



class Element:
    def __init__(self, valueElement, targetElement):
        self.valueElement = valueElement
        self.targetElement = targetElement


def getValues(inputData):
    values = [] #all values from dataset
    target = []

    temp = inputData.split(",")

    target = inputData.split(",")[-1]

    for i in range(len(inputData.split(","))-1):
        values.append(float(temp[i]))


    return Element(values, target)



class Perceptron(object):
    def __init__(self, targetPerceptron ,num_of_weights = 2, learning_rate = 1):
        self.targetPerceptron = targetPerceptron
        self.learning_rate = learning_rate

        self.weights = [] #create random weights for first epoch
        self.bias = 1.0
        for x in range (0,num_of_weights):
            self.weights.append(random.random()*2-1)

    def activation_function(self, inputs): #inputs
        result = 0.0
        for w in range(len(self.weights)):  # number of inputs self.weights - random weights for first epoch
            result += self.weights[w] * inputs[w]
            result -= self.bias

        if result > 0 :
            return 1
        else:
            return 0


    def update_weights_and_bias(self, element, result_activation_function):
        weightPrime = []
        bias = 0

        for indx,inp_par in enumerate(element.valueElement):
            weightPrime.append(self.weights[indx] + \
                               (decode(element,p) - result_activation_function )* self.learning_rate * inp_par)
            bias = self.bias - (decode(element,p) - result_activation_function ) * self.learning_rate*1
        self.weights =  weightPrime
        self.bias = bias

def decode(element,perc):
    if element.targetElement == perc.targetPerceptron:
        return 1
    else:
        return 0


def run_test(dataSet): #method run, dataSet - input fileDataset[0]
    positive = 0
    for element in dataSet:
        resul_act_func = p.activation_function(element.valueElement)
        if ((str(element.targetElement)) == (str(p.targetPerceptron)) and int(decode(element, p)) == int(
                resul_act_func)):
            #print('Result - ok.')
            positive += 1
        if (str(element.targetElement)) != (str(p.targetPerceptron)) and int(resul_act_func) == 0:
            #print('Result - ok.')
            positive += 1

    print('Positive results in test list:', positive)
    accuracy = positive / len(dataSet)
    print("Accuracy for test list: ", accuracy)



def run_training(dataSet, epoch): #method run, dataSet - input fileDataset[0]
    i = 1

    while epoch > 0:
        positive = 0
        print('---------EPOCH: ', i)
        for element in dataSet:
            resul_act_func = p.activation_function(element.valueElement)
            print('perceptron target: ',p.targetPerceptron,' output: ',resul_act_func, ' input: ', element.valueElement,\
                  'target element: ', element.targetElement)

            if ((str(element.targetElement)) == (str(p.targetPerceptron)) and int(decode(element,p)) == int(resul_act_func)):
                print('Result - ok.')
                positive += 1
            if (str(element.targetElement)) != (str(p.targetPerceptron)) and int(resul_act_func) == 0:
                print('Result - ok.')
                positive += 1
            else:
                p.update_weights_and_bias(element, resul_act_func)
                print('Element should be updated.')


        i += 1
        epoch -= 1
        print('\n---------------------------')
        print('Positive results in train list: ',positive)
        accuracy = positive/len(dataSet)
        print("Accuracy for train list: ", accuracy , " \n---------------------------")


traintList = [getValues(i) for i in fileTrain]
testList = [getValues(x) for x in fileTest]

p = Perceptron('Iris-virginica',4)

run_training(traintList, 2) #training
run_test(testList)

print('---------------------------')
test_element = input('Test element: ')
testEl = [float(i) for i in test_element.split(',')]
#test_element = [7.6,3.0,6.6,2.1]
print('-----------------------------')
print( p.targetPerceptron, p.activation_function(testEl))








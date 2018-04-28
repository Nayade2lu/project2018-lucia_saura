#Lucia Saura 26/04/2018
#Iris Data set analysis https://archive.ics.uci.edu/ml/datasets/iris
#Project Programming and Scripting module

#Calculate the mean of each Setosa parameter

#Calculate Setosa sepal length mean
#Improting the numpy library
import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
#selecting the first column of the data
sepallenghtsetosa = data[:,0]
#calculating the mean of the first column
meansepallengthsetosa = numpy.mean(data[:,0])
#Code tested working in iPhyton
print("Setosa sepal length mean", meansepallengthsetosa)

#Calcualate Setosa sepal width mean
#Improting the numpy library
import numpy
#Read setosa data file into array
data = numpy.genfromtxt('iris-data-set-setosa.csv', delimiter=',')
#selecting the second column of the data
sepalwidthtsetosa = data[:,1]
#calculating the mean of the second column
meansepalwidthsetosa = numpy.mean(data[:,1])
print("Setosa sepal width", meansepalwidthsetosa)
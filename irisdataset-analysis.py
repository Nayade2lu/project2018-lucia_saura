#Lucia Saura 26/04/2018
#Iris Data set analysis https://archive.ics.uci.edu/ml/datasets/iris
#Project Programming and Scripting module

#Calculate the mean of each Setosa parameter
import numpy
data = numpy.genfromtxt('iris-data-set.csv', delimiter=',')
sepallenghtsetosa = data[:,0]
meansepallengthsetosa = numpy.mean(data[:,0])
